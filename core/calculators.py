import math
from typing import Dict, Any, Tuple

def get_z_score(p: float) -> float:
    """
    Returns standard normal critical value Z for given two-tailed significance alpha
    or upper tail probability.
    """
    # Common standard critical values in Biostatistics
    table = {
        0.001: 3.291,
        0.01: 2.576,
        0.02: 2.326,
        0.025: 1.960,
        0.05: 1.960,  # two-tailed alpha 0.05 -> Z = 1.96
        0.10: 1.645,  # two-tailed alpha 0.10 -> Z = 1.645 or beta 0.10 -> power 90% Z=1.282
        0.15: 1.036,
        0.20: 0.842   # beta 0.20 -> power 80% Z = 0.842
    }
    if p in table:
        return table[p]
    
    # Accurate rational approximation for standard normal inverse CDF (Wichura / Abramowitz & Stegun)
    if p <= 0 or p >= 1:
        raise ValueError("Probability p must be in (0, 1)")
    
    # Use erf inverse approximation
    q = p / 2.0 if p < 0.5 else (1.0 - p) / 2.0
    t = math.sqrt(-2.0 * math.log(q))
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.189269
    d3 = 0.001308
    z = t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0)
    return z

def calculate_sample_size_two_means(
    mu1: float,
    mu2: float,
    sigma: float,
    alpha: float = 0.05,
    power: float = 0.80,
    dropout_rate: float = 0.15
) -> Dict[str, Any]:
    """
    Sample size calculation for comparing two independent continuous means (Daniel 9th ed. Chapter 7).
    Formula: n = 2 * (Z_alpha/2 + Z_beta)^2 * sigma^2 / (mu1 - mu2)^2
    """
    delta = abs(mu1 - mu2)
    if delta == 0:
        raise ValueError("Difference between means (mu1 - mu2) cannot be zero")
    if sigma <= 0:
        raise ValueError("Standard deviation sigma must be positive")
    
    z_alpha = 1.960 if alpha == 0.05 else get_z_score(alpha)
    beta = 1.0 - power
    z_beta = 0.842 if abs(beta - 0.20) < 0.01 else (1.282 if abs(beta - 0.10) < 0.01 else get_z_score(beta))
    
    numerator = 2.0 * ((z_alpha + z_beta) ** 2) * (sigma ** 2)
    denominator = delta ** 2
    n_per_arm = math.ceil(numerator / denominator)
    total_n = n_per_arm * 2
    total_n_with_dropout = math.ceil(total_n / (1.0 - dropout_rate))
    
    return {
        "formula": "n = 2 * (Z_alpha/2 + Z_beta)^2 * sigma^2 / (mu1 - mu2)^2",
        "alpha": alpha,
        "power": power,
        "z_alpha": round(z_alpha, 3),
        "z_beta": round(z_beta, 3),
        "delta": round(delta, 4),
        "sigma": round(sigma, 4),
        "n_per_arm": n_per_arm,
        "total_n": total_n,
        "total_n_with_dropout": total_n_with_dropout,
        "dropout_rate": dropout_rate
    }

def calculate_sample_size_two_proportions(
    p1: float,
    p2: float,
    alpha: float = 0.05,
    power: float = 0.80,
    dropout_rate: float = 0.15
) -> Dict[str, Any]:
    """
    Sample size calculation for comparing two independent proportions (Daniel 9th ed. Chapter 7).
    """
    if not (0 < p1 < 1 and 0 < p2 < 1):
        raise ValueError("Proportions p1 and p2 must be strictly between 0 and 1")
    delta = abs(p1 - p2)
    if delta == 0:
        raise ValueError("Difference between proportions (p1 - p2) cannot be zero")
        
    z_alpha = 1.960 if alpha == 0.05 else get_z_score(alpha)
    beta = 1.0 - power
    z_beta = 0.842 if abs(beta - 0.20) < 0.01 else (1.282 if abs(beta - 0.10) < 0.01 else get_z_score(beta))
    
    p_bar = (p1 + p2) / 2.0
    term1 = z_alpha * math.sqrt(2.0 * p_bar * (1.0 - p_bar))
    term2 = z_beta * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    
    n_per_arm = math.ceil(((term1 + term2) ** 2) / (delta ** 2))
    total_n = n_per_arm * 2
    total_n_with_dropout = math.ceil(total_n / (1.0 - dropout_rate))
    
    return {
        "formula": "n = (Z_alpha/2 * sqrt(2*p_bar*(1-p_bar)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p1 - p2)^2",
        "alpha": alpha,
        "power": power,
        "p1": p1,
        "p2": p2,
        "delta": round(delta, 4),
        "n_per_arm": n_per_arm,
        "total_n": total_n,
        "total_n_with_dropout": total_n_with_dropout,
        "dropout_rate": dropout_rate
    }

