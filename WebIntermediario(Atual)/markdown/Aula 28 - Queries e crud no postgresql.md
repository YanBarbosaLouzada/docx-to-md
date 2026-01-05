# __ PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Queries e crud

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje vamos criar as conexões com o postgresql,começaremos instalando o postgresql:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970835523200.png)
2. Vamos criar a conexão com o banco:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970836496300.png)
3. Lembrando que o usuário foi criado na aula passada, e por isto é extremamente importante as conexões\. Agora o que é uma pool? Pool nada mais é que uma conexão a um banco de dados, a cada requisição será estabelecido uma nova conexão ao banco\.
4. Vamos criar agora um controller para nossas rotas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970838492800.png)
5. E agora implementar nas nossas rotas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970839505900.png)
6. E atribuir ao banco de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970841493200.png)
7. E agora ao darmos get na url teremos o anime que cadastramos na aula passada:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970843196200.png)
8. Mas teve algo interessante no nosso projeto, se repararmos no pool nós criamos uma query:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970845324900.png)
9. O que é uma query? É uma maneira ESCRITA de nós temos com o banco de dados, os bancos relacionais nos permitem escrever neles e rodar um código, este código nós chamamos de query\.Nesta query do getAllAnimes se traduz para:  
 SELECT = pegue  
 \* = tudo  
FROM =  de   
Animes = tabela animes
10. Agora vamos criar um crud com queries:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970846324000.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970848364000.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970850321000.png)
11. Agora vamos criar as rotas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970852322800.png)
12. Agora repare que nas queries algumas coisas acontecem:
	1. Criando o anime  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970853323700.png)
	2. Editando o anime:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970855353800.png)  

	3. Pegando os animes editados:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970857353700.png)
	4. Agora deletando ele  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970860322800.png)
	5. Vamos tentar procurar o anime deletado e veremos que  o anime não foi encontrado:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970860322800.png)
	6. Porém se pesquisarmos o anime veremos que ele não foi deletado e agora funciona\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970860322800.png)
13. Subir no github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970860322800.png)

Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


