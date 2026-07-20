# Log Analyzer Agent - Agente IA para Análise de Logs

Um agente inteligente alimentado por IA para análise automatizada de arquivos de log de aplicações, gerando relatórios técnicos detalhados usando **LangGraph** e **OpenAI GPT-4**.

## 📋 Visão Geral

Este projeto implementa um agente autônomo que:

1. **Lê** arquivos de log de aplicações
2. **Processa** eventos de log e extrai padrões
3. **Analisa** com IA (GPT-4) para identificar problemas e causas raiz
4. **Gera** relatórios técnicos estruturados e acionáveis

O agente utiliza **LangGraph** para orquestrar o fluxo de trabalho, combinando processamento determinístico com análise inteligente baseada em LLM.

### Caso de Uso

Desenvolvedores e operações usam este agente para:
- Diagnosticar problemas rapidamente a partir de logs
- Identificar padrões de erro recorrentes
- Obter insights sobre saúde da aplicação
- Gerar documentação automatizada de incidentes

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                   Log Analyzer Agent                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐   ┌──────────────┐   ┌───────────────┐   │
│  │   Validate   │──→│  Read Log    │──→│ Parse Events  │   │
│  │    Input     │   │    File      │   │  & Categorize │   │
│  └──────────────┘   └──────────────┘   └───────────────┘   │
│                                             │                │
│                                             ↓                │
│                                    ┌──────────────────┐     │
│                                    │  Analyze with    │     │
│                                    │  LLM (GPT-4)     │     │
│                                    └──────────────────┘     │
│                                             │                │
│                                             ↓                │
│                                    ┌──────────────────┐     │
│                                    │ Generate Report  │     │
│                                    └──────────────────┘     │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Fluxo de Nós

| Nó | Descrição | Entrada | Saída |
|-----|-----------|---------|-------|
| **validate_input** | Valida caminho do arquivo de log | `log_file_path` | `is_valid`, `validation_errors` |
| **read_log** | Lê arquivo de log usando ferramenta customizada | `log_file_path` | `log_file_content`, `log_metadata` |
| **parse_events** | Processa eventos, categoriza por nível (ERROR, WARNING, INFO) | `log_file_content` | `parsed_events` |
| **analyze_with_llm** | Análise inteligente usando GPT-4 | `parsed_events` | `analysis_result` |
| **generate_report** | Formata saída em relatório técnico Markdown | Todos os anteriores | `report` |

## 🚀 Começando

### Pré-requisitos

- Python 3.10+
- Conta OpenAI com API key
- pip ou uv

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/jlausbr/log-analyzer-agent.git
cd log-analyzer-agent
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Instale dependências:**
```bash
pip install -r requirements.txt
```

Ou com uv:
```bash
uv pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Copie `.env.example` para `.env`:
```bash
cp .env.example .env
```

Edite `.env` e adicione sua OpenAI API key:
```env
OPENAI_API_KEY=sk-your-actual-key-here
LOG_FILE_PATH=examples/logs/app.log
MAX_LOG_LINES=500
REPORT_OUTPUT_PATH=examples/reports/
```

### Execução

#### Opção 1: Modo DEMO (Sem OpenAI - Recomendado para começar)

```bash
python main_demo.py
```

Este modo funciona **sem chave OpenAI** e simula a análise de IA com padrões heurísticos.
Ideal para testar, aprender e avaliar a estrutura do projeto.

#### Opção 2: Modo Completo (Com Análise IA Real)

```bash
python main.py
```

Este modo usa **GPT-4** para análise inteligente (requer OpenAI API key).
Para configurar a chave, veja [OPENAI_SETUP.md](OPENAI_SETUP.md).

### Fluxo de Execução

O agente irá:
1. Validar o arquivo de entrada
2. Ler o arquivo de log
3. Processar e categorizar eventos
4. Analisar com IA (ou modo simulado)
5. Gerar um relatório em `examples/reports/`

## 📁 Estrutura do Projeto

```
log-analyzer-agent/
├── src/
│   ├── __init__.py
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── state.py          # Definição do estado do agente
│   │   └── graph.py          # Definição do grafo LangGraph
│   └── tools/
│       ├── __init__.py
│       ├── log_reader.py     # Ferramenta para ler arquivos
│       └── log_processor.py  # Ferramenta para processar eventos
├── examples/
│   ├── logs/
│   │   └── app.log           # Arquivo de log de exemplo
│   └── reports/
│       └── latest_report.md  # Relatório gerado
├── main.py                   # Ponto de entrada
├── pyproject.toml            # Configuração do projeto
├── .env.example              # Exemplo de variáveis de ambiente
├── .gitignore                # Arquivo Git ignore
└── README.md                 # Este arquivo
```

## 🔧 Componentes Principais

### State (`src/agent/state.py`)

Pydantic BaseModel que rastreia o estado da análise:

```python
class LogAnalysisState(BaseModel):
    log_file_path: str                    # Entrada: caminho do arquivo
    log_file_content: Optional[str]       # Conteúdo bruto do log
    log_metadata: Optional[dict]          # Metadados do arquivo
    parsed_events: Optional[dict]         # Eventos categorizados
    analysis_result: Optional[dict]       # Análise do LLM
    validation_errors: List[str]          # Erros de validação
    is_valid: bool                        # Flag de validação
    report: Optional[str]                 # Relatório final (Markdown)
