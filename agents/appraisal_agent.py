from agents.base import BaseMedicalAgent
from core.types import CriticalAppraisalReport, StudyDesignType
from core.state import ResearchState
from tools.appraisal_checklist_tool import appraise_study_design

class AppraisalAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="Critical Appraisal & Reporting Guideline Guardian",
            role="Senior Evidence-Based Medicine Reviewer",
            description="Audits study design against international reporting standards (CONSORT, STROBE, PRISMA, STARD) and CASP checklists (Topic 4)."
        )

    def process(self, state: ResearchState) -> CriticalAppraisalReport:
        design = state.study_design
        study_type = design.selected_design.value if design else "Randomized Controlled Trial"
        
        state.add_log(self.name, f"Auditing study protocol against reporting standards for {study_type}")
        state.knowledge_references.append("reporting_guidelines.json:reporting_checklists")
        state.knowledge_references.append("reporting_guidelines.json:casp_appraisal_framework")

        methodology_details = {
            "randomization": True,
            "allocation_concealment": True,
            "blinding": "Double-blind",
            "itt_analysis": True
        }

        report = appraise_study_design(study_type, methodology_details)
        state.critical_appraisal = report
        state.add_log(self.name, "Critical Appraisal Completed", report.model_dump())
        return report
