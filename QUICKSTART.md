# Quick Start Guide - Log Analyzer Agent

Comece em 2-5 minutos! 🚀

## ⚡ Opção 1: Modo DEMO (SEM OpenAI - Comece AGORA)

```bash
# 1. Entre no diretório do projeto
cd c:\git\sctec\m2s05\log-analyzer-agent

# 2. Crie ambiente virtual
python -m venv venv

# 3. Ative
venv\Scripts\activate

# 4. Instale dependências
pip install -r requirements.txt

# 5. Execute modo DEMO (sem chave OpenAI)
python main_demo.py
```

✅ Pronto! Relatório gerado em `examples/reports/latest_report_demo.md`

---

## 🔑 Opção 2: Modo Completo (Com OpenAI)

```bash
# Depois de fazer os passos 1-4 acima:

# 5. Configure .env
copy .env.example .env

# Edite .env e adicione sua chave:
# OPENAI_API_KEY=sk-sua-chave-aqui

# 6. Execute com análise IA completa
python main.py
```

✅ Relatório com análise GPT-4 em `examples/reports/latest_report.md`

---

## 📋 Diferenças

| Aspecto | DEMO | Completo |
|---------|------|----------|
| **Requer Chave** | ❌ | ✅ |
| **Análise** | Simulada | GPT-4 Real |
| **Tempo Setup** | 2 min | 5 min |
| **Funciona Agora** | ✅ | ⏳ Precisa chave |

---

## 🔑 Como Obter Chave OpenAI

Ver: [OPENAI_SETUP.md](OPENAI_SETUP.md)

Rápido: **https://platform.openai.com/api-keys** (grátis + trial)

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
