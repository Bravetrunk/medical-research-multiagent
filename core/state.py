from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from core.types import (
    PICOQuestion,
    StudyDesignRecommendation,
    SampleSizeResult,
    DiagnosticEvaluationResult,
    CausalDAGAnalysis,
    CriticalAppraisalReport,
    ResearchProtocol
)

class ResearchState(BaseModel):
    # Input
    raw_query: str
    clinical_context: Optional[str] = None
    
    # Knowledge references loaded
    knowledge_references: List[str] = Field(default_factory=list)
    
    # Agent Artifacts
    pico: Optional[PICOQuestion] = None
    study_design: Optional[StudyDesignRecommendation] = None
    biostats_plan: Optional[SampleSizeResult] = None
    diagnostic_eval: Optional[DiagnosticEvaluationResult] = None
    causal_dag: Optional[CausalDAGAnalysis] = None
    critical_appraisal: Optional[CriticalAppraisalReport] = None
    
    # Final Synthesis
    final_protocol: Optional[ResearchProtocol] = None
    markdown_report: Optional[str] = None
    
    # Execution Trace & Audit Trail
    agent_logs: List[Dict[str, Any]] = Field(default_factory=list)
    
    def add_log(self, agent_name: str, action: str, details: Any = None):
        self.agent_logs.append({
            "agent": agent_name,
            "action": action,
            "details": details
        })
