# __PLANO DE AULA__

Aula 03 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- CSS, o que é e para que serve\.

Objetivos

- Introdução à CSS e como estilizar um site;
- Aprendendo a pegar fontes do Google\.

Estratégias e atividades

- Estilizar o site da aula passada e aprender sobre CSS\.
- Entender como funcionam as pastas\.
- prender sobre novas tags HTML: A
	- __<link rel="stylesheet" href="\./linkProCSS">__

1. Hoje nós começaremos tendo 2 arquivos e 2 pastas, para assim organizarmos melhor o código\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600492337700.png)
2. Vamos entender o que é CSS e como ele funciona:
	1. O CSS nada mais é que a aparência do site\. Ele não muda a programação do site\. O que é realmente importante sobre o CSS, é que ele vai alterar as aparências e posições das coisas que colocamos em um site\. Com o CSS é possível estilizar o site\. Para isso, o CSS utiliza de 3 tipos de seletores \(opções\): os __IDs__, as __classes__, e o __nome das tags__\.
3. Vamos entender antes de como o CSS funciona, o porque organizamos ele em 3 arquivos diferentes\. Existe, em sites, um padrão a ser seguido por todo o site\. Existem cores e templates que precisam ser de uma página só e por isto nós temos o __global\.css__, que será para as 2 páginas que temos \(index\.html e comidas\.html\)\. Criaremos um CSS para cada tela, com os nomes *comidas\.css* e *index\.css*\.
4. Agora, vamos começar estilizando o global\.css:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600494339500.png)  
É importante entender que quando colocamos o nome da tag HTML no CSS, nós começamos estilizando o CSS do body, onde o corpo do site será preto e a letra branca\. Já os links agora são brancos, não tem mais a parte sublinhada e mudamos também o tamanho da letra\.
5. O __a:hover\{\}__ significa que quando o mouse passar em cima da tag algo irá acontecer\. Neste caso colocamos a cor da letra em RGB \(red, green, blue\), O RGB é a mistura dessas 3 cores que se transforma em uma nova, o VS Code deixa você customizar a cor se passar o mouse em cima do quadradinho com a cor:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600496340000.png)
6. Para usar este CSS, é preciso puxar o arquivo:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600499361500.png)  
Repare que a tag ‘link’ vai estar puxando o CSS do global e do index\.css\.
7. Agora, vamos customizar ainda mais o index\.html\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600500361100.png)  
Repare que adicionamos uma nova tag chamada* <div>*, porém ela tem um atributo novo\. Chamamos de atributo tudo que fica dentro da tag\. Exemplo: <h1 atributo1=”azul” atributo2=”tomate”>

  
O atributo __id=””__ deve conter dentro dele um nome único\. Fazendo com que seja apenas esta DIV chamada no CSS\. É como o CPF ou a sua identidade: deve ser única\.

1. CSS do index\.css:   
Diminuindo o tamanho da imagem, e agora vamos à etapa nova\.

O __\#__ no CSS significa que depois disso temos nome do ID criado\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600503360700.png)  
  
Explicando o CSS da DIV:

O link ficará na posição sempre fixa, com 0 pixels no topo, também 0 na direita, e o link terá um preenchimento de 10 pixels para dentro\. Lembrando que a diferença de padding e margin, é que padding é para dentro da DIV, já margin é para fora:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600504363800.png)

1. E o resultado destas duas estilizações é:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600505361700.png)
2. O CSS do comidas\.css é assim:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600508360900.png)
3. Não podemos esquecer de colocar o ID na DIV e importar o CSS:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600509359800.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600510362200.png)
4. E o resultado das imagens é:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600511361100.png)
5. Agora salvando e enviando para o Github:  
Lembre\-se Sempre que o aluno, em toda aula, precisa colocar os seguintes comandos:  
*git config —global user\.name “nomeDoGithub”  
git config —global user\.email “emailDoGithub”*  
  
Para poder poder commitar com o nome do aluno:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600513361900.png)

Recursos

- Git\. Chrome e VS Code\.

Observação

- Caso os alunos perguntem algo sobre como funciona tal coisa, ou quero estilizar tal coisa, SEMPRE, mesmo sabendo a resposta, é recomendado dizer: Não sei vamos pesquisar, e ensinar ele a pesquisar exemplo: “como centralizar uma DIV” e ir abrindo os stack overflow \- é um site de perguntas e respostas para profissionais e entusiastas na área de programação de computadores\. É extremamente importante que os alunos se sintam confiantes em jogar as dificuldades no Google para achar as soluções, principalmente porque a ideia de usar o Github é estimulá\-los a continuar os projetos em casa\.

Tarefas

- Nesta aula a tarefa é o aluno procurar em casa sites com CSS incríveis e conversar sobre a pesquisa na próxima aula\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

