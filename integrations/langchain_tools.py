"""
LangChain / LangGraph Tool Integration for Medical Research Multi-Agent
"""

try:
  from langchain_core.tools import tool
except ImportError:
  def tool(fn):
    return fn

import json
from core.calculators import (
  calculate_sample_size_two_proportions,
  calculate_sample_size_two_means,
  calculate_diagnostic_metrics,
  calculate_epidemiologic_association
)
from core.engine import MedicalResearchMultiAgentOrchestrator

@tool
def design_clinical_protocol_tool(question: str) -> str:
  """
  Autonomous 7-agent medical methodology orchestrator.
  Generates publication-grade clinical trial protocols, PICO formulation,
  study design, biostatistics sample size, causal DAG, and EQUATOR compliance.
  """
  orchestrator = MedicalResearchMultiAgentOrchestrator()
  state = orchestrator.run_pipeline(question)
  return state.markdown_report

@tool
def calculate_rct_sample_size_tool(p1: float, p2: float, alpha: float = 0.05, power: float = 0.80, dropout_rate: float = 0.15) -> str:
  """
  Calculate exact sample size for a two-arm superiority randomized controlled trial (binary proportions).
  """
  res = calculate_sample_size_two_proportions(p1=p1, p2=p2, alpha=alpha, power=power, dropout_rate=dropout_rate)
  return json.dumps(res, indent=2)

@tool
def calculate_diagnostic_matrix_tool(tp: float, fp: float, fn: float, tn: float, pre_test_prob: float = None) -> str:
  """
  Calculate diagnostic test accuracy: Sensitivity, Specificity, PPV, NPV, LR+, LR-, and Bayesian post-test probability.
  """
  res = calculate_diagnostic_metrics(tp=tp, fp=fp, fn=fn, tn=tn, pre_test_prob=pre_test_prob)
  return json.dumps(res, indent=2)
