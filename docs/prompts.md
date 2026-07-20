# Documentação de Prompts - Log Analyzer Agent

Este documento descreve os principais prompts utilizados no agente de análise de logs, explicando sua função e como foram otimizados para o caso de uso.

## 1. System Prompt - Análise Técnica

**Localização**: `src/agent/graph.py` - Nó `analyze_with_llm`

```python
system_prompt = """You are a technical log analysis expert. Your task is to analyze application logs and provide:
1. A summary of the log health
2. Critical issues identified
3. Patterns and root causes
4. Recommended actions

Be concise, technical, and actionable."""
```

### Objetivo

Define o papel e comportamento do modelo LLM durante a análise. Este prompt:

- **Estabelece especialidade**: "technical log analysis expert"
- **Define responsabilidades claras**: 4 pontos específicos de análise
- **Define tom**: conciso, técnico, acionável
- **Evita ambiguidade**: instruções diretas e sem margem para interpretação

### Rationale

A escolha de um "expert" com responsabilidades bem-definidas garante que:
1. O modelo foca em análise técnica, não em geração criativa
2. A saída segue um formato previsível e estruturado
3. As recomendações são práticas e implementáveis

## 2. User Prompt - Contexto de Análise

**Localização**: `src/agent/graph.py` - Nó `analyze_with_llm`

```python
events_summary = f"""
Log Analysis Summary:
- Total Lines: {state.parsed_events['total_lines']}
- Error Count: {state.parsed_events['error_count']}
- Warning Count: {state.parsed_events['warning_count']}
- Info Count: {state.parsed_events['info_count']}

Top Error Patterns:
{chr(10).join([f"  - {pattern[0][:80]}... (appears {pattern[1]} times)" for pattern in state.parsed_events['top_error_patterns']])}

Recent Errors (up to 10 most recent):
{chr(10).join(state.parsed_events['error_lines'][-3:])}

Recent Warnings (up to 5 most recent):
{chr(10).join(state.parsed_events['warning_lines'][-2:])}
"""

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=f"Please analyze these logs and provide insights:\n\n{events_summary}")
]
```

### Objetivo

Fornece contexto estruturado e pré-processado ao modelo, incluindo:

- **Estatísticas numéricas**: contagem de cada nível de log
- **Padrões identificados**: erros mais frequentes
- **Exemplos recentes**: últimas ocorrências de problemas
- **Instrução clara**: pedido explícito de análise

### Rationale

Esta estrutura:

1. **Reduz alucinação**: dados concretos limitam especulação
2. **Acelera processamento**: resumo pré-processado vs. milhões de linhas
3. **Melhora precisão**: padrões já identificados guiam análise
4. **Economiza tokens**: contexto focado reduz custos

### Exemplo de Entrada

```
Log Analysis Summary:
- Total Lines: 28
- Error Count: 6
- Warning Count: 5
- Info Count: 12
- Other Count: 5

Top Error Patterns:
  - Failed to connect to external API: timeout after 30s (appears 2 times)
  - Exception in thread pool executor: ConnectionRefusedError (appears 1 times)
  - NullPointerException in data processing pipeline (appears 1 times)
  - FATAL: Unable to process batch - rolling back transaction (appears 1 times)
  - Disk space critical: unable to write logs (appears 1 times)

Recent Errors (up to 10 most recent):
2024-01-15 10:27:04 [ERROR] FATAL: Unable to process batch - rolling back transaction
2024-01-15 10:29:46 [ERROR] Disk space critical: unable to write logs

Recent Warnings (up to 5 most recent):
2024-01-15 10:32:31 [WARNING] CPU usage spike detected: 92%
```

## 3. Processamento de Eventos - Padrões

**Localização**: `src/tools/log_processor.py` - Função `process_log_events`

### Estratégia de Classificação

```python
# Classificação por keywords
if "ERROR" in line_upper or "EXCEPTION" in line_upper:
    error_count += 1
elif "WARNING" in line_upper or "WARN" in line_upper:
    warning_count += 1
elif "INFO" in line_upper:
    info_count += 1
else:
    other_count += 1
```

### Extração de Padrões

```python
# Captura contexto ao redor do erro
pattern = line[max(0, line_upper.find("ERROR") - 20):min(len(line), line_upper.find("ERROR") + 80)]
error_patterns[pattern.strip()] += 1
```

### Objetivo

Transformar logs brutos em dados estruturados e analisáveis:

1. **Categorização**: agrupa por nível
2. **Frequência**: identifica erros recorrentes
3. **Contexto**: preserva mensagem do erro
4. **Ranking**: ordena por frequência

## 4. Validação de Entrada

**Localização**: `src/agent/graph.py` - Nó `validate_input`

```python
def validate_input(state: LogAnalysisState) -> LogAnalysisState:
    if not state.log_file_path:
        state.validation_errors.append("Log file path is required")
        state.is_valid = False
    
    if not state.log_file_path.endswith((".log", ".txt")):
        state.validation_errors.append("File must be a .log or .txt file")
        state.is_valid = False
    
    return state
```

