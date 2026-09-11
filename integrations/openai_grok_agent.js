/**
 * OpenAI & xAI Grok Function Calling Integration (Node.js)
 * Works with GPT-4o, OpenAI Codex, and xAI Grok.
 */

const {
  calculateSampleSizeTwoProportions,
  calculateSampleSizeTwoMeans,
  calculateDiagnosticMetrics,
  calculateEpidemiologicAssociation
} = require('../lib/calculators');
const { MedicalResearchOrchestrator } = require('../lib/engine');
const tools = require('./openai_grok_tools.json');

function executeToolCall(name, args) {
  if (name === 'design_clinical_protocol') {
    const orchestrator = new MedicalResearchOrchestrator();
    const options = {};
    if (args.tp !== undefined && args.fp !== undefined && args.fn !== undefined && args.tn !== undefined) {
      options.diagnosticParams = {
        tp: Number(args.tp),
        fp: Number(args.fp),
        fn: Number(args.fn),
        tn: Number(args.tn),
        preTestProb: args.pre_test_prob !== undefined ? Number(args.pre_test_prob) : null
      };
    }
    const state = orchestrator.runPipeline(args.question, options);
    return state.markdownReport;
  }

  if (name === 'calculate_sample_size_rct') {
    const res = calculateSampleSizeTwoProportions(
      Number(args.p1),
      Number(args.p2),
      args.alpha !== undefined ? Number(args.alpha) : 0.05,
      args.power !== undefined ? Number(args.power) : 0.80,
      args.dropout_rate !== undefined ? Number(args.dropout_rate) : 0.15
    );
    return JSON.stringify(res, null, 2);
  }

  if (name === 'calculate_sample_size_means') {
    const res = calculateSampleSizeTwoMeans(
      Number(args.mu1),
      Number(args.mu2),
      Number(args.sigma),
      args.alpha !== undefined ? Number(args.alpha) : 0.05,
      args.power !== undefined ? Number(args.power) : 0.80,
      args.dropout_rate !== undefined ? Number(args.dropout_rate) : 0.15
    );
    return JSON.stringify(res, null, 2);
  }

  if (name === 'calculate_diagnostic_matrix') {
    const res = calculateDiagnosticMetrics(
      Number(args.tp),
      Number(args.fp),
      Number(args.fn),
      Number(args.tn),
      args.pre_test_prob !== undefined ? Number(args.pre_test_prob) : null
    );
    return JSON.stringify(res, null, 2);
  }

  if (name === 'calculate_epidemiologic_association') {
    const res = calculateEpidemiologicAssociation(
      Number(args.exposed_cases),
      Number(args.exposed_non_cases),
      Number(args.unexposed_cases),
      Number(args.unexposed_non_cases)
    );
    return JSON.stringify(res, null, 2);
  }

  throw new Error(`Unknown tool: ${name}`);
}

module.exports = {
  tools,
  executeToolCall
};

// Quick verification if run directly
if (require.main === module) {
  console.log('Testing JS tool execution:');
  const res = executeToolCall('calculate_sample_size_rct', { p1: 0.35, p2: 0.15 });
  console.log(res);
}
