# __ PLANO DE AULA__

Aula 08 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React

Conteúdos

- Login API e deploy

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. O intuito desta aula é  entender como as builds funcionam, mas primeiro o que é uma build? A build nada mais é que um processo de compilação do seu código, mas o que isto significa? Que o projeto irá pegar todos os arquivos e reescrever o seu código de um modo onde ele irá  ficar mais rápido\. Ou seja, o código que escrevemos serve para ficar legível a outros programadores, porém não para enviar em produção\.
2. Okay mas agora que entendemos, como dar build ? Vamos começar pelo react\.
3. Primeiro de tudo devemos rodar o comando ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970459767500.png)
4. Isto irá criar um arquivo estático, ou seja um código simples e fácil de ser entendido o arquivo estático nada mais é que um código compilado e fácil de ser usado no node :  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970460886900.png)
5. O deploy nada mais é que pegar o nosso código e enviar para a internet para isto iremos usar o render\.com que é um ótimo site tanto para o backend quanto para o frontend, vamos começar pelo backend\.
6. Mas primeiro precisamos colocar o projeto no github:  
 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970462887600.png)
7. Vamos começar subindo o backend como um servidor:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970463887900.png)
8. Importar do github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970465886100.png)
9. Vamos inserir no backend o os dados do projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970466888000.png)
10. Sempre permitir o gratuito né:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970468887300.png)
11. Para este projeto precisaremos colocar as chaves de variáveis no projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970469888800.png)
12. É importante se atentar a versão do node, a aula foi construída com a versão 21\.7\.1 caso não esteja na documentação é necessário criar uma variável de ambiente chamada NODE\_VERSION e colocar como valor 21\.7\.1\.
13. Lembre\-se de verificar se o banco de dados tem livre acesso de qualquer lugar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970471888100.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970472887600.png)
14. Vamos permitir todos os ips:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970473890300.png)	
15. E temos o projeto funcionando:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970474887400.png)
16. Agora vamos criar o frontend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970476534400.png)
17. O frontend SEMPRE será um site estático para carregar mais rápido é importante se atentar aos detalhes\. O nosso backend não se chama mais localhost:4444 se chama o nome que o render der para nós:  
[https://webintermediary\.onrender\.com/](https://webintermediary.onrender.com/)   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970478584600.png)
18. Então devemos mudar na url do site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970479584200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970480584500.png)
19. Agora o que devemos fazer é dar o deploy do frontend no projeto como estático:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970482584500.png)
20. E após o projeto está no ar é apenas entrar no link do site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970484584900.png)  
 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970485583400.png)
21. Agora tanto o backend quanto o frontend estão onlines com isto a partir de agora vocês conseguem subir os projetos de vocês online, aproveitem que a partir de agora qualquer desafio estará na internet\.

Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.
- Na hora de explicar pros alunos sobre criptografia, vale a pena mostrar um pedaço deste vídeo \(em torno de 4 minutos\) sobre criptografia do cellbit:  
[CICADA 3301 \- PARTE 1 \- CELLBIT](https://www.youtube.com/watch?v=Ep5qn8pLCMA)
- Links Extras de estudo sobre o Github:  
[O QUE É GIT E GITHUB? \- definição e conceitos importantes 1/2](https://youtu.be/DqTITcMq68k?si=0gEyQuywjrcMM4jI)  
[COMO USAR GIT E GITHUB NA PRÁTICA\! \- desde o primeiro commit até o pull request\! 2/2](https://youtu.be/UBAX-13g8OM?si=9LqJceHGIfj-osHz)

Tarefas

- sem tarefa  


