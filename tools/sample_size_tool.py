from typing import Dict, Any, Optional
from core.calculators import calculate_sample_size_two_means, calculate_sample_size_two_proportions
from core.types import SampleSizeResult

def run_sample_size_planning(
    outcome_type: str,
    mu1: Optional[float] = None,
    mu2: Optional[float] = None,
    sigma: Optional[float] = None,
    p1: Optional[float] = None,
    p2: Optional[float] = None,
    alpha: float = 0.05,
    power: float = 0.80,
    dropout_rate: float = 0.15
) -> SampleSizeResult:
    """
    Automated Sample Size Determination tool for Medical Research based on Daniel 9th ed. Chapter 7.
    """
    if outcome_type.lower() in ["continuous", "mean", "measurement"]:
        if mu1 is None or mu2 is None or sigma is None:
            # Provide clinical standard defaults if not specified
            mu1 = mu1 or 10.0
            mu2 = mu2 or 12.5
            sigma = sigma or 5.0
        res = calculate_sample_size_two_means(mu1, mu2, sigma, alpha, power, dropout_rate)
        return SampleSizeResult(
            formula_used=res["formula"],
            alpha=alpha,
            power=power,
            effect_size_metric=f"Difference in Means (Delta = {res['delta']}, SD = {res['sigma']})",
            parameters={"mu1": mu1, "mu2": mu2, "sigma": sigma},
            n_per_arm=res["n_per_arm"],
            total_n=res["total_n"],
            total_n_with_dropout=res["total_n_with_dropout"],
            dropout_rate_assumed=dropout_rate,
            recommendations=(
                f"Recruit at least {res['total_n_with_dropout']} patients ({math_ceil_half(res['total_n_with_dropout'])} per arm) "
                f"to achieve {int(power*100)}% power at two-sided alpha {alpha}, assuming a {int(dropout_rate*100)}% loss to follow-up."
            )
        )
    else: # Binary / proportion
        p1 = p1 or 0.25
        p2 = p2 or 0.15
        res = calculate_sample_size_two_proportions(p1, p2, alpha, power, dropout_rate)
        return SampleSizeResult(
            formula_used=res["formula"],
            alpha=alpha,
            power=power,
            effect_size_metric=f"Proportion Reduction ({p1*100:.1f}% vs {p2*100:.1f}%, Delta = {res['delta']*100:.1f}%)",
            parameters={"p1": p1, "p2": p2},
            n_per_arm=res["n_per_arm"],
            total_n=res["total_n"],
            total_n_with_dropout=res["total_n_with_dropout"],
            dropout_rate_assumed=dropout_rate,
            recommendations=(
                f"Recruit at least {res['total_n_with_dropout']} patients ({math_ceil_half(res['total_n_with_dropout'])} per arm) "
                f"to achieve {int(power*100)}% power at two-sided alpha {alpha}, accounting for {int(dropout_rate*100)}% attrition."
            )
        )

def math_ceil_half(val: int) -> int:
    return (val + 1) // 2
