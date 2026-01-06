# __PLANO DE AULA__

Aula 10 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): S4A instalado no computador

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774342118500.png)

Conteúdos

-  Push Button / Resistor

Objetivos

- Lógica de programação;
- Conhecer os componentes\.

  


Estratégias e atividades

Na aula de hoje, iniciaremos a montagem de um circuito com o push button, mas primeiro precisamos saber o que é um Push Button

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774342118500.png)

Um "push button" \(ou botão de pressão\) é um dispositivo de comutação que ativa ou desativa um circuito elétrico quando pressionado\. Eles são amplamente usados em vários dispositivos eletrônicos e sistemas para executar uma variedade de funções, desde acender luzes até iniciar motores ou ativar outras operações\.

O que é um resistor? 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774358385000.png)

Um resistor é um componente eletrônico que limita ou regula o fluxo de corrente elétrica em um circuito\. Ele é uma parte fundamental de muitos circuitos elétricos e eletrônicos, desempenhando várias funções importantes, como controlar a corrente, dividir a tensão, ajustar sinais e proteger componentes sensíveis\.

Depois de ter explicado cada um dos componentes, o professor deve começar a montagem do circuito\.

Programando arduino\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774359394200.png)

1° Bloco de Programação

- Precisamos criar uma variável chamada button que servirá para verificar se o botão está ou não pressionado\.\(Esta variável pega o valor que vem do digital2 \)

Programando morcego\.

- Pegue o morcego na loja de asset\. 
- Arraste o morcego para canto esquerdo da tela 
- Clique na Aba __Trajes__ e depois em "__Importar__\. Pegue a animação que o morcego está com a asa para baixo\.

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774359394200.png)

Programação do morcego

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774364764600.png)

1° Bloco de comando 

- Sempre que a variável botão for igual a 1 o morcego muda a animação

2° Bloco de comando 

- Sempre que a variável botao for igual a 1 o morcego sobe 3 unidades para cima, se não vai \-3 unidades para baixo

3° Bloco de Comando 

- Sempre que o morcego colidir com um espinho ele vai parar o jogo

Criando espinho

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774364764600.png)

Dica tire todo o zoom da tela de desenho e faça igual a o desenho da imagem

Programação do espinho 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774364764600.png)

1° Bloco de comando 

- O espinho sempre vai começar no canto direito da tela 
- Vamos deixar ele bem grande
- E por último vamos fazer uma lógica para que sempre que a posição do espinho for < que \-238 ele vai voltar para o canto direito da tela e vai sortear a próxima altura, se não o espinha vai em direção ao morcego

2° Bloco de comando 

- Precisamos criar uma variável chamada Score que vai servir para contar nossos pontos 
- Sempre que começar o jogo ela vai ser zero e caso nós passemos por um espinho sem bater ela vai aumentar 1 ponto e esperar 2 segundos \( tempo do espinho ir para a direita da tela novamente\)\.

Pintando palco:

- __Para pintar o palco__ basta clicar nele e depois ir na aba __fundo de tela__ e clicar em __editar__  


Terminamos nosso joguinho\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774364764600.png)

Recursos

- S4A instalado, LEDs, protoboards, internet e computador\.

Observação

Tarefas

- Experimente replicar o código em sua residência, seguindo os passos da aula, e compartilhe o resultado\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

