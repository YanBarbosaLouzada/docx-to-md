# __PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- \(R\) Bootstrap 2\.

Objetivos

- Ensinar os alunos sobre como o mundo real funciona;
- Apresentar o site [https://fonts\.google\.com/](https://fonts.google.com/);
- Conhecer o [https://getbootstrap\.com/docs/5\.3/getting\-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/);
- Usar o [https://color\.adobe\.com/pt/trends](https://color.adobe.com/pt/trends)\.  


Estratégias e atividades

- Estilizar o site da aula passada e aprender sobre posições\.
- Entender como funcionam as pastas\.
- Aprender sobre novas tags HTML: 
	- Links;
	- Loaders\.

1. Hoje vamos usar novos templates de código e funcionalidades: Formulário de contato, rodapé e um incrível carrousel\.
2. Vamos começar pelo formulário\. Muitas vezes precisamos digitar algo no site para poder interagir com ferramentas e funcionalidades\. O formulário que iremos criar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600806956800.png)  
Vamos começar pelo HTML:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600810925400.png)  
Nele nós usamos uma mistura de Bootstrap com CSS customizado\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600812273000.png)  
Repare que para alterar o contato dentro do CSS, eu não precisei de uma DIV com um ID dentro do formulário, invés disso eu entrei na DIV ‘\#contato’ e dentro dela coloquei o form, ou seja, posso ir direto para uma tag HTML usando seletores HTML\. Aqui está um site para praticar: [https://flukeout\.github\.io/](https://flukeout.github.io/) 
3. Vamos criar agora, uma nova etapa de planos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600814897500.png)  


CSS:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600816896800.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600817897400.png)  


E o resultado será:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600819905700.png)

1. Agora, vamos criar um belíssimo carrousel:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600821896600.png)
	1. Repare que ele gira para ter mais duas imagens com legendas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600824895600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600827914100.png)

- 
	1. Para construir um carrousel é preciso utilizar o JavaScript do Bootstrap, então é extremamente importante que na primeira aula você tenha copiado o link do script e colocado ele embaixo do seu código HTML, pois coisas como cliques e giros são necessários\. 
	2. Vamos começar pelo CSS, primeiro deixar o fundo com o linear gradient e modificar os textos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600830896500.png)
	3. Escolha um carrousel no Bootstrap:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600833052100.png)
	4. Agora, vamos editar algumas partes\. Primeiro vamos checar se existe as DIVs com os IDs carouselExampleCaptions e sobre:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600836046600.png)
	5. Como editar um dos cards:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600837046800.png)  
Coloque o caminho de uma imagem e edite o <h5> e do <p>\.
	6. Após editar todos os 3 cards, o carrousel já estará funcionando

1. Finalizando com o conteúdo do rodapé:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600839046400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600840047200.png)  
O resultado será o final será a parte de baixo do site:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600841047600.png)

1. Agora, vamos aprender algo novo, a tag __<a href=”linkDeAlgo”>texto</a>__\. Se colocarmos um ‘\#nomeDoIdDeAlgumaDiv’ dentro do href da tag <a>, quando clicarmos no link, ele irá nos levar direto para a sessão, dito isto vamos observar a navbar agora:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600843302900.png)
2. Repare que os <a> tem um href com o ID das DIV que criamos:  


Então, se clicarmos em um dos links:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600845307700.png)  
Vamos direto para a sessão que clicamos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600846316200.png) 

1. Para finalizar a aula, iremos postar o nosso site atualizado no Github:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600849309900.png)  


Recursos

- Git Chrome e VS Code\.

Observação

- Caso os alunos perguntem algo sobre como funciona tal coisa, ou quero estilizar tal coisa, SEMPRE, mesmo sabendo a resposta, é recomendado dizer: Não sei vamos pesquisar, e ensinar ele a pesquisar exemplo: “como centralizar uma DIV” e ir abrindo os stack overflow \- é um site de perguntas e respostas para profissionais e entusiastas na área de programação de computadores\. É extremamente importante que os alunos se sintam confiantes em jogar as dificuldades no Google para achar as soluções, principalmente porque a ideia de usar o Github é estimulá\-los a continuar os projetos em casa\.
- Incentive os alunos a procurarem coisas novas no Bootstrap, uma muito legal é Popovers, diga para procurarem em casa como implementar no site\.

Tarefas

- Fazer uma tela que contenha cards do bootstrap

