const {
  PICOAgent,
  StudyDesignAgent,
  BiostatisticsAgent,
  DiagnosticAgent,
  CausalRWEAgent,
  AppraisalAgent,
  LeadMethodologistAgent
} = require('./agents');

class ResearchState {
  constructor(rawQuery, clinicalContext = null) {
    this.rawQuery = rawQuery;
    this.clinicalContext = clinicalContext;
    this.agentLogs = [];
    this.pico = null;
    this.studyDesign = null;
    this.biostatsPlan = null;
    this.diagnosticEval = null;
    this.causalDag = null;
    this.criticalAppraisal = null;
    this.markdownReport = null;
  }

  addLog(agent, action, details = null) {
    this.agentLogs.push({ agent, action, details, timestamp: new Date().toISOString() });
  }
}

class MedicalResearchOrchestrator {
  constructor() {
    this.picoAgent = new PICOAgent();
    this.designAgent = new StudyDesignAgent();
    this.biostatsAgent = new BiostatisticsAgent();
    this.diagnosticAgent = new DiagnosticAgent();
    this.causalAgent = new CausalRWEAgent();
    this.appraisalAgent = new AppraisalAgent();
    this.leadAgent = new LeadMethodologistAgent();
  }

  runPipeline(query, options = {}) {
    const state = new ResearchState(query, options.clinicalContext);
    state.addLog("Orchestrator", "Starting Multi-Agent Medical Research Workflow", { query });

    // Step 1: PICO & Gap Analysis
    this.picoAgent.process(state);

    // Step 2: Study Design Architecture
    this.designAgent.process(state);

    // Step 3: Biostatistics & Sample Size Planning
    this.biostatsAgent.process(state);

    // Step 4: Diagnostic Accuracy (if applicable or params provided)
    if (options.diagnosticParams) {
      this.diagnosticAgent.process(state, options.diagnosticParams);
    } else {
      this.diagnosticAgent.process(state);
    }

    // Step 5: Causal Inference & Target Trial Emulation
    this.causalAgent.process(state);

    // Step 6: Critical Appraisal & Reporting Compliance
    this.appraisalAgent.process(state);

    // Step 7: Lead Methodologist Master Synthesis
    this.leadAgent.process(state);

    state.addLog("Orchestrator", "Multi-Agent Workflow Completed Successfully");
    return state;
  }
}

module.exports = {
  ResearchState,
  MedicalResearchOrchestrator
};
