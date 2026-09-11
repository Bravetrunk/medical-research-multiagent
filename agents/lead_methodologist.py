from agents.base import BaseMedicalAgent
from core.types import ResearchProtocol
from core.state import ResearchState

class LeadMethodologistAgent(BaseMedicalAgent):
    def __init__(self):
        super().__init__(
            name="Lead Methodologist & Principal Investigator",
            role="Director of Medical Research & Biostatistics",
            description="Synthesizes findings from PICO, Study Design, Biostatistics, Diagnostic, Causal RWE, and Appraisal agents into a publication-ready Medical Research Protocol."
        )

    def process(self, state: ResearchState) -> ResearchProtocol:
        state.add_log(self.name, "Synthesizing comprehensive Medical Research Protocol & Dossier")
        
        pico = state.pico
        design = state.study_design
        biostats = state.biostats_plan
        diag = state.diagnostic_eval
        causal = state.causal_dag
        appraisal = state.critical_appraisal

        title = f"Clinical Research Protocol: Investigating {pico.intervention} vs {pico.comparison} on {pico.outcome} in {pico.population}" if pico else f"Clinical Protocol: {state.raw_query}"

        sap_summary = (
            f"Primary analysis will evaluate {pico.outcome if pico else 'the primary endpoint'} "
            f"using {biostats.formula_used if biostats else 'standard inferential modeling'} under the Intention-to-Treat (ITT) principle. "
            f"Target sample size is {biostats.total_n_with_dropout if biostats else 'N/A'} patients "
            f"({biostats.n_per_arm if biostats else 'N/A'} per arm) to achieve {int((biostats.power if biostats else 0.8)*100)}% power at alpha = {biostats.alpha if biostats else 0.05}. "
            "Continuous endpoints will be analyzed via ANCOVA adjusting for baseline covariates; binary endpoints will be evaluated via multivariable logistic regression or Cox proportional hazards."
        )

        protocol = ResearchProtocol(
            title=title,
            pico=pico,
            background_and_gap=(
                f"Despite modern clinical standards, significant uncertainty exists regarding optimal management in {pico.population if pico else 'this patient cohort'}. "
                "Current literature exhibits conflicting evidence and methodological heterogeneity. "
                "This study aims to resolve this evidence gap through rigorous epidemiological design and bias mitigation."
            ),
            study_design=design,
            biostatistics_plan=biostats,
            causal_dag_or_rwe=causal,
            diagnostic_evaluation=diag,
            appraisal_compliance=appraisal,
            statistical_analysis_plan_summary=sap_summary,
            references=[
                "Daniel WW, Cross CL. Biostatistics: A Foundation for Analysis in the Health Sciences. 9th ed.",
                "Fletcher RH, Fletcher SW, Fletcher GS. Clinical Epidemiology: The Essentials. 5th ed.",
                "Hernán MA, Robins JM. Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available. Am J Epidemiol. 2016.",
                "Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 Statement. BMJ. 2010.",
                "Bossuyt PM, et al. STARD 2015: An Updated List of Essential Items for Reporting Diagnostic Accuracy Studies. BMJ. 2015.",
                "Data and Data Analytics in Digital Health, Faculty of Medicine, Chulalongkorn University (DAB Unit)."
            ]
        )
        state.final_protocol = protocol

        # Render rich Markdown Report
        md = self._render_markdown(protocol, state)
        state.markdown_report = md
        state.add_log(self.name, "Final Synthesis Protocol Rendered")
        return protocol

    def _render_markdown(self, p: ResearchProtocol, state: ResearchState) -> str:
        lines = []
        lines.append(f"# 🩺 {p.title}")
        lines.append(f"**Lead Investigator / Methodologist:** {p.investigators}")
        lines.append(f"**Methodological Framework:** EBM, Clinical Epidemiology (Fletcher), Biostatistics (Daniel 9th ed.), Causal AI (Pearl, Hernán & Robins)")
        lines.append(f"**Source Knowledge Base:** Extracted from Notion (*Data and Data Analytics in Digital Health* — DAB Unit, MDCU)\n")
        lines.append("---")

        lines.append("\n## 🎯 1. Clinical Research Question & PICO Framework")
        lines.append(f"- **Topic:** {p.pico.topic}")
        lines.append(f"- **Question Type:** `{p.pico.question_type.value}`")
        lines.append(f"- **Population (P):** {p.pico.population}")
        lines.append(f"- **Intervention / Exposure (I):** {p.pico.intervention}")
        lines.append(f"- **Comparator / Control (C):** {p.pico.comparison}")
        lines.append(f"- **Primary Outcome (O):** {p.pico.outcome}")
        if p.pico.secondary_outcomes:
            lines.append("- **Secondary Outcomes:**")
            for so in p.pico.secondary_outcomes:
                lines.append(f"  - {so}")
        
        lines.append("\n### ⚖️ FINER Feasibility & Quality Matrix")
        for k, v in p.pico.finer_assessment.items():
            lines.append(f"- **{k}:** {v}")

        lines.append("\n---\n")
        lines.append("## 🏗️ 2. Study Design & Methodological Architecture")
        lines.append(f"- **Recommended Design:** **{p.study_design.selected_design.value}**")
        lines.append(f"- **Methodological Rationale:** {p.study_design.justification}")
        lines.append("\n### 🛡️ Critical Methodological Safeguards")
        for sg in p.study_design.key_methodological_safeguards:
            lines.append(f"1. {sg}")
        lines.append("\n### ⚠️ Anticipated Biases & Mitigation Strategies")
        lines.append("| Bias Type | Mechanism & Clinical Risk | Mitigation Strategy |")
        lines.append("| :--- | :--- | :--- |")
        for b in p.study_design.anticipated_biases:
            lines.append(f"| {b.get('name')} | Systematic distortion of true effect | {b.get('mitigation')} |")

        lines.append("\n---\n")
        lines.append("## 🧮 3. Biostatistics & Sample Size Determination")
        lines.append(f"- **Statistical Formula:** `{p.biostatistics_plan.formula_used}`")
        lines.append(f"- **Significance Level (Alpha):** `{p.biostatistics_plan.alpha}` (Two-sided)")
        lines.append(f"- **Statistical Power (1 - Beta):** `{int(p.biostatistics_plan.power * 100)}%`")
        lines.append(f"- **Effect Size Metric:** {p.biostatistics_plan.effect_size_metric}")
        lines.append(f"- **Sample Size per Arm:** `{p.biostatistics_plan.n_per_arm}` patients")
        lines.append(f"- **Total Sample Size:** `{p.biostatistics_plan.total_n}` patients")
        lines.append(f"- **Total Sample (with {int(p.biostatistics_plan.dropout_rate_assumed*100)}% Attrition Buffer):** **`{p.biostatistics_plan.total_n_with_dropout}` patients**")
        lines.append(f"> 💡 **Biostatistical Recommendation:** {p.biostatistics_plan.recommendations}")

        if p.diagnostic_evaluation:
            lines.append("\n---\n")
            lines.append("## 🔬 4. Diagnostic Performance & Bayesian Likelihood Ratios")
            d = p.diagnostic_evaluation
            lines.append("| Metric | Value | 95% Interpretation |")
            lines.append("| :--- | :--- | :--- |")
            lines.append(f"| **Prevalence** | {d.prevalence*100:.1f}% | Pre-test probability in target population |")
            lines.append(f"| **Sensitivity** | **{d.sensitivity*100:.1f}%** | True Positive Rate (SnNout rule) |")
            lines.append(f"| **Specificity** | **{d.specificity*100:.1f}%** | True Negative Rate (SpPin rule) |")
            lines.append(f"| **Positive Predictive Value (PPV)** | {d.ppv*100:.1f}% | Post-test probability given positive result |")
            lines.append(f"| **Negative Predictive Value (NPV)** | {d.npv*100:.1f}% | Probability of no disease given negative result |")
            lines.append(f"| **Likelihood Ratio Positive (LR+)** | **{d.lr_plus:.2f}** | Ratio of true pos to false pos rate |")
            lines.append(f"| **Likelihood Ratio Negative (LR-)** | **{d.lr_minus:.2f}** | Ratio of false neg to true neg rate |")
            lines.append(f"| **Youden's Index J** | {d.youden_index:.3f} | Optimal cutoff summary |")
            lines.append(f"\n> 🧠 **Bayesian Fagan Shift:** Pre-test probability **{d.pre_test_prob*100:.1f}%** $\\rightarrow$ Post-test probability Positive: **{d.post_test_prob_positive*100:.1f}%**, Negative: **{d.post_test_prob_negative*100:.1f}%**")

        if p.causal_dag_or_rwe:
            lines.append("\n---\n")
            lines.append("## 🕸️ 5. Causal Inference, DAG Analysis & Target Trial Emulation")
            c = p.causal_dag_or_rwe
            lines.append(f"- **Exposure $\\rightarrow$ Outcome:** `{c.treatment_exposure}` $\\longrightarrow$ `{c.outcome}`")
            lines.append(f"- **Minimal Sufficient Adjustment Set (Backdoor Criterion):** `{', '.join(c.minimal_sufficient_adjustment_set)}`")
            if c.mediators:
                lines.append(f"- **Mediators Identified:** `{', '.join(c.mediators)}` *(Do NOT condition when estimating total causal effect)*")
            if c.colliders:
                lines.append(f"- **Colliders Identified:** `{', '.join(c.colliders)}` *(NEVER condition; causes Berkson's / Collider Stratification Bias!)*")
            if c.warnings:
                lines.append("\n### ⚠️ Causal Guardian Warnings")
                for w in c.warnings:
                    lines.append(f"- {w}")

            if c.target_trial_protocol:
                lines.append("\n### 📋 Target Trial Emulation Protocol (Hernán & Robins Framework)")
                for step, desc in c.target_trial_protocol.items():
                    lines.append(f"**{step.replace('_', ' ')}:**\n{desc}\n")

        if p.appraisal_compliance:
            lines.append("\n---\n")
            lines.append("## 🛡️ 6. Critical Appraisal & Reporting Compliance")
            app = p.appraisal_compliance
            lines.append(f"- **Primary Reporting Guideline:** `{app.guideline_used}`")
            lines.append(f"- **Internal Validity Rating:** `{app.internal_validity_score}`")
            lines.append(f"- **External Validity Rating:** `{app.external_validity_score}`")
            lines.append("\n### Detailed Checklist Audit")
            for item in app.detailed_checklist:
                lines.append(f"- **[{item.rating}]** `{item.criterion}`: {item.explanation}")
            if app.bradford_hill_evaluation:
                lines.append("\n### Bradford Hill Causality Assessment")
                for k, v in app.bradford_hill_evaluation.items():
                    lines.append(f"- **{k}:** {v}")

        lines.append("\n---\n")
        lines.append("## 📊 7. Statistical Analysis Plan (SAP) Summary")
        lines.append(p.statistical_analysis_plan_summary)

        lines.append("\n---\n")
        lines.append("## 📚 8. Methodological References")
        for r in p.references:
            lines.append(f"- {r}")

        return "\n".join(lines)
