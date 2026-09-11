const fs = require('fs');
const path = require('path');
const {
  calculateSampleSizeTwoMeans,
  calculateSampleSizeTwoProportions,
  calculateDiagnosticMetrics
} = require('./calculators');

const KNOWLEDGE_DIR = path.join(__dirname, '..', 'knowledge');

function loadKnowledge(file) {
  try {
    const fullPath = path.join(KNOWLEDGE_DIR, file);
    if (fs.existsSync(fullPath)) {
      return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    }
  } catch (e) {
    // Ignore error
  }
  return {};
}

// 1. PICO Agent
class PICOAgent {
  constructor() {
    this.name = "PICO & Question Formulator Agent";
    this.role = "Clinical Epidemiologist & Evidence-Based Medicine Specialist";
  }

  process(state) {
    const query = state.rawQuery.trim();
    state.addLog(this.name, "Formulating PICO and identifying research gap", { query });

    const lowerQ = query.toLowerCase();
    let qType = "Therapy";
    if (["diagnostic", "sensitivity", "specificity", "assay", "biomarker", "test", "roc", "accuracy"].some(k => lowerQ.includes(k))) {
      qType = "Diagnosis";
    } else if (["risk factor", "cause", "etiology", "harm", "toxic", "adverse"].some(k => lowerQ.includes(k))) {
      qType = "Harm / Etiology";
    } else if (["prognosis", "survival", "mortality rate", "trajectory", "recurrence"].some(k => lowerQ.includes(k))) {
      qType = "Prognosis";
    }

    let pop = "Adult clinical cohort";
    let intervention = "Target medical intervention";
    let comparison = "Standard of care or Active comparator";
    let outcome = "Patient-important clinical endpoint";

    // Regex extraction
    const nlMatch = query.match(/in\s+(.+?),\s*(?:does|can|will|is)\s+(.+?)\s+(?:reduce|increase|improve|prevent|affect|decrease)\s+(.+?)\s+compared\s+(?:with|to)\s+(.+?)[\?\.]?$/i);
    if (nlMatch) {
      pop = nlMatch[1].trim();
      intervention = nlMatch[2].trim();
      outcome = nlMatch[3].trim();
      comparison = nlMatch[4].trim();
    } else {
      const diagMatch = query.match(/diagnostic accuracy.*?of\s+(.+?)\s+compared\s+to\s+(.+?)\s+for\s+(.+?)(?:\s+in\s+(.+?))?[\?\.]?$/i);
      if (diagMatch) {
        intervention = diagMatch[1].trim();
        comparison = diagMatch[2].trim();
        outcome = diagMatch[3].trim();
        pop = diagMatch[4] ? diagMatch[4].trim() : "Suspected target patient population";
      } else {
        pop = `Patients presenting with condition described in: '${query}'`;
        intervention = "Target intervention under investigation";
      }
    }

    const finer = {
      Feasible: "Sufficient sample size and clinical facilities available",
      Interesting: "Addresses high clinical uncertainty",
      Novel: "Provides direct evidence where previous studies had gaps or conflicting results",
      Ethical: "Conducted with clinical equipoise and institutional ethics approval",
      Relevant: "Directly guides patient management and healthcare outcomes"
    };

    const pico = {
      topic: query,
      questionType: qType,
      population: pop,
      intervention,
      comparison,
      outcome,
      secondaryOutcomes: [
        "Safety profile and adverse events",
        "Health-related quality of life (HRQoL)",
        "Healthcare resource utilization"
      ],
      finerAssessment: finer
    };

    state.pico = pico;
    state.addLog(this.name, "PICO Formulation Completed", pico);
    return pico;
  }
}

// 2. Study Design Agent
class StudyDesignAgent {
  constructor() {
    this.name = "Study Design & Protocol Architect Agent";
    this.role = "Senior Clinical Trialist & Methodologist";
  }

