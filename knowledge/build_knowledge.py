import json
import os

target_dir = "/Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/knowledge"
os.makedirs(target_dir, exist_ok=True)

# 2. Biostatistics (Daniel 9th ed & Topic 3)
biostats = {
    "module": "Biostatistics and Clinical Inference",
    "source": "Daniel (Biostatistics 9th ed.) & Topic 3 & Topic 8",
    "hypothesis_testing": {
        "null_hypothesis_H0": "No difference / no association",
        "alternative_hypothesis_Ha": "True difference / association exists",
        "type_I_error_alpha": "Rejecting true H0 (False Positive), standard = 0.05",
        "type_II_error_beta": "Failing to reject false H0 (False Negative), standard = 0.20 or 0.10",
        "statistical_power": "1 - beta (Probability of detecting a true effect, standard = 80% or 90%)",
        "p_value_definition": "Probability of observing a test statistic as extreme as, or more extreme than, the observed value under H0. Does NOT equal P(H0 is true)!"
    },
    "test_selection_matrix": {
        "continuous_independent_2_groups": {
            "parametric_normal": "Two-sample Student t-test",
            "non_parametric_skewed": "Mann-Whitney U test / Wilcoxon Rank-Sum test"
        },
        "continuous_paired_2_groups": {
            "parametric_normal": "Paired Student t-test",
            "non_parametric_skewed": "Wilcoxon Signed-Rank test"
        },
        "continuous_k_groups": {
            "parametric_normal": "One-Way Analysis of Variance (ANOVA) + Post-hoc (Tukey / Bonferroni)",
            "non_parametric_skewed": "Kruskal-Wallis H test"
        },
        "categorical_2x2": {
            "expected_all_ge_5": "Pearson Chi-Square test",
            "expected_any_lt_5": "Fisher Exact test",
            "paired_proportions": "McNemar test"
        },
        "time_to_event": {
            "univariable_curve": "Kaplan-Meier estimator + Log-Rank test",
            "multivariable_hazard": "Cox Proportional Hazards Regression"
        },
        "multivariable_regression": {
            "continuous_outcome": "Multiple Linear Regression",
            "binary_outcome": "Multivariable Logistic Regression (produces Adjusted OR)",
            "count_rate_outcome": "Poisson / Negative Binomial Regression"
        }
    },
    "sample_size_formulas": {
        "single_mean": "n = (Z^2 * sigma^2) / d^2",
        "single_proportion": "n = (Z^2 * p * (1-p)) / d^2",
        "two_means_comparison": "n = 2 * (Z_alpha2 + Z_beta)^2 * sigma^2 / (mu1 - mu2)^2",
        "two_proportions_comparison": "n = (Z_alpha2 * sqrt(2*p_bar*(1-p_bar)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p1 - p2)^2",
        "diagnostic_study": "n = (Z^2 * Sens * (1 - Sens)) / (d^2 * Prevalence)"
    },
    "measures_of_effect": {
        "Risk_Ratio_RR": "[a/(a+b)] / [c/(c+d)]",
        "Odds_Ratio_OR": "(a*d) / (b*c)",
        "Absolute_Risk_Reduction_ARR": "Risk_control - Risk_intervention",
        "Number_Needed_to_Treat_NNT": "1 / ARR",
        "Attributable_Risk_Percent_AR_pct": "(RR - 1) / RR * 100",
        "Population_Attributable_Fraction_PAF": "P_pop * (RR - 1) / (1 + P_pop * (RR - 1))"
    }
}

# 3. Diagnostic Studies & Performance (Topic 8)
diagnostic = {
    "module": "Diagnostic Studies & Performance Matrices",
    "source": "Topic 8 & Fletcher Chapter 3",
    "contingency_table": {
        "TP": "True Positive (Disease +, Test +)",
        "FP": "False Positive (Disease -, Test +)",
        "FN": "False Negative (Disease +, Test -)",
        "TN": "True Negative (Disease -, Test -)"
    },
    "metrics": {
        "Sensitivity": {
            "formula": "TP / (TP + FN)",
            "meaning": "Ability to correctly identify diseased patients",
            "rule": "SnNout: High Sensitivity, Negative test rules OUT disease"
        },
        "Specificity": {
            "formula": "TN / (TN + FP)",
            "meaning": "Ability to correctly identify non-diseased individuals",
            "rule": "SpPin: High Specificity, Positive test rules IN disease"
        },
        "PPV": {
            "formula": "TP / (TP + FP)",
            "meaning": "Probability of disease given positive test",
            "prevalence_dependency": "Strongly decreases as disease prevalence decreases"
        },
        "NPV": {
            "formula": "TN / (TN + FN)",
            "meaning": "Probability of no disease given negative test",
            "prevalence_dependency": "Increases as disease prevalence decreases"
        },
        "Likelihood_Ratio_Positive_LR_plus": {
            "formula": "Sensitivity / (1 - Specificity)",
            "clinical_utility": "> 10 very strong rule-in, 5-10 moderate, 2-5 small, 1 uninformative"
        },
        "Likelihood_Ratio_Negative_LR_minus": {
            "formula": "(1 - Sensitivity) / Specificity",
            "clinical_utility": "< 0.1 very strong rule-out, 0.1-0.2 moderate, 0.2-0.5 small, 1 uninformative"
        },
        "ROC_AUC": {
            "description": "Plot of Sensitivity (y) vs 1-Specificity (x) across all thresholds",
            "interpretation": "> 0.9 Outstanding, 0.8-0.9 Excellent, 0.7-0.8 Acceptable, 0.5 Chance"
        },
        "Youden_Index_J": "Sensitivity + Specificity - 1 (Optimal cutoff balancing Sens and Spec)"
    },
    "bayesian_nomogram": {
        "step_1": "Pre-test Odds = Pre-test Probability / (1 - Pre-test Probability)",
        "step_2": "Post-test Odds = Pre-test Odds * Likelihood Ratio",
        "step_3": "Post-test Probability = Post-test Odds / (1 + Post-test Odds)",
        "fagan_nomogram": "Graphical tool aligning Pre-test Probability, LR, and Post-test Probability"
    }
}

