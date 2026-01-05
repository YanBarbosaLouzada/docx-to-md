# __ PLANO DE AULA__

Aula 10 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Login API e deploy

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje é uma aula de introdução a bancos de dados relacionais, mas primeiro precisamos entender a diferença entre banco de dados relacionais e banco de dados não relacionais:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970629701800.png)
2. Mas qual a vantagem do banco relacional? Sendo que podemos utilizar dados como o mongoDB e armazenarmos tudo que quisermos sem se preocupar com as implementações? Os bancos relacionais tem sua maior vantagem a organização e padrão de dados, exemplo se tentarmos cadastrar em uma coluna do tipo número algum texto ele irá retornar um erro, logo precisamos entender que os projetos utilizam regras e padrões mais estabelecidos\.
3. Mas com isto, como sabemos qual banco é o melhor? Ai que está os dois são igualmente bons então o que vai definir a qualidade do banco é na verdade o que o programador atrás da cadeira irá fazer\. Para o banco de dados iremos utilizar o postgresql:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970631674600.png)
4. Vamos fazer o download![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970634671200.png)
5. Passo a passo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970636702400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970638671200.png)
6. Não podemos esquecer essa senha PRINCIPALMENTE porque se esquecermos a senha na hora de instalar teremos que desinstalar o  postgresql e instalar de novo pois este é o maior privilégio de administrador![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970639673100.png)
7. A porta por padrão vamos usar a 5432:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970641672500.png)
8. Vamos deixar o default para região:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
9. E pronto finalizamos![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
10. Vamos entrar no pgAdmin:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
11. Ao conectar o server ele irá pedir a senha:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
12. Agora vamos entender o dashboard\. Ele é aonde fica nossos dados e bancos de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
13. Vamos nos conectar com o banco de dados, é extremamente importante usar a senha e a versão que temos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
14. Vamos criar um banco de dados chamado de Teste:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
15. Vamos agora criar uma tabela chamada anime onde ela terá um id que será do tipo chave primária\(veremos isto futuramente\), um nome do tipo varchar que é basicamente uma string de até 250 caracteres, o número de episódios e a nota do anime que é um float:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
16. Agora vamos dar um refresh no projeto:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970643672300.png)
17. E vamos também visualizar a tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970659794600.png)
18. Vamos com a query tool criar a tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)
19. E verificar se foi realmente salva vamos selecionar todos os dados da tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)  

20. Onde ficam as informações das tabelas? Dentro de public tables  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)
21. Vamos inserir um dado na tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)
22. E se repararmos agora podemos pesquisar todos os dados da tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)
23. Vamos agora criar uma view para visualizar os dados da tabela![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png) 
24. E agora sempre que quisermos ver os dados podemos ir diretamente aos dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970660109200.png)
25.   
  


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

- Sem tarefa  


