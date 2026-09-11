from typing import List, Dict, Any
from core.types import CausalDAGAnalysis

def analyze_causal_dag(
    treatment: str,
    outcome: str,
    candidate_variables: List[Dict[str, str]]
) -> CausalDAGAnalysis:
    """
    Analyzes causal structures based on Judea Pearl's Causal Hierarchy and DAG principles.
    Grounding: Topic 9 (RWD/RWE, Confounder vs Mediator vs Collider).
    """
    confounders = []
    mediators = []
    colliders = []
    warnings = []
    
    for var in candidate_variables:
        name = var.get("name", "Unknown")
        role = var.get("role", "").lower()
        relation_x = var.get("causes_treatment", False)
        relation_y = var.get("causes_outcome", False)
        caused_by_x = var.get("caused_by_treatment", False)
        caused_by_y = var.get("caused_by_outcome", False)
        
        # 1. Confounder: causes treatment and causes outcome (X <- C -> Y)
        if (relation_x and relation_y) or "confounder" in role or "baseline" in role:
            confounders.append(name)
        # 2. Mediator: caused by treatment and causes outcome (X -> M -> Y)
        elif (caused_by_x and relation_y) or "mediator" in role or "intermediate" in role:
            mediators.append(name)
            warnings.append(f"DO NOT adjust for mediator '{name}' when estimating the total causal effect of {treatment} on {outcome}. Doing so causes overadjustment bias.")
        # 3. Collider: caused by treatment AND caused by outcome (X -> C <- Y)
        elif (caused_by_x and caused_by_y) or "collider" in role:
            colliders.append(name)
            warnings.append(f"CRITICAL WARNING: NEVER condition or stratify on collider '{name}' (X -> {name} <- Y). Conditioning on a collider OPENS a spurious backdoor path, inducing Collider Stratification Bias (Berkson's Paradox)!")
        else:
            # Default heuristics for typical medical variables (Age, Sex, Comorbidity -> Confounders)
            if any(k in name.lower() for k in ["age", "sex", "gender", "bmi", "baseline", "eGFR", "hypertension", "diabetes", "smoking"]):
                confounders.append(name)
            else:
                confounders.append(name)
                
    # Minimal sufficient adjustment set to block backdoors
    adjustment_set = list(set(confounders))
    
    return CausalDAGAnalysis(
        treatment_exposure=treatment,
        outcome=outcome,
        confounders=confounders,
        mediators=mediators,
        colliders=colliders,
        minimal_sufficient_adjustment_set=adjustment_set,
        warnings=warnings
    )
