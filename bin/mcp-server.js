#!/usr/bin/env node
/**
 * Model Context Protocol (MCP) Stdio Server
 * Compatible with Claude Code, Claude Desktop, Cursor, Windsurf, Antigravity, Cline, Roo Code
 */

const readline = require('readline');
const path = require('path');
const {
  calculateSampleSizeTwoProportions,
  calculateSampleSizeTwoMeans,
  calculateDiagnosticMetrics,
  calculateEpidemiologicAssociation
} = require('../lib/calculators');
const { MedicalResearchOrchestrator } = require('../lib/engine');

const TOOLS = [
  {
    name: 'design_clinical_protocol',
    description: 'Autonomous 7-agent DAG for medical research methodology: generates full publication-grade clinical trial protocols, PICO formulation, study design, biostatistics sample size, causal DAG, and EQUATOR compliance.',
    inputSchema: {
      type: 'object',
      properties: {
        question: {
          type: 'string',
          description: 'The clinical research question or hypothesis (e.g., "Can topical calcipotriol reduce skin cancer in renal transplant recipients?")'
        },
        tp: { type: 'number', description: 'True Positives (optional, for diagnostic evaluations)' },
        fp: { type: 'number', description: 'False Positives (optional)' },
        fn: { type: 'number', description: 'False Negatives (optional)' },
        tn: { type: 'number', description: 'True Negatives (optional)' },
        pre_test_prob: { type: 'number', description: 'Pre-test probability or prevalence (0 to 1, optional)' }
      },
      required: ['question']
    }
  },
  {
    name: 'calculate_sample_size_rct',
    description: 'Calculate sample size for two-arm parallel superiority randomized controlled trial (binary proportions) based on Daniel Biostatistics.',
    inputSchema: {
      type: 'object',
      properties: {
        p1: { type: 'number', description: 'Event proportion in control group (e.g. 0.35)' },
        p2: { type: 'number', description: 'Event proportion in intervention group (e.g. 0.15)' },
        alpha: { type: 'number', description: 'Two-sided type I error rate (default: 0.05)' },
        power: { type: 'number', description: 'Statistical power 1 - beta (default: 0.80)' },
        dropout_rate: { type: 'number', description: 'Anticipated loss to follow-up (default: 0.15)' }
      },
      required: ['p1', 'p2']
    }
  },
  {
    name: 'calculate_sample_size_means',
    description: 'Calculate sample size for two independent continuous means (t-test / parallel trial) based on Daniel Biostatistics.',
    inputSchema: {
      type: 'object',
      properties: {
        mu1: { type: 'number', description: 'Expected mean in group 1' },
        mu2: { type: 'number', description: 'Expected mean in group 2' },
        sigma: { type: 'number', description: 'Pooled standard deviation' },
        alpha: { type: 'number', description: 'Two-sided alpha (default: 0.05)' },
        power: { type: 'number', description: 'Power 1 - beta (default: 0.80)' },
        dropout_rate: { type: 'number', description: 'Loss to follow-up (default: 0.15)' }
      },
      required: ['mu1', 'mu2', 'sigma']
    }
  },
  {
    name: 'calculate_diagnostic_matrix',
    description: 'Calculate diagnostic accuracy metrics: Sensitivity, Specificity, PPV, NPV, Likelihood Ratios (LR+, LR-), Youden Index, SnNout/SpPin rule, and Bayesian Post-Test Probability (Fagan Nomogram).',
    inputSchema: {
      type: 'object',
      properties: {
        tp: { type: 'number', description: 'True Positives' },
        fp: { type: 'number', description: 'False Positives' },
        fn: { type: 'number', description: 'False Negatives' },
        tn: { type: 'number', description: 'True Negatives' },
        pre_test_prob: { type: 'number', description: 'Pre-test probability (prior probability, 0 to 1, optional)' }
      },
      required: ['tp', 'fp', 'fn', 'tn']
    }
  },
  {
    name: 'calculate_epidemiologic_association',
    description: 'Calculate 2x2 epidemiological association: Relative Risk (RR), Odds Ratio (OR), Absolute Risk Reduction (ARR), and Number Needed to Treat (NNT).',
    inputSchema: {
      type: 'object',
      properties: {
        exposed_cases: { type: 'number', description: 'Exposed cases (a)' },
        exposed_non_cases: { type: 'number', description: 'Exposed non-cases (b)' },
        unexposed_cases: { type: 'number', description: 'Unexposed cases (c)' },
        unexposed_non_cases: { type: 'number', description: 'Unexposed non-cases (d)' }
      },
      required: ['exposed_cases', 'exposed_non_cases', 'unexposed_cases', 'unexposed_non_cases']
    }
  }
];

