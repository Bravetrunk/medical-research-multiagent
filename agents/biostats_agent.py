from agents.base import BaseMedicalAgent
from core.types import SampleSizeResult, QuestionType
from core.state import ResearchState
from tools.sample_size_tool import run_sample_size_planning

class BiostatisticsAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="Biostatistics & Sample Size Planner Agent",
            role="Lead Biostatistician",
            description="Designs statistical analysis plans (SAP), determines test selection rules (Daniel 9th ed.), and computes formal sample size requirements."
        )

    def process(self, state: ResearchState) -> SampleSizeResult:
        state.add_log(self.name, "Calculating sample size and defining statistical analysis plan")
        state.knowledge_references.append("biostatistics_daniel.json:hypothesis_testing")
        state.knowledge_references.append("biostatistics_daniel.json:test_selection_matrix")

        pico = state.pico
        q_type = pico.question_type if pico else QuestionType.THERAPY

        # Determine outcome type based on clinical question
        outcome_text = (pico.outcome if pico else "").lower()
        if any(k in outcome_text for k in ["rate", "proportion", "incidence", "death", "mortality", "remission", "response rate", "event"]):
            res = run_sample_size_planning("binary", p1=0.25, p2=0.15, alpha=0.05, power=0.80, dropout_rate=0.15)
        elif any(k in outcome_text for k in ["score", "blood pressure", "hba1c", "level", "reduction", "weight", "ldl", "change"]):
            res = run_sample_size_planning("continuous", mu1=10.0, mu2=13.0, sigma=6.0, alpha=0.05, power=0.80, dropout_rate=0.15)
        else:
            # Default to robust binary event sample size
            res = run_sample_size_planning("binary", p1=0.25, p2=0.15, alpha=0.05, power=0.80, dropout_rate=0.15)

        state.biostats_plan = res
        state.add_log(self.name, "Sample Size Planning Completed", res.model_dump())
        return res
