---
name: medical-research-methodology
description: >-
  Use this skill when designing medical research protocols, clinical trials (RCTs), observational studies, diagnostic accuracy evaluations, sample size calculations, or Real-World Evidence (RWE) Target Trial Emulations. Grounded on Faculty of Medicine Chulalongkorn University (DAB Unit), Fletcher Clinical Epidemiology, Daniel Biostatistics, and Judea Pearl Causal AI.
---

# Medical Research & Methodology Multi-Agent Skill

This skill allows you to autonomously architect publication-grade clinical trial protocols, calculate biostatistical sample sizes, evaluate diagnostic performance matrices (SnNout/SpPin, Likelihood Ratios, Fagan Nomogram), analyze causal Directed Acyclic Graphs (DAGs), and emulate Target Trials for observational EHR data.

The system is powered by a 7-agent DAG architecture located at `/Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent`.

## Instructions for Execution

When the user asks to design a clinical trial, formulate a PICO question, calculate sample size, evaluate a diagnostic assay, or appraise a medical study:

### 1. Execute via Node.js / npx (Zero Dependencies, Fastest)
Run directly via Node.js or npx:

```bash
# Using Node directly from repo
node /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/bin/cli.js "<User Clinical Question>"

# Or using npx from GitHub
npx -y github:Bravetrunk/medical-research-multiagent "<User Clinical Question>"
```

### 2. For Diagnostic Testing Evaluation
Include the 2x2 contingency table values and pre-test probability:

```bash
node /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/bin/cli.js "<Diagnostic Research Question>" \
  --tp <TP> --fp <FP> --fn <FN> --tn <TN> --pre-test-prob <Prevalence>
```

### 3. Execute via Python CLI
```bash
python3 /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/cli/main.py "<User Clinical Question>" \
  --output protocol_report.md
```

### 4. Present Findings
1. Present the structured PICO, Study Design, Biostatistics/Sample Size plan (with 10-15% dropout inflation), Causal DAG analysis, and Reporting guidelines compliance (CONSORT, STROBE, STARD) to the user.