# 4. Causal Inference & RWE (Topic 9)
causal_rwe = {
    "module": "Causal Inference and Real-World Evidence",
    "source": "Topic 9 (RWD/RWE, Pearl DAGs, Potential Outcomes)",
    "pearl_causal_hierarchy": {
        "Rung_1_Association": {
            "question": "What is? (Seeing)",
            "notation": "P(Y|X)",
            "tool": "Standard ML, Regression, Correlation"
        },
        "Rung_2_Intervention": {
            "question": "What if we do? (Doing)",
            "notation": "P(Y|do(X))",
            "tool": "RCT, Policy intervention, Backdoor adjustment"
        },
        "Rung_3_Counterfactuals": {
            "question": "What if we had acted differently? (Imagining/Retrospection)",
            "notation": "P(Y_x | x_prime, y_prime)",
            "tool": "Structural Causal Models (SCM), Personalized Medicine"
        }
    },
    "dag_structures": {
        "Fork_Confounder": {
            "structure": "X <- C -> Y",
            "action": "Must adjust/condition on C to close backdoor path"
        },
        "Chain_Mediator": {
            "structure": "X -> M -> Y",
            "action": "Do NOT condition on M when estimating total causal effect of X on Y"
        },
        "Collider_Inverted_Fork": {
            "structure": "X -> C <- Y",
            "action": "NEVER condition on C; conditioning on a collider OPENS a spurious non-causal path (Berkson/Selection bias)!"
        }
    },
    "potential_outcomes_framework": {
        "individual_treatment_effect": "ITE_i = Y_i(1) - Y_i(0)",
        "average_treatment_effect": "ATE = E[Y(1) - Y(0)]",
        "fundamental_problem": "We can never observe both potential outcomes for the same individual at the same time",
        "identifiability_assumptions": [
            "Exchangeability (Conditional ignorability / No unmeasured confounding): Y(1), Y(0) independent of T given X",
            "Positivity (Common Support): 0 < P(T=1|X) < 1 for all X",
            "SUTVA (Stable Unit Treatment Value Assumption): No interference between units and no variation in treatment versions"
        ]
    },
    "target_trial_emulation": {
        "concept": "Hernan & Robins framework for conducting valid causal inference using observational RWD",
        "key_components": [
            "Eligibility criteria: Identical to hypothetical RCT",
            "Treatment strategies: Clearly defined interventions (e.g. Initiators vs Active comparators)",
            "Assignment procedures: Emulated at Time Zero (prevents immortal time bias)",
            "Follow-up period: Starts at Time Zero until event, death, or loss to follow-up",
            "Outcome definition: Blinded or objective endpoint ascertainment",
            "Causal contrasts: Intention-to-treat analog (ITT) vs Per-protocol analog",
            "Analysis plan: PSM, IPTW, or G-methods"
        ],
        "biases_mitigated": ["Immortal time bias", "Prevalent user bias", "Confounding by indication"]
    }
}

# 5. Reporting Guidelines & CASP (Topic 4)
guidelines = {
    "module": "Critical Appraisal & Reporting Guidelines",
    "source": "Topic 4 (Research Methodology & Medical Paper Appraisal)",
    "reporting_checklists": {
        "CONSORT": "Consolidated Standards of Reporting Trials (For RCTs: 25-item checklist, flow diagram)",
        "STROBE": "Strengthening the Reporting of Observational Studies in Epidemiology (For Cohort, Case-Control, Cross-sectional: 22 items)",
        "PRISMA": "Preferred Reporting Items for Systematic Reviews and Meta-Analyses (27 items, flow diagram)",
        "STARD": "Standards for Reporting Diagnostic Accuracy Studies (30 items)",
        "TRIPOD": "Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis (22 items)"
    },
    "casp_appraisal_framework": {
        "Section_A": "Are the results of the study valid? (Randomization, allocation concealment, blinding, baseline balance, complete follow-up)",
        "Section_B": "What are the results? (Magnitude of effect, RR/OR/HR, precision with 95% CI, p-values)",
        "Section_C": "Will the results help locally? (Applicability to local patients, all clinical outcomes considered, benefits vs harms/costs)"
    }
}

with open(f"{target_dir}/biostatistics_daniel.json", "w", encoding="utf-8") as f:
    json.dump(biostats, f, indent=2, ensure_ascii=False)

with open(f"{target_dir}/diagnostic_performance.json", "w", encoding="utf-8") as f:
    json.dump(diagnostic, f, indent=2, ensure_ascii=False)

with open(f"{target_dir}/causal_inference_rwe.json", "w", encoding="utf-8") as f:
    json.dump(causal_rwe, f, indent=2, ensure_ascii=False)

with open(f"{target_dir}/reporting_guidelines.json", "w", encoding="utf-8") as f:
    json.dump(guidelines, f, indent=2, ensure_ascii=False)

print("All knowledge JSON files successfully created!")
