# __PLANO DE AULA__

Aula 09 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): S4A instalado no computador

Conteúdos

- Aprendendo sobre o S4A\.

Objetivos

- Download do S4A;
- Conhecer a plataforma;
- Lógica de programação\.

  


Estratégias e atividades

- Hoje vamos aprender uma nova plataforma: o S4A, ela servirá para programarmos os componentes de robótica\.
- Link para download > [https://s4a\.cat/](https://s4a.cat/)
- Siga o passo a passo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774241790400.png)

- Inicie o programa e familiarize\-se com sua interface\. Observe que o programa realiza uma busca por uma placa\. Essa placa se chama Arduino\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774241790400.png)

- Sobre o Arduino:
	- Imagine que o Arduino é como um ‘cérebrozinho’ que pode ajudar a fazer coisas interessantes acontecerem\. É como se fosse um super herói que você pode programar para fazer o que quiser\!

Então, o Arduino é um pequeno computador que você pode programar para acender luzes, fazer um robô se mover, ou até mesmo medir a temperatura\. É como se fosse um controlador mágico que você pode ensinar a fazer truques legais usando a linguagem de programação\.

As pessoas gostam de usar o Arduino para criar coisas incríveis, como brinquedos que se movem sozinhos, termostatos inteligentes que ajustam a temperatura da casa e até mesmo máquinas de fazer música\! É uma maneira divertida de aprender sobre eletrônica e programação enquanto faz coisas legais acontecerem no mundo real\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774241790400.png)

- Abra o Google e instale o firmware:
	- Firware: É um software que você precisa instalar em sua placa Arduino para poder se comunicar com ela a partir do S4A\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774258368400.png)

- Após a conclusão da instalação do firmware, será gerado um arquivo que deve ser aberto por meio do software Arduino disponível em: https://www\.arduino\.cc/\. 
	- Iniciando o programa, conecte a placa do Arduino na porta USB e execute o código correspondente\.
	- Abra o S4A e veja se sumiu aquela mensagem do começo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774259739400.png)

- Agora vamos nos familiarizar com os blocos, no lado esquerdo da tela\.
	- Para manter a paleta organizada e fácil de usar, ela está dividida em nove grupos de blocos, juntamente com um botão de extensões: Movimento, Aparência, Som, Eventos, Controle, Sensores, Operadores, Variáveis e Caneta\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774263756200.png)

- Vamos começar com a montagem\.
	- A perninha \(terminal\) maior do LED está no número 13 e a perna menor está no GND\. Monte desta forma;
	- Veja esse vídeo para entender melhor de como funciona um LED: [https://www\.youtube\.com/shorts/EJdhIrF5dx0](https://www.youtube.com/shorts/EJdhIrF5dx0)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774263756200.png)

- Muito bem, agora vamos para a parte da programação, que irá fazer com que o LED acenda\.
	- Abra o Controle e pegue o bloco “Quando bandeira clicada”\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774267328000.png)

- O Digital 13 irá ficar ligado\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774269338800.png)

- Clique na bandeira\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774272084500.png)

- Agora, para fazer o LED ligar e desligar, é só brincar um pouco com o jeito como o programa está escrito\.
	- Ligue a porta 13;
	- Espere 1 segundo;
	- Desligue a porta 13\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774276074800.png)

- Agora iniciaremos a montagem de um semáforo se baseando no que aprendemos até agora:

A montagem deve ser feita desta forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774277071500.png)

-  O código será relativamente simples; a cada intervalo de tempo, um LED será desligado enquanto o outro é aceso, criando um padrão de alternância\. 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774280076700.png)

