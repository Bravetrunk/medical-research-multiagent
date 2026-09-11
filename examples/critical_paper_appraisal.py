#!/usr/bin/env python3
"""
Example 4: Critical Appraisal of an Observational vs Experimental Clinical Paper
Grounded on: CASP Checklists, STROBE statement, Topic 4.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.calculators import calculate_epidemiologic_association
from tools.appraisal_checklist_tool import appraise_study_design

def main():
    print("Executing Medical Paper Critical Appraisal...")
    
    # 1. Methodological Audit
    study_type = "Prospective Cohort Study"
    details = {
        "randomization": False,
        "allocation_concealment": False,
        "blinding": "Single-blind (outcomes adjudicator)",
        "itt_analysis": False
    }
    report = appraise_study_design(study_type, details)
    
    # 2. Re-calculating Effect Estimates from 2x2 contingency data
    # E.g. Statin in primary prevention: 40 events in 1000 exposed vs 80 events in 1000 unexposed
    assoc = calculate_epidemiologic_association(
        exposed_cases=40, exposed_non_cases=960,
        unexposed_cases=80, unexposed_non_cases=920
    )
    
    print("\n--- 🛡️ Appraisal Summary ---")
    print(f"Guideline: {report.guideline_used}")
    print(f"Overall Validity: {report.overall_validity}")
    print(f"Identified Biases: {', '.join(report.identified_biases)}")
    print(f"\n--- 📊 Association Re-evaluation ---")
    print(f"Risk Ratio (RR): {assoc['risk_ratio_rr']}")
    print(f"Absolute Risk Reduction (ARR): {assoc['absolute_risk_reduction_arr']*100:.2f}%")
    print(f"Number Needed to Treat (NNT): {assoc['number_needed_to_treat_nnt']} patients")
    print(f"Attributable Risk % in Exposed: {assoc['attributable_risk_percent']}%")
    print("\nAppraisal complete!")

if __name__ == "__main__":
    main()
