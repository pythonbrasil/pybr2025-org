# 🐍 Python Brasil 2025 - Contexto Completo de Organização

*Documentação abrangente sobre como a organização da Python Brasil 2025 funciona*

---

## 📅 **Informações Básicas do Evento**

### **Evento Principal**
- **Nome:** Python Brasil 2025 - Maior evento Python da América Latina
- **Site:** [2025.pythonbrasil.org.br](https://2025.pythonbrasil.org.br/)
- **Código APyB:** pybr2025
- **Datas:** 21 a 27 de outubro de 2025
- **Local Principal:** Centro de Eventos São Luís (R. Luís Coelho, 323 - Consolação, São Paulo)

### **Estrutura do Evento**
1. **Tutoriais (21-23 out):** Eventos gratuitos, mini-cursos da comunidade
   - Local: Faculdade Impacta (Av. Paulista)
2. **Palestras (24-26 out):** Evento principal pago, talks via CFP
   - Local: Centro de Eventos São Luís (Consolação/SP)
3. **Sprints (27 out):** Atividades de contribuição OpenSource

### **Público-Alvo**
- **Participantes:** 600-800 pessoas
- **Perfil:** Desenvolvedores, Administradores de Sistema, Cientistas de Dados
- **Níveis:** Não-técnico, Iniciante, Intermediário, Avançado
- **Track Principal:** Data Science and Analysis

### **Keynotes Confirmados**
- Sebastián Ramírez (criador FastAPI e Typer)

---

## 👥 **Estrutura Organizacional**

### **Liderança**
- **Big Kahunas (Líderes):**
  - Izabela Cristina (@belaaiza)
  - Renan de Assis (@renan-asantos)

### **Características da Organização**
- **Natureza:** 100% voluntária, sem fins lucrativos
- **Modelo:** Todo dinheiro arrecadado é investido no próprio evento
- **Flexibilidade:** Voluntários trabalham conforme disponibilidade pessoal/profissional
- **Transparência:** Organização pública via GitHub

### **Grupos de Trabalho (Baseado em Manual Big Kahuna)**

#### **1. Time de Aquisição de Recursos**
- Desenvolver plano de patrocínio
- Buscar patrocínios e parcerias
- Gerenciar vendas de ingressos e códigos promocionais
- **Níveis:** Platinum, Gold, Silver, Bronze, Supporter

#### **2. Time Financeiro/Fiscal**
- Gerenciar fluxo de caixa
- Previsão de custos
- Coordenar com APyB
- Configurar plataforma de ticketing

#### **3. Time de Marketing/Publicidade (Comunicação)**
- Desenvolver identidade visual do evento
- Gerenciar redes sociais
- Criar mockups para materiais do evento
- Engajamento da comunidade
- Comunicações multi-canal

#### **4. Time de Infraestrutura**
- Garantir local do evento
- Arranjar suporte técnico (audiovisual, internet)
- Organizar tradução, filmagem e transmissão online
- Gerenciar logística para keynote speakers

#### **5. Time de Experiência do Evento**
- Organizar catering (com opções dietéticas)
- Gerenciar amenidades do evento
- Criar guia da cidade
- Projetar espaços do evento

#### **6. Time Administrativo**
- Lidar com orçamento
- Gerenciar contratos
- Adquirir materiais do evento

#### **7. Time Técnico (Automações)**
- Criar site do evento
- Gerenciar acesso e notificações
- Integrar plataformas de ticketing e apresentação
- Desenvolvimento de automações organizacionais
- Integração GitHub-Telegram

#### **8. Time de Conteúdo**
- Gerenciar cronograma do evento
- Lidar com call for papers (C4P)
- Selecionar keynote speakers
- Gestão plataforma de submissão (Pretalx)

---

## 🛠️ **Ferramentas e Plataformas**

### **Comunicação**
- **Telegram:** Comunicação assíncrona diária (grupo principal)
  - Chat ID: -1002120660974
  - Thread ID: 1888
- **Google Meet:** Reuniões semanais síncronas (quintas 18:30 GMT-3)
- **HackMD:** Pautas colaborativas de reunião
- **FreshDesk:** Gestão centralizada de emails
  - URL: pythonbrasil.freshdesk.com
  - Email: eventos@python.org.br
  - **Limitação:** Apenas 2 agentes por conta gratuita

### **Gestão de Projetos**
- **GitHub:** Transparência e tracking de tarefas
  - Repositório: pythonbrasil/pybr2025-org
  - Projeto: [Planejamento pybr2025](https://github.com/orgs/pythonbrasil/projects/8)
  - **120+ issues** para organização
- **Google Drive:** Documentos sensíveis e arquivos
  - Pasta: "Python Brasil 2025" (propriedade APyB)

### **Desenvolvimento**
- **Pretalx:** Plataforma para submissão de palestras
- **Site do Evento:** 2025.pythonbrasil.org.br

### **Financeiro**
- **APyB:** Gestão financeira oficial
- **Formulário de Pagamentos:** ultradox.com/app/apyb-solicitacao-pagamento
- **Planilha Fluxo de Caixa:** Google Sheets (controle interno)

---

## 🔄 **Processos e Workflows**

### **Gestão de Tarefas**
1. **Issues GitHub:** Transparência pública das atividades
2. **Projeto GitHub:** Organização visual de prioridades
3. **Sem labels formais:** Títulos descritivos em português
4. **Atribuição orgânica:** Voluntários escolhem tarefas conforme disponibilidade

### **Padrões de Issues**
- **Vendor Research:** "Reunir orçamentos de..."
- **Sponsor Tracking:** "Acompanhamento patrocínio [Empresa]"
- **Communication Tasks:** "Mandar email/mensagem..."
- **Decision Making:** "Decidir..."
- **Implementation:** "Adicionar/Criar..."
- **Partnership Development:** "Parceria com..."

### **Workflow de Reuniões**
1. **Preparação:** Pauta colaborativa no HackMD
2. **Execução:** Google Meet semanal (quintas 18:30)
3. **Documentação:** Transferência manual HackMD → GitHub issues
4. **Follow-up:** Ações convertidas em issues específicas

### **Automações Existentes**

#### **GitHub → Telegram Integration**
- **Trigger:** Novas issues e comentários
- **Formato:** Markdown/MarkdownV2
- **Scripts:**
  - `main.py`: Comentários de issues → Telegram
  - `new-issue.py`: Novas issues → Telegram
  - **Filtros:** Exclui pull requests, issues deletadas

#### **Meeting Reminders**
- **Frequência:** Cron job (atualmente a cada 10 min para teste)
- **Plataforma:** Telegram
- **Script:** `lembrete-reuniao.py`
- **Conteúdo:** Link Google Meet + call for agenda

#### **HackMD Integration**
- **Funcionalidade:** Criação automática de notas de reunião
- **Formato:** Template com data atual
- **Permissões:** Público (leitura/escrita para todos)
- **Script:** `hackmd-integration.py`

---

## 📊 **Análise do Estado Atual (Agosto 2025)**

### **Estatísticas GitHub**
- **Total Issues:** 120+ issues
- **Status:** ~40 abertas, ~60+ fechadas
- **Taxa de Conclusão:** ~60% (demonstra boa execução)

### **Distribuição de Trabalho**
- **Renan de Assis:** ~40% das issues (coordenação geral)
- **Juan Borges:** Pesquisa de fornecedores e coordenação técnica
- **Izabela Cardoso:** Co-liderança, patrocínio e parcerias estratégicas
- **Vitor Buxbaum:** Logística e gestão de fornecedores
- **Ana Dulce:** Engajamento comunitário e conteúdo

### **Issues Ativas Prioritárias**
- **Sponsorship:** RocketSeat (#119), Elastic (#118), Pythonic Café (#102)
- **Vendors:** Crachás (#114), cadeiras (#87), audiovisual (#98), segurança (#92)
- **Partnerships:** {re}programa (#120), hotéis (#59)
- **Content:** FAQ (#106), keynotes (#97)
- **Infrastructure:** Detalhes local tutoriais (#112), internet (#93)

### **Work Completed**
- Updates do site (logo APyB, condições tickets, plano patrocínio)
- Configuração plataforma Pretalx
- Decisões sobre parcerias hoteleiras
- Comunicações e contratos com sponsors

---

## 💰 **Estrutura Financeira e Diretrizes APyB**

### **Requisitos Fundamentais APyB**
- **Organizador:** Deve ser membro da APyB
- **Natureza do Evento:** 
  - Promover Python no Brasil
  - Sem fins lucrativos
  - Código de Conduta obrigatório
- **Canal Oficial:** APyB-condir@googlegroups.com

### **Estrutura Financeira APyB**
- **Taxa APyB:** 10% das taxas de inscrição
- **Regra Fundamental:** Eventos não podem gastar mais do que arrecadam
- **Superávit:** Saldo positivo vira doação para APyB
- **Transparência:** Relatório pós-evento obrigatório

### **Gestão Operacional**
- **Entidade Responsável:** Associação Python Brasil
- **Código Evento:** pybr2025
- **Email Oficial:** eventos@python.org.br
- **Processo:** Solicitação via formulário específico

### **Processos de Patrocínio (via APyB)**
1. Submeter solicitação de apoio (formulário oficial)
2. Buscar patrocínios
3. APyB fornece infraestrutura burocrática
4. Emitir notas fiscais/recibos para sponsors
5. Rastrear créditos financeiros do evento
6. Submeter relatório pós-evento

### **Pagamentos e Reembolsos**
- **Preferência:** Pix
- **Requisito:** Notas fiscais dos fornecedores
- **Prazo:** Até 3 dias úteis para processamento
- **Formulários:** Oficiais para solicitações, notas fiscais, pagamentos, reembolsos

### **Controle Interno**
- **Planilha Fluxo de Caixa:** Google Sheets
- **Requisitos:** Comprovantes obrigatórios de todos os pagamentos
- **Transparência:** Registros detalhados para prestação de contas

### **Programa de Auxílio Financeiro**
- **Objetivo:** Apoiar grupos sub-representados
- **Gestão:** Coordenação entre sponsors de bolsas e beneficiários

---

## 📋 **Metodologias Estabelecidas**

### **Pesquisa de Fornecedores**
- **Estratégia:** Busca nacional (não restrita a SP)
- **Verificação:** Credibilidade via Reclame Aqui, reviews, presença digital
- **Coleta:** Contatos, localização, preços, cases, avaliações
- **Avaliação:** Sistema de estrelas baseado em critérios específicos
- **Comunicação:** Templates para WhatsApp/Instagram/Email

### **Critérios de Fornecedores**
- **⭐⭐⭐⭐⭐:** +15K seguidores, +5 anos, 90%+ satisfação
- **⭐⭐⭐⭐:** 5K-15K seguidores, 3-5 anos, 80%+ satisfação
- **⭐⭐⭐:** 1K-5K seguidores, 1-3 anos, 70%+ satisfação

### **Argumentos de Negociação**
- Volume significativo (600-800 unidades)
- Credibilidade nacional do evento
- Visibilidade para público qualificado (devs, empresários)
- Planejamento antecipado
- Potencial de case/referência
- Networking com comunidade tech

---

## 🎯 **Padrões de Comunicação**

### **Templates WhatsApp (Conciso)**
```
Olá! 👋 

Vi vocês no Instagram e preciso de orçamento para [PRODUTO].

🐍 EVENTO: PYTHON BRASIL 2025
• Maior evento Python da América Latina
• Site: 2025.pythonbrasil.org.br
• Data: [DATA ESPECÍFICA]
• Local: Centro de Eventos São Luis - Consolação/SP
• Pessoas: 600 a 800 [unidades]
• Entrega: até [DATA - 1 MÊS ANTES]

💡 ESPECIFICAÇÕES:
✅ [Especificação 1]
✅ [Especificação 2]
✅ [Especificação 3]
✅ Entrega: Consolação/SP ou Correios

Podem enviar:
📋 Preços para 600 e 800 unidades
📦 Prazo produção + entrega
📱 Fotos dos modelos

Aguardo! 🙏
```

### **Templates Email/Instagram (Completo)**
- Apresentação formal do evento
- Contexto de importância nacional
- Especificações técnicas detalhadas
- Solicitações específicas de informação
- Tom profissional mas acessível

### **Timing de Contatos**
- **Melhor horário:** 9h-12h (empresas B2B)
- **Melhores dias:** Terça a quinta
- **Sequência:** WhatsApp → Instagram → Email → Telefone
- **Follow-up:** 3 dias (WhatsApp) → 1 semana (Instagram) → telefone

---

## 🚨 **Desafios e Limitações Atuais**

### **Limitações de Ferramentas**
- **FreshDesk:** Apenas 2 agentes (limitação do plano gratuito)
- **Automações:** Limitadas a notificações simples
- **Documentação:** Transferência manual HackMD → GitHub

### **Gargalos Organizacionais**
- **Pesquisa Manual:** Fornecedores e orçamentos consomem muito tempo
- **Follow-up:** Acompanhamento manual de sponsors e fornecedores
- **Coordenação:** Dependência de voluntários com disponibilidade limitada
- **Conhecimento:** Risco de perda de contexto entre edições

### **Como Claude Code Pode Apoiar a Organização**

**Tipos de Tarefas onde Claude Pode Ajudar:**

1. **Pesquisa de Fornecedores:** Aplicar metodologia de orçamentos estabelecida para pesquisar e ranquear empresas
2. **Análise de Tarefas:** Monitorar issues GitHub, calcular prioridades e sugerir redistribuição de workload
3. **Suporte a Comunicação:** Rascunhar emails de follow-up e preparar talking points para reuniões
4. **Planejamento Estratégico:** Criar cronogramas, analisar riscos e comparar opções de decisão
5. **Documentação:** Processar notas de reunião e manter knowledge base atualizada

**Workflow Recomendado:**
- **Diário**: Relatórios de prioridades e tarefas específicas conforme demanda
- **Semanal**: Análise de workload e progresso vs cronograma
- **Ad-hoc**: Pesquisas urgentes e suporte a decisões críticas

**Vantagens**: Flexibilidade, integração natural com ferramentas existentes, transparência total e evolução orgânica conforme necessidades da equipe

---

## 🔄 **Ciclo Organizacional**

### **Comunicação Assíncrona (Diária)**
- **Telegram:** Updates, questões rápidas, coordenação
- **GitHub:** Documentação formal, tracking, transparência
- **FreshDesk:** Comunicações externas formais

### **Comunicação Síncrona (Semanal)**
- **Google Meet:** Quintas 18:30 GMT-3
- **HackMD:** Pauta colaborativa pré-reunião
- **Resultados:** Issues GitHub com ações específicas

### **Onboarding de Voluntários**
1. Adicionar ao Telegram
2. Compartilhar README + guia onboarding
3. Acesso ao Google Drive
4. Convite reunião semanal (opcional)
5. Membro team GitHub `pybr2025-org`

---

## 📚 **Recursos e Referências**

### **Documentação Oficial**
- [Manual Big Kahuna Python Brasil](https://manual.pythonbrasil.org.br/organizacao/index.html)
- [Guia APyB Organização Eventos](https://apyb.python.org.br/associados/guias/como-organizar-eventos/)
- README.md e docs/ deste repositório

### **Recomendações do Manual Big Kahuna**
- **Planejamento:** Começar cedo com planos de patrocínio
- **Estrutura:** Definir tamanho do evento e times
- **Identidade:** Criar identidade visual
- **Cronograma:** Planejar calendário do evento
- **Publicação:** Focar em publicação precoce de grade/cronograma
- **Inclusão:** Apoiar participação de estudantes e grupos sub-representados

### **Considerações Críticas**
- **Entrada Gratuita:** Decidir sobre entrada gratuita para organizadores/palestrantes
- **Código de Conduta:** Implementação obrigatória
- **Programas de Apoio:** Considerar programas para grupos sub-representados
- **Flexibilidade:** Manual enfatiza flexibilidade e planejamento antecipado

### **Opções de Registro (APyB)**
- **Eventos Gratuitos:** Usar plataformas como Eventbrite
- **Eventos Pagos:** Duas opções disponíveis (direto ou através da APyB)

### **Ferramentas de Referência**
- Código de Conduta
- Programa de Auxílio Financeiro
- Templates de comunicação
- Metodologias de orçamento

### **Contatos Importantes**
- **Líderes:** @belaaiza, @renan-asantos
- **APyB Oficial:** APyB-condir@googlegroups.com
- **APyB Eventos:** eventos@python.org.br
- **Telegram:** Grupo principal da organização
- **FreshDesk:** pythonbrasil.freshdesk.com

---

## 🏗️ **Infraestrutura Técnica**

### **Stack Atual**
- **Backend:** Python 3.12
- **Automação:** GitHub Actions
- **Integrações:** Telegram Bot API, GitHub API
- **Dependências:** httpx para requisições HTTP

### **Arquitetura de Automação**
```
GitHub Webhooks → Python Scripts → Telegram Bot API
     ↓                   ↓               ↓
  Issues/Comments   Processing &     Formatted
                   Formatting      Notifications
```

### **Deploy e Execução**
- **GitHub Actions:** Workflows automatizados
- **Triggers:** Events (issues, comments, schedule)
- **Environment:** Ubuntu latest com Python 3.12
- **Secrets:** TELEGRAM_BOT_TOKEN via GitHub Secrets

---

**Documento criado em:** 14 de agosto de 2025  
**Evento:** Python Brasil 2025 (21-27 out/2025)  
**Contexto:** Análise completa da organização para desenvolvimento de AI Agents  
**Localização:** `/assistente-ia//contexto/py-planner.md`