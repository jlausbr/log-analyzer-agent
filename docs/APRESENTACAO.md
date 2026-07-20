# Log Analyzer Agent - Apresentação Mini-Projeto

## Slide 1: Visão Geral do Projeto

### Log Analyzer Agent 🤖📊

**Agente IA para Análise Automatizada de Logs**

---

### O Problema

```
Desenvolvedores e DevOps enfrentam desafios:
❌ Análise manual de logs é demorada
❌ Difícil identificar padrões em milhares de linhas
❌ Diagnóstico de root cause exige expertise
❌ Gerar relatórios é processo repetitivo
```

### A Solução

```
✅ Agente inteligente com LangGraph + GPT-4
✅ Processa logs e identifica padrões
✅ Análise contextual com IA
✅ Relatórios técnicos automáticos
```

---

### Fluxo da Aplicação

```
📝 Log File
    ↓
✅ Validate Input
    ↓
📖 Read Log File (Custom Tool)
    ↓
🔍 Parse Events & Categorize
    ↓
🤖 Analyze with GPT-4 (LLM)
    ↓
📋 Generate Report (Markdown)
    ↓
✨ Professional Report
```

---

### Stack Tecnológico

| Componente | Tecnologia | Função |
|-----------|-----------|---------|
| **Orquestração** | LangGraph | Gerencia fluxo de nós |
| **LLM** | OpenAI GPT-4 | Análise inteligente |
| **Framework** | LangChain | Integração com modelos |
| **Tipagem** | Pydantic | Validação de dados |
| **Linguagem** | Python 3.10+ | Implementação |

---

### Ferramentas Customizadas

#### 1️⃣ `read_log_file(path, max_lines)`
- Lê arquivos de log com segurança
- Previne path traversal attacks
- Retorna metadados do arquivo
- Suporta truncamento de linhas grandes

#### 2️⃣ `process_log_events(content)`
- Categoriza eventos por nível (ERROR, WARNING, INFO)
- Extrai padrões de erro recorrentes
- Conta frequência de problemas
- Prepara contexto para LLM

---

### Exemplo de Entrada & Saída

**Entrada: arquivo app.log**
```
[ERROR] Failed to connect to external API: timeout
[ERROR] Failed to connect to external API: timeout
[WARNING] Retrying API connection in 5 seconds
[ERROR] NullPointerException in data processing
```

**Saída: Relatório Técnico Markdown**
```markdown
# Technical Log Analysis Report

## Critical Issues
1. **API Connectivity**: External API is unreachable
   - Appears 2 times
   - Root Cause: Service timeout
   
2. **Data Processing Error**: NullPointerException detected
   - Impact: Transaction rolled back
```

---

### Conceitos de IA Aplicados

🧠 **LangGraph - Orchestration**
- StateGraph para definir workflow
- Nós executam lógica determinística
- Edges conectam nós em sequência
- Estado imutável entre transições

🤖 **LLM - Análise Inteligente**
- GPT-4 para insights contextuais
- Prompts otimizados para log analysis
- System + User messages para guiar modelo
- Chain of thought para raciocínio estruturado

🔐 **Segurança**
- Validação de entrada rigorosa
- Prevenção de path traversal
- Tratamento de erros estruturado
- Encoding seguro de arquivos

---

### Resultados Esperados

✅ **Funcionalidade Completa**
- Agent lê logs reais
- Processamento automático
- Relatórios gerados com sucesso

✅ **Qualidade de Análise**
- Identifica problemas corretamente
- Sugere ações corretivas
- Formato profissional

✅ **Robustez**
- Maneja erros gracefully
- Validação em cada etapa
- Segurança nas operações

---

## Slide 2: Implementação Técnica Detalhada

### Arquitetura em Detalhes

```python
# Estado do Agent (Pydantic BaseModel)
class LogAnalysisState(BaseModel):
    log_file_path: str              # Input
    log_file_content: Optional[str] # Raw content
    parsed_events: Optional[dict]   # Structured data
    analysis_result: Optional[dict] # LLM output
    report: Optional[str]           # Final markdown
    is_valid: bool                  # Validation flag
```