### Validações Implementadas

1. **Não-nulidade**: arquivo deve ser especificado
2. **Tipo de arquivo**: apenas .log ou .txt
3. **Segurança**: verificação de path traversal em `read_log_file`
4. **Existência**: arquivo deve existir

## 5. Segurança na Leitura de Arquivos

**Localização**: `src/tools/log_reader.py`

```python
# Prevenção de path traversal
if ".." in file_path or file_path.startswith("/etc"):
    return {"success": False, "error": "Invalid file path: path traversal detected"}

# Validação de existência
if not path.exists():
    return {"success": False, "error": f"File not found: {file_path}"}

# Validação de tipo
if not path.is_file():
    return {"success": False, "error": f"Path is not a file: {file_path}"}
```

### Princípios de Segurança

1. **Validação de entrada**: rejeita padrões suspeitos
2. **Tratamento de erros**: retorna respostas estruturadas
3. **Encoding seguro**: `encoding="utf-8", errors="ignore"`
4. **Limite de linhas**: `max_lines` previne carregamento de arquivos enormes

## 6. Estrutura de Saída - Relatório

**Localização**: `src/agent/graph.py` - Nó `generate_report`

```markdown
# Technical Log Analysis Report

## Executive Summary
File: {file_path}
Analysis Date: {date}

## Log Statistics
- **Total Lines**: {total}
- **Lines Analyzed**: {analyzed}
- **File Size**: {size} bytes

## Issue Distribution
| Level | Count |
|-------|-------|
| ERROR | {error_count} |
| WARNING | {warning_count} |
| INFO | {info_count} |
| OTHER | {other_count} |

## Analysis & Insights
{llm_analysis}

## Top Error Patterns
{top_patterns}
```

### Objetivo

Estrutura profissional que:

1. **Sumariza executivamente**: títulos e datas claros
2. **Apresenta dados**: tabelas e números
3. **Integra análise IA**: insights estruturados
4. **Lista ações**: padrões específicos
5. **É documentável**: Markdown pronto para compartilhamento

## 7. Optimizações e Trade-offs

### Otimizações Implementadas

| Aspecto | Otimização | Benefício |
|---------|-----------|-----------|
| **Tokens** | Summarização de logs | Reduz custo de API |
| **Velocidade** | Processamento local primero | Análise IA apenas onde necessário |
| **Precisão** | Padrões pré-processados | Contexto melhor para LLM |
| **Segurança** | Validação rigorosa | Previne exploração |
| **Usabilidade** | Formato Markdown | Pronto para documentação |

### Trade-offs

1. **Limite de linhas**: Máx 500 linhas por padrão
   - **Pro**: Reduz tokens, acelera processamento
   - **Con**: Pode perder contexto de logs grandes

2. **Extração de padrões**: Top 5 apenas
   - **Pro**: Foca em principais problemas
   - **Con**: Padrões menores são ignorados

3. **Análise GPT-4**:
   - **Pro**: Qualidade superior vs GPT-3.5
   - **Con**: Custo mais alto, latência aumentada

## 8. Casos de Uso e Exemplos

### Caso 1: Diagnóstico de Falha de API

**Log de entrada**:
```
[ERROR] Failed to connect to external API: timeout after 30s
[ERROR] Failed to connect to external API: timeout after 30s
[WARNING] Retrying API connection in 5 seconds
```

**Análise esperada**:
```
Critical Issue: External API is unreachable
Root Cause: Service timeout or connectivity issue
Recommended Action: Check API service status and network connectivity
```

### Caso 2: Problema de Recursos

**Log de entrada**:
```
[WARNING] High memory usage detected: 78% of available RAM
[WARNING] Disk usage warning: 85% capacity
[ERROR] Disk space critical: unable to write logs
```

**Análise esperada**:
```
Critical Issue: Resource exhaustion (disk and memory)
Root Cause: Insufficient cleanup, accumulation of temporary files
Recommended Action: Implement automated cleanup and increase monitoring
```

## 9. Evolução Futura

### Prompts Sugeridos para Expansão

1. **Classificação de Severidade** (TODO)
   ```
   Classify each error into: CRITICAL, HIGH, MEDIUM, LOW
   ```

2. **Detecção de Anomalias** (TODO)
   ```
   Compare error rates against historical baselines
   Flag unusual patterns
   ```

3. **Sugestões de Correção** (TODO)
   ```
   For each critical error, suggest specific code fixes
   Include relevant documentation links
   ```

4. **Análise Temporal** (TODO)
   ```
   Identify if errors cluster at specific times
   Correlate with deployment events or schedule
   ```

## 10. Referências

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [LangChain Prompts Documentation](https://python.langchain.com/docs/modules/model_io/prompts/)
- [Best Practices for LLM Applications](https://www.promptingguide.ai/)

---

**Última atualização**: 20 de julho de 2026
**Versão**: 1.0
**Status**: Completo para Mini-Projeto M2S05
