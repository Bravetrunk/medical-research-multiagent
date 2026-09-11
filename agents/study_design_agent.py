from agents.base import BaseMedicalAgent
from core.types import StudyDesignType, StudyDesignRecommendation, QuestionType
from core.state import ResearchState

class StudyDesignAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="Study Design & Protocol Architect Agent",
            role="Senior Clinical Trialist & Methodologist",
            description="Selects and architects optimal clinical study designs based on EBM hierarchy, question type, feasibility, and bias control."
        )

    def process(self, state: ResearchState) -> StudyDesignRecommendation:
        pico = state.pico
        state.add_log(self.name, "Architecting optimal study design", {"question_type": pico.question_type.value if pico else "Unknown"})
        
        epi_knowledge = self.load_knowledge("clinical_epidemiology.json")
        state.knowledge_references.append("clinical_epidemiology.json:study_designs")

        def deterministic_design():
            q_type = pico.question_type if pico else QuestionType.THERAPY
            
            if q_type == QuestionType.THERAPY:
                selected = StudyDesignType.RCT_PARALLEL
                justification = (
                    "Randomized Controlled Trial (RCT) is the gold standard for therapeutic interventions. "
                    "Randomization balances both known and unknown confounders across arms, establishing true internal validity."
                )
                safeguards = [
                    "Computer-generated central block randomization with stratification by baseline severity",
                    "Allocation concealment using sequentially numbered opaque sealed envelopes (SNOSE) or interactive web response system",
                    "Double-blind design (participants, clinical care team, and outcome adjudicators)",
                    "Strict Intention-to-Treat (ITT) principle preserving prognostic balance of randomized groups"
                ]
                biases = [
                    {"name": "Selection Bias", "mitigation": "Robust allocation concealment"},
                    {"name": "Performance Bias", "mitigation": "Double-blinding with matched placebo"},
                    {"name": "Attrition Bias", "mitigation": "Retention protocol and multiple imputation for missing endpoints"}
                ]
                alternatives = ["Cluster RCT (if intervention is delivered at facility level)", "Pragmatic RCT (for real-world effectiveness)"]

            elif q_type == QuestionType.DIAGNOSIS:
                selected = StudyDesignType.DIAGNOSTIC_ACCURACY
                justification = (
                    "Cross-sectional diagnostic accuracy study comparing index test against an established reference standard (Gold Standard). "
                    "Enables calculation of Sensitivity, Specificity, Likelihood Ratios, and ROC/AUC."
                )
                safeguards = [
                    "Consecutive or random recruitment of eligible patients suspected of harboring target condition",
                    "Independent and blinded interpretation of index test and reference standard",
                    "Verification of all patients with reference standard to eliminate partial/differential workup bias",
                    "Prespecified diagnostic cutoff threshold"
                ]
                biases = [
                    {"name": "Verification / Workup Bias", "mitigation": "All patients receive reference standard regardless of index test result"},
                    {"name": "Review / Observer Bias", "mitigation": "Blinded evaluation of tests"},
                    {"name": "Spectrum Bias", "mitigation": "Include full spectrum of mild, moderate, and severe cases alongside relevant differential diagnoses"}
                ]
                alternatives = ["Prospective paired diagnostic cohort"]

            elif q_type == QuestionType.HARM or q_type == QuestionType.ETIOLOGY:
                # Observational Cohort or Target Trial
                selected = StudyDesignType.COHORT_PROSPECTIVE
                justification = (
                    "Prospective cohort design ensures temporality (exposure strictly documented before outcome onset). "
                    "Randomization is unethical or impractical for evaluating harmful exposures."
                )
                safeguards = [
                    "Objective verification and quantification of exposure at baseline",
                    "Active follow-up with standardized endpoint adjudication",
                    "Comprehensive baseline covariate measurement for multivariable confounding adjustment"
                ]
                biases = [
                    {"name": "Confounding by Indication", "mitigation": "Propensity score matching or multivariable Cox modeling"},
                    {"name": "Loss to Follow-up Bias", "mitigation": "Censoring sensitivity analyses and inverse probability weighting"},
                    {"name": "Information / Recall Bias", "mitigation": "Prospective registry data collection"}
                ]
                alternatives = ["Target Trial Emulation (RWD/RWE)", "Nested Case-Control Study"]

            else: # Prognosis
                selected = StudyDesignType.COHORT_PROSPECTIVE
                justification = (
                    "Inception cohort of patients enrolled at a uniform, early point in the course of their disease, "
                    "followed forward in time to measure time-to-event outcomes (survival analysis)."
                )
                safeguards = [
                    "Uniform inception point (e.g. at initial clinical diagnosis)",
                    "Objective prognostic factor measurement",
                    "Complete follow-up over sufficient time horizon"
                ]
                biases = [
                    {"name": "Lead-Time Bias", "mitigation": "Strict definition of inception point"},
                    {"name": "Attrition Bias", "mitigation": "Kaplan-Meier censoring tracking"}
                ]
                alternatives = ["Retrospective registry cohort"]

            return StudyDesignRecommendation(
                selected_design=selected,
                justification=justification,
                alternative_designs=alternatives,
                key_methodological_safeguards=safeguards,
                anticipated_biases=biases,
                ethical_considerations="Protocol complies with Declaration of Helsinki, GCP guidelines, and requires Institutional Review Board (IRB) approval."
            )

        recommendation = deterministic_design()
        state.study_design = recommendation
        state.add_log(self.name, "Study Design Recommendation Completed", recommendation.model_dump())
        return recommendation
