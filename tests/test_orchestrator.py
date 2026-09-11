import unittest
from core.engine import MedicalResearchMultiAgentOrchestrator
from core.types import QuestionType, StudyDesignType

class TestMedicalResearchOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = MedicalResearchMultiAgentOrchestrator()

    def test_therapy_rct_pipeline(self):
        query = "In adult type 2 diabetes patients with heart failure, does dapagliflozin reduce cardiovascular death compared with standard of care?"
        state = self.orchestrator.run_pipeline(query)

        self.assertIsNotNone(state.pico)
        self.assertEqual(state.pico.question_type, QuestionType.THERAPY)
        self.assertIn("dapagliflozin", state.pico.intervention.lower())
        self.assertIsNotNone(state.study_design)
        self.assertEqual(state.study_design.selected_design, StudyDesignType.RCT_PARALLEL)
        self.assertIsNotNone(state.biostats_plan)
        self.assertGreater(state.biostats_plan.total_n_with_dropout, 0)
        self.assertIsNotNone(state.critical_appraisal)
        self.assertIn("CONSORT", state.critical_appraisal.guideline_used)
        self.assertIsNotNone(state.final_protocol)
        self.assertIsNotNone(state.markdown_report)
        self.assertIn("dapagliflozin", state.markdown_report.lower())

    def test_diagnostic_accuracy_pipeline(self):
        query = "What is the diagnostic accuracy and sensitivity/specificity of point-of-care hs-cTnI assay compared to central lab test for rapid rule-out of acute myocardial infarction?"
        diag_params = {"tp": 190, "fp": 15, "fn": 10, "tn": 285, "pre_test_prob": 0.40}
        state = self.orchestrator.run_pipeline(query, diagnostic_params=diag_params)

        self.assertIsNotNone(state.pico)
        self.assertEqual(state.pico.question_type, QuestionType.DIAGNOSIS)
        self.assertIsNotNone(state.diagnostic_eval)
        self.assertAlmostEqual(state.diagnostic_eval.sensitivity, 190/200, places=2)
        self.assertAlmostEqual(state.diagnostic_eval.specificity, 285/300, places=2)
        self.assertGreater(state.diagnostic_eval.lr_plus, 10.0)
        self.assertLess(state.diagnostic_eval.lr_minus, 0.10)
        self.assertIn("STARD", state.critical_appraisal.guideline_used)

    def test_rwe_target_trial_pipeline(self):
        query = "Using observational EHR data, does SGLT2 inhibitors vs GLP-1 RA initiation prevent chronic kidney disease progression (RWE Target Trial Emulation)?"
        state = self.orchestrator.run_pipeline(query)

        self.assertIsNotNone(state.causal_dag)
        self.assertIsNotNone(state.causal_dag.target_trial_protocol)
        self.assertIn("4_Assignment_Procedure_and_Time_Zero", state.causal_dag.target_trial_protocol)
        self.assertIn("Immortal Time Bias", state.causal_dag.target_trial_protocol["4_Assignment_Procedure_and_Time_Zero"])

if __name__ == "__main__":
    unittest.main()
