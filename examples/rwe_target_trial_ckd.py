#!/usr/bin/env python3
"""
Example 3: Real-World Evidence (RWE) Target Trial Emulation using EHR Data
Grounded on: Hernán & Robins Framework, Judea Pearl DAGs, Topic 9.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.engine import MedicalResearchMultiAgentOrchestrator

def main():
    query = (
        "In patients with Type 2 Diabetes and stage 3 Chronic Kidney Disease (CKD), "
        "does initiation of SGLT2 inhibitors vs DPP-4 inhibitors prevent progression to end-stage renal disease (ESRD) "
        "using real-world electronic health records (Target Trial Emulation)?"
    )
    print(f"Executing Causal Inference & Target Trial Emulation for: {query}\n")
    orchestrator = MedicalResearchMultiAgentOrchestrator()
    state = orchestrator.run_pipeline(query)
    
    out_file = "rwe_target_trial_ckd.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(state.markdown_report)
    print(f"Success! Target Trial Protocol saved to {out_file}")

if __name__ == "__main__":
    main()
