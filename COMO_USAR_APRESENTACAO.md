# Como Usar a Apresentação no Google Slides

## 📚 Arquivos Disponíveis

Você tem **2 guias** para criar a apresentação:

### 1. `APRESENTACAO_GOOGLE_SLIDES.md` ⭐ **USE ESTE**
- Conteúdo otimizado para Google Slides
- Já formatado e estruturado
- Pronto para copiar e colar

### 2. `SLIDE_VISUAL_REFERENCE.md`
- Referência visual com ASCII art
- Cores, fontes e dimensões
- Dicas de design

---

## 🚀 Passo a Passo (5 Minutos)

### Passo 1: Criar Apresentação no Google Slides
```
1. Abrir: slides.google.com
2. Criar nova apresentação: "Apresentação em branco"
3. Nomear: "Log Analyzer Agent - Mini-Projeto M2S05"
```

### Passo 2: Criar Slide 1

#### No Google Slides:
```
1. Clicar em "Slide" → "Novo slide"
2. Escolher layout: "Título com subtítulo"
3. Adicionar:
   - Título: 🤖 LOG ANALYZER AGENT
   - Subtítulo: Agente IA para Análise Automatizada de Logs
```

#### Adicionar Conteúdo:
```
1. Clicar em: Layout → "Com título e 2 colunas"
2. OU: Inserir → Caixa de texto (criar 3 colunas manualmente)
3. Copiar do arquivo APRESENTACAO_GOOGLE_SLIDES.md:
   - Seção "SLIDE 1: Visão Geral e Solução"
   - Copiar "Coluna Esquerda - O Problema"
   - Copiar "Coluna Central - A Solução"
   - Copiar "Coluna Direita - Fluxo Resumido"
```

#### Aplicar Cores:
```
1. Coluna 1 (Problema):
   - Fundo: #FFE5E5 (Vermelho claro)
   - Texto: #CC0000 (Vermelho escuro)

2. Coluna 2 (Solução):
   - Fundo: #E5F5E5 (Verde claro)
   - Texto: #009900 (Verde escuro)

3. Coluna 3 (Fluxo):
   - Fundo: #E5F0FF (Azul claro)
   - Texto: #0033CC (Azul escuro)
```

#### Adicionar Rodapé:
```
1. Inserir → Caixa de texto
2. Posicionar na base
3. Texto: "Mini-Projeto M2S05 • IA para Desenvolvedores • 20 de julho de 2026"
4. Fonte: 12pt, Cinza
```

---

### Passo 3: Criar Slide 2

#### No Google Slides:
```
1. Novo slide: Layout "Com título em branco"
2. Título: ⚙️ ARQUITETURA TÉCNICA
3. Subtítulo: 5 Nós LangGraph + 2 Ferramentas + GPT-4
```

#### Layout em 3 Colunas:
```
Usar Inserir → Tabela (1 linha × 3 colunas)
OU criar 3 caixas de texto lado a lado
```

#### Conteúdo por Coluna:

**Coluna 1 (Fluxo de Nós) - Esquerda**:
```
Copiar de APRESENTACAO_GOOGLE_SLIDES.md:
- Seção 1 - Fluxo de 5 Nós (Lado Esquerdo)
- Usar as caixas numeradas (1️⃣ até 5️⃣)
- Conectar com setas ↓
```

**Coluna 2 (Ferramentas) - Centro**:
```
Copiar de APRESENTACAO_GOOGLE_SLIDES.md:
- Seção 2 - Ferramentas Customizadas
- Tool 1 e Tool 2 com descrição
```

**Coluna 3 (Stack + Exemplo) - Direita**:
```
Copiar de APRESENTACAO_GOOGLE_SLIDES.md:
- Seção 3 - Stack Tecnológico
- Tabela de tecnologias
- Caixa de Exemplo (Entrada/Saída)
```

#### Aplicar Cores:
```
1. Coluna 1 (Fluxo):
   - Nós: Gradiente azul (#4C6EF5) → verde (#51CF66)
   - Cada nó: cor progressivamente mais verde
   - Setas: Cinza (#999999)

2. Coluna 2 (Ferramentas):
   - Fundo: Laranja claro (#FFF0E5)
   - Texto: Laranja escuro (#FF6B00)
   - Checkmarks: Verde (#51CF66)

3. Coluna 3 (Stack):
   - Fundo: Cinza (#F0F0F0)
   - Texto: Preto (#333333)
   - Caixa Exemplo: Cinza mais escuro (#E0E0E0)
```

#### Adicionar Rodapé:
```
1. Inserir → Caixa de texto
2. Texto: "Validação em 8 camadas • 10 testes unitários • 100% type hints"
3. Segunda linha: "Mini-Projeto M2S05 • Autor: jlausbr • 20 de julho de 2026"
4. Fonte: 11pt, Cinza
```

