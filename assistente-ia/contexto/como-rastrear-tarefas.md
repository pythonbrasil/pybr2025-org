# 🤖 TaskTrackingAgent - Especificação Funcional

*AI Agent especializado em monitoramento e priorização de tarefas organizacionais para Python Brasil 2025*

---

## 🎯 **Função Principal**

Monitorar continuamente as tarefas organizacionais da Python Brasil 2025, analisar prioridades, identificar gargalos e otimizar a distribuição de trabalho entre voluntários através de análise inteligente do repositório GitHub e integração com Telegram.

---

## 🧠 **Capacidades Funcionais**

### **1. Issue Analysis (Análise de Issues)**

**Objetivo:** Processar e categorizar automaticamente todas as issues do repositório

**O que o Agent faz:**
- **Categorização Automática:** Identifica padrões nos títulos para classificar tipos:
  - Vendor Research: "Reunir orçamentos de...", "Pesquisar fornecedores..."
  - Sponsor Tracking: "Acompanhamento patrocínio [Empresa]"
  - Communication Tasks: "Mandar email...", "Entrar em contato..."
  - Decision Making: "Decidir...", "Definir..."
  - Implementation: "Adicionar...", "Criar...", "Implementar..."
  - Partnership Development: "Parceria com..."

- **Extração de Informações Críticas:**
  - Datas mencionadas no texto da issue
  - Pessoas/empresas envolvidas
  - Valores monetários quando citados
  - Localizações geográficas
  - Dependências implícitas entre tarefas

- **Análise de Status Real:**
  - Lê comentários para detectar progresso não refletido no status
  - Identifica blockers através de palavras-chave
  - Reconhece conclusão implícita vs fechamento formal
  - **⚠️ CUIDADO:** Não assumir progresso apenas por haver comentários - verificar se há trabalho substancial realizado

**Resultado:** Issues categorizadas com metadados extraídos e status real identificado

---

### **2. Priority Scoring (Pontuação de Prioridade)**

**Objetivo:** Calcular prioridade numérica baseada em impacto no evento

**Fatores Analisados:**

**Deadline Impact (Peso: 40%)**
- Issues com prazo < 7 dias = CRÍTICO
- Issues com prazo < 30 dias = ALTO
- Issues com prazo < 60 dias = MÉDIO
- Issues com prazo > 60 dias = BAIXO

**Business Impact (Peso: 30%)**
- CRÍTICO: Patrocínio, local do evento, keynotes
- ALTO: Fornecedores essenciais, parcerias estratégicas
- MÉDIO: Comunicação, materiais, logística
- BAIXO: Documentação, automações internas

**Dependency Impact (Peso: 20%)**
- Issues que bloqueiam outras tarefas recebem pontuação maior
- Análise de menções cruzadas entre issues
- Identificação de gargalos em cascata

**Completion Risk (Peso: 10%)**
- Issues sem responsável = alto risco
- Issues paradas há >7 dias = médio risco
- Issues com múltiplas reassignações = médio risco

**Categorias Finais:**
- **CRÍTICA (90-100 pontos):** Ação imediata necessária
- **ALTA (70-89 pontos):** Próximas 2 semanas
- **MÉDIA (50-69 pontos):** Próximo mês
- **BAIXA (0-49 pontos):** Pode aguardar

---

### **3. Progress Tracking (Acompanhamento de Progresso)**

**Objetivo:** Monitorar evolução e identificar padrões problemáticos

**Métricas por Issue:**
- Tempo desde criação vs tempo esperado de resolução
- Frequência de atualizações (comments, edits)
- Mudanças de responsável
- Padrão de interação (comentários ativos vs silêncio)

**Métricas por Categoria:**
- Taxa de conclusão por tipo de tarefa
- Tempo médio para completar cada categoria
- Categorias com maior taxa de issues "travadas"

**Métricas por Voluntário:**
- Carga atual (número de issues assignadas)
- Taxa histórica de conclusão
- Áreas de especialização (categorias mais trabalhadas)
- Tempo médio de resposta

**Detecção de Problemas:**
- **Issues Paradas:** >7 dias sem qualquer atividade
- **Voluntários Sobrecarregados:** >5 issues ativas simultaneamente
- **Categorias Problemáticas:** <50% de taxa de conclusão
- **Padrões de Risco:** Issues com múltiplas transferências
- **⚠️ Falso Progresso:** Issues com comentários isolados mas sem trabalho estrutural (ex: apenas 1 fornecedor contactado)

**Análise de Tendências:**
- Velocidade de conclusão semana a semana
- Acúmulo vs resolução de novas issues
- Performance por time/área de atuação

---

### **4. Deadline Alerts (Alertas de Prazo)**

**Objetivo:** Notificações proativas via Telegram baseadas em urgência

