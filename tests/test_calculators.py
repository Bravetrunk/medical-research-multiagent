import unittest
from core.calculators import (
    calculate_sample_size_two_means,
    calculate_sample_size_two_proportions,
    calculate_diagnostic_metrics,
    calculate_epidemiologic_association
)

class TestMedicalCalculators(unittest.TestCase):
    def test_sample_size_two_means(self):
        # mu1=10, mu2=12.5 (delta=2.5), sigma=5, alpha=0.05, power=0.80
        res = calculate_sample_size_two_means(mu1=10.0, mu2=12.5, sigma=5.0, alpha=0.05, power=0.80)
        self.assertGreater(res["n_per_arm"], 0)
        self.assertEqual(res["total_n"], res["n_per_arm"] * 2)
        self.assertGreater(res["total_n_with_dropout"], res["total_n"])
        # Standard formula gives 2 * (1.96 + 0.842)^2 * 25 / 6.25 = 62.8 -> 63 per arm
        self.assertEqual(res["n_per_arm"], 63)

    def test_sample_size_two_proportions(self):
        # p1=0.30, p2=0.15, alpha=0.05, power=0.80
        res = calculate_sample_size_two_proportions(p1=0.30, p2=0.15, alpha=0.05, power=0.80)
        self.assertGreater(res["n_per_arm"], 50)
        self.assertEqual(res["total_n"], res["n_per_arm"] * 2)

    def test_diagnostic_metrics(self):
        # 2x2 table: TP=80, FP=10, FN=20, TN=90
        # Sens = 80/100 = 0.80, Spec = 90/100 = 0.90
        # LR+ = 0.80 / (1 - 0.90) = 8.0
        # LR- = (1 - 0.80) / 0.90 = 0.222
        res = calculate_diagnostic_metrics(tp=80, fp=10, fn=20, tn=90, pre_test_prob=0.50)
        self.assertAlmostEqual(res["sensitivity"], 0.80, places=2)
        self.assertAlmostEqual(res["specificity"], 0.90, places=2)
        self.assertAlmostEqual(res["lr_plus"], 8.0, places=1)
        self.assertAlmostEqual(res["lr_minus"], 0.222, places=2)
        self.assertAlmostEqual(res["youden_index"], 0.70, places=2)
        self.assertAlmostEqual(res["post_test_prob_positive"], 0.8889, places=2)
        self.assertAlmostEqual(res["post_test_prob_negative"], 0.1818, places=2)

    def test_epidemiologic_association(self):
        # Cohort study:
        # Exposed: 20 cases out of 100 (risk = 0.20)
        # Unexposed: 5 cases out of 100 (risk = 0.05)
        # RR = 0.20 / 0.05 = 4.0
        # ARR = 0.05 - 0.20 = -0.15 (or absolute risk increase = 0.15)
        res = calculate_epidemiologic_association(20, 80, 5, 95)
        self.assertAlmostEqual(res["risk_ratio_rr"], 4.0, places=2)
        self.assertAlmostEqual(res["attributable_risk_percent"], 75.0, places=1)

if __name__ == "__main__":
    unittest.main()