def calculate_diagnostic_metrics(tp: int, fp: int, fn: int, tn: int, pre_test_prob: float = None) -> Dict[str, Any]:
    """
    Computes all standard diagnostic accuracy metrics, Likelihood Ratios, and Bayesian post-test updates.
    (Topic 8 & Fletcher Chapter 3)
    """
    total = tp + fp + fn + tn
    if total == 0:
        raise ValueError("Total sample size in 2x2 contingency table cannot be 0")
        
    diseased = tp + fn
    non_diseased = fp + tn
    test_positive = tp + fp
    test_negative = fn + tn
    
    prevalence = diseased / total
    prior_prob = pre_test_prob if pre_test_prob is not None else prevalence
    
    sensitivity = tp / diseased if diseased > 0 else 0.0
    specificity = tn / non_diseased if non_diseased > 0 else 0.0
    ppv = tp / test_positive if test_positive > 0 else 0.0
    npv = tn / test_negative if test_negative > 0 else 0.0
    accuracy = (tp + tn) / total
    youden_index = sensitivity + specificity - 1.0
    
    # Likelihood Ratios
    fpr = 1.0 - specificity
    fnr = 1.0 - sensitivity
    
    lr_plus = sensitivity / fpr if fpr > 0 else 999.0
    lr_minus = fnr / specificity if specificity > 0 else 0.001
    
    # Bayesian Fagan Nomogram Calculation
    # Pre-test Odds = P / (1 - P)
    prior_prob_clamped = min(max(prior_prob, 0.0001), 0.9999)
    pre_test_odds = prior_prob_clamped / (1.0 - prior_prob_clamped)
    
    # Post-test Odds Positive = Pre-test Odds * LR+
    post_test_odds_pos = pre_test_odds * lr_plus
    post_test_prob_pos = post_test_odds_pos / (1.0 + post_test_odds_pos)
    
    # Post-test Odds Negative = Pre-test Odds * LR-
    post_test_odds_neg = pre_test_odds * lr_minus
    post_test_prob_neg = post_test_odds_neg / (1.0 + post_test_odds_neg)
    
    # Clinical Heuristics
    snnout = sensitivity >= 0.90
    sppin = specificity >= 0.90
    
    return {
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "total": total,
        "prevalence": round(prevalence, 4),
        "sensitivity": round(sensitivity, 4),
        "specificity": round(specificity, 4),
        "ppv": round(ppv, 4),
        "npv": round(npv, 4),
        "accuracy": round(accuracy, 4),
        "youden_index": round(youden_index, 4),
        "lr_plus": round(lr_plus, 3),
        "lr_minus": round(lr_minus, 3),
        "pre_test_prob": round(prior_prob, 4),
        "post_test_prob_positive": round(post_test_prob_pos, 4),
        "post_test_prob_negative": round(post_test_prob_neg, 4),
        "snnout_rule_out_power": "High (SnNout applicable)" if snnout else "Moderate/Low",
        "sppin_rule_in_power": "High (SpPin applicable)" if sppin else "Moderate/Low"
    }

def calculate_epidemiologic_association(
    exposed_cases: int,
    exposed_non_cases: int,
    unexposed_cases: int,
    unexposed_non_cases: int
) -> Dict[str, Any]:
    """
    Computes Risk Ratio, Odds Ratio, Absolute Risk Reduction, and Number Needed to Treat (NNT).
    (Topic 3 & Topic 4)
    """
    a = exposed_cases
    b = exposed_non_cases
    c = unexposed_cases
    d = unexposed_non_cases
    
    n_exposed = a + b
    n_unexposed = c + d
    
    risk_exposed = a / n_exposed if n_exposed > 0 else 0.0
    risk_unexposed = c / n_unexposed if n_unexposed > 0 else 0.0
    
    rr = risk_exposed / risk_unexposed if risk_unexposed > 0 else 0.0
    odds_exposed = a / b if b > 0 else 0.0
    odds_unexposed = c / d if d > 0 else 0.0
    odds_ratio = (a * d) / (b * c) if (b * c) > 0 else 0.0
    
    # Absolute Risk Reduction (ARR) or Risk Difference (RD)
    arr = risk_unexposed - risk_exposed
    nnt = math.ceil(1.0 / arr) if arr > 0 else None
    
    # Attributable Risk Percent in exposed
    ar_percent = ((rr - 1.0) / rr * 100.0) if rr > 0 else 0.0
    
    return {
        "risk_exposed": round(risk_exposed, 4),
        "risk_unexposed": round(risk_unexposed, 4),
        "risk_ratio_rr": round(rr, 3),
        "odds_ratio_or": round(odds_ratio, 3),
        "absolute_risk_reduction_arr": round(arr, 4),
        "number_needed_to_treat_nnt": nnt,
        "attributable_risk_percent": round(ar_percent, 2),
        "rare_disease_assumption_met": (a + c) / (n_exposed + n_unexposed) < 0.10
    }
