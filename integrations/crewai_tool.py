"""
CrewAI Tool Integration for Medical Research Multi-Agent
Allows CrewAI agents to generate clinical protocols and calculate biostatistics.
"""

from typing import Type
from pydantic import BaseModel, Field

try:
  from crewai.tools import BaseTool
except ImportError:
  # Mock BaseTool if crewai is not installed in the current environment
  class BaseTool:
    name: str = ""
    description: str = ""
    args_schema: Type[BaseModel] = None

from core.calculators import calculate_sample_size_two_proportions, calculate_diagnostic_metrics
from core.engine import MedicalResearchMultiAgentOrchestrator

class ClinicalProtocolInput(BaseModel):
  question: str = Field(..., description="The clinical research question or hypothesis")

class ClinicalProtocolTool(BaseTool):
  name: str = "clinical_trial_protocol_architect"
  description: str = (
    "Generates complete, publication-grade clinical trial protocols with PICO formulation, "
    "study design, biostatistics sample size, and causal DAG based on Chulalongkorn DAB Unit."
  )
  args_schema: Type[BaseModel] = ClinicalProtocolInput

  def _run(self, question: str) -> str:
    orchestrator = MedicalResearchMultiAgentOrchestrator()
    state = orchestrator.run_pipeline(question)
    return state.markdown_report

class SampleSizeRCTInput(BaseModel):
  p1: float = Field(..., description="Control arm proportion (0 to 1)")
  p2: float = Field(..., description="Experimental arm proportion (0 to 1)")
  alpha: float = Field(0.05, description="Significance level (default 0.05)")
  power: float = Field(0.80, description="Statistical power (default 0.80)")
  dropout_rate: float = Field(0.15, description="Anticipated attrition rate (default 0.15)")

class SampleSizeRCTTool(BaseTool):
  name: str = "rct_sample_size_calculator"
  description: str = "Calculates exact sample size per arm and total size for two-arm parallel superiority RCT."
  args_schema: Type[BaseModel] = SampleSizeRCTInput

  def _run(self, p1: float, p2: float, alpha: float = 0.05, power: float = 0.80, dropout_rate: float = 0.15) -> str:
    import json
    res = calculate_sample_size_two_proportions(p1=p1, p2=p2, alpha=alpha, power=power, dropout_rate=dropout_rate)
    return json.dumps(res, indent=2)
