# __ PLANO DE AULA__

Aula 02 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\): Node api

Conteúdos

- Criação de uma api com node

Objetivos

- Criar Repositório
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Para entendermos o que são controllers e rotas precisamos entender as funções de um website:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969795043800.png)
2. Para fazer isto precisaremos criar duas pastas dentro do backend/src, controllers e routes:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969796625000.png)
3.  Agora vamos criar um oieRouter\.js dentro de routes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969797633100.png)
4. Para usar esta rota vamos importar ela no projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969799062400.png)
5. Agora que já está funcionando se nós formos ao google e procurar:   
__http:localhost:4444/exemplo/oie__ olha o que aparece:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969800057000.png)
6. Como nós vimos o projeto já está funcionando, porém algo estranho aconteceu, eu disse no código que o__ /exemplo__ usaria meu__ oieRouter __porém não criei nenhum controller como isto aconteceu?
7. Se eu disser a verdade nós já criamos um controller dentro da rota:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969801827700.png)
8. O controller nada mais é que uma função que é composta por duas coisas: 
	1. Requisição: Dados que vão chegar e informações de quando alguém pedir algo para nossa api
	2. Resposta: O resultado de uma sequência de operações necessárias do projeto\.
9. Agora vamos criar um controller no lugar correto e importar ele no routes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969802834800.png)
10. Se vocês repararem foi necessário colocar a extensão \.mjs no server e no route isto ocorre porque existem duas diferentes versões de javascript, a antes do es6 e a outra no formato de módulos, então o conceito de classes é do javascript sem ser esmodules então vamos utilizar a extensão para avisar o nodejs o que deverá ser ou não alterado, e para importar no routes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969804816500.png)
11. Agora se formos ao [http://localhost:4444/exemplo/oie](http://localhost:4444/exemplo/oie) veremos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969806333300.png)	
12. Agora que já estamos entendendo o conceito de funções que passam entre si, vamos entender os diferentes tipos de requisições que podemos fazer no backend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969807653600.png)
13. E para criar os controllers é preciso:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969808661600.png)
14. Mas como vamos testar enviar as coisas pelo google? Ai que está ao criar algo não se pode ser diretamente pela api, o primeiro passo necessário é instalar uma ferramenta que possa interagir com o backend neste caso usaremos o insomnia:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969810662400.png)
15. Para começar a testar as requisições colocamos um get na url: [http://localhost:4444/exemplo/oie](http://localhost:4444/exemplo/oie)
16. Para habilitarmos o projeto a ter diferentes métodos que trabalham com json precisamos permitir nosso servidor ler estes tipos de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969812420700.png)
17. Agora usaremos as 4 rotas de CRUD que temos \(Create, Read, Update,Delete\):
	1. get\- nele é passado apenas a url e já pedimos autorização:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969812420700.png)
	2. delete\- Se você reparar tem um número ao fim da url indicando qual o id do item que iremos deletar, este id é chamado de parametro : ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969815073000.png)
	3. create\- é passado os dados como um body do json:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969817080100.png)
	4. update\- Os novos dados são passados como corpo  da requisição:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969817080100.png)  
   
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias a ferramenta Git\.
- Na hora de explicar pros alunos sobre criptografia, vale a pena mostrar um pedaço deste vídeo \(em torno de 4 minutos\) sobre criptografia do cellbit:  
[CICADA 3301 \- PARTE 1 \- CELLBIT](https://www.youtube.com/watch?v=Ep5qn8pLCMA)
- Links Extras de estudo sobre o Github:  
[O QUE É GIT E GITHUB? \- definição e conceitos importantes 1/2](https://youtu.be/DqTITcMq68k?si=0gEyQuywjrcMM4jI)  
[COMO USAR GIT E GITHUB NA PRÁTICA\! \- desde o primeiro commit até o pull request\! 2/2](https://youtu.be/UBAX-13g8OM?si=9LqJceHGIfj-osHz)

Tarefas

- Sem tarefa  


