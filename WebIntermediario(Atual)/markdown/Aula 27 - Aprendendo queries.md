# __ PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  Postgresql

Conteúdos

- Queries

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje é uma aula de introdução à queries e como elas funcionam\.
2. Mas o que é o uma querie? Queries na verdade são maneiras lógicas de explicar ao banco de dados o que ele deve ou não fazer, um banco relacional nada mais é que um espaço na memória do computador onde ele guarda e ordena binários do projeto\. Ué como assim binários? Tudo que você guarda em um banco de dados de verdade será convertido para binário\.
3. Ou seja, para salvar em um banco de dados: “tomates são incríveis”\.  Será na verdade salvo no banco:  
01110100 01101111 01101101 01100001 01110100 01100101 01110011 00100000 01110011 11100011 01101111 00100000 01101001 01101110 01100011 01110010 11101101 01110110 01100101 01101001 01110011 
4. Mas porque é importante sabermos disto? Porque todos os bancos de dados relacionais nada mais é que um organizador de binário, onde cada banco de dados é uma maneira de organizar os dados\.
5. O que nos leva a próxima parte da aula: Queries\. As queries nada mais são que maneiras de digitar o que desejamos buscar no banco de dados\. Para isto usaremos o site [https://sqlbolt\.com/lesson/select\_queries\_introduction](https://sqlbolt.com/lesson/select_queries_introduction), para aulas   

6. Vamos começar entendendo a query de coletar os dados\. Nela nós usamos o Select para selecionar as colunas que queremos coletar e da tabela do banco\.Tabelas são “estruturas” de dados e colunas os tipos\. Exemplo eu vou ter uma tabela de carros com as colunas cor do tipo varchar, ano do tipo integer e placa do tipo TEXT  
7. Exemplo  de Select:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970755110400.png)
8. Mas e se eu quiser selecionar tudo da tabela?  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970757112900.png)
9. Agora vamos mexer na query no final da tela:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970758113000.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970759842400.png)
10. Selecionar os diretores por filmes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970760895400.png)
11. Selecionar filmes e diretores juntos![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970762894800.png)
12. Selecionar título e ano:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970763895300.png)
13. Selecionar tudo dos filmes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970765895000.png)
14. Agora podemos ter também condições de queries\. Exemplo pegue todos os filmes depois de 2021:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970767893100.png)
15. Pegar um filme onde o id é 6:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970769896700.png)
16. Pegar os filmes entre 2000 e 2010:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970771894800.png)
17. Encontrar os filmes que não estejam entre 2010 e 2000   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970773894000.png)
18. Encontrar os 5 primeiros filmes da pixar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970775894100.png)
	1. Agora de desafio para o resto da aula os alunos devem descobrir como as queries funcionam\.  
  


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


