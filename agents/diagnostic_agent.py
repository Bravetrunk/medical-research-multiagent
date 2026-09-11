from typing import Optional
from agents.base import BaseMedicalAgent
from core.types import DiagnosticEvaluationResult, QuestionType
from core.state import ResearchState
from tools.diagnostic_eval_tool import run_diagnostic_analysis

class DiagnosticAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="Diagnostic Accuracy & Clinical Decision Evaluator Agent",
            role="Clinical Pathologist & Diagnostic Test Methodologist",
            description="Evaluates diagnostic 2x2 performance matrices, SnNout/SpPin rules, Likelihood Ratios, and Bayesian Fagan Nomogram updates (Topic 8 & Fletcher)."
        )

    def process(self, state: ResearchState, tp: int = 85, fp: int = 15, fn: int = 15, tn: int = 85, pre_test_prob: Optional[float] = 0.20) -> Optional[DiagnosticEvaluationResult]:
        pico = state.pico
        if pico and pico.question_type != QuestionType.DIAGNOSIS and "diagnostic" not in state.raw_query.lower() and "biomarker" not in state.raw_query.lower():
            state.add_log(self.name, "Skipped (Not a diagnostic research question)")
            return None
            
        state.add_log(self.name, "Evaluating diagnostic accuracy and Likelihood Ratios", {"tp": tp, "fp": fp, "fn": fn, "tn": tn})
        state.knowledge_references.append("diagnostic_performance.json:metrics")
        state.knowledge_references.append("diagnostic_performance.json:bayesian_nomogram")

        diag_res = run_diagnostic_analysis(tp, fp, fn, tn, pre_test_prob=pre_test_prob)
        state.diagnostic_eval = diag_res
        state.add_log(self.name, "Diagnostic Accuracy Evaluation Completed", diag_res.model_dump())
        return diag_res
