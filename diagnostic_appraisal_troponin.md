# 🩺 Clinical Research Protocol: Investigating a novel point-of-care hs-cTnI assay vs standard central laboratory assay on rule-out of acute myocardial infarction in the Emergency Department
**Lead Investigator / Methodologist:** Multidisciplinary Clinical Research Team
**Methodological Framework:** EBM, Clinical Epidemiology (Fletcher), Biostatistics (Daniel 9th ed.), Causal AI (Pearl, Hernán & Robins)
**Source Knowledge Base:** Extracted from Notion (*Data and Data Analytics in Digital Health* — DAB Unit, MDCU)

---

## 🎯 1. Clinical Research Question & PICO Framework
- **Topic:** Diagnostic accuracy and sensitivity/specificity of a novel point-of-care hs-cTnI assay compared to standard central laboratory assay for rule-out of acute myocardial infarction in the Emergency Department.
- **Question Type:** `Diagnosis`
- **Population (P):** the Emergency Department
- **Intervention / Exposure (I):** a novel point-of-care hs-cTnI assay
- **Comparator / Control (C):** standard central laboratory assay
- **Primary Outcome (O):** rule-out of acute myocardial infarction
- **Secondary Outcomes:**
  - Safety profile and adverse events
  - Health-related quality of life (HRQoL)
  - Healthcare resource utilization

### ⚖️ FINER Feasibility & Quality Matrix
- **Feasible:** Sufficient sample size and clinical facilities available
- **Interesting:** Addresses high clinical uncertainty
- **Novel:** Provides direct evidence where previous studies had gaps or conflicting results
- **Ethical:** Conducted with clinical equipoise and institutional ethics approval
- **Relevant:** Directly guides patient management and healthcare outcomes

---

## 🏗️ 2. Study Design & Methodological Architecture
- **Recommended Design:** **Cross-Sectional Diagnostic Accuracy Study**
- **Methodological Rationale:** Cross-sectional diagnostic accuracy study comparing index test against an established reference standard (Gold Standard). Enables calculation of Sensitivity, Specificity, Likelihood Ratios, and ROC/AUC.

### 🛡️ Critical Methodological Safeguards
1. Consecutive or random recruitment of eligible patients suspected of harboring target condition
1. Independent and blinded interpretation of index test and reference standard
1. Verification of all patients with reference standard to eliminate partial/differential workup bias
1. Prespecified diagnostic cutoff threshold

### ⚠️ Anticipated Biases & Mitigation Strategies
| Bias Type | Mechanism & Clinical Risk | Mitigation Strategy |
| :--- | :--- | :--- |
| Verification / Workup Bias | Systematic distortion of true effect | All patients receive reference standard regardless of index test result |
| Review / Observer Bias | Systematic distortion of true effect | Blinded evaluation of tests |
| Spectrum Bias | Systematic distortion of true effect | Include full spectrum of mild, moderate, and severe cases alongside relevant differential diagnoses |

---

## 🧮 3. Biostatistics & Sample Size Determination
- **Statistical Formula:** `n = (Z_alpha/2 * sqrt(2*p_bar*(1-p_bar)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p1 - p2)^2`
- **Significance Level (Alpha):** `0.05` (Two-sided)
- **Statistical Power (1 - Beta):** `80%`
- **Effect Size Metric:** Proportion Reduction (25.0% vs 15.0%, Delta = 10.0%)
- **Sample Size per Arm:** `251` patients
- **Total Sample Size:** `502` patients
- **Total Sample (with 15% Attrition Buffer):** **`591` patients**
> 💡 **Biostatistical Recommendation:** Recruit at least 591 patients (296 per arm) to achieve 80% power at two-sided alpha 0.05, accounting for 15% attrition.

---

## 🔬 4. Diagnostic Performance & Bayesian Likelihood Ratios
| Metric | Value | 95% Interpretation |
| :--- | :--- | :--- |
| **Prevalence** | 40.0% | Pre-test probability in target population |
| **Sensitivity** | **95.0%** | True Positive Rate (SnNout rule) |
| **Specificity** | **95.0%** | True Negative Rate (SpPin rule) |
| **Positive Predictive Value (PPV)** | 92.7% | Post-test probability given positive result |
| **Negative Predictive Value (NPV)** | 96.6% | Probability of no disease given negative result |
| **Likelihood Ratio Positive (LR+)** | **19.00** | Ratio of true pos to false pos rate |
| **Likelihood Ratio Negative (LR-)** | **0.05** | Ratio of false neg to true neg rate |
| **Youden's Index J** | 0.900 | Optimal cutoff summary |

> 🧠 **Bayesian Fagan Shift:** Pre-test probability **25.0%** $\rightarrow$ Post-test probability Positive: **86.4%**, Negative: **1.7%**

---