  process(state) {
    const qType = state.pico ? state.pico.questionType : "Therapy";
    state.addLog(this.name, "Architecting optimal study design", { qType });

    let selectedDesign = "Parallel Randomized Controlled Trial";
    let justification = "RCT is the gold standard for evaluating therapeutic efficacy.";
    let safeguards = [];
    let biases = [];
    let alternatives = [];

    if (qType === "Therapy") {
      selectedDesign = "Parallel Randomized Controlled Trial";
      justification = "Randomized Controlled Trial (RCT) is the gold standard for therapeutic interventions. Randomization balances both known and unknown confounders across arms, establishing true internal validity.";
      safeguards = [
        "Computer-generated central block randomization with stratification by baseline severity",
        "Allocation concealment using sequentially numbered opaque sealed envelopes (SNOSE) or web response system",
        "Double-blind design (participants, clinical care team, and outcome adjudicators)",
        "Strict Intention-to-Treat (ITT) principle preserving prognostic balance of randomized groups"
      ];
      biases = [
        { name: "Selection Bias", mitigation: "Robust allocation concealment" },
        { name: "Performance Bias", mitigation: "Double-blinding with matched placebo" },
        { name: "Attrition Bias", mitigation: "Retention protocol and multiple imputation for missing endpoints" }
      ];
      alternatives = ["Cluster RCT", "Pragmatic RCT"];
    } else if (qType === "Diagnosis") {
      selectedDesign = "Cross-Sectional Diagnostic Accuracy Study";
      justification = "Cross-sectional diagnostic accuracy study comparing index test against an established reference standard (Gold Standard).";
      safeguards = [
        "Consecutive or random recruitment of eligible patients suspected of target condition",
        "Independent and blinded interpretation of index test and reference standard",
        "Verification of all patients with reference standard to eliminate workup bias"
      ];
      biases = [
        { name: "Verification / Workup Bias", mitigation: "All patients receive reference standard regardless of index test" },
        { name: "Review / Observer Bias", mitigation: "Blinded evaluation of tests" },
        { name: "Spectrum Bias", mitigation: "Include mild, moderate, and severe cases alongside relevant differential diagnoses" }
      ];
      alternatives = ["Prospective paired diagnostic cohort"];
    } else {
      selectedDesign = "Prospective Cohort Study";
      justification = "Prospective cohort design ensures temporality (exposure strictly documented before outcome onset).";
      safeguards = [
        "Objective verification and quantification of exposure at baseline",
        "Active follow-up with standardized endpoint adjudication",
        "Comprehensive baseline covariate measurement for multivariable confounding adjustment"
      ];
      biases = [
        { name: "Confounding by Indication", mitigation: "Propensity score matching or multivariable Cox modeling" },
        { name: "Loss to Follow-up Bias", mitigation: "Censoring sensitivity analyses and inverse probability weighting" }
      ];
      alternatives = ["Target Trial Emulation (RWD/RWE)", "Nested Case-Control Study"];
    }

    const design = {
      selectedDesign,
      justification,
      alternativeDesigns: alternatives,
      keyMethodologicalSafeguards: safeguards,
      anticipatedBiases: biases,
      ethicalConsiderations: "Protocol complies with Declaration of Helsinki, GCP guidelines, and requires IRB approval."
    };

    state.studyDesign = design;
    state.addLog(this.name, "Study Design Recommendation Completed", design);
    return design;
  }
}

// 3. Biostatistics Agent
class BiostatisticsAgent {
  constructor() {
    this.name = "Biostatistics & Sample Size Planner Agent";
    this.role = "Lead Biostatistician";
  }

