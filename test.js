const assert = require('assert');
const {
  MedicalResearchOrchestrator,
  calculators
} = require('./index');

console.log("🧪 Running Node.js Test Suite...");

// 1. Test Calculators
const meansRes = calculators.calculateSampleSizeTwoMeans(10, 12.5, 5.0, 0.05, 0.80);
assert.strictEqual(meansRes.nPerArm, 63, "Sample size per arm should be 63");
assert.strictEqual(meansRes.totalN, 126, "Total sample size should be 126");
console.log("✅ calculateSampleSizeTwoMeans passed");

const diagRes = calculators.calculateDiagnosticMetrics(80, 10, 20, 90, 0.50);
assert.strictEqual(diagRes.sensitivity, 0.80, "Sensitivity should be 0.80");
assert.strictEqual(diagRes.specificity, 0.90, "Specificity should be 0.90");
assert.strictEqual(diagRes.lrPlus, 8.0, "LR+ should be 8.0");
console.log("✅ calculateDiagnosticMetrics passed");

const assocRes = calculators.calculateEpidemiologicAssociation(20, 80, 5, 95);
assert.strictEqual(assocRes.riskRatioRR, 4.0, "RR should be 4.0");
assert.strictEqual(assocRes.attributableRiskPercent, 75.0, "AR% should be 75.0%");
console.log("✅ calculateEpidemiologicAssociation passed");

// 2. Test Orchestrator
const orchestrator = new MedicalResearchOrchestrator();
const state = orchestrator.runPipeline(
  "In adult type 2 diabetes patients with heart failure, does dapagliflozin reduce cardiovascular death compared with standard of care?"
);

assert.ok(state.pico, "PICO should exist");
assert.strictEqual(state.pico.questionType, "Therapy");
assert.ok(state.studyDesign, "Study design should exist");
assert.ok(state.biostatsPlan, "Biostats plan should exist");
assert.ok(state.causalDag, "Causal DAG should exist");
assert.ok(state.criticalAppraisal, "Critical appraisal should exist");
assert.ok(state.markdownReport.includes("dapagliflozin"), "Report should include dapagliflozin");
console.log("✅ MedicalResearchOrchestrator end-to-end pipeline passed");

console.log("\n🎉 ALL Node.js TESTS PASSED (100%)!");
