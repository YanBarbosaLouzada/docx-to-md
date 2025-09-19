# __PLANO DE AULA__

Aula 07 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Animations CSS e Displays\.

Objetivos

- Ensinar os alunos sobre como o mundo real funciona;
- Apresentar o site [https://fonts\.google\.com/](https://fonts.google.com/);
- Conhecer o [https://getbootstrap\.com/docs/5\.3/getting\-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/);
- Usar o [https://color\.adobe\.com/pt/trends](https://color.adobe.com/pt/trends)\.  


Estratégias e atividades

- Estilizar o site da aula passada e aprender sobre posições\.
- Entender como funcionam as pastas\.
- Aprender sobre novas funcionalidades CSS: 
	- Animations;
	- Key streams\.

1. Hoje vamos fazer os sites se moverem com animações lindas\.
2. __Professor:__ separei para você 2 projetos com CSS\. Um com o sistema solar para mostrar para os alunos coisas possíveis com CSS\. O sistema solar é algo difícil, então não é preciso fazer com os alunos, porém como é bonito, olhe e mostre aos alunos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911028480800.png)  
Mostre também projetos do [https://codepen\.io/](https://codepen.io/) que é um site com CSS mirabolantes\.
3. Vamos começar o nosso projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911028480800.png)
4. Neste nosso projeto, existem apenas 3 coisas no HTML: uma DIV de plano de fundo contendo tudo, uma DIV com o carrinho e a última com as nuvens\. Então a estrutura de HTML é extremamente simples:  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911028480800.png)  
5. Agora como funciona para o carro e as nuvens se moverem? Isto tudo é uma mágica do CSS, guarde em mente as seguintes informações:
	1. O ID da pista de corrida;
	2. A classe nuvens e o ID nuvens;
	3. A classe carrinho\-positions e ID carrinho\.
6.  Vamos, agora ver a mágica por baixo dos panos do nosso CSS:
	1. A pista de corrida, nada mais é que uma DIV de fundo que tem um linear gradient que vai se misturar perto de onde o carrinho vai ficar\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911028480800.png)

		  
  
  
Repare também que existem duas coisas extras: o position relative faz com que tudo dentro dela possa usar o espaçamento da DIV pista\-de\-corrida como referência, e o overflow hidden serve para esconder as DIVs do carrinho ou nuvens quando passar da tela\.

- 
	1. Vamos mexer no tamanho das DIVs e bloquear as DIVs de fora do body de poder sair:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911044357800.png)
	2. Agora, como funciona o position relative/absolute, se a DIV que tem outras DIVs dentro for relative, as outras podem usar o espaçamento dela livremente com o position absolute\. Por isso, vamos criar a posição inicial do carrinho e das nuvens:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911046367600.png)  
O top, right, left, e bottom representam a distância de cima, direita, esquerda e baixo \(respectivamente\) da DIV superior, que no caso é a pista de corrida\. 
	3. Porém, agora como irá funcionar essa linha nova chamada animation? Neste caso usaremos duas animações, uma chamada carrinho\-andante  que será linear durará 3 segundos e será infinita\. Já a das nuvens durará 10s para ser completada\. __Professor:__ olhe o site para poder ver mais opções de CSS:  
[https://developer\.mozilla\.org/en\-US/docs/Web/CSS/animation](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)
	4. Para finalizar, vamos entender como funciona a animação:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911047366400.png)  
Quando estiver 0% \(ou 0 segundos\), o left do carrinho começa em \-200px de distância da esquerda, e termina calculando 100% da largura da tela mais 200 pixels pro carrinho sumir, este 100% representa o tempo da animação, então será 3 segundos\. A mesma coisa serve para as nuvens\. Ela deverá ser um desafio pros alunos tentarem fazer sozinho, pois a única coisa que muda é a direção e a distância\. 

1. Agora que já está feito o código, simples, porém bem divertido\. Vamos subir ele no Github\. Lembre\-se SEMPRE de criar um repositório novo para cada projeto diferente\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911049401300.png)

Recursos

- Git Chrome e VS Code\.

Observação

- Caso os alunos perguntem algo sobre como funciona tal coisa, ou quero estilizar tal coisa, SEMPRE, mesmo sabendo a resposta, é recomendado dizer: Não sei vamos pesquisar, e ensinar ele a pesquisar exemplo: “como centralizar uma DIV” e ir abrindo os stack overflow \- é um site de perguntas e respostas para profissionais e entusiastas na área de programação de computadores\. É extremamente importante que os alunos se sintam confiantes em jogar as dificuldades no Google para achar as soluções, principalmente porque a ideia de usar o Github é estimulá\-los a continuar os projetos em casa\.
- Incentive os alunos a procurarem coisas novas no Bootstrap, uma muito legal é Popovers, diga para procurarem em casa como implementar no site\.

Tarefas

- Procurar em sites online no Google CSS de animações lindas\.

