from typing import Optional, Dict, Any
from core.state import ResearchState
from core.types import ResearchProtocol
from agents.pico_agent import PICOAgent
from agents.study_design_agent import StudyDesignAgent
from agents.biostats_agent import BiostatisticsAgent
from agents.diagnostic_agent import DiagnosticAgent
from agents.causal_rwe_agent import CausalRWEAgent
from agents.appraisal_agent import AppraisalAgent
from agents.lead_methodologist import LeadMethodologistAgent

class MedicalResearchMultiAgentOrchestrator:
    """
    Production-Grade Multi-Agent System for Medical Research & Methodology.
    Grounded directly on knowledge from Chulalongkorn University DAB Unit,
    Clinical Epidemiology (Fletcher), Biostatistics (Daniel), and Causal AI (Pearl, Hernán & Robins).
    """
    def __init__(self):
        self.pico_agent = PICOAgent()
        self.design_agent = StudyDesignAgent()
        self.biostats_agent = BiostatisticsAgent()
        self.diagnostic_agent = DiagnosticAgent()
        self.causal_agent = CausalRWEAgent()
        self.appraisal_agent = AppraisalAgent()
        self.lead_agent = LeadMethodologistAgent()

    def run_pipeline(
        self,
        query: str,
        clinical_context: Optional[str] = None,
        diagnostic_params: Optional[Dict[str, Any]] = None
    ) -> ResearchState:
        state = ResearchState(raw_query=query, clinical_context=clinical_context)
        state.add_log("Orchestrator", "Starting Multi-Agent Medical Research Workflow", {"query": query})

        # Step 1: PICO & Gap Analysis
        pico = self.pico_agent.process(state)

        # Step 2: Study Design Architecture
        design = self.design_agent.process(state)

        # Step 3: Biostatistics & Sample Size Planning
        biostats = self.biostats_agent.process(state)

        # Step 4: Diagnostic Accuracy (if applicable or params provided)
        if diagnostic_params:
            self.diagnostic_agent.process(
                state,
                tp=diagnostic_params.get("tp", 85),
                fp=diagnostic_params.get("fp", 15),
                fn=diagnostic_params.get("fn", 15),
                tn=diagnostic_params.get("tn", 85),
                pre_test_prob=diagnostic_params.get("pre_test_prob", 0.20)
            )
        else:
            self.diagnostic_agent.process(state)

        # Step 5: Causal Inference & Target Trial Emulation
        self.causal_agent.process(state)

        # Step 6: Critical Appraisal & Reporting Compliance
        self.appraisal_agent.process(state)

        # Step 7: Lead Methodologist Master Synthesis
        self.lead_agent.process(state)

        state.add_log("Orchestrator", "Multi-Agent Medical Research Workflow Completed Successfully")
        return state
