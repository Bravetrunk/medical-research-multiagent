import os
import json
import unittest

class TestKnowledgeBase(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.knowledge_dir = os.path.join(self.base_dir, "knowledge")

    def test_knowledge_files_exist(self):
        expected_files = [
            "clinical_epidemiology.json",
            "biostatistics_daniel.json",
            "diagnostic_performance.json",
            "causal_inference_rwe.json",
            "reporting_guidelines.json",
            "notion_source_dump.md"
        ]
        for fname in expected_files:
            fpath = os.path.join(self.knowledge_dir, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing knowledge file: {fname}")
            self.assertGreater(os.path.getsize(fpath), 0, f"File is empty: {fname}")

    def test_clinical_epidemiology_schema(self):
        with open(os.path.join(self.knowledge_dir, "clinical_epidemiology.json"), "r") as f:
            data = json.load(f)
        self.assertIn("pico_framework", data)
        self.assertIn("study_designs", data)
        self.assertIn("RCT", data["study_designs"])
        self.assertIn("Cohort", data["study_designs"])

    def test_biostatistics_daniel_schema(self):
        with open(os.path.join(self.knowledge_dir, "biostatistics_daniel.json"), "r") as f:
            data = json.load(f)
        self.assertIn("hypothesis_testing", data)
        self.assertIn("sample_size_formulas", data)
        self.assertIn("test_selection_matrix", data)

    def test_diagnostic_performance_schema(self):
        with open(os.path.join(self.knowledge_dir, "diagnostic_performance.json"), "r") as f:
            data = json.load(f)
        self.assertIn("metrics", data)
        self.assertIn("Sensitivity", data["metrics"])
        self.assertIn("Likelihood_Ratio_Positive_LR_plus", data["metrics"])
        self.assertIn("bayesian_nomogram", data)

    def test_causal_rwe_schema(self):
        with open(os.path.join(self.knowledge_dir, "causal_inference_rwe.json"), "r") as f:
            data = json.load(f)
        self.assertIn("pearl_causal_hierarchy", data)
        self.assertIn("dag_structures", data)
        self.assertIn("target_trial_emulation", data)

if __name__ == "__main__":
    unittest.main()
