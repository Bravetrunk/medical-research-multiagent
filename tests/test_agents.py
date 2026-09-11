import unittest
from core.state import ResearchState
from core.types import QuestionType, StudyDesignType
from agents.pico_agent import PICOAgent
from agents.study_design_agent import StudyDesignAgent
from agents.biostats_agent import BiostatisticsAgent
from agents.diagnostic_agent import DiagnosticAgent
from agents.causal_rwe_agent import CausalRWEAgent
from agents.appraisal_agent import AppraisalAgent
from agents.lead_methodologist import LeadMethodologistAgent

class TestIndividualMedicalAgents(unittest.TestCase):
    def test_pico_agent_therapy(self):
        agent = PICOAgent()
        state = ResearchState(raw_query="In patients with hypertension, does amlodipine reduce stroke compared to placebo?")
        pico = agent.process(state)
        self.assertEqual(pico.question_type, QuestionType.THERAPY)
        self.assertIn("hypertension", pico.population.lower())
        self.assertIn("amlodipine", pico.intervention.lower())

    def test_study_design_agent_rct(self):
        pico_agent = PICOAgent()
        design_agent = StudyDesignAgent()
        state = ResearchState(raw_query="In patients with acute stroke, does tenecteplase improve functional recovery compared to alteplase?")
        pico_agent.process(state)
        design = design_agent.process(state)
        self.assertEqual(design.selected_design, StudyDesignType.RCT_PARALLEL)
        self.assertTrue(len(design.key_methodological_safeguards) >= 3)

    def test_biostats_agent_sample_size(self):
        pico_agent = PICOAgent()
        biostats_agent = BiostatisticsAgent()
        state = ResearchState(raw_query="In patients with dyslipidemia, does atorvastatin reduce LDL cholesterol compared to diet?")
        pico_agent.process(state)
        res = biostats_agent.process(state)
        self.assertGreater(res.total_n_with_dropout, 0)
        self.assertEqual(res.alpha, 0.05)
        self.assertEqual(res.power, 0.80)

    def test_causal_rwe_agent_dag(self):
        pico_agent = PICOAgent()
        design_agent = StudyDesignAgent()
        causal_agent = CausalRWEAgent()
        state = ResearchState(raw_query="Evaluating real-world EHR data: does metformin vs sulfonylurea reduce cardiovascular events?")
        pico_agent.process(state)
        design_agent.process(state)
        causal = causal_agent.process(state)
        self.assertIsNotNone(causal)
        self.assertTrue(len(c_vars := causal.minimal_sufficient_adjustment_set) > 0)
        self.assertTrue(any("collider" in w.lower() for w in causal.warnings))

    def test_diagnostic_agent(self):
        pico_agent = PICOAgent()
        diag_agent = DiagnosticAgent()
        state = ResearchState(raw_query="Diagnostic accuracy of ultrasound for acute appendicitis compared to pathology")
        pico_agent.process(state)
        diag_res = diag_agent.process(state, tp=90, fp=10, fn=10, tn=90, pre_test_prob=0.30)
        self.assertIsNotNone(diag_res)
        self.assertAlmostEqual(diag_res.sensitivity, 0.90, places=2)
        self.assertAlmostEqual(diag_res.specificity, 0.90, places=2)
        self.assertAlmostEqual(diag_res.lr_plus, 9.0, places=1)

if __name__ == "__main__":
    unittest.main()
