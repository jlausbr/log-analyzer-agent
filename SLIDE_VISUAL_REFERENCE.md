# Referência Visual para Google Slides

## SLIDE 1 - Visão Geral (Layout Recomendado)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🤖 LOG ANALYZER AGENT                                 ║
║         Agente IA para Análise Automatizada de Logs                      ║
║                                                                           ║
║ ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐          ║
║ │  O PROBLEMA     │  │   A SOLUÇÃO     │  │     FLUXO       │          ║
║ ├─────────────────┤  ├─────────────────┤  ├─────────────────┤          ║
║ │ ❌ Demorado     │  │ ✅ LangGraph    │  │  📝 LOG FILE    │          ║
║ │ ❌ Padrões      │  │ ✅ GPT-4        │  │      ↓          │          ║
║ │ ❌ Root Cause   │  │ ✅ Ferramentas  │  │  ✅ VALIDAR     │          ║
║ │ ❌ Repetitivo   │  │ ✅ Relatórios   │  │      ↓          │          ║
║ │                 │  │                 │  │  📖 LER         │          ║
║ │ Análise manual  │  │ Automático +    │  │      ↓          │          ║
║ │ é lenta, cara   │  │ Inteligente     │  │  🔍 PROCESSAR   │          ║
║ │ e imprecisa     │  │                 │  │      ↓          │          ║
║ │                 │  │                 │  │  🤖 ANALISAR    │          ║
║ │                 │  │                 │  │      ↓          │          ║
║ │                 │  │                 │  │  📋 RELATÓRIO   │          ║
║ └─────────────────┘  └─────────────────┘  └─────────────────┘          ║
║                                                                           ║
║            Mini-Projeto M2S05 • IA para Desenvolvedores                 ║
║                    20 de julho de 2026                                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Recomendações para Slide 1:

**Área de Conteúdo**:
- Dividir em 3 colunas de largura aproximadamente igual
- Cada coluna tem um tópico (Problema, Solução, Fluxo)