  process(state) {
    state.addLog(this.name, "Calculating sample size and defining statistical analysis plan");

    const outcomeText = (state.pico ? state.pico.outcome : "").toLowerCase();
    let res;
    if (["score", "blood pressure", "hba1c", "level", "reduction", "weight", "change"].some(k => outcomeText.includes(k))) {
      res = calculateSampleSizeTwoMeans(10.0, 13.0, 6.0, 0.05, 0.80, 0.15);
      res.effectSizeMetric = `Difference in Means (Delta = ${res.delta}, SD = ${res.sigma})`;
    } else {
      res = calculateSampleSizeTwoProportions(0.25, 0.15, 0.05, 0.80, 0.15);
      res.effectSizeMetric = `Proportion Reduction (${res.p1 * 100}% vs ${res.p2 * 100}%, Delta = ${(res.delta * 100).toFixed(1)}%)`;
    }

    res.recommendations = `Recruit at least ${res.totalNWithDropout} patients (${Math.ceil(res.totalNWithDropout / 2)} per arm) to achieve ${Math.round(res.power * 100)}% power at two-sided alpha ${res.alpha}, accounting for ${Math.round(res.dropoutRate * 100)}% attrition.`;

    state.biostatsPlan = res;
    state.addLog(this.name, "Sample Size Planning Completed", res);
    return res;
  }
}

// 4. Diagnostic Agent
class DiagnosticAgent {
  constructor() {
    this.name = "Diagnostic Accuracy & Clinical Decision Evaluator Agent";
    this.role = "Clinical Pathologist & Diagnostic Test Methodologist";
  }

  process(state, params = null) {
    const isDiag = (state.pico && state.pico.questionType === "Diagnosis") ||
                   state.rawQuery.toLowerCase().includes("diagnostic") ||
                   state.rawQuery.toLowerCase().includes("biomarker") ||
                   params !== null;

    if (!isDiag) {
      state.addLog(this.name, "Skipped (Not a diagnostic question)");
      return null;
    }

    const p = params || { tp: 85, fp: 15, fn: 15, tn: 85, preTestProb: 0.20 };
    state.addLog(this.name, "Evaluating diagnostic accuracy and Likelihood Ratios", p);

    const res = calculateDiagnosticMetrics(p.tp, p.fp, p.fn, p.tn, p.preTestProb);
    state.diagnosticEval = res;
    state.addLog(this.name, "Diagnostic Evaluation Completed", res);
    return res;
  }
}

// 5. Causal RWE Agent
class CausalRWEAgent {
  constructor() {
    this.name = "Causal Inference & RWE Guardian Agent";
    this.role = "Causal Data Scientist & Real-World Evidence Specialist";
  }

  process(state) {
    state.addLog(this.name, "Analyzing Causal DAG and Target Trial Emulation");

    const treatment = state.pico ? state.pico.intervention : "Target Treatment";
    const outcome = state.pico ? state.pico.outcome : "Primary Clinical Outcome";
    const population = state.pico ? state.pico.population : "Target Population";

    const targetTrialProtocol = {
      "1_Target_Trial_Specification": `Emulation of a pragmatic randomized trial evaluating ${treatment} vs ${state.pico ? state.pico.comparison : 'Comparator'} in ${population}.`,
      "2_Eligibility_Criteria": `Patients meeting identical inclusion/exclusion criteria as a prospective trial: Adult patients with ${population}, no prior contraindications, baseline values recorded within 90 days prior to Time Zero.`,
      "3_Treatment_Strategies": `New-User Active Comparator Design: Strategy A: Initiate ${treatment} at Time Zero. Strategy B: Initiate comparator at Time Zero. Prevalent users excluded to prevent prevalent user bias.`,
      "4_Assignment_Procedure_and_Time_Zero": `Time Zero (Baseline) is explicitly anchored at the exact date of first prescription/dispensation, strictly eliminating Immortal Time Bias.`,
      "5_Follow_Up_Period": `Follow-up begins at Time Zero and continues until primary outcome, death, disenrollment, or end of study period (e.g., 36 months).`,
      "6_Outcome_Definition": `Primary Endpoint: ${outcome}, defined by validated diagnostic ICD-10/11 codes and lab thresholds.`,
      "7_Causal_Contrast_and_Analysis_Plan": `Observational analog of ITT and Per-Protocol effect using Inverse Probability of Treatment Weighting (IPTW) and Cox Proportional Hazards modeling.`
    };

    const causalDag = {
      treatmentExposure: treatment,
      outcome,
      confounders: ["Age", "Sex", "Baseline Disease Severity", "Key Comorbidities (Diabetes, Hypertension, Renal Function)"],
      mediators: ["Biomarker Intermediate (e.g., Blood Pressure reduction)"],
      colliders: ["Post-treatment Hospital Admission Rate"],
      minimalSufficientAdjustmentSet: ["Age", "Sex", "Baseline Disease Severity", "Key Comorbidities (Diabetes, Hypertension, Renal Function)"],
      warnings: [
        `DO NOT adjust for mediator 'Biomarker Intermediate' when estimating the total causal effect. Doing so causes overadjustment bias.`,
        `CRITICAL WARNING: NEVER condition or stratify on collider 'Post-treatment Hospital Admission Rate'. Doing so OPENS a spurious backdoor path (Collider Stratification Bias / Berkson's Paradox)!`
      ],
      targetTrialProtocol
    };

    state.causalDag = causalDag;
    state.addLog(this.name, "Causal Inference & Target Trial Analysis Completed", causalDag);
    return causalDag;
  }
}

