export interface SampleSizeTwoMeansResult {
  formula: string;
  alpha: number;
  power: number;
  zAlpha: number;
  zBeta: number;
  delta: number;
  sigma: number;
  nPerArm: number;
  totalN: number;
  totalNWithDropout: number;
  dropoutRate: number;
}

export interface DiagnosticMetricsResult {
  tp: number;
  fp: number;
  fn: number;
  tn: number;
  total: number;
  prevalence: number;
  sensitivity: number;
  specificity: number;
  ppv: number;
  npv: number;
  accuracy: number;
  youdenIndex: number;
  lrPlus: number;
  lrMinus: number;
  preTestProb: number;
  postTestProbPositive: number;
  postTestProbNegative: number;
  snnoutRuleOutPower: string;
  sppinRuleInPower: string;
}

export interface ResearchPipelineOptions {
  clinicalContext?: string;
  diagnosticParams?: {
    tp: number;
    fp: number;
    fn: number;
    tn: number;
    preTestProb?: number;
  };
}

export class ResearchState {
  rawQuery: string;
  clinicalContext?: string;
  pico: any;
  studyDesign: any;
  biostatsPlan: any;
  diagnosticEval: any;
  causalDag: any;
  criticalAppraisal: any;
  markdownReport: string;
  agentLogs: Array<{ agent: string; action: string; details: any; timestamp: string }>;
}

export class MedicalResearchOrchestrator {
  runPipeline(query: string, options?: ResearchPipelineOptions): ResearchState;
}

export const calculators: {
  getZScore(p: number): number;
  calculateSampleSizeTwoMeans(mu1: number, mu2: number, sigma: number, alpha?: number, power?: number, dropoutRate?: number): SampleSizeTwoMeansResult;
  calculateSampleSizeTwoProportions(p1: number, p2: number, alpha?: number, power?: number, dropoutRate?: number): any;
  calculateDiagnosticMetrics(tp: number, fp: number, fn: number, tn: number, preTestProb?: number): DiagnosticMetricsResult;
  calculateEpidemiologicAssociation(exposedCases: number, exposedNonCases: number, unexposedCases: number, unexposedNonCases: number): any;
};
