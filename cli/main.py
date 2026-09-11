#!/usr/bin/env python3
import sys
import os
import argparse

# Add parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.engine import MedicalResearchMultiAgentOrchestrator

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.table import Table
    console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

def print_banner():
    banner = """
================================================================================
 🩺 Medical Research & Methodology Multi-Agent AI System
 Grounded on: Chulalongkorn University DAB Unit (Dr. Amarit Tansawet),
              Clinical Epidemiology (Fletcher), Biostatistics (Daniel 9th ed.),
              and Causal AI & RWE (Pearl, Hernán & Robins)
================================================================================
"""
    if HAS_RICH:
        console.print(Panel(
            "[bold cyan]🩺 Medical Research & Methodology Multi-Agent AI System[/bold cyan]\n"
            "[dim]Faculty of Medicine, Chulalongkorn University (DAB Unit) Knowledge Base[/dim]\n"
            "[green]Multi-Agent DAG: PICO → Study Design → Biostats → Diagnostic → Causal RWE → Appraisal → PI Synthesis[/green]",
            border_style="blue"
        ))
    else:
        print(banner)

def main():
    parser = argparse.ArgumentParser(
        description="Autonomous Multi-Agent AI System for Medical Research & Methodology (Notion-Grounded)"
    )
    parser.add_argument("query", nargs="?", help="Clinical research question or trial description")
    parser.add_argument("--population", "-p", help="Target population")
    parser.add_argument("--intervention", "-i", help="Experimental intervention / exposure")
    parser.add_argument("--comparison", "-c", help="Comparator / control")
    parser.add_argument("--outcome", "-o", help="Primary clinical outcome")
    parser.add_argument("--output", "-f", help="Path to save the final Markdown Protocol report")
    parser.add_argument("--tp", type=int, help="True Positives (for diagnostic test evaluation)")
    parser.add_argument("--fp", type=int, help="False Positives")
    parser.add_argument("--fn", type=int, help="False Negatives")
    parser.add_argument("--tn", type=int, help="True Negatives")
    parser.add_argument("--pre-test-prob", type=float, default=0.20, help="Pre-test probability (0.0 to 1.0)")
    parser.add_argument("--interactive", action="store_true", help="Launch interactive interview mode")

    args = parser.parse_args()
    print_banner()

    query = args.query
    if args.interactive or not query:
        print("\n--- 📝 Interactive Medical Research Formulation ---")
        if not query:
            query = input("Enter your clinical research topic or question: ").strip()
            if not query:
                query = "In adult patients with heart failure and reduced ejection fraction, does dapagliflozin reduce cardiovascular death compared with standard of care?"
                print(f"Defaulting to: {query}\n")

    # Combine PICO flags if provided
    combined_query = query
    extras = []
    if args.population: extras.append(f"Population: {args.population}")
    if args.intervention: extras.append(f"Intervention: {args.intervention}")
    if args.comparison: extras.append(f"Comparison: {args.comparison}")
    if args.outcome: extras.append(f"Outcome: {args.outcome}")
    if extras:
        combined_query += " (" + ", ".join(extras) + ")"

    diagnostic_params = None
    if args.tp is not None and args.fp is not None and args.fn is not None and args.tn is not None:
        diagnostic_params = {
            "tp": args.tp,
            "fp": args.fp,
            "fn": args.fn,
            "tn": args.tn,
            "pre_test_prob": args.pre_test_prob
        }

    if HAS_RICH:
        console.print(f"\n[bold yellow]🚀 Initiating Multi-Agent Pipeline for:[/bold yellow] [bold white]'{combined_query}'[/bold white]\n")
    else:
        print(f"\n🚀 Initiating Multi-Agent Pipeline for: '{combined_query}'\n")

    orchestrator = MedicalResearchMultiAgentOrchestrator()
    state = orchestrator.run_pipeline(combined_query, diagnostic_params=diagnostic_params)

    # Display Execution Logs
    if HAS_RICH:
        table = Table(title="🤖 Multi-Agent Execution Trace", border_style="dim")
        table.add_column("Agent", style="cyan", no_wrap=True)
        table.add_column("Action Performed", style="green")
        for log in state.agent_logs:
            table.add_row(log["agent"], log["action"])
        console.print(table)
        console.print("\n")
        console.print(Panel("[bold green]✅ Protocol Dossier Generated Successfully![/bold green]", border_style="green"))
        console.print(Markdown(state.markdown_report))
    else:
        print("\n--- 🤖 Multi-Agent Execution Trace ---")
        for log in state.agent_logs:
            print(f"[{log['agent']}] -> {log['action']}")
        print("\n" + "="*80)
        print(state.markdown_report)
        print("="*80)

    # Save to file
    out_file = args.output or "medical_research_protocol.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(state.markdown_report)
    
    if HAS_RICH:
        console.print(f"\n[bold cyan]💾 Master Research Protocol saved to:[/bold cyan] [bold underline]{out_file}[/bold underline]\n")
    else:
        print(f"\n💾 Master Research Protocol saved to: {out_file}\n")

if __name__ == "__main__":
    main()