```

### Ferramentas Customizadas

#### `read_log_file(file_path, max_lines)`
Lê arquivo de log com validações de segurança:
- Previne path traversal attacks
- Valida existência e tipo de arquivo
- Retorna metadados (tamanho, linhas totais, etc)
- Suporta limite de linhas a ler

#### `process_log_events(log_content)`
Processa conteúdo bruto de log:
- Categoriza por nível (ERROR, WARNING, INFO, OTHER)
- Extrai padrões de erro recorrentes
- Identifica últimas linhas de cada categoria
- Retorna estatísticas e sumários

### Análise com LLM

O nó `analyze_with_llm` usa GPT-4 para:
- Avaliar saúde geral dos logs
- Identificar problemas críticos
- Reconhecer padrões root cause
- Sugerir ações corretivas

Exemplo de análise:
```
Log Analysis Summary:
- Total Lines: 28
- Error Count: 6
- Warning Count: 5
- Info Count: 12

Critical Issues:
1. API connection failures (3 occurrences)
2. Disk space running critically low
3. Data processing pipeline errors
```

### Geração de Relatório

O relatório gerado em Markdown inclui:
- Sumário executivo
- Estatísticas de log
- Distribuição de níveis
- Análise detalhada
- Padrões de erro principais

Exemplo de relatório: `examples/reports/latest_report.md`

## 📊 Exemplo de Uso

### Arquivo de Log de Entrada
```
2024-01-15 10:23:45 [INFO] Application started successfully
2024-01-15 10:26:34 [ERROR] Failed to connect to external API: timeout after 30s
2024-01-15 10:26:35 [ERROR] Exception in thread pool executor: ConnectionRefusedError
2024-01-15 10:26:36 [WARNING] Retrying API connection in 5 seconds
...
```

### Saída - Relatório Gerado
```markdown
# Technical Log Analysis Report

## Executive Summary
File: examples/logs/app.log
Analysis Date: Mon Jan 15 10:35:00 2024

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
The logs show a pattern of repeated API connection failures followed by successful fallback to cache mechanisms. The critical issues are:
1. External API is unreachable or experiencing timeouts
2. Disk space pressure (85% capacity)
3. High memory usage spike (78-92%)

Recommended actions:
- Investigate external API service health
- Implement disk cleanup automation
- Monitor and optimize memory usage patterns
...
```

## 🛠️ Desenvolvimento

### Executar testes
```bash
pytest tests/ -v
```

### Lint do código
```bash
ruff check src/
black --check src/
```

### Type checking
```bash
mypy src/
```

## 🎓 Conceitos Principais

Este projeto demonstra:

1. **LangGraph**: Orquestração de workflows com LLMs
   - StateGraph para definir fluxo
   - Nós para lógica determinística
   - Edges para conectar nós
   - END para conclusão

2. **LangChain**: Integração com LLMs
   - ChatOpenAI para invocações
   - SystemMessage/HumanMessage para prompts
   - Chain of thought para análise

3. **Ferramentas Customizadas**: Estender capacidades do agente
   - Integração com recursos externos
   - Validação e tratamento de erros
   - Tipagem com Pydantic

4. **Padrão de Estado**: Tracking de informação através do fluxo
   - Estado imutável
   - Transformações determinísticas
   - Validação em cada etapa

## 📚 Referências

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

## 👤 Autor

**jlausbr** - Desenvolvedor e Aprendiz de IA

## 📄 Licença

Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request.

---

**Última atualização**: Janeiro 2024
**Status**: Protótipo - Mini-Projeto Avaliativo (M2S05)
