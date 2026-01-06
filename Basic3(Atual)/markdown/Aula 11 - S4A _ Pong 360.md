# __\-PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): S4A instalado no computador

Conteúdos

-  Pong 360\.

Objetivos

- Lógica de programação\.
- Na aula de hoje, nos dedicaremos à criação do renomado jogo Pong\. Este conteúdo poderá ser dividido em duas partes caso necessário\.

Estratégias e atividades

Antes de entrarmos nos detalhes, vamos definir o que estamos estudando: o joystick analógico\.

O que é um joystick analógico?

Um joystick analógico é um dispositivo de entrada comum em jogos, simuladores e outras aplicações que exigem controle preciso e contínuo\. Ele permite que os usuários movam um cursor ou indicador na tela com diferentes graus de precisão, dependendo da força e da direção da pressão aplicada no joystick\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774470578300.png)					![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774471548700.png)

Vamos fazer primeiro a montagem do circuito:

FOTO DO CIRCUITO

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774473549600.png)

Analagico 1 

- Gnd \- Ligar no Gnd do arduino
- \+5v \-  Ligar no \+5v do arduino
- Vrx \-  Ligar no A0 do arduino
- Vry \-  Ligar no A1  do arduino
- Sw \- Não utilizar

Analagico 2

- Gnd \- Ligar no Gnd do arduino
- \+5v \-  Ligar no \+5v do arduino
- Vrx \-  Ligar no A2 do arduino
- Vry \-  Ligar no A3  do arduino
- Sw \- Não utilizar

Led

- Colocar 4 leds em uma protoboard
- Conectar um fio macho\-macho no Gnd do arduino e outro na linha azul da protoboard
- Cada led vai ter um fio que sai da linha azul e conecta na perna negativa 
- Cada led vai ter um fio que liga a porta digital na sua perna positiva

Dica 

- Use leds de cores diferentes para o jogador 1 \(Porta 13 e 12 \) e para o jogador 2 \(Porta 11 e 10\)\.

Vamos criar todas as variáveis do nosso projeto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774475550700.png)

__j1 e j2 point__ = Variável que guarda um valor Verdadeiro ou Falso \(Fez um gol ou não\)

__Player 1 e 2__ = Variável que guarda a pontuação dos players

__Winpoint__ = Variável que guarda o máximo de pontos que deve ser feito para ganhar

__Speed __= Variável que guarda a velocidade da bola 

__joystick 1 e 2__ = Variável que guarda o valor do componente joystick que é passado através das portas analogicas

Vamos agora programar nosso arduino:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774475550700.png)

Aqui usamos as variáveis joystick para captar o valor que vem de analog 0 e 2 sendo assim possível controlar o player 1 e 2 com o joystick\. Também estamos desligando todos os leds do circuito\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774475550700.png)

Aqui estamos estabelecendo as regras de quando deve ser aceso os leds, por exemplo: quando o jogador 1 faz ponto a variável __j1\_point__ se torna __true __a variável__ Player 1 se torna = 1__ fazendo com que o led da porta 13 acenda e assim por diante\.

Agora vamos programar nosso player 1 e 2

Player 1 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774481282900.png)

Programação player 1

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774481282900.png)

Player 2 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774481282900.png)

Programação player 2

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774481282900.png)

Nas programações dos player 

- Definimos suas posições iniciais e seu tamanho 
- E depois fizemos a lógica da movimentação do jogador

Agora vamos para os gol’s\. 

Eles são apenas os sprites não tem programação

Gol do jogador 1

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774486731100.png)

Gol do jogador 2

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774489005200.png)

Por último, vamos para a programação da bola\.

Crie uma bola ou pegue um asset pronto na plataforma\.

Agora vamos para a programação da bola\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774489005200.png)

Nesta programação 

- Definimos o valor de todas as variáveis que criamos 
- Sorteamos a direção da bola 
- Redefinimos a direção da bola caso ela toque no player
- É feita a lógica de som e pontos caso nenhum dos jogadores tenha ganhado ainda\.

E no final você pode posicionar as coisas dessa maneira\.

- Gol atrás dos respectivos players
- Bola ao centro da tela 
- Placar nas extremidades superiores

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774491328200.png)

Recursos

- S4A instalado, internet e computador\.

Observação

- Nada a observar\.

Tarefas

- Sem tarefa\.