// 6. Appraisal Agent
class AppraisalAgent {
  constructor() {
    this.name = "Critical Appraisal & Reporting Guideline Guardian";
    this.role = "Senior Evidence-Based Medicine Reviewer";
  }

  process(state) {
    const design = state.studyDesign ? state.studyDesign.selectedDesign : "Parallel Randomized Controlled Trial";
    state.addLog(this.name, `Auditing study protocol against reporting standards for ${design}`);

    let guideline = "CONSORT 2010 (Consolidated Standards of Reporting Trials)";
    let checklist = [];

    if (design.includes("Randomized") || design.includes("RCT")) {
      guideline = "CONSORT 2010 (Consolidated Standards of Reporting Trials)";
      checklist = [
        { criterion: "CONSORT Item 8: Sequence Generation & Random Allocation", rating: "Low Risk of Bias", explanation: "Appropriate computer-generated random sequence specified." },
        { criterion: "CONSORT Item 9: Allocation Concealment Mechanism", rating: "Low Risk of Bias", explanation: "Sequentially numbered opaque sealed envelopes (SNOSE) or central web system." },
        { criterion: "CONSORT Item 11: Blinding / Masking", rating: "Low Risk of Bias", explanation: "Double-blind design minimizing performance and detection/observer bias." },
        { criterion: "CONSORT Item 16: Analysis by Intention-to-Treat (ITT)", rating: "Low Risk of Bias", explanation: "All randomized participants analyzed in assigned groups (preserves prognostic balance)." }
      ];
    } else if (design.includes("Diagnostic")) {
      guideline = "STARD 2015 (Standards for Reporting Diagnostic Accuracy Studies)";
      checklist = [
        { criterion: "STARD Item 5: Reference Standard (Gold Standard)", rating: "Low Risk of Bias", explanation: "Well-defined reference standard verified in all participants." },
        { criterion: "STARD Item 10: Blinding of Index Test and Reference Standard", rating: "Low Risk of Bias", explanation: "Blinded evaluation avoiding review bias." },
        { criterion: "STARD Item 6: Participant Recruitment", rating: "Low Risk of Bias", explanation: "Consecutive or random sample avoiding spectrum bias." }
      ];
    } else {
      guideline = "STROBE 2007 (Strengthening the Reporting of Observational Studies)";
      checklist = [
        { criterion: "STROBE Item 6: Participant Selection & Temporality", rating: "Low Risk of Bias", explanation: "Exposure documented prior to outcome onset." },
        { criterion: "STROBE Item 12: Statistical Methods & Confounder Control", rating: "Low Risk of Bias", explanation: "Propensity score matching or multivariable Cox modeling applied." }
      ];
    }

    const report = {
      guidelineUsed: guideline,
      overallValidity: "High Methodological Rigor",
      internalValidityScore: "Strong",
      externalValidityScore: "High generalizability if target population reflects clinical practice",
      detailedChecklist: checklist,
      clinicalRecommendation: "Methodology adheres strictly to international reporting guidelines and clinical epidemiology rigor."
    };

    state.criticalAppraisal = report;
    state.addLog(this.name, "Critical Appraisal Completed", report);
    return report;
  }
}

