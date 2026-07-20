# Quick Start Guide - Log Analyzer Agent

Comece em 5 minutos! 🚀

## 1. Setup (2 min)

```bash
# Entre no diretório do projeto
cd c:\git\sctec\m2s05\log-analyzer-agent

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## 2. Configuração (1 min)

```bash
# Copie o arquivo de exemplo
copy .env.example .env
```

Edite o arquivo `.env` e adicione sua chave OpenAI:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
LOG_FILE_PATH=examples/logs/app.log
MAX_LOG_LINES=500
REPORT_OUTPUT_PATH=examples/reports/
```

## 3. Execute (2 min)

```bash
python main.py
```

Você deverá ver:

```
Initializing Log Analyzer Agent...
Analyzing log file: examples/logs/app.log
============================================================
ANALYSIS COMPLETE
============================================================

[Relatório técnico completo aqui]

Report saved to: examples/reports/latest_report.md
```

## 4. Verifique o Relatório

Abra `examples/reports/latest_report.md` em seu editor de texto ou markdown viewer.

---

## 📚 Próximas Etapas

- Leia o [README.md](README.md) para documentação completa
- Explore [docs/prompts.md](docs/prompts.md) para entender os prompts
- Veja [docs/APRESENTACAO.md](docs/APRESENTACAO.md) para arquitetura
- Execute os testes: `pytest tests/ -v`

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY not set in .env file"
Certifique-se de que você:
1. Copiou `.env.example` para `.env`
2. Adicionou sua chave real do OpenAI
3. Não adicionou espaços extras

### "File not found: examples/logs/app.log"
O arquivo de exemplo deve existir. Se não, crie um arquivo `.log` com conteúdo de teste.

## 📝 Exemplo de Arquivo de Log Customizado

Crie `test.log`:
```
2024-01-15 10:23:45 [INFO] Application started
2024-01-15 10:23:46 [ERROR] Failed to connect
2024-01-15 10:23:47 [WARNING] Retrying...
```

Execute:
```bash
LOG_FILE_PATH=test.log python main.py
```

---

**Sucesso!** 🎉 Seu agente de análise de logs está pronto!
