/**
 * Biostatistical and Epidemiological Calculators
 * Grounded on Daniel (Biostatistics 9th ed.) & Fletcher (Clinical Epidemiology)
 */

function getZScore(p) {
  const table = {
    0.001: 3.291,
    0.01: 2.576,
    0.02: 2.326,
    0.025: 1.960,
    0.05: 1.960,
    0.10: 1.645,
    0.15: 1.036,
    0.20: 0.842
  };
  if (table[p]) return table[p];

  if (p <= 0 || p >= 1) throw new Error("Probability p must be between 0 and 1");
  const q = p < 0.5 ? p / 2.0 : (1.0 - p) / 2.0;
  const t = Math.sqrt(-2.0 * Math.log(q));
  const c0 = 2.515517, c1 = 0.802853, c2 = 0.010328;
  const d1 = 1.432788, d2 = 0.189269, d3 = 0.001308;
  return t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0);
}

function calculateSampleSizeTwoMeans(mu1, mu2, sigma, alpha = 0.05, power = 0.80, dropoutRate = 0.15) {
  const delta = Math.abs(mu1 - mu2);
  if (delta === 0) throw new Error("Difference between means (mu1 - mu2) cannot be zero");
  if (sigma <= 0) throw new Error("Standard deviation sigma must be positive");

  const zAlpha = alpha === 0.05 ? 1.960 : getZScore(alpha);
  const beta = 1.0 - power;
  const zBeta = Math.abs(beta - 0.20) < 0.01 ? 0.842 : (Math.abs(beta - 0.10) < 0.01 ? 1.282 : getZScore(beta));

  const numerator = 2.0 * Math.pow(zAlpha + zBeta, 2) * Math.pow(sigma, 2);
  const denominator = Math.pow(delta, 2);
  const nPerArm = Math.ceil(numerator / denominator);
  const totalN = nPerArm * 2;
  const totalNWithDropout = Math.ceil(totalN / (1.0 - dropoutRate));

  return {
    formula: "n = 2 * (Z_alpha/2 + Z_beta)^2 * sigma^2 / (mu1 - mu2)^2",
    alpha,
    power,
    zAlpha: Number(zAlpha.toFixed(3)),
    zBeta: Number(zBeta.toFixed(3)),
    delta: Number(delta.toFixed(4)),
    sigma: Number(sigma.toFixed(4)),
    nPerArm,
    totalN,
    totalNWithDropout,
    dropoutRate
  };
}

function calculateSampleSizeTwoProportions(p1, p2, alpha = 0.05, power = 0.80, dropoutRate = 0.15) {
  if (!(p1 > 0 && p1 < 1 && p2 > 0 && p2 < 1)) {
    throw new Error("Proportions p1 and p2 must be strictly between 0 and 1");
  }
  const delta = Math.abs(p1 - p2);
  if (delta === 0) throw new Error("Difference between proportions (p1 - p2) cannot be zero");

  const zAlpha = alpha === 0.05 ? 1.960 : getZScore(alpha);
  const beta = 1.0 - power;
  const zBeta = Math.abs(beta - 0.20) < 0.01 ? 0.842 : (Math.abs(beta - 0.10) < 0.01 ? 1.282 : getZScore(beta));

  const pBar = (p1 + p2) / 2.0;
  const term1 = zAlpha * Math.sqrt(2.0 * pBar * (1.0 - pBar));
  const term2 = zBeta * Math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2));

  const nPerArm = Math.ceil(Math.pow(term1 + term2, 2) / Math.pow(delta, 2));
  const totalN = nPerArm * 2;
  const totalNWithDropout = Math.ceil(totalN / (1.0 - dropoutRate));

  return {
    formula: "n = (Z_alpha/2 * sqrt(2*p_bar*(1-p_bar)) + Z_beta * sqrt(p1*(1-p1) + p2*(1-p2)))^2 / (p1 - p2)^2",
    alpha,
    power,
    p1,
    p2,
    delta: Number(delta.toFixed(4)),
    nPerArm,
    totalN,
    totalNWithDropout,
    dropoutRate
  };
}

