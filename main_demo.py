"""Demo entry point for testing without OpenAI API key."""

import os
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Change to project root
os.chdir(Path(__file__).parent)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Now import tools directly without going through graph
from tools.log_reader import read_log_file
from tools.log_processor import process_log_events


def demo_without_llm():
    """
    Demo version that shows the agent flow without needing OpenAI API.
    This simulates LLM analysis with mock data.
    """
    load_dotenv()
    
    log_file = "examples/logs/app.log"
    
    if not Path(log_file).exists():
        print(f"ERROR: Log file not found: {log_file}")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("LOG ANALYZER AGENT - DEMO MODE (Sem OpenAI)")
    print("=" * 70)
    print(f"\nAnalisando: {log_file}")
    print("\n[*] Executando nos do agente (sem LLM)...\n")
    
    # Node 1: Validation
    print("[1/5] [validate_input] Validando arquivo...")
    if not log_file.endswith((".log", ".txt")):
        print("   [X] Arquivo invalido")
        sys.exit(1)
    print("   [OK] Arquivo validado")
    
    # Node 2: Reading
    print("\n[2/5] [read_log] Lendo arquivo...")
    max_lines = int(os.getenv("MAX_LOG_LINES", 500))
    result = read_log_file(log_file, max_lines=max_lines)
    
    if not result["success"]:
        print(f"   [X] Erro: {result['error']}")
        sys.exit(1)
    
    print(f"   [OK] Arquivo lido com sucesso")
    print(f"   [INFO] Total de linhas: {result['total_lines']}")
    print(f"   [INFO] Tamanho do arquivo: {result['file_size']} bytes")
    
    log_content = result["content"]
    metadata = {
        "file_path": log_file,
        "total_lines": result["total_lines"],
        "lines_read": result["lines_read"],
        "file_size": result["file_size"],
    }
    
    # Node 3: Processing
    print("\n[3/5] [parse_events] Processando eventos...")
    parsed_events = process_log_events(log_content)
    
    print(f"   [OK] Eventos processados")
    print(f"   [ERROR] ERRORs: {parsed_events['error_count']}")
    print(f"   [WARN] WARNINGs: {parsed_events['warning_count']}")
    print(f"   [INFO] INFOs: {parsed_events['info_count']}")
    print(f"   [OTHER] Outros: {parsed_events['other_count']}")
    
    # Node 4: Analysis (mock)
    print("\n[4/5] [analyze_with_llm] Analisando com IA (MOCK - sem OpenAI)...")
    
    mock_analysis = generate_mock_analysis(parsed_events)
    print("   [OK] Analise realizada (modo demo)")
    
    # Node 5: Report
    print("\n[5/5] [generate_report] Gerando relatorio...")
    
    report = generate_demo_report(
        metadata,
        parsed_events,
        mock_analysis
    )
    
    print("   [OK] Relatorio gerado\n")
    
    # Display report
    print("\n" + "=" * 70)
    print("RELATORIO GERADO")
    print("=" * 70)
    print(report)
    
    # Save report
    output_path = os.getenv("REPORT_OUTPUT_PATH", "examples/reports/")
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    report_file = Path(output_path) / "latest_report_demo.md"
    report_file.write_text(report, encoding='utf-8')
    print(f"\n[OK] Relatorio salvo em: {report_file}")
    
    print("\n" + "=" * 70)
    print("DEMO CONCLUIDO COM SUCESSO!")
    print("=" * 70)
    print("\n[*] Observacoes:")
    print("   - Este eh o modo DEMO (sem OpenAI)")
    print("   - A analise de IA foi substituida por padroes pre-definidos")
    print("   - Para analise completa, use main.py com OpenAI API key")
    print("   - Todos os outros nos funcionam normalmente\n")