## 🕸️ 5. Causal Inference, DAG Analysis & Target Trial Emulation
- **Exposure $\rightarrow$ Outcome:** `a novel point-of-care hs-cTnI assay` $\longrightarrow$ `rule-out of acute myocardial infarction`
- **Minimal Sufficient Adjustment Set (Backdoor Criterion):** `Age, Key Comorbidities (Diabetes, Hypertension, Renal Function), Baseline Disease Severity, Sex`
- **Mediators Identified:** `Biomarker Intermediate (e.g., Blood Pressure reduction)` *(Do NOT condition when estimating total causal effect)*
- **Colliders Identified:** `Post-treatment Hospital Admission Rate` *(NEVER condition; causes Berkson's / Collider Stratification Bias!)*

### ⚠️ Causal Guardian Warnings
- DO NOT adjust for mediator 'Biomarker Intermediate (e.g., Blood Pressure reduction)' when estimating the total causal effect of a novel point-of-care hs-cTnI assay on rule-out of acute myocardial infarction. Doing so causes overadjustment bias.
- CRITICAL WARNING: NEVER condition or stratify on collider 'Post-treatment Hospital Admission Rate' (X -> Post-treatment Hospital Admission Rate <- Y). Conditioning on a collider OPENS a spurious backdoor path, inducing Collider Stratification Bias (Berkson's Paradox)!

### 📋 Target Trial Emulation Protocol (Hernán & Robins Framework)
**1 Target Trial Specification:**
Emulation of a pragmatic randomized trial evaluating a novel point-of-care hs-cTnI assay vs standard central laboratory assay in the Emergency Department.

**2 Eligibility Criteria:**
Patients meeting identical inclusion/exclusion criteria as a prospective trial: Adult patients with the Emergency Department, no prior contraindications, baseline laboratory and clinical values recorded within 90 days prior to Time Zero.

**3 Treatment Strategies:**
New-User Active Comparator Design: Strategy A: Initiate a novel point-of-care hs-cTnI assay at Time Zero. Strategy B: Initiate standard central laboratory assay at Time Zero. Prevalent users are excluded to prevent prevalent user bias.

**4 Assignment Procedure and Time Zero:**
Time Zero (Baseline) is explicitly anchored at the exact date of first prescription/dispensation. Eligibility criteria, treatment assignment, and start of follow-up synchronize simultaneously at Time Zero, strictly eliminating Immortal Time Bias.

**5 Follow Up Period:**
Follow-up begins at Time Zero and continues until occurrence of primary outcome, death, disenrollment, or end of study period (e.g., 36 months). Right-censoring will be accounted for.

**6 Outcome Definition:**
Primary Endpoint: rule-out of acute myocardial infarction, defined by validated diagnostic ICD-10/11 codes, laboratory thresholds, or procedure codes.

**7 Causal Contrast and Analysis Plan:**
Primary contrast: Observational analog of Intention-to-Treat (ITT) effect and Per-Protocol effect.
Confounding control via Inverse Probability of Treatment Weighting (IPTW) based on high-dimensional propensity scores, with weighted Cox proportional hazards modeling to estimate Hazard Ratios (HR) with 95% robust sandwich confidence intervals.


---

## 🛡️ 6. Critical Appraisal & Reporting Compliance
- **Primary Reporting Guideline:** `STARD 2015 (Standards for Reporting Diagnostic Accuracy Studies)`
- **Internal Validity Rating:** `Strong`
- **External Validity Rating:** `High generalizability if target population reflects clinical practice`

### Detailed Checklist Audit
- **[Low Risk of Bias]** `STARD Item 5: Reference Standard (Gold Standard)`: Well-defined, independent reference standard verified in all participants.
- **[Low Risk of Bias]** `STARD Item 10: Blinding of Index Test and Reference Standard`: Readers of index test blinded to reference results and vice-versa (avoids review bias).
- **[Low Risk of Bias]** `STARD Item 6: Participant Recruitment`: Consecutive or random sample of suspected patients to avoid spectrum bias.

### Bradford Hill Causality Assessment
- **Temporality:** Met: Exposure strictly documented prior to outcome onset
- **Biological_Plausibility:** Met: Mechanism consistent with known clinical pathophysiology
- **Consistency:** Pending: Requires replication across diverse populations
- **Strength_of_Association:** Estimated effect size provides clinically meaningful separation

---

## 📊 7. Statistical Analysis Plan (SAP) Summary
Primary analysis will evaluate rule-out of acute myocardial infarction using n = (Z_alpha/2 * sqrt(2*p_bar*(1-p_bar)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p1 - p2)^2 under the Intention-to-Treat (ITT) principle. Target sample size is 591 patients (251 per arm) to achieve 80% power at alpha = 0.05. Continuous endpoints will be analyzed via ANCOVA adjusting for baseline covariates; binary endpoints will be evaluated via multivariable logistic regression or Cox proportional hazards.

---

## 📚 8. Methodological References
- Daniel WW, Cross CL. Biostatistics: A Foundation for Analysis in the Health Sciences. 9th ed.
- Fletcher RH, Fletcher SW, Fletcher GS. Clinical Epidemiology: The Essentials. 5th ed.
- Hernán MA, Robins JM. Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available. Am J Epidemiol. 2016.
- Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 Statement. BMJ. 2010.
- Bossuyt PM, et al. STARD 2015: An Updated List of Essential Items for Reporting Diagnostic Accuracy Studies. BMJ. 2015.
- Data and Data Analytics in Digital Health, Faculty of Medicine, Chulalongkorn University (DAB Unit).