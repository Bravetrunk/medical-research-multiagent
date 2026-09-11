import re
from typing import Optional
from agents.base import BaseMedicalAgent
from core.types import PICOQuestion, QuestionType
from core.state import ResearchState

class PICOAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="PICO & Question Formulator Agent",
            role="Clinical Epidemiologist & Evidence-Based Medicine Specialist",
            description="Deconstructs unstructured medical queries into formal PICO frameworks, classifies foreground question type, and assesses FINER criteria."
        )

    def process(self, state: ResearchState) -> PICOQuestion:
        query = state.raw_query.strip()
        state.add_log(self.name, "Formulating PICO and identifying research gap", {"raw_query": query})
        
        epi_knowledge = self.load_knowledge("clinical_epidemiology.json")
        state.knowledge_references.append("clinical_epidemiology.json:pico_framework")

        def deterministic_fallback():
            lower_q = query.lower()
            q_type = QuestionType.THERAPY
            if any(k in lower_q for k in ["diagnostic", "sensitivity", "specificity", "assay", "biomarker", "test", "roc", "accuracy"]):
                q_type = QuestionType.DIAGNOSIS
            elif any(k in lower_q for k in ["risk factor", "cause", "etiology", "harm", "toxic", "adverse"]):
                q_type = QuestionType.HARM
            elif any(k in lower_q for k in ["prognosis", "survival", "mortality rate", "trajectory", "recurrence"]):
                q_type = QuestionType.PROGNOSIS

            pop = "Adult clinical cohort"
            intervention = "Target medical intervention"
            comparison = "Standard of care or Active comparator"
            outcome = "Patient-important clinical endpoint"

            # 1. Check for explicit P: / I: / C: / O: prefixes
            explicit_found = False
            if "p:" in lower_q or "population:" in lower_q:
                m = re.search(r"(?:p|population):\s*([^;\n]+)", query, re.IGNORECASE)
                if m: pop = m.group(1).strip(); explicit_found = True
            if "i:" in lower_q or "intervention:" in lower_q:
                m = re.search(r"(?:i|intervention):\s*([^;\n]+)", query, re.IGNORECASE)
                if m: intervention = m.group(1).strip(); explicit_found = True
            if "c:" in lower_q or "comparison:" in lower_q:
                m = re.search(r"(?:c|comparison):\s*([^;\n]+)", query, re.IGNORECASE)
                if m: comparison = m.group(1).strip(); explicit_found = True
            if "o:" in lower_q or "outcome:" in lower_q:
                m = re.search(r"(?:o|outcome):\s*([^;\n]+)", query, re.IGNORECASE)
                if m: outcome = m.group(1).strip(); explicit_found = True

            # 2. Natural language clinical question pattern:
            # "In [P], does/can [I] [action] [O] compared (with/to) [C]?"
            if not explicit_found:
                nl_match = re.search(
                    r"in\s+(.+?),\s*(?:does|can|will|is)\s+(.+?)\s+(?:reduce|increase|improve|prevent|affect|decrease)\s+(.+?)\s+compared\s+(?:with|to)\s+(.+?)[\?\.]?$",
                    query,
                    re.IGNORECASE
                )
                if nl_match:
                    pop = nl_match.group(1).strip()
                    intervention = nl_match.group(2).strip()
                    outcome = nl_match.group(3).strip()
                    comparison = nl_match.group(4).strip()
                else:
                    # Diagnostic accuracy pattern:
                    # "... diagnostic accuracy ... of [I] compared to [C] for [O] in [P]"
                    diag_match = re.search(
                        r"diagnostic accuracy.*?of\s+(.+?)\s+compared\s+to\s+(.+?)\s+for\s+(.+?)(?:\s+in\s+(.+?))?[\?\.]?$",
                        query,
                        re.IGNORECASE
                    )
                    if diag_match:
                        intervention = diag_match.group(1).strip()
                        comparison = diag_match.group(2).strip()
                        outcome = diag_match.group(3).strip()
                        if diag_match.group(4):
                            pop = diag_match.group(4).strip()
                        else:
                            pop = "Suspected target patient population"
                    else:
                        pop = f"Patients presenting with condition described in: '{query}'"
                        intervention = "Target intervention under investigation"

            finer = {
                "Feasible": "Sufficient sample size and clinical facilities available",
                "Interesting": "Addresses high clinical uncertainty",
                "Novel": "Provides direct evidence where previous studies had gaps or conflicting results",
                "Ethical": "Conducted with clinical equipoise and institutional ethics approval",
                "Relevant": "Directly guides patient management and healthcare outcomes"
            }

            return PICOQuestion(
                topic=query,
                question_type=q_type,
                population=pop,
                intervention=intervention,
                comparison=comparison,
                outcome=outcome,
                secondary_outcomes=[
                    "Safety profile and adverse events",
                    "Health-related quality of life (HRQoL)",
                    "Healthcare resource utilization"
                ],
                finer_assessment=finer
            )

        pico_res = deterministic_fallback()
        state.pico = pico_res
        state.add_log(self.name, "PICO Formulation Completed", pico_res.model_dump())
        return pico_res
