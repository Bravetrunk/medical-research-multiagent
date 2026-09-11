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

### 1. Execute via CLI
Run the multi-agent CLI tool directly:

```bash
python /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/cli/main.py "<User Clinical Question>" \
  --output protocol_report.md
```

### 2. For Diagnostic Testing Evaluation
Include the 2x2 contingency table values and pre-test probability:

```bash
python /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/cli/main.py "<Diagnostic Research Question>" \
  --tp <TP> --fp <FP> --fn <FN> --tn <TN> --pre-test-prob <Prevalence> \
  --output diagnostic_appraisal.md
```

### 3. For Interactive Interview Mode
Launch the interactive wizard:

```bash
python /Users/tonkla/.gemini/antigravity/scratch/medical_research_multiagent/cli/main.py --interactive
```

### 4. Present Findings
1. Read the generated markdown protocol using `view_file`.
2. Present the structured PICO, Study Design, Biostatistics/Sample Size plan, Causal DAG analysis, and Reporting guidelines compliance to the user.