**Tipos de Alerta:**

**Deadline Warning (7 dias antes):**
```
⚠️ PRAZO SE APROXIMANDO

Issue #119: Acompanhamento patrocínio RocketSeat
⏰ Prazo: 21/08/2025 (7 dias)
👤 Responsável: @renan-asantos
📊 Prioridade: ALTA (85/100)

💡 Sugestão: Agendar follow-up esta semana
🔗 https://github.com/pythonbrasil/pybr2025-org/issues/119
```

**Deadline Critical (3 dias antes):**
```
🚨 URGENTE - PRAZO CRÍTICO

Issue #98: Orçamento equipamento audiovisual
⏰ Prazo: QUINTA-FEIRA (17/08)
👤 Responsável: @vbuxbaum
📊 Prioridade: CRÍTICA (95/100)

⚡ AÇÃO NECESSÁRIA: Conclusão nos próximos 2 dias
🔗 https://github.com/pythonbrasil/pybr2025-org/issues/98
```

**Issue Stalled (7+ dias sem update):**
```
⏰ ISSUE PARADA

Issue #87: Orçamento aluguel cadeiras
🕐 Sem atividade há: 10 dias
👤 Responsável: @ssh-juan
📊 Status: Pode estar travada

❓ Verificar: Precisa de ajuda ou pode ser reassignada?
🔗 https://github.com/pythonbrasil/pybr2025-org/issues/87
```

**Unassigned Critical:**
```
👥 ISSUE CRÍTICA SEM RESPONSÁVEL

Issue #102: Definir parceria Pythonic Café
📊 Prioridade: CRÍTICA (92/100)
⏰ Prazo: 20/08/2025

🙋 VOLUNTÁRIOS: Quem pode assumir esta tarefa?
🔗 https://github.com/pythonbrasil/pybr2025-org/issues/102
```

**Configurações de Envio:**
- Horário: 9h-18h (horário comercial)
- Máximo 1 alerta por issue por dia
- Escalation com mention direta em casos críticos
- Thread organizada no Telegram

---

### **5. Workload Balancing (Balanceamento de Carga)**

**Objetivo:** Sugerir redistribuição de tarefas para otimizar eficiência

**Análise de Carga de Trabalho:**

**Cálculo de "Pontos de Carga" por Voluntário:**
- Cada issue ativa = 10 pontos
- Issue crítica = +10 pontos extras
- Issue parada há >7 dias = +5 pontos extras
- Histórico de resposta lenta = +5 pontos extras

**Classificação de Voluntários:**
- **Sobrecarregado (>80 pontos):** Precisa de alívio
- **Equilibrado (30-80 pontos):** Carga adequada
- **Subutilizado (<30 pontos):** Pode assumir mais

**Critérios para Redistribuição:**
- **Especialização:** Match entre expertise e tipo de tarefa
- **Disponibilidade:** Baseada em histórico de atividade
- **Interesse:** Issues que o voluntário já acompanha/comentou
- **Complexidade:** Tasks simples para voluntários novos

**Exemplo de Sugestão:**
```
📊 ANÁLISE DE WORKLOAD - 14/08/2025

🔴 SOBRECARREGADOS:
• @renan-asantos (95 pts) - 15 issues ativas
• @vbuxbaum (85 pts) - 12 issues ativas

🟡 EQUILIBRADOS:
• @belaaiza (55 pts) - 7 issues ativas
• @anadulce (40 pts) - 5 issues ativas

🟢 SUBUTILIZADOS:
• @ssh-juan (25 pts) - 3 issues ativas

💡 SUGESTÕES DE REDISTRIBUIÇÃO:
1. Issue #114 (Orçamentos crachás): @renan-asantos → @ssh-juan
   Motivo: @ssh-juan tem experiência em vendor research
   
2. Issue #93 (Internet evento): @vbuxbaum → @anadulce
   Motivo: Task de comunicação, área de @anadulce

3. Issue #112 (Local tutoriais): @renan-asantos → @belaaiza
   Motivo: @belaaiza já acompanha thread sobre venue
```

---

## 📊 **Relatórios e Dashboards**

### **Relatório Diário (09:00 no Telegram)**