---

### Nós do LangGraph

#### Nó 1: `validate_input`
```python
def validate_input(state: LogAnalysisState) -> LogAnalysisState:
    """Valida caminho do arquivo e tipo"""
    if not state.log_file_path:
        state.validation_errors.append("Path required")
    if not state.log_file_path.endswith((".log", ".txt")):
        state.validation_errors.append("Must be .log or .txt")
    return state
```
**Output**: `is_valid`, `validation_errors`

#### Nó 2: `read_log`
```python
def read_log(state: LogAnalysisState) -> LogAnalysisState:
    """Lê arquivo usando ferramenta customizada"""
    result = read_log_file(
        state.log_file_path, 
        max_lines=int(os.getenv("MAX_LOG_LINES", 500))
    )
    state.log_file_content = result["content"]
    state.log_metadata = {
        "file_path": state.log_file_path,
        "total_lines": result["total_lines"],
        "lines_read": result["lines_read"],
        "file_size": result["file_size"]
    }
    return state
```
**Output**: `log_file_content`, `log_metadata`

---

#### Nó 3: `parse_events`
```python
def parse_events(state: LogAnalysisState) -> LogAnalysisState:
    """Processa e categoriza eventos de log"""
    state.parsed_events = process_log_events(
        state.log_file_content
    )
    # Resultado inclui:
    # - total_lines, error_count, warning_count, info_count
    # - error_lines, warning_lines (últimos N)
    # - top_error_patterns (ranking por frequência)
    return state
```
**Output**: `parsed_events` com análise estatística

#### Nó 4: `analyze_with_llm`
```python
def analyze_with_llm(state: LogAnalysisState) -> LogAnalysisState:
    """Análise inteligente com GPT-4"""
    system_prompt = """You are a technical log analysis expert..."""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Analyze: {events_summary}")
    ]
    
    response = llm.invoke(messages)
    state.analysis_result = {
        "llm_analysis": response.content
    }
    return state
```
**Output**: `analysis_result` com insights do LLM

#### Nó 5: `generate_report`
```python
def generate_report(state: LogAnalysisState) -> LogAnalysisState:
    """Formata análise em relatório Markdown profissional"""
    report = f"""# Technical Log Analysis Report
    
## Executive Summary
File: {state.log_metadata['file_path']}
...
## Log Statistics
| Level | Count |
|-------|-------|
| ERROR | {events['error_count']} |
| WARNING | {events['warning_count']} |
...
## Analysis & Insights
{state.analysis_result['llm_analysis']}
    """
    state.report = report
    return state
```
**Output**: `report` em Markdown

---

### Construção do Grafo

```python
def create_log_analyzer_agent():
    """Compila o grafo LangGraph"""
    workflow = StateGraph(LogAnalysisState)
    
    # Adiciona nós
    workflow.add_node("validate_input", validate_input)
    workflow.add_node("read_log", read_log)
    workflow.add_node("parse_events", parse_events)
    workflow.add_node("analyze_with_llm", analyze_with_llm)
    workflow.add_node("generate_report", generate_report)
    
    # Conecta nós em sequência
    workflow.add_edge("validate_input", "read_log")
    workflow.add_edge("read_log", "parse_events")
    workflow.add_edge("parse_events", "analyze_with_llm")
    workflow.add_edge("analyze_with_llm", "generate_report")
    workflow.add_edge("generate_report", END)
    
    # Define entrada e compila
    workflow.set_entry_point("validate_input")
    return workflow.compile()
```

---

### Ferramentas Customizadas - Implementação

#### Tool 1: `read_log_file`
```python
def read_log_file(file_path: str, max_lines: Optional[int] = None) -> dict:
    """
    Lê arquivo com segurança
    - Valida path (previne traversal)
    - Verifica existência e tipo
    - Retorna metadata
    """
    # Validações de segurança
    if ".." in file_path or file_path.startswith("/etc"):
        return {"success": False, "error": "Path traversal detected"}
    
    path = Path(file_path)
    if not path.exists():
        return {"success": False, "error": "File not found"}
    
    # Lê com limite
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    if max_lines and max_lines > 0:
        lines = lines[:max_lines]
    
    return {
        "success": True,
        "content": "".join(lines),
        "total_lines": len(lines),
        "file_size": path.stat().st_size
    }
```