function sendResponse(response) {
  process.stdout.write(JSON.stringify(response) + '\n');
}

function handleMessage(msg) {
  if (!msg || typeof msg !== 'object') return;

  if (msg.method === 'initialize') {
    sendResponse({
      jsonrpc: '2.0',
      id: msg.id,
      result: {
        protocolVersion: '2024-11-05',
        capabilities: {
          tools: {}
        },
        serverInfo: {
          name: 'medical-research-mcp',
          version: '1.0.0'
        }
      }
    });
    return;
  }

  if (msg.method === 'notifications/initialized') {
    return;
  }

  if (msg.method === 'ping') {
    sendResponse({ jsonrpc: '2.0', id: msg.id, result: {} });
    return;
  }

  if (msg.method === 'tools/list') {
    sendResponse({
      jsonrpc: '2.0',
      id: msg.id,
      result: { tools: TOOLS }
    });
    return;
  }

  if (msg.method === 'tools/call') {
    const { name, arguments: args = {} } = msg.params || {};
    try {
      let resultText = '';
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
        resultText = state.markdownReport;
      } else if (name === 'calculate_sample_size_rct') {
        const res = calculateSampleSizeTwoProportions(
          Number(args.p1),
          Number(args.p2),
          args.alpha !== undefined ? Number(args.alpha) : 0.05,
          args.power !== undefined ? Number(args.power) : 0.80,
          args.dropout_rate !== undefined ? Number(args.dropout_rate) : 0.15
        );
        resultText = JSON.stringify(res, null, 2);
      } else if (name === 'calculate_sample_size_means') {
        const res = calculateSampleSizeTwoMeans(
          Number(args.mu1),
          Number(args.mu2),
          Number(args.sigma),
          args.alpha !== undefined ? Number(args.alpha) : 0.05,
          args.power !== undefined ? Number(args.power) : 0.80,
          args.dropout_rate !== undefined ? Number(args.dropout_rate) : 0.15
        );
        resultText = JSON.stringify(res, null, 2);
      } else if (name === 'calculate_diagnostic_matrix') {
        const res = calculateDiagnosticMetrics(
          Number(args.tp),
          Number(args.fp),
          Number(args.fn),
          Number(args.tn),
          args.pre_test_prob !== undefined ? Number(args.pre_test_prob) : null
        );
        resultText = JSON.stringify(res, null, 2);
      } else if (name === 'calculate_epidemiologic_association') {
        const res = calculateEpidemiologicAssociation(
          Number(args.exposed_cases),
          Number(args.exposed_non_cases),
          Number(args.unexposed_cases),
          Number(args.unexposed_non_cases)
        );
        resultText = JSON.stringify(res, null, 2);
      } else {
        throw new Error(`Unknown tool: ${name}`);
      }

      sendResponse({
        jsonrpc: '2.0',
        id: msg.id,
        result: {
          content: [
            {
              type: 'text',
              text: resultText
            }
          ]
        }
      });
    } catch (err) {
      sendResponse({
        jsonrpc: '2.0',
        id: msg.id,
        result: {
          content: [
            {
              type: 'text',
              text: `Error executing ${name}: ${err.message}`
            }
          ],
          isError: true
        }
      });
    }
    return;
  }

  if (msg.id !== undefined) {
    sendResponse({
      jsonrpc: '2.0',
      id: msg.id,
      error: {
        code: -32601,
        message: `Method not found: ${msg.method}`
      }
    });
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', (line) => {
  const trimmed = line.trim();
  if (!trimmed) return;
  try {
    const msg = JSON.parse(trimmed);
    handleMessage(msg);
  } catch (err) {
    // Non-JSON input ignored
  }
});
