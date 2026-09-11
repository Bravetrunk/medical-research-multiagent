# 🩺 Clinical Research Protocol: Investigating Empagliflozin vs matched Placebo on the composite of cardiovascular death or hospitalization for heart failure in adult patients with Heart Failure with preserved Ejection Fraction (HFpEF)
**Lead Investigator / Methodologist:** Multidisciplinary Clinical Research Team
**Methodological Framework:** EBM, Clinical Epidemiology (Fletcher), Biostatistics (Daniel 9th ed.), Causal AI (Pearl, Hernán & Robins)
**Source Knowledge Base:** Extracted from Notion (*Data and Data Analytics in Digital Health* — DAB Unit, MDCU)

---

## 🎯 1. Clinical Research Question & PICO Framework
- **Topic:** In adult patients with Heart Failure with preserved Ejection Fraction (HFpEF), does Empagliflozin reduce the composite of cardiovascular death or hospitalization for heart failure compared with matched Placebo?
- **Question Type:** `Therapy`
- **Population (P):** adult patients with Heart Failure with preserved Ejection Fraction (HFpEF)
- **Intervention / Exposure (I):** Empagliflozin
- **Comparator / Control (C):** matched Placebo
- **Primary Outcome (O):** the composite of cardiovascular death or hospitalization for heart failure
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
- **Recommended Design:** **Parallel Randomized Controlled Trial**
- **Methodological Rationale:** Randomized Controlled Trial (RCT) is the gold standard for therapeutic interventions. Randomization balances both known and unknown confounders across arms, establishing true internal validity.

### 🛡️ Critical Methodological Safeguards
1. Computer-generated central block randomization with stratification by baseline severity
1. Allocation concealment using sequentially numbered opaque sealed envelopes (SNOSE) or interactive web response system
1. Double-blind design (participants, clinical care team, and outcome adjudicators)
1. Strict Intention-to-Treat (ITT) principle preserving prognostic balance of randomized groups

### ⚠️ Anticipated Biases & Mitigation Strategies
| Bias Type | Mechanism & Clinical Risk | Mitigation Strategy |
| :--- | :--- | :--- |
| Selection Bias | Systematic distortion of true effect | Robust allocation concealment |
| Performance Bias | Systematic distortion of true effect | Double-blinding with matched placebo |
| Attrition Bias | Systematic distortion of true effect | Retention protocol and multiple imputation for missing endpoints |

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

