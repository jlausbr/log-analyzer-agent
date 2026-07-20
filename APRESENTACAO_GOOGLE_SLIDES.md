# Log Analyzer Agent - Apresentação (Google Slides)

**Instruções**: Copie o conteúdo de cada slide e cole no Google Slides. Use a formatação indicada.

---

## SLIDE 1: Visão Geral e Solução

### Título Principal
```
🤖 LOG ANALYZER AGENT
Agente IA para Análise Automatizada de Logs
```

### Conteúdo

#### Coluna Esquerda - O Problema

**Desafios Atuais:**
- ❌ Análise manual de logs é demorada
- ❌ Difícil identificar padrões em milhares de linhas  
- ❌ Diagnóstico de root cause exige expertise
- ❌ Gerar relatórios é processo repetitivo

#### Coluna Central - A Solução

**Agente Inteligente com:**
- ✅ **LangGraph** - Orquestração de fluxo
- ✅ **GPT-4** - Análise inteligente
- ✅ **2 Ferramentas** - Leitura segura + Processamento
- ✅ **Relatórios** - Estruturados e acionáveis

#### Coluna Direita - Fluxo Resumido

```
📝 LOG
  ↓
✅ Validar
  ↓
📖 Ler
  ↓
🔍 Processar
  ↓
🤖 Analisar
  ↓
📋 Relatório
```

### Rodapé
```
Mini-Projeto M2S05 • IA para Desenvolvedores • 20 de julho de 2026
```

---

## SLIDE 2: Arquitetura Técnica e Implementação

### Título Principal
```
⚙️ ARQUITETURA TÉCNICA
5 Nós LangGraph + 2 Ferramentas + GPT-4
```

### Conteúdo em 3 Seções

#### Seção 1 - Fluxo de 5 Nós (Lado Esquerdo)

```
┌─────────────────────────────────┐
│ 1️⃣ validate_input               │
│ Valida arquivo e extensão       │
└─────────────┬───────────────────┘
              ↓
┌─────────────────────────────────┐
│ 2️⃣ read_log_file                │
│ Lê com segurança (Tool 1)       │
└─────────────┬───────────────────┘
              ↓
┌─────────────────────────────────┐
│ 3️⃣ parse_events                 │
│ Categoriza por nível (Tool 2)   │
└─────────────┬───────────────────┘
              ↓
┌─────────────────────────────────┐
│ 4️⃣ analyze_with_llm             │
│ Análise com GPT-4               │
└─────────────┬───────────────────┘
              ↓
┌─────────────────────────────────┐
│ 5️⃣ generate_report              │
│ Markdown profissional           │
└─────────────────────────────────┘
```

#### Seção 2 - Ferramentas Customizadas (Centro)

**Tool 1: read_log_file()**
- ✅ Leitura segura de arquivos
- ✅ Prevenção de path traversal
- ✅ Retorna metadados
- ✅ Suporta truncamento

**Tool 2: process_log_events()**
- ✅ Categoriza (ERROR, WARNING, INFO)
- ✅ Extrai padrões recorrentes
- ✅ Ranking por frequência
- ✅ Prepara contexto para LLM

#### Seção 3 - Stack Tecnológico (Lado Direito)

| Componente | Tecnologia |
|-----------|-----------|
| **Orquestração** | LangGraph |
| **LLM** | GPT-4 Turbo |
| **Framework** | LangChain |
| **Tipagem** | Pydantic |
| **Linguagem** | Python 3.10+ |

**Estado:**
```python
LogAnalysisState (Pydantic)
├── log_file_path
├── log_file_content
├── parsed_events
├── analysis_result
└── report
```

### Exemplo Prático (Rodapé)

**Entrada:**
```
[ERROR] API timeout
[ERROR] API timeout
[WARNING] Retrying...
```

**Saída:**
```
# Technical Log Analysis Report
Critical Issues:
1. API unreachable (2x)
2. Retry mechanism triggered
Recommendation: Check API health
```