#### Tool 2: `process_log_events`
```python
def process_log_events(log_content: str) -> dict:
    """
    Processa log em estrutura analisável
    - Categoriza por nível
    - Extrai padrões
    - Ordena por frequência
    """
    error_lines = []
    error_patterns = defaultdict(int)
    
    for line in log_content.split("\n"):
        if "ERROR" in line.upper():
            error_lines.append(line)
            # Extrai padrão (contexto ao redor de ERROR)
            pattern = line[...window...]
            error_patterns[pattern] += 1
    
    # Retorna análise estruturada
    top_patterns = sorted(
        error_patterns.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]
    
    return {
        "total_lines": total,
        "error_count": error_cnt,
        "error_lines": error_lines[-10:],
        "top_error_patterns": top_patterns
    }
```

---

### Integração com OpenAI

```python
from langchain_openai import ChatOpenAI

# Inicializa modelo
llm = ChatOpenAI(
    model="gpt-4-turbo-preview",
    temperature=0.3,  # Mais determinístico
    api_key=os.getenv("OPENAI_API_KEY")
)

# Usa em prompts
from langchain.schema import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="Você é especialista em análise de logs..."),
    HumanMessage(content="Analise estes logs...")
]

response = llm.invoke(messages)
```

**Configurações**:
- `model`: GPT-4 Turbo para qualidade superior
- `temperature`: 0.3 para análise consistente (não criativa)
- `api_key`: Carregado de `.env`

---

### Estrutura de Saída

```markdown
# Technical Log Analysis Report

## Executive Summary
File: examples/logs/app.log
Analysis Date: [timestamp]

## Log Statistics
- Total Lines: 28
- Lines Analyzed: 28
- File Size: 2847 bytes

## Issue Distribution
| Level | Count |
|-------|-------|
| ERROR | 6 |
| WARNING | 5 |
| INFO | 12 |
| OTHER | 5 |

## Analysis & Insights
[Análise do GPT-4]

## Top Error Patterns
- Pattern 1: Failed to connect to external API (2x)
- Pattern 2: NullPointerException (1x)

---
*Generated by Log Analyzer Agent using LangGraph*
```

---

### Execução

```bash
# Instalação
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Configuração
cp .env.example .env
# Editar .env com OpenAI API key

# Execução
python main.py
```

**Output**:
```
Initializing Log Analyzer Agent...
Analyzing log file: examples/logs/app.log
============================================================
ANALYSIS COMPLETE
============================================================

Report saved to: examples/reports/latest_report.md
```

---

### Aprendizados Principais

📚 **Conceitos de IA Aplicados**
1. ✅ LangGraph para orquestração
2. ✅ LLMs para análise contextual
3. ✅ Ferramentas customizadas
4. ✅ Validação de estado
5. ✅ Prompts otimizados

🔧 **Boas Práticas**
1. ✅ Validação rigorosa de entrada
2. ✅ Tratamento de erros estruturado
3. ✅ Código modular e reutilizável
4. ✅ Tipagem com Pydantic
5. ✅ Documentação completa

🚀 **Próximos Passos (Futuro)**
- Armazenamento em banco de dados
- Dashboard web com Flask/FastAPI
- Alertas em tempo real
- Análise histórica comparativa
- Integração com Slack/Teams

---

### Conclusão

Este projeto demonstra:

✨ **Aplicação prática de LangGraph** em problema real
✨ **Integração com LLMs** para análise inteligente
✨ **Engenharia de prompts** otimizada
✨ **Boas práticas de desenvolvimento** com Python
✨ **Fundação sólida** para sistemas de IA complexos

---

**Mini-Projeto M2S05 - IA para Desenvolvedores**
**Autor**: jlausbr
**Data**: 20 de julho de 2026
**Status**: ✅ Completo