## 🕸️ 5. Causal Inference, DAG Analysis & Target Trial Emulation
- **Exposure $\rightarrow$ Outcome:** `Empagliflozin` $\longrightarrow$ `the composite of cardiovascular death or hospitalization for heart failure`
- **Minimal Sufficient Adjustment Set (Backdoor Criterion):** `Sex, Age, Key Comorbidities (Diabetes, Hypertension, Renal Function), Baseline Disease Severity`
- **Mediators Identified:** `Biomarker Intermediate (e.g., Blood Pressure reduction)` *(Do NOT condition when estimating total causal effect)*
- **Colliders Identified:** `Post-treatment Hospital Admission Rate` *(NEVER condition; causes Berkson's / Collider Stratification Bias!)*

### ⚠️ Causal Guardian Warnings
- DO NOT adjust for mediator 'Biomarker Intermediate (e.g., Blood Pressure reduction)' when estimating the total causal effect of Empagliflozin on the composite of cardiovascular death or hospitalization for heart failure. Doing so causes overadjustment bias.
- CRITICAL WARNING: NEVER condition or stratify on collider 'Post-treatment Hospital Admission Rate' (X -> Post-treatment Hospital Admission Rate <- Y). Conditioning on a collider OPENS a spurious backdoor path, inducing Collider Stratification Bias (Berkson's Paradox)!

### 📋 Target Trial Emulation Protocol (Hernán & Robins Framework)
**1 Target Trial Specification:**
Emulation of a pragmatic randomized trial evaluating Empagliflozin vs matched Placebo in adult patients with Heart Failure with preserved Ejection Fraction (HFpEF).

**2 Eligibility Criteria:**
Patients meeting identical inclusion/exclusion criteria as a prospective trial: Adult patients with adult patients with Heart Failure with preserved Ejection Fraction (HFpEF), no prior contraindications, baseline laboratory and clinical values recorded within 90 days prior to Time Zero.

**3 Treatment Strategies:**
New-User Active Comparator Design: Strategy A: Initiate Empagliflozin at Time Zero. Strategy B: Initiate matched Placebo at Time Zero. Prevalent users are excluded to prevent prevalent user bias.

**4 Assignment Procedure and Time Zero:**
Time Zero (Baseline) is explicitly anchored at the exact date of first prescription/dispensation. Eligibility criteria, treatment assignment, and start of follow-up synchronize simultaneously at Time Zero, strictly eliminating Immortal Time Bias.

**5 Follow Up Period:**
Follow-up begins at Time Zero and continues until occurrence of primary outcome, death, disenrollment, or end of study period (e.g., 36 months). Right-censoring will be accounted for.

**6 Outcome Definition:**
Primary Endpoint: the composite of cardiovascular death or hospitalization for heart failure, defined by validated diagnostic ICD-10/11 codes, laboratory thresholds, or procedure codes.

**7 Causal Contrast and Analysis Plan:**
Primary contrast: Observational analog of Intention-to-Treat (ITT) effect and Per-Protocol effect.
Confounding control via Inverse Probability of Treatment Weighting (IPTW) based on high-dimensional propensity scores, with weighted Cox proportional hazards modeling to estimate Hazard Ratios (HR) with 95% robust sandwich confidence intervals.


---

## 🛡️ 6. Critical Appraisal & Reporting Compliance
- **Primary Reporting Guideline:** `CONSORT 2010 (Consolidated Standards of Reporting Trials)`
- **Internal Validity Rating:** `Strong`
- **External Validity Rating:** `High generalizability if target population reflects clinical practice`

### Detailed Checklist Audit
- **[Low Risk of Bias]** `CONSORT Item 8: Sequence Generation & Random Allocation`: Appropriate computer-generated random sequence specified.
- **[Low Risk of Bias]** `CONSORT Item 9: Allocation Concealment Mechanism`: Sequentially numbered opaque sealed envelopes (SNOSE) or central web system.
- **[Low Risk of Bias]** `CONSORT Item 11: Blinding / Masking`: Blinding implemented: Double-blind. Minimizes performance and detection/observer bias.
- **[Low Risk of Bias]** `CONSORT Item 16: Analysis by Intention-to-Treat (ITT)`: All randomized participants analyzed in assigned groups (preserves prognostic balance).

### Bradford Hill Causality Assessment
- **Temporality:** Met: Exposure strictly documented prior to outcome onset
- **Biological_Plausibility:** Met: Mechanism consistent with known clinical pathophysiology
- **Consistency:** Pending: Requires replication across diverse populations
- **Strength_of_Association:** Estimated effect size provides clinically meaningful separation

---

## 📊 7. Statistical Analysis Plan (SAP) Summary
Primary analysis will evaluate the composite of cardiovascular death or hospitalization for heart failure using n = (Z_alpha/2 * sqrt(2*p_bar*(1-p_bar)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p1 - p2)^2 under the Intention-to-Treat (ITT) principle. Target sample size is 591 patients (251 per arm) to achieve 80% power at alpha = 0.05. Continuous endpoints will be analyzed via ANCOVA adjusting for baseline covariates; binary endpoints will be evaluated via multivariable logistic regression or Cox proportional hazards.

---

## 📚 8. Methodological References
- Daniel WW, Cross CL. Biostatistics: A Foundation for Analysis in the Health Sciences. 9th ed.
- Fletcher RH, Fletcher SW, Fletcher GS. Clinical Epidemiology: The Essentials. 5th ed.
- Hernán MA, Robins JM. Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available. Am J Epidemiol. 2016.
- Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 Statement. BMJ. 2010.
- Bossuyt PM, et al. STARD 2015: An Updated List of Essential Items for Reporting Diagnostic Accuracy Studies. BMJ. 2015.
- Data and Data Analytics in Digital Health, Faculty of Medicine, Chulalongkorn University (DAB Unit).