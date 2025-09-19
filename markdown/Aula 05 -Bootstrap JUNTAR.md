# __PLANO DE AULA__

Aula 05 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Fontes CSS e Bootstrap\.

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

1. Hoje vamos conhecer novas ferramentas e funcionalidades que o mundo real usa na web, serão na aula de hoje apresentada 3 novas ferramentas: Google fonts, Bootstrap e Adobe Colors\.
2. Vamos começar conhecendo o projeto\. Tomei a liberdade de postar o site no ar neste link: [https://aula\-bootstrap\-mynds\-x44f\.vercel\.app/](https://aula-bootstrap-mynds-x44f.vercel.app/)
3. Para começar, vamos montar o CSS da __navbar __e dos cards dos tênis, mas antes vamos começar a configurar o projeto, esta é a estrutura do meu projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910900307400.png)
4. Pode deixar os alunos escolherem uma imagem para produto que querem mostrar nos cards, pode ser anime, desenho, comida, cantores, etc, e uma logo para o site\.
5. Agora vamos abrir o [https://fonts\.google\.com/](https://fonts.google.com/) e escolher uma fonte, eu escolhi a Roboto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910903306400.png)
6. Agora que já escolhemos devemos “linkar” a imagem no nosso projeto\. Para fazer isso, clique em um selecionar na direita:  
  

	1. Selecione a letra:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910908307500.png)
	2. Agora repare que tem um <link> e um @import, clique no @import:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910916305800.png)
	3. Copie apenas o conteúdo e cole no começo do seu CSS:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910921303700.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910923304600.png)
7. Abrindo o Adobe Colors para escolher cores\. Nele vá em tendências e escolha uma paleta de cores que achar legal, cada paleta tem 5 códigos de cores que pode escolher:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910925304000.png)
8. Para criar a navbar, usaremos o Bootstrap\. Imagine que queira diminuir o trabalho de construir um site, usando templates de código e apenas editando\-os, e é exatamente isto que o Bootstrap faz\. Ele permite que você use coisas pré montadas para poder colocar no site\. Para configurar ele você vai precisar colocar 4 linhas pra importar, vá no site [https://getbootstrap\.com](https://getbootstrap.com) e pegue as linhas:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910940872300.png)  
Coloque\-as no seu site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910940872300.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910944336400.png)  
Lembre\-se que os scripts sempre estão no final do HTML e o link dentro do head\.
9. Para a navbar, pegaremos um template do Bootstrap e colocaremos no site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910947343900.png)  
Construindo uma navbar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910950821300.png)  
CSS da navbar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910952833800.png)  
__z\-index__ é a posição da tela, enquanto mais alto, mais “por cima” dos itens vão ficar, depois disso vamos deixar a posição dela fixa no topo e deixar um gradiente de cor de fundo dela, não esqueça de criar uma classe com a letra que escolheu:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910954841200.png)
10. Agora, vamos criar a tela de produtos\. Criaremos uma DIV com o id produtos e dentro dela, colocar um card várias vezes, cada card irá representar um produto:			  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910956853700.png)  
Depois disso crie um CSS para poder visualizar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910958861500.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910960871000.png)
11. E o resultado destas linhas no CSS é:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910963025600.png)
12. Agora, para finalizar a aula, o aluno deverá ter que colocar os diferentes produtos e tentar se ambientar o máximo possível com o conceito de DIVs e se localizar no card\. Não se esqueça de enviar para o Github a matéria da aula de hoje:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290910965821400.png)  


Recursos

- Git, Chrome e VS Code\.

Observação

- Caso os alunos perguntem algo sobre como funciona tal coisa, ou quero estilizar tal coisa, SEMPRE, mesmo sabendo a resposta, é recomendado dizer: Não sei vamos pesquisar, e ensinar ele a pesquisar exemplo: “como centralizar uma DIV” e ir abrindo os stack overflow \- é um site de perguntas e respostas para profissionais e entusiastas na área de programação de computadores\. É extremamente importante que os alunos se sintam confiantes em jogar as dificuldades no Google para achar as soluções, principalmente porque a ideia de usar o Github é estimulá\-los a continuar os projetos em casa\.
- Dica: muito provavelmente, para os alunos, será um bom desafio, sempre ajude\-os quando as fases começarem a ficar difíceis, mostre tentativas erradas na lousa e construa com eles a solução “fingindo resolver” com eles\.

Tarefas

- Dar__ git pull __no projeto e tentar customizar ainda mais os cards do produto\. Não se esqueça de salvar no Github após as atualizações\.

