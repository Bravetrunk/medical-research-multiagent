#!/usr/bin/env python3
"""
Example 1: Designing a Phase III Double-Blind Parallel RCT in Cardiology
Grounded on: CONSORT 2010, Daniel 9th ed. Chapter 7, Topic 3 & 4.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.engine import MedicalResearchMultiAgentOrchestrator

def main():
    query = (
        "In adult patients with Heart Failure with preserved Ejection Fraction (HFpEF), "
        "does Empagliflozin reduce the composite of cardiovascular death or hospitalization for heart failure "
        "compared with matched Placebo?"
    )
    print(f"Executing Multi-Agent Protocol Design for: {query}\n")
    orchestrator = MedicalResearchMultiAgentOrchestrator()
    state = orchestrator.run_pipeline(query)
    
    out_file = "protocol_hfpef_rct.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(state.markdown_report)
    print(f"Success! Protocol generated and saved to {out_file}")

if __name__ == "__main__":
    main()
