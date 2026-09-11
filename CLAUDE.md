# CLAUDE.md — Medical Research Multi-Agent Guidelines

This file guides Claude Code (and Anthropic agents) when operating in or interacting with this repository and medical research tasks.

---

## 1. Quick Execution Commands

### Zero-Install Execution (Recommended via npx)
```bash
# Generate full 7-agent clinical research protocol
npx -y github:Bravetrunk/medical-research-multiagent "Can topical calcipotriol reduce skin cancer risk in renal transplant recipients?"

# Evaluate diagnostic test accuracy (2x2 contingency + Fagan nomogram)
npx -y github:Bravetrunk/medical-research-multiagent "Is high-sensitivity troponin superior to standard troponin for NSTEMI?" --tp 280 --fp 40 --fn 20 --tn 660 --pre-test-prob 0.15
```

### Local CLI (If Installed or Cloned)
```bash
# Node.js CLI
node bin/cli.js "<question>"
npm test

# Python CLI
python cli/main.py "<question>"
pytest tests/
```

### Model Context Protocol (MCP) Server
Claude Code can connect to this repository as an MCP tool server:
```bash
# Add MCP server to Claude Code
claude mcp add medical-research -- npx -y github:Bravetrunk/medical-research-multiagent medical-research-mcp
```

---

## 2. Core Methodological Standards

When answering clinical research, biostatistics, or epidemiological questions, adhere strictly to these principles:

1. **PICO & FINER First**:
   - Every clinical inquiry must decompose into Population, Intervention, Comparator, and Outcome.
   - Validate using FINER criteria (Feasible, Interesting, Novel, Ethical, Relevant).

2. **Biostatistical Sample Size Rigor (Daniel Biostatistics 9th ed.)**:
   - Parallel RCT sample size:
     $$n = \frac{\left(Z_{\alpha/2}\sqrt{2\bar{p}(1-\bar{p})} + Z_\beta\sqrt{p_1(1-p_1) + p_2(1-p_2)}\right)^2}{(p_1 - p_2)^2}$$
   - Always adjust for anticipated loss to follow-up (default $10-15\%$):
     $$N_{\text{adjusted}} = \frac{N_{\text{raw}}}{1 - \text{dropout\_rate}}$$
   - Never accept an underpowered study ($\text{Power} < 80\%$) or arbitrary sample size without variance estimation.

3. **Diagnostic Testing (Fletcher Clinical Epidemiology)**:
   - Calculate Sensitivity, Specificity, Positive Predictive Value (PPV), Negative Predictive Value (NPV).
   - Compute Likelihood Ratios ($LR+ = \frac{\text{Sensitivity}}{1 - \text{Specificity}}$, $LR- = \frac{1 - \text{Sensitivity}}{\text{Specificity}}$).
   - Apply **SnNout** (High Sensitivity rules OUT) and **SpPin** (High Specificity rules IN).
   - Apply Bayesian updating (Pre-test odds $\times LR \to$ Post-test odds $\to$ Post-test probability).

4. **Causal Inference & RWE (Judea Pearl DAGs & Hernán Target Trial Emulation)**:
   - Identify Confounders, Mediators, and Colliders.
   - **Never** condition on a collider ($X \to C \leftarrow Y$) or post-treatment intermediate.
   - Apply Backdoor Criterion to find the minimal sufficient adjustment set.
   - For EHR/Observational data, emulate a target trial: Time zero alignment, intention-to-treat clone-censor-weighting, and active comparator new-user design.

5. **EQUATOR Network & Risk of Bias Reporting Guidelines**:
   - RCT $\to$ **CONSORT 2010** + **Cochrane RoB 2**
   - Observational / Cohort $\to$ **STROBE** + **ROBINS-I**
   - Diagnostic Accuracy $\to$ **STARD 2015** + **QUADAS-2**
   - Systematic Review $\to$ **PRISMA 2020** + **AMSTAR 2**

---

## 3. Architecture Overview

- `lib/calculators.js` / `core/biostatistics.py`: Pure mathematical calculators for sample sizes, 2x2 contingency tables, and likelihood ratios.
- `lib/agents.js` / `agents/`: The 7 multi-agent roles:
  1. `PICOAgent` — Clinical question decomposition & FINER check.
  2. `StudyDesignAgent` — Methodological hierarchy & blinding/randomization.
  3. `BiostatisticsAgent` — Daniel formula calculation & power analysis.
  4. `DiagnosticAgent` — SnNout/SpPin, LR+/LR-, Bayesian Fagan updating.
  5. `CausalRWEAgent` — Judea Pearl DAG backdoor blocking & Target Trial Emulation.
  6. `AppraisalAgent` — EQUATOR guidelines & Risk of Bias audits.
  7. `LeadMethodologistAgent` — Chula DAB master clinical protocol synthesis.
- `bin/mcp-server.js`: Zero-dependency JSON-RPC stdio Model Context Protocol server.
