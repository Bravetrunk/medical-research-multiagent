from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class QuestionType(str, Enum):
    THERAPY = "Therapy"
    HARM = "Harm / Etiology"
    DIAGNOSIS = "Diagnosis"
    PROGNOSIS = "Prognosis"
    ETIOLOGY = "Etiology"

class StudyDesignType(str, Enum):
    RCT_PARALLEL = "Parallel Randomized Controlled Trial"
    RCT_CROSSOVER = "Crossover Randomized Controlled Trial"
    RCT_FACTORIAL = "Factorial (2x2) RCT"
    RCT_CLUSTER = "Cluster RCT"
    COHORT_PROSPECTIVE = "Prospective Cohort Study"
    COHORT_RETROSPECTIVE = "Retrospective Cohort Study"
    CASE_CONTROL = "Case-Control Study"
    NESTED_CASE_CONTROL = "Nested Case-Control Study"
    CROSS_SECTIONAL = "Cross-Sectional Study"
    DIAGNOSTIC_ACCURACY = "Cross-Sectional Diagnostic Accuracy Study"
    TARGET_TRIAL_EMULATION = "Target Trial Emulation (RWD/RWE)"

class PICOQuestion(BaseModel):
    topic: str = Field(..., description="General clinical research topic")
    question_type: QuestionType = Field(QuestionType.THERAPY, description="Clinical question classification")
    population: str = Field(..., description="Target population / Patient condition / Setting")
    intervention: str = Field(..., description="Experimental treatment, exposure, or index diagnostic test")
    comparison: str = Field("Standard of Care / Placebo", description="Active control, placebo, or reference standard")
    outcome: str = Field(..., description="Primary patient-important outcome (clinical endpoint)")
    secondary_outcomes: List[str] = Field(default_factory=list, description="Secondary or surrogate endpoints")
    finer_assessment: Dict[str, str] = Field(
        default_factory=lambda: {
            "Feasible": "Assess sample size, clinical resources, time, technical expertise",
            "Interesting": "Novel insights for clinical community",
            "Novel": "Addresses an established clinical evidence gap",
            "Ethical": "Adheres to Declaration of Helsinki, equipoise maintained",
            "Relevant": "Impacts clinical decision-making, patient outcomes, or health policy"
        }
    )

class StudyDesignRecommendation(BaseModel):
    selected_design: StudyDesignType
    justification: str
    alternative_designs: List[str] = Field(default_factory=list)
    key_methodological_safeguards: List[str] = Field(default_factory=list)
    anticipated_biases: List[Dict[str, str]] = Field(default_factory=list)
    ethical_considerations: str = ""

class SampleSizeResult(BaseModel):
    formula_used: str
    alpha: float = 0.05
    power: float = 0.80
    effect_size_metric: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    n_per_arm: int
    total_n: int
    total_n_with_dropout: int
    dropout_rate_assumed: float = 0.15
    recommendations: str

class DiagnosticEvaluationResult(BaseModel):
    tp: int
    fp: int
    fn: int
    tn: int
    total_sample: int
    prevalence: float
    sensitivity: float
    specificity: float
    ppv: float
    npv: float
    accuracy: float
    lr_plus: float
    lr_minus: float
    youden_index: float
    pre_test_prob: float
    post_test_prob_positive: float
    post_test_prob_negative: float
    clinical_interpretation: str

class CausalDAGAnalysis(BaseModel):
    treatment_exposure: str
    outcome: str
    confounders: List[str] = Field(default_factory=list)
    mediators: List[str] = Field(default_factory=list)
    colliders: List[str] = Field(default_factory=list)
    minimal_sufficient_adjustment_set: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    target_trial_protocol: Optional[Dict[str, str]] = None

class CriticalAppraisalItem(BaseModel):
    criterion: str
    rating: str  # e.g., "Met", "Unclear", "High Risk of Bias", "Low Risk of Bias"
    explanation: str

class CriticalAppraisalReport(BaseModel):
    guideline_used: str  # CONSORT, STROBE, PRISMA, STARD, TRIPOD, CASP
    overall_validity: str
    internal_validity_score: str
    external_validity_score: str
    key_findings: List[str] = Field(default_factory=list)
    identified_biases: List[str] = Field(default_factory=list)
    detailed_checklist: List[CriticalAppraisalItem] = Field(default_factory=list)
    bradford_hill_evaluation: Optional[Dict[str, str]] = None
    clinical_recommendation: str

class ResearchProtocol(BaseModel):
    title: str
    investigators: str = "Multidisciplinary Clinical Research Team"
    pico: PICOQuestion
    background_and_gap: str
    study_design: StudyDesignRecommendation
    biostatistics_plan: SampleSizeResult
    causal_dag_or_rwe: Optional[CausalDAGAnalysis] = None
    diagnostic_evaluation: Optional[DiagnosticEvaluationResult] = None
    appraisal_compliance: Optional[CriticalAppraisalReport] = None
    statistical_analysis_plan_summary: str
    references: List[str] = Field(default_factory=list)