### Rodapé
```
Implementação: 5 nós • 2 ferramentas • Validação em 8 camadas • 10 testes unitários
Mini-Projeto M2S05 • Autor: jlausbr • 20 de julho de 2026
```

---

## 📝 GUIA PARA CRIAR NO GOOGLE SLIDES

### Passos para Slide 1:

1. **Título**: "🤖 LOG ANALYZER AGENT"
   - Fonte: Arial, 54pt, Bold
   - Subtítulo: "Agente IA para Análise Automatizada de Logs" (32pt)

2. **Layout**: Três colunas
   - Coluna 1: "O Problema" (Vermelho/Warning)
   - Coluna 2: "A Solução" (Verde/Success)
   - Coluna 3: "Fluxo" (Azul/Info)

3. **Cores Recomendadas**:
   - Fundo: Branco ou Cinza Claro
   - Problema: #FF6B6B (Vermelho)
   - Solução: #51CF66 (Verde)
   - Fluxo: #4C6EF5 (Azul)

4. **Elementos Visuais**:
   - Use ícones/emojis: ❌ ✅ 🤖 📝 🔍 📋
   - Setas para indicar direção

---

### Passos para Slide 2:

1. **Título**: "⚙️ ARQUITETURA TÉCNICA"
   - Fonte: Arial, 54pt, Bold

2. **Layout**: Três colunas ou áreas
   - Esquerda: Fluxo de nós (vertical)
   - Centro: Ferramentas
   - Direita: Stack + Exemplo

3. **Fluxo de Nós**:
   - Use caixas com bordas arredondadas
   - Conecte com setas
   - Cada nó em cor diferente ou com ícone

4. **Caixa de Exemplo** (Rodapé):
   - Código monoespacial (Courier New, 10pt)
   - Fundo cinza claro (#F0F0F0)

5. **Cores**:
   - Nós: Gradiente de azul (inicio) a verde (fim)
   - Ferramentas: Laranja/Amarelo
   - Stack: Cinza com texto escuro

---

## 🎨 DICAS DE DESIGN

### Tipografia
- **Títulos**: Arial/Roboto Bold, 48-54pt
- **Subtítulos**: Arial/Roboto, 28-32pt
- **Corpo**: Arial/Roboto, 18-22pt
- **Código**: Courier New, 10-12pt

### Espaçamento
- Margem externa: ~40px
- Espaço entre seções: ~30px
- Padding interno: ~20px

### Paleta de Cores Sugerida
- Primária: #4C6EF5 (Azul)
- Sucesso: #51CF66 (Verde)
- Warning: #FFD93D (Amarelo)
- Erro: #FF6B6B (Vermelho)
- Neutro: #F0F0F0 (Cinza)

### Ícones e Emojis
- 🤖 Agente/IA
- 📝 Logs/Arquivo
- ✅ Sucesso/Check
- ❌ Problema/Error
- 🔍 Análise/Search
- 📋 Relatório/Report
- ⚙️ Arquitetura/Configuração
- 🔐 Segurança
- 📊 Dados/Gráfico

---

## 📤 EXPORTAR DO GOOGLE SLIDES

1. File → Download → PDF
2. Nomear: `APRESENTACAO_Log_Analyzer_Agent.pdf`
3. Colocar na raiz do projeto
4. Commit e push para GitHub

---

## ✅ CHECKLIST

- [ ] Slide 1 criado com problema/solução/fluxo
- [ ] Slide 2 criado com arquitetura/ferramentas/exemplo
- [ ] Cores consistentes aplicadas
- [ ] Fontes legíveis (18pt mínimo no corpo)
- [ ] Emojis/ícones adicionados
- [ ] Informações do rodapé completas
- [ ] PDF exportado
- [ ] Arquivo na raiz do projeto
- [ ] Commit e push realizados

---

**Criado em**: 20 de julho de 2026  
**Versão**: 1.0  
**Status**: Pronto para Google Slides
