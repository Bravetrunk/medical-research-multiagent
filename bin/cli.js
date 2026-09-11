#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { MedicalResearchOrchestrator } = require('../lib/engine');

// ANSI Color Helpers
const c = {
  reset: "\x1b[0m",
  bold: "\x1b[1m",
  dim: "\x1b[2m",
  cyan: "\x1b[36m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  white: "\x1b[37m"
};

function printBanner() {
  console.log(`\n${c.bold}${c.cyan}================================================================================${c.reset}`);
  console.log(` ${c.bold}${c.white}🩺 Medical Research & Methodology Multi-Agent AI System${c.reset} ${c.dim}(Node.js CLI)${c.reset}`);
  console.log(` ${c.dim}Grounded on: Faculty of Medicine, Chulalongkorn University (DAB Unit)${c.reset}`);
  console.log(` ${c.green}7-Agent DAG: PICO → Study Design → Biostats → Diagnostic → Causal RWE → Appraisal → PI${c.reset}`);
  console.log(`${c.bold}${c.cyan}================================================================================${c.reset}\n`);
}

function parseArgs() {
  const args = process.argv.slice(2);
  const options = {
    query: "",
    output: "medical_research_protocol.md",
    tp: null,
    fp: null,
    fn: null,
    tn: null,
    preTestProb: 0.20,
    interactive: false
  };

  const positional = [];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === '--interactive' || arg === '-i') {
      options.interactive = true;
    } else if (arg === '--output' || arg === '-o' || arg === '-f') {
      options.output = args[++i];
    } else if (arg === '--tp') {
      options.tp = parseInt(args[++i], 10);
    } else if (arg === '--fp') {
      options.fp = parseInt(args[++i], 10);
    } else if (arg === '--fn') {
      options.fn = parseInt(args[++i], 10);
    } else if (arg === '--tn') {
      options.tn = parseInt(args[++i], 10);
    } else if (arg === '--pre-test-prob') {
      options.preTestProb = parseFloat(args[++i]);
    } else if (arg.startsWith('-')) {
      // ignore unknown flag
    } else {
      positional.push(arg);
    }
  }

  options.query = positional.join(' ');
  return options;
}

async function run() {
  printBanner();
  const options = parseArgs();

  let query = options.query;
  if (options.interactive || !query) {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    query = await new Promise(resolve => {
      rl.question(`${c.bold}${c.yellow}Enter your clinical research question / trial topic:${c.reset} `, answer => {
        rl.close();
        resolve(answer.trim());
      });
    });

    if (!query) {
      query = "In adult patients with heart failure, does dapagliflozin reduce cardiovascular death compared with standard of care?";
      console.log(`${c.dim}Defaulting to: ${query}${c.reset}\n`);
    }
  }

  console.log(`${c.bold}${c.yellow}🚀 Initiating Multi-Agent Pipeline for:${c.reset} ${c.bold}${c.white}"${query}"${c.reset}\n`);

  const orchestrator = new MedicalResearchOrchestrator();
  const diagParams = (options.tp !== null && options.fp !== null && options.fn !== null && options.tn !== null)
    ? { tp: options.tp, fp: options.fp, fn: options.fn, tn: options.tn, preTestProb: options.preTestProb }
    : null;

  const state = orchestrator.runPipeline(query, { diagnosticParams: diagParams });

  console.log(`${c.bold}${c.green}--- 🤖 Multi-Agent Execution Trace ---${c.reset}`);
  state.agentLogs.forEach(log => {
    console.log(`[${c.cyan}${log.agent}${c.reset}] ➔ ${c.green}${log.action}${c.reset}`);
  });

  console.log(`\n${c.bold}${c.cyan}================================================================================${c.reset}`);
  console.log(state.markdownReport);
  console.log(`${c.bold}${c.cyan}================================================================================${c.reset}\n`);

  fs.writeFileSync(options.output, state.markdownReport, 'utf8');
  console.log(`${c.bold}${c.green}💾 Master Research Protocol saved to:${c.reset} ${c.bold}${c.white}${options.output}${c.reset}\n`);
}

run().catch(err => {
  console.error(`${c.bold}\x1b[31mError:${c.reset}`, err);
  process.exit(1);
});