function calculateDiagnosticMetrics(tp, fp, fn, tn, preTestProb = null) {
  const total = tp + fp + fn + tn;
  if (total === 0) throw new Error("Total count in 2x2 table cannot be zero");

  const diseased = tp + fn;
  const nonDiseased = fp + tn;
  const testPositive = tp + fp;
  const testNegative = fn + tn;

  const prevalence = diseased / total;
  const priorProb = preTestProb !== null ? preTestProb : prevalence;

  const sensitivity = diseased > 0 ? tp / diseased : 0.0;
  const specificity = nonDiseased > 0 ? tn / nonDiseased : 0.0;
  const ppv = testPositive > 0 ? tp / testPositive : 0.0;
  const npv = testNegative > 0 ? tn / testNegative : 0.0;
  const accuracy = (tp + tn) / total;
  const youdenIndex = sensitivity + specificity - 1.0;

  const fpr = 1.0 - specificity;
  const fnr = 1.0 - sensitivity;

  const lrPlus = fpr > 0 ? sensitivity / fpr : 999.0;
  const lrMinus = specificity > 0 ? fnr / specificity : 0.001;

  // Bayesian Fagan Nomogram
  const clampedPrior = Math.min(Math.max(priorProb, 0.0001), 0.9999);
  const preTestOdds = clampedPrior / (1.0 - clampedPrior);

  const postTestOddsPos = preTestOdds * lrPlus;
  const postTestProbPos = postTestOddsPos / (1.0 + postTestOddsPos);

  const postTestOddsNeg = preTestOdds * lrMinus;
  const postTestProbNeg = postTestOddsNeg / (1.0 + postTestOddsNeg);

  const snnout = sensitivity >= 0.90;
  const sppin = specificity >= 0.90;

  return {
    tp, fp, fn, tn, total,
    prevalence: Number(prevalence.toFixed(4)),
    sensitivity: Number(sensitivity.toFixed(4)),
    specificity: Number(specificity.toFixed(4)),
    ppv: Number(ppv.toFixed(4)),
    npv: Number(npv.toFixed(4)),
    accuracy: Number(accuracy.toFixed(4)),
    youdenIndex: Number(youdenIndex.toFixed(4)),
    lrPlus: Number(lrPlus.toFixed(3)),
    lrMinus: Number(lrMinus.toFixed(3)),
    preTestProb: Number(priorProb.toFixed(4)),
    postTestProbPositive: Number(postTestProbPos.toFixed(4)),
    postTestProbNegative: Number(postTestProbNeg.toFixed(4)),
    snnoutRuleOutPower: snnout ? "High (SnNout applicable)" : "Moderate/Low",
    sppinRuleInPower: sppin ? "High (SpPin applicable)" : "Moderate/Low"
  };
}

function calculateEpidemiologicAssociation(exposedCases, exposedNonCases, unexposedCases, unexposedNonCases) {
  const a = exposedCases, b = exposedNonCases, c = unexposedCases, d = unexposedNonCases;
  const nExposed = a + b;
  const nUnexposed = c + d;

  const riskExposed = nExposed > 0 ? a / nExposed : 0.0;
  const riskUnexposed = nUnexposed > 0 ? c / nUnexposed : 0.0;

  const rr = riskUnexposed > 0 ? riskExposed / riskUnexposed : 0.0;
  const or = (b * c) > 0 ? (a * d) / (b * c) : 0.0;

  const arr = riskUnexposed - riskExposed;
  const nnt = arr > 0 ? Math.ceil(1.0 / arr) : null;
  const arPercent = rr > 0 ? ((rr - 1.0) / rr) * 100.0 : 0.0;

  return {
    riskExposed: Number(riskExposed.toFixed(4)),
    riskUnexposed: Number(riskUnexposed.toFixed(4)),
    riskRatioRR: Number(rr.toFixed(3)),
    oddsRatioOR: Number(or.toFixed(3)),
    absoluteRiskReductionARR: Number(arr.toFixed(4)),
    numberNeededToTreatNNT: nnt,
    attributableRiskPercent: Number(arPercent.toFixed(2)),
    rareDiseaseAssumptionMet: (a + c) / (nExposed + nUnexposed) < 0.10
  };
}

module.exports = {
  getZScore,
  calculateSampleSizeTwoMeans,
  calculateSampleSizeTwoProportions,
  calculateDiagnosticMetrics,
  calculateEpidemiologicAssociation
};
