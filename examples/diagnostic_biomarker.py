#!/usr/bin/env python3
"""
Example 2: Diagnostic Accuracy Evaluation of a Novel Point-of-Care Biomarker
Grounded on: STARD 2015, Fletcher Chapter 3, Topic 8 (2x2 Table, SnNout/SpPin, LR+, LR-, Fagan Nomogram).
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.engine import MedicalResearchMultiAgentOrchestrator

def main():
    query = (
        "Diagnostic accuracy and sensitivity/specificity of a novel point-of-care hs-cTnI assay "
        "compared to standard central laboratory assay for rule-out of acute myocardial infarction in the Emergency Department."
    )
    # Simulated validation cohort of 500 emergency patients (200 with confirmed AMI, 300 without)
    # Index test identifies 190 TP, 15 FP, 10 FN, 285 TN
    diag_params = {
        "tp": 190,
        "fp": 15,
        "fn": 10,
        "tn": 285,
        "pre_test_prob": 0.25 # Typical 25% prevalence of AMI among suspected chest pain in ED
    }
    
    print(f"Executing Diagnostic Multi-Agent Appraisal for: {query}\n")
    orchestrator = MedicalResearchMultiAgentOrchestrator()
    state = orchestrator.run_pipeline(query, diagnostic_params=diag_params)
    
    out_file = "diagnostic_appraisal_troponin.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(state.markdown_report)
    print(f"Success! Diagnostic appraisal report saved to {out_file}")

if __name__ == "__main__":
    main()
