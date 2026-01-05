# __PLANO DE AULA__

Aula 15 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- WebSocket

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje vamos construir um novo formato de conexão chamado websocket, no geral o websocket nada mais é que uma conexão aberta vamos entender os 2 tipos de conexões que conhecemos até o momento:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971110246300.png)
2. Esta conexão é por meio de requisições HTTP\. HTTP é a sigla para Hypertext Transfer Protocol, ou Protocolo de Transferência de Hipertexto\. Esse é o principal protocolo responsável pela transferência de dados na Internet, criando as bases necessárias para a conexão entre um cliente e um servidor\.Porém existe outro formato de conexão chamada WEBSOCKET que imagine que tanto o frontend quanto o backend JÁ tem uma conexão aberta e apenas transitam informações entre elas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971110246300.png)
3. Ou seja, já teremos uma conexão aberta e podemos enviar coisas em tempo real do frontend para o backend\.Sem precisar aguardar as respostas\.
4. Vamos começar instalar o websocket tanto no frontend quanto no backend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971110246300.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971118741900.png)
5. Nesta aula vamos criar um bate papo para os usuários da nossa plataforma poderem enviar as cartinhas pokemon no chat, para isto vamos começar a utilizar o websocket

:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971118741900.png)

1. Vamos começar com o backend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971120882800.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971122890500.png)

programar nosso servidor socket que as mensagens, agora vamos ao frontend para podermos criar o chat, mas como sempre vamos adicionar ele as rotas e navbar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971122890500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971126071700.png)

1. Agora vamos criar a tela de bate papo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971126071700.png)
2. O componente do join é responsável por criar a conexão websocket:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971126071700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971130422900.png)
3. Agora o componente do chat:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971132887400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971132887400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971134897300.png)
4. Não podemos esquecer o css do site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971134897300.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971134897300.png)
5. Agora o chat está funcionando e podemos enviar mensagens em tempo real sobre o site:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971134897300.png)
6. Agora vamos subir ao github:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971141806500.png)

Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


