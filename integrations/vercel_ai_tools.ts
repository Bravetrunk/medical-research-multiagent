/**
 * Vercel AI SDK (ai) Integration for Medical Research Multi-Agent
 * Compatible with Next.js, Node.js, and TypeScript AI agents.
 */

import { z } from 'zod';
// @ts-ignore: Imported from parent package
const { calculateSampleSizeTwoProportions, calculateDiagnosticMetrics } = require('../lib/calculators');
// @ts-ignore: Imported from parent package
const { MedicalResearchOrchestrator } = require('../lib/engine');

export const medicalResearchTools = {
  designClinicalProtocol: {
    description: 'Autonomous 7-agent DAG for medical research methodology: generates full publication-grade clinical trial protocols, PICO formulation, study design, biostatistics sample size, and causal DAG.',
    parameters: z.object({
      question: z.string().describe('The clinical research question or hypothesis')
    }),
    execute: async ({ question }: { question: string }) => {
      const orchestrator = new MedicalResearchOrchestrator();
      const state = orchestrator.runPipeline(question);
      return state.markdownReport;
    }
  },

  calculateRCTSampleSize: {
    description: 'Calculates exact sample size for two-arm parallel superiority RCT based on Daniel Biostatistics.',
    parameters: z.object({
      p1: z.number().describe('Event proportion in control group (e.g. 0.35)'),
      p2: z.number().describe('Event proportion in intervention group (e.g. 0.15)'),
      alpha: z.number().default(0.05),
      power: z.number().default(0.80),
      dropoutRate: z.number().default(0.15)
    }),
    execute: async ({ p1, p2, alpha, power, dropoutRate }: any) => {
      return calculateSampleSizeTwoProportions(p1, p2, alpha, power, dropoutRate);
    }
  },

  calculateDiagnosticMatrix: {
    description: 'Calculate diagnostic accuracy metrics: Sensitivity, Specificity, PPV, NPV, LR+, LR-, and Bayesian post-test probability.',
    parameters: z.object({
      tp: z.number().describe('True Positives'),
      fp: z.number().describe('False Positives'),
      fn: z.number().describe('False Negatives'),
      tn: z.number().describe('True Negatives'),
      preTestProb: z.number().optional().describe('Pre-test probability / prevalence (0-1)')
    }),
    execute: async ({ tp, fp, fn, tn, preTestProb }: any) => {
      return calculateDiagnosticMetrics(tp, fp, fn, tn, preTestProb ?? null);
    }
  }
};
