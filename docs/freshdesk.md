# Tutorial de gerenciamento de email da Python Brasil 2025

Na Python Brasil 2025 utilizamos o [freshdesk](https://pythonbrasil.freshdesk.com/a/dashboard/default) como ferramenta para gerenciar emails. 

## Termos utilizados no freshdesk

* Contato: similar a um contato do celular, um contato no freshdesk deve possui um **Nome** e um **email**
* Ticket: um conjunto de emails agrupados de um mesmo contato
* Grupo: categoria para organizar os tickets, na Python Brasil utilizamos o ano do evento como grupo (exemplo: "Python Brasil 2024" ou "Python Brasil 2025")
* Agente ou analista: pessoa com acesso para responder tickets no freshdesk (exemplo: alguém da organização)
* Cliente: outro nome para o contato destinatário de um ticket
* Status de tickets:
  * Aberto: O ticket requer uma ação de um agente. Novos tickets são marcados como Abertos por padrão. Sempre que um cliente responde a um ticket, ele é automaticamente movido de volta para o status Aberto.
  * Pendente: O ticket é "pausado" enquanto o agente coleta informações adicionais.
  * Resolvido: O ticket é concluído de acordo com o agente, ou seja, uma solução foi fornecida.
  * Fechado: O ticket é concluído de acordo com o cliente, ou seja, uma solução foi aceita.

## Como obter acesso?

Para obter acesso siga os passos abaixo:
1. Crie uma conta na organização "Associação Python Brasil" do Freshdesk através desse [link](https://pythonbrasil.freshdesk.com/support/signup)
2. Peça para um dos organizadores te incluir no grupo "Python Brasil 2025" da ferramenta
3. Entre na sua conta atrvés desse [link](https://pythonbrasil.freshworks.com/login?client_id=451979510707337272&redirect_uri=https%3A%2F%2Fpythonbrasil.freshdesk.com%2Ffreshid%2Fauthorize_callback%3Fhd%3Dhttps%3A%2F%2Fpythonbrasil.freshdesk.com) para acessar o Portal do Analista.

Ao seguir os passos acima, vai ver a tela de Painel de Controle, ao clicar no segundo ícone da barra lateral direita temos a visualização de tickets (similar a imagem abaixo), principal tela utilizada.
![image](https://github.com/user-attachments/assets/a1af4c74-1c12-44ac-bd4d-5de8ff6e2b59)

## Como criar um novo ticket?

Para enviar um novo email é necessário criar um novo ticket. Isso é feito no botão "Novo" >> "Ticket" no canto superior direito.
![image](https://github.com/user-attachments/assets/eae6887c-8a18-4e47-bdda-dffd4bf5d4d2)

> Todo novo email deve ser vinculado a um ticket, o campo "Novo" >> "Email" só cria um ticket depois do cliente responder e isso nos faz perder informações importantes

Alguns campos já vão estar preenchidos, vou comentar os que precisam ser completados:

1. Contato:
  a. Fazer a busca do contato por email, caso não encontre, siga para o passo abaixo
  b. Clique no campo "adicionar um novo contato" no canto direito, preencha um nome e email
2. Assunto: assunto necessário para o email
3. Grupo: **selecionar o grupo "Python Brasil 2025"**
4. Descrição: redigir o email nesse campo

Ao clicar em "Criar" no final da tela será criado um novo ticket atribuído a você.

## Como responder um ticket existente?

Ao abrir um ticket podemos ver uma barra superior igual a da imagem abaixo
![image](https://github.com/user-attachments/assets/53b5e5b4-7c1d-4b31-ae8c-91ce817c327e)

O botão "Responder" cria uma nova resposta(email) ao cliente daquele ticket. Assim, podemos redigir o email e no final escolher um dos 4 status descritos na seção de termos dessa paǵina. **O recomendado é responder o email e classificar o status como "Resolvido"**


## Como mesclar dois tickets?

É possível que um cliente responda um mesmo ticket com outro campo assunto e endereço de email, assim criando dois tickets diferentes para a mesma conversa.
Assim, podemos mesclar dois tickets para manter toda a comunicação de um assunto específico em um único local.

Para mesclar dois tickets podemos abrir um deles e clicar no campo "mesclar", escolher o(s) outro(s) ticket(s) para mesclar e concluir a ação.
![image](https://github.com/user-attachments/assets/a7a8cdc7-1983-440a-8ed2-5079774aadd0)

Para mais informações de mesclar tickets, leia essa [seção](https://support.freshdesk.com/support/solutions/articles/231527-how-to-process-a-ticket#Merge-two-or-more-tickets) da documentação do freshdesk.


## Links de referência:
* [How to Process a Ticket?](https://support.freshdesk.com/support/solutions/articles/231527-how-to-process-a-ticket)
* [Understand the Ticket List View](https://support.freshdesk.com/support/solutions/articles/37559-understand-the-ticket-list-view)
* [Understand the Ticket Details View](https://support.freshdesk.com/support/solutions/articles/37588-understand-the-ticket-details-view)