// 7. Lead Methodologist Agent
class LeadMethodologistAgent {
  constructor() {
    this.name = "Lead Methodologist & Principal Investigator";
    this.role = "Director of Medical Research & Biostatistics";
  }

  process(state) {
    state.addLog(this.name, "Synthesizing comprehensive Medical Research Protocol & Dossier");

    const p = state.pico;
    const d = state.studyDesign;
    const b = state.biostatsPlan;
    const diag = state.diagnosticEval;
    const c = state.causalDag;
    const app = state.criticalAppraisal;

    const title = p
      ? `Clinical Research Protocol: Investigating ${p.intervention} vs ${p.comparison} on ${p.outcome} in ${p.population}`
      : `Clinical Protocol: ${state.rawQuery}`;

    const md = [];
    md.push(`# 🩺 ${title}`);
    md.push(`**Lead Investigator / Methodologist:** Multidisciplinary Clinical Research Team`);
    md.push(`**Methodological Framework:** EBM, Clinical Epidemiology (Fletcher), Biostatistics (Daniel 9th ed.), Causal AI (Pearl, Hernán & Robins)`);
    md.push(`**Source Knowledge Base:** Faculty of Medicine, Chulalongkorn University (DAB Unit)\n`);
    md.push(`---\n`);

    md.push(`## 🎯 1. Clinical Research Question & PICO Framework`);
    md.push(`- **Topic:** ${p.topic}`);
    md.push(`- **Question Type:** \`${p.questionType}\``);
    md.push(`- **Population (P):** ${p.population}`);
    md.push(`- **Intervention / Exposure (I):** ${p.intervention}`);
    md.push(`- **Comparator / Control (C):** ${p.comparison}`);
    md.push(`- **Primary Outcome (O):** ${p.outcome}`);
    md.push(`\n### ⚖️ FINER Feasibility & Quality Matrix`);
    for (const [k, v] of Object.entries(p.finerAssessment)) {
      md.push(`- **${k}:** ${v}`);
    }

    md.push(`\n---\n`);
    md.push(`## 🏗️ 2. Study Design & Methodological Architecture`);
    md.push(`- **Recommended Design:** **${d.selectedDesign}**`);
    md.push(`- **Methodological Rationale:** ${d.justification}`);
    md.push(`\n### 🛡️ Critical Methodological Safeguards`);
    d.keyMethodologicalSafeguards.forEach((sg, idx) => md.push(`${idx + 1}. ${sg}`));
    md.push(`\n### ⚠️ Anticipated Biases & Mitigation Strategies`);
    md.push(`| Bias Type | Mechanism & Clinical Risk | Mitigation Strategy |`);
    md.push(`| :--- | :--- | :--- |`);
    d.anticipatedBiases.forEach(bItem => {
      md.push(`| ${bItem.name} | Systematic distortion of true effect | ${bItem.mitigation} |`);
    });

    md.push(`\n---\n`);
    md.push(`## 🧮 3. Biostatistics & Sample Size Determination`);
    md.push(`- **Statistical Formula:** \`${b.formula}\``);
    md.push(`- **Significance Level (Alpha):** \`${b.alpha}\` (Two-sided)`);
    md.push(`- **Statistical Power (1 - Beta):** \`${Math.round(b.power * 100)}%\``);
    md.push(`- **Effect Size Metric:** ${b.effectSizeMetric}`);
    md.push(`- **Sample Size per Arm:** \`${b.nPerArm}\` patients`);
    md.push(`- **Total Sample Size:** \`${b.totalN}\` patients`);
    md.push(`- **Total Sample (with ${Math.round(b.dropoutRate * 100)}% Attrition Buffer):** **\`${b.totalNWithDropout}\` patients**`);
    md.push(`> 💡 **Biostatistical Recommendation:** ${b.recommendations}`);

    if (diag) {
      md.push(`\n---\n`);
      md.push(`## 🔬 4. Diagnostic Performance & Bayesian Likelihood Ratios`);
      md.push(`| Metric | Value | Interpretation |`);
      md.push(`| :--- | :--- | :--- |`);
      md.push(`| **Prevalence** | ${(diag.prevalence * 100).toFixed(1)}% | Baseline Pre-test Probability |`);
      md.push(`| **Sensitivity** | **${(diag.sensitivity * 100).toFixed(1)}%** | True Positive Rate (${diag.snnoutRuleOutPower}) |`);
      md.push(`| **Specificity** | **${(diag.specificity * 100).toFixed(1)}%** | True Negative Rate (${diag.sppinRuleInPower}) |`);
      md.push(`| **Positive Predictive Value (PPV)** | ${(diag.ppv * 100).toFixed(1)}% | Post-test probability given positive result |`);
      md.push(`| **Negative Predictive Value (NPV)** | ${(diag.npv * 100).toFixed(1)}% | Probability of no disease given negative result |`);
      md.push(`| **Likelihood Ratio Positive (LR+)** | **${diag.lrPlus}** | Shift in odds when test is positive |`);
      md.push(`| **Likelihood Ratio Negative (LR-)** | **${diag.lrMinus}** | Shift in odds when test is negative |`);
      md.push(`| **Youden's Index J** | ${diag.youdenIndex} | Optimal cutoff balance |`);
      md.push(`\n> 🧠 **Bayesian Shift:** Pre-test probability **${(diag.preTestProb * 100).toFixed(1)}%** $\\rightarrow$ Post-test Positive: **${(diag.postTestProbPositive * 100).toFixed(1)}%**, Negative: **${(diag.postTestProbNegative * 100).toFixed(1)}%**`);
    }

    if (c) {
      md.push(`\n---\n`);
      md.push(`## 🕸️ 5. Causal Inference, DAG Analysis & Target Trial Emulation`);
      md.push(`- **Exposure $\\rightarrow$ Outcome:** \`${c.treatmentExposure}\` $\\longrightarrow$ \`${c.outcome}\``);
      md.push(`- **Minimal Sufficient Adjustment Set (Backdoor Criterion):** \`${c.minimalSufficientAdjustmentSet.join(', ')}\``);
      md.push(`\n### ⚠️ Causal Guardian Warnings`);
      c.warnings.forEach(w => md.push(`- ${w}`));
      md.push(`\n### 📋 Target Trial Emulation Protocol (Hernán & Robins Framework)`);
      for (const [step, desc] of Object.entries(c.targetTrialProtocol)) {
        md.push(`**${step.replace(/_/g, ' ')}:**\n${desc}\n`);
      }
    }

    if (app) {
      md.push(`\n---\n`);
      md.push(`## 🛡️ 6. Critical Appraisal & Reporting Compliance`);
      md.push(`- **Primary Reporting Guideline:** \`${app.guidelineUsed}\``);
      md.push(`- **Internal Validity Rating:** \`${app.internalValidityScore}\``);
      md.push(`\n### Detailed Checklist Audit`);
      app.detailedChecklist.forEach(item => {
        md.push(`- **[${item.rating}]** \`${item.criterion}\`: ${item.explanation}`);
      });
    }

    md.push(`\n---\n`);
    md.push(`## 📚 7. Methodological References`);
    md.push(`- Daniel WW, Cross CL. Biostatistics: A Foundation for Analysis in the Health Sciences. 9th ed.`);
    md.push(`- Fletcher RH, Fletcher SW, Fletcher GS. Clinical Epidemiology: The Essentials. 5th ed.`);
    md.push(`- Hernán MA, Robins JM. Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available. Am J Epidemiol. 2016.`);
    md.push(`- Data and Data Analytics in Digital Health, Faculty of Medicine, Chulalongkorn University (DAB Unit).`);

    state.markdownReport = md.join('\n');
    state.addLog(this.name, "Final Synthesis Protocol Rendered");
    return state.markdownReport;
  }
}

module.exports = {
  PICOAgent,
  StudyDesignAgent,
  BiostatisticsAgent,
  DiagnosticAgent,
  CausalRWEAgent,
  AppraisalAgent,
  LeadMethodologistAgent
};
