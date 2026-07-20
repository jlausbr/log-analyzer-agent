# 🔑 OpenAI Setup - Como Obter API Key

Você tem 2 opções para usar este projeto:

---

## ✅ Opção 1: Modo DEMO (Sem Chave OpenAI) - RECOMENDADO PARA COMEÇAR

Se **não tem** uma chave OpenAI ou quer testar rapidamente:

```bash
python main_demo.py
```

**Benefícios**:
- ✅ Funciona imediatamente (sem API key)
- ✅ Mostra o fluxo completo do agente
- ✅ Análise simulada (heurística)
- ✅ Ideal para aprender e testar

**Limitações**:
- Análise de IA é simulada (não é GPT-4 real)
- Padrões pré-definidos em vez de análise contextual

---

## 🚀 Opção 2: Modo Completo (Com OpenAI API)

Para análise completa com IA real (GPT-4):

### Passo 1: Criar Conta OpenAI (Grátis)

1. Vá para: **https://platform.openai.com/signup**
2. Faça login com Google, GitHub ou email
3. Valide seu email (confira spam se necessário)

### Passo 2: Obter API Key

1. Vá para: **https://platform.openai.com/account/api-keys**
2. Clique em **"Create new secret key"**
3. Dê um nome à chave (ex: "log-analyzer")
4. **COPIE A CHAVE** (aparece apenas uma vez!)
   - Formato: `sk-...`
   - ⚠️ Nunca compartilhe essa chave!

### Passo 3: Configurar no Projeto

1. Abra o arquivo `.env` (na raiz do projeto):
   ```bash
   cd c:\git\sctec\m2s05\log-analyzer-agent
   notepad .env
   ```

2. Adicione sua chave:
   ```env
   OPENAI_API_KEY=sk-sua-chave-aqui
   ```

3. Salve o arquivo

### Passo 4: Executar

```bash
python main.py
```

---

## 💰 Custos

### Trial Grátis (Novo)
- **$5 de crédito** nos primeiros 3 meses
- Suficiente para testar bastante
- Sem cartão de crédito (por 3 meses)

### Preços depois do trial
- GPT-4 Turbo: ~$0.01 por 1000 tokens
- Análise de um log: típicamente **$0.002-0.01**
- Muito barato para uso educacional

### Como Monitorar Custos
1. Vá para: **https://platform.openai.com/account/billing/overview**
2. Veja crédito disponível
3. Configure limite se desejar

---

## 🔒 Segurança

### Boas Práticas
- ✅ Guarde sua chave em `.env`
- ✅ `.env` está no `.gitignore` (não é commitado)
- ✅ Nunca compartilhe ou coloque em código
- ✅ Se vazar, regenere em: https://platform.openai.com/account/api-keys

### Se Precisar Regenerar Chave
1. Vá para: https://platform.openai.com/account/api-keys
2. Clique no ícone de "delete" na chave antiga
3. Crie uma nova chave

---

## 🆘 Troubleshooting

### "Invalid API Key" ou "Unauthorized"
```
1. Verifique se copou a chave corretamente (sem espaços)
2. Verifique se está em .env (não em código)
3. Regenere a chave se necessário
```

### "Rate limit exceeded"
```
1. Você fez muitas requisições rápido
2. Espere alguns minutos
3. Configure um limite de uso em: 
   https://platform.openai.com/account/billing/limits
```

### "Insufficient quota"
```
1. Seu crédito ou limite foi atingido
2. Adicione um método de pagamento em:
   https://platform.openai.com/account/billing/overview
3. Ou vá para modo DEMO
```

### "OPENAI_API_KEY not found"
```
1. Verifique se .env existe
2. Verifique se tem a linha: OPENAI_API_KEY=sk-...
3. Reinicie o PowerShell para recarregar .env
4. Use modo DEMO enquanto resolve
```

---

## 📊 Comparação: DEMO vs Completo

| Aspecto | DEMO | Completo |
|---------|------|----------|
| **Requer API Key** | ❌ Não | ✅ Sim |
| **Análise** | 🤖 Heurística | 🧠 GPT-4 |
| **Custo** | 💰 Grátis | 💵 ~0.005-0.05 |
| **Tempo** | ⚡ Rápido | ⏱️ 2-5 seg |
| **Qualidade** | 📊 Razoável | 🌟 Excelente |
| **Para Aprender** | ✅ Ótimo | ✅ Perfeito |

---

## 🎯 Recomendações

### Se você quer...

**Testar o projeto rapidamente**
→ Use: `python main_demo.py`

**Aprender sobre LangGraph**
→ Use: `python main_demo.py` (mesmo sem API)

**Avaliar a qualidade de análise**
→ Use: `python main.py` (com API key)

**Usar em produção**
→ Use: `python main.py` (com API key configurada)

**Não tem cartão de crédito**
→ Use: `python main_demo.py` ou obtenha trial grátis

---

## 📚 Recursos Adicionais

- **Documentação OpenAI**: https://platform.openai.com/docs
- **Modelos disponíveis**: https://platform.openai.com/docs/models
- **Pricing**: https://openai.com/pricing
- **Status da API**: https://status.openai.com

---

## ✅ Checklist Rápido

```bash
# 1. Testar sem chave (agora!)
python main_demo.py

# 2. Se quiser completo:
# - Vá para https://platform.openai.com/api-keys
# - Crie uma chave
# - Edite .env com a chave
# - Execute: python main.py

# 3. Monitorar uso
# - https://platform.openai.com/account/billing/overview
```

---

## 🎉 Conclusão

Você pode **começar agora sem OpenAI**:
```bash
python main_demo.py
```

Para experiência completa, obtenha a chave (grátis + trial):
```bash
# Depois de configurar .env
python main.py
```

---

**Perguntas?** Consulte `QUICKSTART.md` ou `README.md`

Boa sorte! 🚀
