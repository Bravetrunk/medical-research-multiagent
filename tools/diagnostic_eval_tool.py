from typing import Dict, Any, Optional
from core.calculators import calculate_diagnostic_metrics
from core.types import DiagnosticEvaluationResult

def run_diagnostic_analysis(
    tp: int,
    fp: int,
    fn: int,
    tn: int,
    pre_test_prob: Optional[float] = None
) -> DiagnosticEvaluationResult:
    """
    Evaluates diagnostic performance, Likelihood Ratios, and Bayesian Fagan Nomogram metrics.
    Grounding: Topic 8 & Fletcher Chapter 3.
    """
    res = calculate_diagnostic_metrics(tp, fp, fn, tn, pre_test_prob)
    
    # Interpretation text based on Topic 8 rules
    lr_p = res["lr_plus"]
    lr_m = res["lr_minus"]
    
    lr_p_text = (
        "conclusively rules IN the diagnosis (LR+ > 10)" if lr_p >= 10 else
        ("provides moderate evidence to rule in (LR+ 5-10)" if lr_p >= 5 else
        ("provides small shift in probability (LR+ 2-5)" if lr_p >= 2 else "is uninformative (LR+ near 1)"))
    )
    lr_m_text = (
        "conclusively rules OUT the diagnosis (LR- < 0.1)" if lr_m <= 0.1 else
        ("provides moderate evidence to rule out (LR- 0.1-0.2)" if lr_m <= 0.2 else
        ("provides small shift in probability (LR- 0.2-0.5)" if lr_m <= 0.5 else "is uninformative (LR- near 1)"))
    )
    
    interpretation = (
        f"Test shows Sensitivity of {res['sensitivity']*100:.1f}% ({res['snnout_rule_out_power']}) and "
        f"Specificity of {res['specificity']*100:.1f}% ({res['sppin_rule_in_power']}).\n"
        f"At baseline prevalence of {res['pre_test_prob']*100:.1f}%, a POSITIVE test increases probability to "
        f"{res['post_test_prob_positive']*100:.1f}% (LR+ = {lr_p}, {lr_p_text}).\n"
        f"A NEGATIVE test decreases probability to {res['post_test_prob_negative']*100:.1f}% (LR- = {lr_m}, {lr_m_text}).\n"
        f"Overall Youden's Index J = {res['youden_index']:.3f}."
    )
    
    return DiagnosticEvaluationResult(
        tp=tp,
        fp=fp,
        fn=fn,
        tn=tn,
        total_sample=res["total"],
        prevalence=res["prevalence"],
        sensitivity=res["sensitivity"],
        specificity=res["specificity"],
        ppv=res["ppv"],
        npv=res["npv"],
        accuracy=res["accuracy"],
        lr_plus=res["lr_plus"],
        lr_minus=res["lr_minus"],
        youden_index=res["youden_index"],
        pre_test_prob=res["pre_test_prob"],
        post_test_prob_positive=res["post_test_prob_positive"],
        post_test_prob_negative=res["post_test_prob_negative"],
        clinical_interpretation=interpretation
    )