```
📊 PYTHON BRASIL 2025 - STATUS DIÁRIO
📅 14 de agosto de 2025

🎯 VISÃO GERAL:
• Issues Ativas: 42 (+3 vs ontem)
• Issues Críticas: 5 (⚠️ +2 vs ontem)
• Taxa Conclusão Semanal: 68%
• Dias até evento: 68

🔥 TOP PRIORIDADES:
1. #119 Patrocínio RocketSeat (CRÍTICA - prazo hoje)
2. #98 Audiovisual (CRÍTICA - prazo 16/08)
3. #102 Parceria Pythonic (CRÍTICA - sem responsável)
4. #87 Aluguel cadeiras (ALTA - parada 10 dias)
5. #114 Crachás (ALTA - prazo 20/08)

⚠️ ALERTAS:
• 3 issues críticas com prazo <7 dias
• @renan-asantos sobrecarregado (95 pts)
• Categoria 'vendor_research' com 40% conclusão

✅ CONQUISTAS:
• Issue #115 finalizada (Parceria hotel)
• Issue #97 avançou (Keynote confirmado)
• 2 novos voluntários ativos esta semana

🎯 PRÓXIMAS AÇÕES:
• Follow-up urgente: Issues #119, #98, #102
• Redistribuir carga de @renan-asantos
• Focar em vendor research (categoria crítica)

📈 Dashboard: https://github.com/orgs/pythonbrasil/projects/8
```

### **Relatório Semanal (Sextas 17:00 via GitHub Issue)**

- **Análise de Tendências:** Performance vs semana anterior
- **Identificação de Gargalos:** Categorias/pessoas com dificuldades
- **Progresso vs Cronograma:** Status em relação aos milestones do evento
- **Recomendações Estratégicas:** Ajustes necessários na organização
- **Previsões:** Riscos identificados para as próximas semanas

### **Comandos Interativos (Telegram)**

- `/status` - Resumo geral atual
- `/criticos` - Lista issues críticas
- `/workload` - Análise de carga por pessoa
- `/categoria [nome]` - Status de uma categoria específica
- `/prazo [dias]` - Issues com prazo nos próximos X dias
- `/help` - Lista de comandos

---

## 🔄 **Workflow de Operação**

### **Monitoramento Contínuo**
1. **Webhooks GitHub:** Recebe notificações de mudanças em tempo real
2. **Análise Automática:** Processa cada evento (criação, edição, comentário)
3. **Atualização de Prioridades:** Recalcula scores quando necessário
4. **Verificação de Alertas:** Checa se novos alertas devem ser enviados
5. **Update do Dashboard:** Mantém métricas atualizadas

### **Ciclo Diário**
- **09:00:** Relatório diário no Telegram
- **A cada 2h:** Verificação de deadlines críticos
- **17:00:** Update de métricas de progresso
- **Contínuo:** Alertas por webhook

### **Ciclo Semanal**
- **Sexta 17:00:** Relatório estratégico semanal
- **Domingo:** Análise de workload e sugestões de redistribuição
- **Análise mensal:** Tendências e previsões para o evento

---

## 🎯 **Resultados Esperados**

### **Melhorias de Eficiência**
- Redução de 50% em issues "esquecidas" (>14 dias sem update)
- Melhoria de 30% no tempo médio de resolução
- Distribuição mais equilibrada de carga entre voluntários

### **Melhorias de Qualidade**
- Zero issues críticas perdendo prazo por falta de acompanhamento
- Identificação precoce de gargalos e problemas
- Decisões baseadas em dados sobre redistribuição de recursos

### **Melhorias de Experiência**
- Voluntários recebem alertas relevantes no momento certo
- Lideranças têm visibilidade completa do progresso
- Menos stress e correria de última hora

---

## 🎓 **Lições Aprendidas**

### **Erro Crítico: Assumir Progresso por Comentários (18/08/2025)**

**O que aconteceu:**  
Durante análise da issue #71 (Coffee Break), assumi que estava "sendo trabalhada" apenas porque @belaaiza havia comentado. Na realidade:
- ❌ Apenas 1 fornecedor contactado
- ❌ Sem follow-up sobre resposta  
- ❌ Sem responsável assignado
- ❌ Sem pesquisa estrutural

**Erro conceitual:**  
Confundi **atividade** com **progresso efetivo**. Um comentário isolado ≠ trabalho substancial.

**Correção aplicada:**  
- ✅ Adicionar verificação de "trabalho estrutural realizado"
- ✅ Não categorizar como "em progresso" se houver apenas comentário isolado
- ✅ Exigir evidência de múltiplos fornecedores/pesquisa para vendor research
- ✅ Distinguir entre "alguém comentou" vs "alguém está trabalhando ativamente"

**Regra para futuro:**  
Para vendor research, considerar "em progresso" apenas com:
- 3+ fornecedores identificados OU
- Template de mensagem criado OU  
- Múltiplas cotações solicitadas OU
- Orçamentos recebidos

---

**Documento criado em:** 14 de agosto de 2025  
**Última atualização:** 18 de agosto de 2025  
**Evento:** Python Brasil 2025 (21-27 out/2025)  
**Contexto:** Especificação funcional para operação via Claude Code  
**Localização:** `/assistente-ia/contexto/como-rastrear-tarefas.md`