**Cores por Coluna**:
- Coluna 1 (Problema): Fundo avermelhado (#FFE5E5), texto vermelho escuro
- Coluna 2 (Solução): Fundo verde (#E5F5E5), texto verde escuro
- Coluna 3 (Fluxo): Fundo azul (#E5F0FF), texto azul escuro

**Tipografia**:
- Títulos das colunas: 24pt Bold
- Bullets: 18pt Regular
- Rodapé: 14pt Cinza

**Elementos Visuais**:
- Usar caixas/cards com borda sutil
- Shadow leve em cada coluna
- Emojis grandes (32-40pt)

---

## SLIDE 2 - Arquitetura Técnica (Layout Recomendado)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    ⚙️ ARQUITETURA TÉCNICA                                ║
║           5 Nós LangGraph + 2 Ferramentas + GPT-4                        ║
║                                                                           ║
║ ┌───────────────────────────────┐  ┌─────────────────┐  ┌─────────────┐ ║
║ │                               │  │   FERRAMENTAS   │  │ STACK TECH  │ ║
║ │     FLUXO DE 5 NÓS            │  ├─────────────────┤  ├─────────────┤ ║
║ │                               │  │                 │  │ LangGraph   │ ║
║ │  ┌──────────────────────────┐ │  │ 🔧 TOOL 1       │  │ GPT-4       │ ║
║ │  │ 1️⃣ VALIDATE INPUT        │ │  │ read_log_file   │  │ LangChain   │ ║
║ │  │ Valida arquivo           │ │  │                 │  │ Pydantic    │ ║
║ │  └─────────────┬────────────┘ │  │ ✓ Seguro        │  │ Python 3.10 │ ║
║ │                ↓               │  │ ✓ Path safe     │  │             │ ║
║ │  ┌──────────────────────────┐ │  │ ✓ Metadata      │  │ EXEMPLO     │ ║
║ │  │ 2️⃣ READ LOG FILE         │ │  │                 │  │             │ ║
║ │  │ Lê com segurança         │ │  │ 🔧 TOOL 2       │  │ IN: app.log │ ║
║ │  └─────────────┬────────────┘ │  │ process_events  │  │             │ ║
║ │                ↓               │  │                 │  │ OUT:        │ ║
║ │  ┌──────────────────────────┐ │  │ ✓ Categoriza    │  │ Relatório   │ ║
║ │  │ 3️⃣ PARSE EVENTS          │ │  │ ✓ Padrões       │  │ Markdown    │ ║
║ │  │ Processa categorias      │ │  │ ✓ Ranking       │  │             │ ║
║ │  └─────────────┬────────────┘ │  │                 │  │ Crítico:    │ ║
║ │                ↓               │  │                 │  │ API timeout │ ║
║ │  ┌──────────────────────────┐ │  │                 │  │ (2x)        │ ║
║ │  │ 4️⃣ ANALYZE WITH LLM      │ │  │                 │  │             │ ║
║ │  │ GPT-4 análise            │ │  │                 │  │ Ação:       │ ║
║ │  └─────────────┬────────────┘ │  │                 │  │ Check API   │ ║
║ │                ↓               │  │                 │  │             │ ║
║ │  ┌──────────────────────────┐ │  │                 │  │             │ ║
║ │  │ 5️⃣ GENERATE REPORT       │ │  │                 │  │             │ ║
║ │  │ Markdown profissional    │ │  │                 │  │             │ ║
║ │  └──────────────────────────┘ │  │                 │  │             │ ║
║ │                               │  │                 │  │             │ ║
║ └───────────────────────────────┘  └─────────────────┘  └─────────────┘ ║
║                                                                           ║
║     Validação em 8 camadas • 10 testes unitários • 100% type hints      ║
║            Mini-Projeto M2S05 • jlausbr • 20 de julho de 2026            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Recomendações para Slide 2:

**Área de Conteúdo**:
- Dividir em 3 colunas/seções
- Esquerda: Fluxo vertical dos nós
- Centro: Ferramentas com descrição
- Direita: Stack + Exemplo

**Cores por Seção**:
- Coluna 1 (Fluxo): Nós em gradiente azul → verde
- Coluna 2 (Ferramentas): Laranja (#FF9500)
- Coluna 3 (Stack): Cinza (#F0F0F0) com destaque azul

**Nós - Numeração com Emojis**:
```
1️⃣ = U+0031 U+FE0F U+20E3
2️⃣ = U+0032 U+FE0F U+20E3
3️⃣ = U+0033 U+FE0F U+20E3
4️⃣ = U+0034 U+FE0F U+20E3
5️⃣ = U+0035 U+FE0F U+20E3
```

**Conexões entre Nós**:
- Usar setas (↓ U+2193)
- Criar com linhas/shapes do Google Slides
- Espessura: 2-3px
- Cor: Cinza médio (#999999)

**Tipografia**:
- Título seção: 18pt Bold
- Descrição nó: 14pt Regular
- Labels ferramentas: 16pt Bold
- Exemplo código: 11pt Courier (monospace)

**Rodapé Informativo**:
- Estatísticas: "Validação em 8 camadas • 10 testes unitários • 100% type hints"
- Dados do projeto: "Mini-Projeto M2S05 • jlausbr • 20 de julho de 2026"

---

## 🎨 GUIA DE CORES (RGB / HEX)

| Elemento | RGB | HEX | Uso |
|----------|-----|-----|-----|
| Azul Primário | 76, 110, 245 | #4C6EF5 | Títulos, destaques |
| Verde Sucesso | 81, 207, 102 | #51CF66 | Solução, success |
| Vermelho Aviso | 255, 107, 107 | #FF6B6B | Problema, error |
| Laranja Info | 255, 149, 0 | #FF9500 | Ferramentas, info |
| Amarelo | 255, 217, 61 | #FFD93D | Highlights, warnings |
| Cinza Fundo | 240, 240, 240 | #F0F0F0 | Background, subtle |
| Branco | 255, 255, 255 | #FFFFFF | Principal background |
| Preto Texto | 51, 51, 51 | #333333 | Texto principal |

---

## 📐 DIMENSÕES RECOMENDADAS

**Google Slides Padrão**: 10" × 7.5" (proporção 4:3)
ou
**Google Slides Widescreen**: 13.33" × 7.5" (proporção 16:9)

### Margens
- Superior: 0.5"
- Inferior: 0.5"
- Esquerda: 0.75"
- Direita: 0.75"

### Áreas de Conteúdo
- Cada coluna: ~2.5" de largura
- Espaço entre: ~0.25"
- Altura do conteúdo: ~5.5"

---

## 📝 FONTES RECOMENDADAS

### Google Slides Nativas (Disponíveis)
- **Títulos**: Roboto Bold, 48-54pt
- **Subtítulos**: Roboto, 28-32pt
- **Corpo**: Roboto, 18-22pt
- **Código**: Courier Prime, 10-12pt

### Alternativas
- **Títulos**: Arial Bold, Lato Bold, Montserrat Bold
- **Corpo**: Arial, Open Sans, Lato
- **Código**: Courier New, Consolas (monospace)

---

## ✅ CHECKLIST VISUAL

### Slide 1
- [ ] Título principal destacado
- [ ] 3 colunas bem distribuídas
- [ ] Cores contrastantes para cada seção
- [ ] Emojis legíveis e alinhados
- [ ] Texto legível (18pt+ corpo)
- [ ] Rodapé com informações
- [ ] Espaçamento uniforme

### Slide 2
- [ ] Título com subtítulo técnico
- [ ] Fluxo de 5 nós vertical
- [ ] Setas conectando nós
- [ ] Cores gradientes (azul→verde)
- [ ] Ferramentas bem descritas
- [ ] Stack tecnológico organizado
- [ ] Exemplo prático visível
- [ ] Rodapé com estatísticas

---

## 🔗 PRÓXIMOS PASSOS

1. Abrir Google Slides (slides.google.com)
2. Criar apresentação nova
3. Copiar conteúdo de cada slide conforme layout acima
4. Aplicar cores e formatação
5. Adicionar shapes/caixas para estrutura
6. Revisar legibilidade
7. Exportar como PDF
8. Salvar como `APRESENTACAO.pdf` na raiz
9. Commit e push no GitHub

---

**Versão**: 1.0  
**Data**: 20 de julho de 2026  
**Status**: Pronto para implementação no Google Slides