---

## 🎨 Dicas Rápidas

### Para Melhor Aparência:

**1. Emojis Grandes**
```
- Tamanho do emoji: 32-40pt
- Centralizado na caixa
- Alinhado ao topo
```

**2. Setas de Fluxo**
```
- Usar: Inserir → Forma → Seta
- Cor: Cinza (#999999)
- Tamanho: ~0.5" de altura
```

**3. Caixas com Border**
```
- Inserir → Caixa
- Border: 2px
- Cor border: Matching com coluna
- Fill: Cor de fundo (consultar referência)
- Radius: ~8px (arredondado)
```

**4. Sombra Sutil**
```
- Clique direito caixa → Opções de formato
- Shadow: Deslocamento 2pt, Desfoque 4pt, Opacidade 20%
```

---

## 📥 Exportar como PDF

### No Google Slides:
```
1. Menu: Arquivo → Fazer download
2. Formato: PDF Document (.pdf)
3. Nomear: APRESENTACAO.pdf
4. Salvar na raiz do projeto
```

### Na linha de comando:
```bash
# Ir para a raiz do projeto
cd c:\git\sctec\m2s05\log-analyzer-agent

# Criar commit com PDF
git add APRESENTACAO.pdf
git commit -m ":memo: docs: add presentation slides as PDF - Google Slides export"
git push origin main
```

---

## ✅ Checklist Final

### Slide 1
- [ ] Título "🤖 LOG ANALYZER AGENT" destacado
- [ ] Subtítulo presente
- [ ] 3 colunas: Problema, Solução, Fluxo
- [ ] Cores aplicadas (Vermelho, Verde, Azul)
- [ ] Emojis visíveis e legíveis
- [ ] Bullets com 18pt+ de fonte
- [ ] Rodapé com data e disciplina

### Slide 2
- [ ] Título "⚙️ ARQUITETURA TÉCNICA"
- [ ] Subtítulo com tecnologias
- [ ] 3 colunas: Fluxo, Ferramentas, Stack
- [ ] Nós numerados (1️⃣-5️⃣) com setas
- [ ] Cores gradientes no fluxo
- [ ] Ferramentas bem descritas
- [ ] Stack em tabela clara
- [ ] Exemplo prático visível
- [ ] Rodapé com estatísticas

### Exportação
- [ ] PDF criado (APRESENTACAO.pdf)
- [ ] PDF na raiz do projeto
- [ ] Commit realizado
- [ ] Push para GitHub completo

---

## 🔗 Links Úteis

### Google Slides
- Criar: https://docs.google.com/presentation/create
- Cores: https://material.io/resources/color/

### Para Copiar Direto
- Abrir: `APRESENTACAO_GOOGLE_SLIDES.md`
- Selecionar seção do slide
- Ctrl+C (copiar)
- Ctrl+V no Google Slides

---

## 💡 Alternativas

Se preferir **não usar Google Slides**:

### Opção 1: Markdown → PDF
```bash
# Instalar pandoc
choco install pandoc

# Converter
pandoc APRESENTACAO_GOOGLE_SLIDES.md -o APRESENTACAO.pdf
```

### Opção 2: PowerPoint
```
1. Criar no PowerPoint
2. Salvar como: APRESENTACAO.pdf
3. Mesmo resultado visual
```

### Opção 3: Usar Arquivo Markdown
```
- Manter APRESENTACAO_GOOGLE_SLIDES.md no repositório
- Avaliador lê direto do GitHub
- Simples e eficaz
```

---

## 📞 Suporte

Se tiver dúvidas:

1. **Cores não aparecem**: Verificar hexadecimal (ex: #4C6EF5)
2. **Emojis não aparecem**: Usar font "Segoe UI Emoji" ou "Noto Color Emoji"
3. **Layout desalinhado**: Usar grid/guidelines do Google Slides
4. **Fonte pequena**: Aumentar para 18pt (mínimo recomendado)

---

## 📝 Próximos Passos

```
1. ✅ Copiar conteúdo de APRESENTACAO_GOOGLE_SLIDES.md
2. ✅ Criar slides no Google Slides (2 slides)
3. ✅ Aplicar cores e formatação
4. ✅ Adicionar emojis e setas
5. ✅ Revisar legibilidade
6. ✅ Exportar como PDF (APRESENTACAO.pdf)
7. ✅ Colocar na raiz do projeto
8. ✅ Commit e push
9. ✅ Pronto para avaliação!
```

---

**Tempo estimado**: 15-20 minutos  
**Dificuldade**: Fácil  
**Resultado**: Profissional e completo ✅

Boa apresentação! 🎯
