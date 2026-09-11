"""
OpenAI & xAI Grok Function Calling Integration
Demonstrates how to equip GPT-4o, Codex, or Grok with the Medical Research Multi-Agent tools.
"""

import json
import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.calculators import (
  calculate_sample_size_two_proportions,
  calculate_sample_size_two_means,
  calculate_diagnostic_metrics,
  calculate_epidemiologic_association
)

try:
  from core.engine import MedicalResearchMultiAgentOrchestrator
except ImportError:
  MedicalResearchMultiAgentOrchestrator = None

import subprocess

# Load Tool Schemas
TOOLS_PATH = Path(__file__).parent / "openai_grok_tools.json"
with open(TOOLS_PATH, "r", encoding="utf-8") as f:
  MEDICAL_TOOLS = json.load(f)

def execute_tool_call(name: str, arguments: dict) -> str:
  """Dispatch LLM tool call to the native medical research engine."""
  if name == "design_clinical_protocol":
    if MedicalResearchMultiAgentOrchestrator is not None:
      orchestrator = MedicalResearchMultiAgentOrchestrator()
      diag_params = None
      if "tp" in arguments and "fp" in arguments and "fn" in arguments and "tn" in arguments:
        diag_params = {
          "tp": arguments["tp"],
          "fp": arguments["fp"],
          "fn": arguments["fn"],
          "tn": arguments["tn"],
          "pre_test_prob": arguments.get("pre_test_prob")
        }
      state = orchestrator.run_pipeline(arguments["question"], diagnostic_params=diag_params)
      return state.markdown_report
    else:
      # Node.js zero-dependency fallback
      cli_path = str(Path(__file__).resolve().parent.parent / "bin" / "cli.js")
      cmd = ["node", cli_path, arguments["question"]]
      if "tp" in arguments and "fp" in arguments:
        cmd.extend([
          "--tp", str(arguments["tp"]),
          "--fp", str(arguments["fp"]),
          "--fn", str(arguments.get("fn", 0)),
          "--tn", str(arguments.get("tn", 0))
        ])
        if "pre_test_prob" in arguments:
          cmd.extend(["--pre-test-prob", str(arguments["pre_test_prob"])])
      res = subprocess.run(cmd, capture_output=True, text=True, check=True)
      return res.stdout

  elif name == "calculate_sample_size_rct":
    res = calculate_sample_size_two_proportions(
      p1=arguments["p1"],
      p2=arguments["p2"],
      alpha=arguments.get("alpha", 0.05),
      power=arguments.get("power", 0.80),
      dropout_rate=arguments.get("dropout_rate", 0.15)
    )
    return json.dumps(res, indent=2)

  elif name == "calculate_sample_size_means":
    res = calculate_sample_size_two_means(
      mu1=arguments["mu1"],
      mu2=arguments["mu2"],
      sigma=arguments["sigma"],
      alpha=arguments.get("alpha", 0.05),
      power=arguments.get("power", 0.80),
      dropout_rate=arguments.get("dropout_rate", 0.15)
    )
    return json.dumps(res, indent=2)

  elif name == "calculate_diagnostic_matrix":
    res = calculate_diagnostic_metrics(
      tp=arguments["tp"],
      fp=arguments["fp"],
      fn=arguments["fn"],
      tn=arguments["tn"],
      pre_test_prob=arguments.get("pre_test_prob")
    )
    return json.dumps(res, indent=2)

  elif name == "calculate_epidemiologic_association":
    res = calculate_epidemiologic_association(
      exposed_cases=arguments["exposed_cases"],
      exposed_non_cases=arguments["exposed_non_cases"],
      unexposed_cases=arguments["unexposed_cases"],
      unexposed_non_cases=arguments["unexposed_non_cases"]
    )
    return json.dumps(res, indent=2)

  return f"Error: Unknown tool {name}"

def run_agent_turn(client, model: str, user_prompt: str):
  """
  Executes a model turn with automatic function calling resolution.
  Compatible with:
    - OpenAI: client = OpenAI(api_key="..."), model="gpt-4o"
    - xAI Grok: client = OpenAI(api_key="...", base_url="https://api.x.ai/v1"), model="grok-beta"
  """
  messages = [
    {
      "role": "system",
      "content": (
        "You are an elite Clinical Epidemiologist & Biostatistician. "
        "Use the provided medical research tools to design protocols, calculate exact sample sizes, "
        "and evaluate diagnostic test performance whenever the user asks medical or epidemiological questions."
      )
    },
    {"role": "user", "content": user_prompt}
  ]

  response = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=MEDICAL_TOOLS,
    tool_choice="auto"
  )

  response_message = response.choices[0].message
  if response_message.tool_calls:
    messages.append(response_message)
    for tool_call in response_message.tool_calls:
      fn_name = tool_call.function.name
      fn_args = json.loads(tool_call.function.arguments)
      tool_result = execute_tool_call(fn_name, fn_args)
      messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "name": fn_name,
        "content": tool_result
      })

    # Get final synthesis from LLM
    final_response = client.chat.completions.create(
      model=model,
      messages=messages
    )
    return final_response.choices[0].message.content
  else:
    return response_message.content

if __name__ == "__main__":
  # Local demo without API key: test tool dispatch directly
  print("Testing local tool dispatch:")
  rct_res = execute_tool_call("calculate_sample_size_rct", {"p1": 0.35, "p2": 0.15})
  print("Sample Size RCT Tool Result:\n", rct_res)
