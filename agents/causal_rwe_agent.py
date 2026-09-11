from typing import Optional
from agents.base import BaseMedicalAgent
from core.types import CausalDAGAnalysis, QuestionType, StudyDesignType
from core.state import ResearchState
from tools.dag_analyzer_tool import analyze_causal_dag
from tools.target_trial_tool import formulate_target_trial_emulation

class CausalRWEAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="Causal Inference & RWE Guardian Agent",
            role="Causal Data Scientist & Real-World Evidence Specialist",
            description="Constructs Directed Acyclic Graphs (DAGs), enforces Judea Pearl's rules against collider bias, and formulates Target Trial Emulation protocols for RWD."
        )

    def process(self, state: ResearchState) -> Optional[CausalDAGAnalysis]:
        pico = state.pico
        design = state.study_design
        is_observational = (
            design and design.selected_design in [
                StudyDesignType.COHORT_PROSPECTIVE,
                StudyDesignType.COHORT_RETROSPECTIVE,
                StudyDesignType.CASE_CONTROL,
                StudyDesignType.TARGET_TRIAL_EMULATION
            ]
        ) or any(k in state.raw_query.lower() for k in ["rwd", "rwe", "ehr", "observational", "registry", "target trial", "causal"])

        if not is_observational and pico and pico.question_type == QuestionType.THERAPY:
            # Even for RCT, provide DAG for clarity of baseline confounder balance
            pass

        state.add_log(self.name, "Analyzing Causal DAG and Backdoor Adjustment Sets")
        state.knowledge_references.append("causal_inference_rwe.json:dag_structures")
        state.knowledge_references.append("causal_inference_rwe.json:target_trial_emulation")

        treatment = pico.intervention if pico else "Experimental Treatment"
        outcome = pico.outcome if pico else "Clinical Endpoint"

        candidate_vars = [
            {"name": "Age", "role": "Confounder", "causes_treatment": True, "causes_outcome": True},
            {"name": "Sex", "role": "Confounder", "causes_treatment": True, "causes_outcome": True},
            {"name": "Baseline Disease Severity", "role": "Confounder", "causes_treatment": True, "causes_outcome": True},
            {"name": "Key Comorbidities (Diabetes, Hypertension, Renal Function)", "role": "Confounder", "causes_treatment": True, "causes_outcome": True},
            {"name": "Biomarker Intermediate (e.g., Blood Pressure reduction)", "role": "Mediator", "caused_by_treatment": True, "causes_outcome": True},
            {"name": "Post-treatment Hospital Admission Rate", "role": "Collider", "caused_by_treatment": True, "caused_by_outcome": True}
        ]

        dag_analysis = analyze_causal_dag(treatment, outcome, candidate_vars)

        # Formulate Target Trial Emulation protocol
        target_trial_spec = formulate_target_trial_emulation(
            research_question=state.raw_query,
            target_population=pico.population if pico else "Target Population",
            intervention_strategy=treatment,
            comparator_strategy=pico.comparison if pico else "Standard Comparator",
            primary_outcome=outcome
        )
        dag_analysis.target_trial_protocol = target_trial_spec

        state.causal_dag = dag_analysis
        state.add_log(self.name, "Causal Inference & Target Trial Analysis Completed", dag_analysis.model_dump())
        return dag_analysis