def generate_mock_analysis(events: dict) -> str:
    """Generate mock LLM analysis without calling OpenAI."""
    
    analysis = "## Log Health Assessment\n\n"
    
    # Error rate analysis
    total = (events['error_count'] + events['warning_count'] + 
             events['info_count'] + events['other_count'])
    error_rate = (events['error_count'] / total * 100) if total > 0 else 0
    
    if error_rate > 20:
        analysis += f"** CRITICAL: Taxa de erro muito alta ({error_rate:.1f}%)\n\n"
    elif error_rate > 10:
        analysis += f"** HIGH: Taxa de erro elevada ({error_rate:.1f}%)\n\n"
    else:
        analysis += f"** GOOD: Taxa de erro aceitavel ({error_rate:.1f}%)\n\n"
    
    # Critical issues
    analysis += "## Critical Issues Identified\n\n"
    
    if events['error_count'] > 0:
        analysis += f"1. **Error Pattern**: {events['error_count']} ERRORs detected\n"
        
        if events['top_error_patterns']:
            analysis += "   Top error patterns:\n"
            for i, (pattern, count) in enumerate(events['top_error_patterns'][:3], 1):
                analysis += f"   - {pattern[:60]}... (x{count})\n"
    
    analysis += "\n## Root Cause Analysis\n\n"
    
    if any("API" in line.upper() or "connect" in line.lower() 
           for line in events['error_lines']):
        analysis += "- **Connectivity Issues**: Multiple API connection failures detected\n"
    
    if any("disk" in line.lower() or "memory" in line.lower() 
           for line in events['error_lines']):
        analysis += "- **Resource Exhaustion**: Disk or memory constraints detected\n"
    
    if any("null" in line.lower() or "exception" in line.lower() 
           for line in events['error_lines']):
        analysis += "- **Code Errors**: Null pointer or exception handling issues\n"
    
    analysis += "\n## Recommended Actions\n\n"
    analysis += "1. Investigate top error patterns with detailed logs\n"
    analysis += "2. Check system resource availability\n"
    analysis += "3. Review recent code deployments\n"
    analysis += "4. Set up alerts for error rate thresholds\n"
    
    return analysis


def generate_demo_report(metadata: dict, events: dict, analysis: str) -> str:
    """Generate the final demo report."""
    
    report = f"""# Technical Log Analysis Report - DEMO MODE

** NOTA: Este relatorio foi gerado em modo DEMO (sem OpenAI API).
A analise de IA eh simulada usando padroes heuristicos.
Para analise completa com IA, execute: `python main.py` com OpenAI API key.

## Executive Summary

File: {metadata['file_path']}
Analysis Date: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}
Mode: Demo (sem LLM)

## Log Statistics

- **Total Lines**: {events['total_lines']}
- **Lines Analyzed**: {metadata['lines_read']}
- **File Size**: {metadata['file_size']} bytes

## Issue Distribution

| Level | Count | Percentage |
|-------|-------|-----------|
| ERROR | {events['error_count']} | {(events['error_count']/events['total_lines']*100):.1f}% |
| WARNING | {events['warning_count']} | {(events['warning_count']/events['total_lines']*100):.1f}% |
| INFO | {events['info_count']} | {(events['info_count']/events['total_lines']*100):.1f}% |
| OTHER | {events['other_count']} | {(events['other_count']/events['total_lines']*100):.1f}% |

## Analysis & Insights (DEMO)

{analysis}

## Top Error Patterns

"""
    if events['top_error_patterns']:
        for i, (pattern, count) in enumerate(events['top_error_patterns'], 1):
            report += f"- **Pattern {i}**: {pattern[:80]}... \n  Occurrences: {count}\n"
    else:
        report += "- No error patterns found\n"
    
    report += """
## Recent Errors (Last 3)

"""
    
    if events['error_lines']:
        for line in events['error_lines'][-3:]:
            report += f"- {line}\n"
    else:
        report += "- No errors found\n"
    
    report += """
---

## Como Usar Este Projeto

### Modo DEMO (sem OpenAI):
```bash
python main_demo.py
```

### Modo Completo (com analise IA):
```bash
# 1. Obtenha uma chave OpenAI em: https://platform.openai.com/api-keys
# 2. Configure no .env
# 3. Execute:
python main.py
```

### Como Obter OpenAI API Key (Gratis ate $5):

1. Va para: https://platform.openai.com/account/api-keys
2. Faca login ou crie conta
3. Clique em "Create new secret key"
4. Copie a chave (comeca com 'sk-')
5. Cole no arquivo `.env`:
   ```
   OPENAI_API_KEY=sk-sua-chave-aqui
   ```

---

*Generated by Log Analyzer Agent - Demo Mode*
*Para analise completa, use OpenAI API*
"""
    
    return report


if __name__ == "__main__":
    demo_without_llm()
