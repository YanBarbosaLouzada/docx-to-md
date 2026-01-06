# __PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 1

Tipo da atividade: Offline 		

Ferramenta\(s\): Protoboard, Resistores, Botão, leds, jumpers e Arduino\.

Conteúdos

- Genius\.

Objetivos

- Trabalhar com coordenação motora\.
- Montar um jogo com componentes eletrônicos

Estratégias e atividades

- O Genius é um brinquedo muito popular com uma ideia muito simples: Memorizar a ordem das cores\. 
- O jogo consiste em 4 botões coloridos que piscam formando uma sequência que aumenta a cada rodada\. Na primeira rodada, um botão qualquer pisca e o jogador deve apertar o botão que piscou\. Na próxima rodada o primeiro botão pisca novamente junto de outro botão qualquer\. Dessa forma, o usuário deve memorizar a sequência dos botões e pressioná\-los na ordem correta para avançar para o próximo nível\. A cada etapa a sequência aumenta e o objetivo é memorizar a maior sequência possível\.
- __O que é uma Protoboard?__
	- A protoboard é uma placa que facilita a montagem dos circuitos eletrônicos\. Ela possui vários furos onde podem ser encaixados LEDs, Resistores, fios e muitos outros componentes\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543592435800.png)

- __O que são Resistores?__
	- Os resistores são componentes eletrônicos que protegem os outros componentes\. Algumas vezes a energia que usamos em um circuito é muito forte para ligar um LED, por exemplo\. Para evitar que ocorra um acidente, podemos utilizar resistores para pegar um pouco da energia e proteger os LEDs\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543598200600.png)

- __O que é um Botão?__
	- Assim como o interruptor das lâmpadas de nossos quartos, os botões servem para ligar ou desligar luzes, motores, alarmes, sensores e muitos outros componentes\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543604222600.png)

- __O que são LEDs?__
	- Os LEDs são componentes que, assim como as lâmpadas, brilham e emitem luz\. Eles podem ser de várias cores, várias intensidades e vários tamanhos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543606231300.png)

- O que são Jumpers?
	- Os Jumpers são pequenos fios que podem ser encaixados em componentes e nas protoboards\. Eles facilitam a montagem dos circuitos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543616012600.png)

- O que é Arduino?
	- O Arduino é um pequeno controlador que pode ser programado\. Ele é capaz de controlar luzes, alarmes, motores, sensores e até mesmo outro arduino\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543647624600.png)

- __PROFESSOR:__ Instrua aos estudantes que realizaremos a criação de um clone do jogo Genius\. Para facilitar o processo, monte o circuito disponibilizado a seguir:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543655656800.png)

- __PROFESSOR:__ O código utilizado para esse jogo:

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\*  Jogo 3 \- Jogo Genius

\*  Criado por: [https://meetarduino\.wordpress\.com](https://meetarduino.wordpress.com)

\*  https://www\.tinkercad\.com/things/lXYHk11zZsK\-jogo\-da\-memoria\-jogo\-3

\*  Adaptado por: Angelo Luis Ferreira

\*

\*       http://squids\.com\.br/arduino

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

//Vamos começar definindo as notas para os sons

\#define NOTE\_D4  294

\#define NOTE\_G4  392

\#define NOTE\_A4  440

\#define NOTE\_A5  880

 

// criando o array para os 4 sons para sortear um som

int tons\[4\] = \{ NOTE\_A5, NOTE\_A4, NOTE\_G4, NOTE\_D4 \};

// Nossa sequência de até 100 itens vai começar vazia\.

int sequencia\[100\] = \{\};

// Indica a rodada atual que o jogo se encontra\.

int rodada\_atual = 0;

// Indica o passo atual dentro da sequência, é usado enquanto a sequência

// está sendo reproduzida\.

int passo\_atual\_na\_sequencia = 0;

 

/\*

 \* Indica o pino de áudio, leds e botões\.

 \* Os pinos de leds e botões estão em ordem, relacionados uns aos outros, ou

 \* seja, o primeiro led está relacionado ao primeiro botão\. A ordem destas

 \* sequências também estão relacionadas a ordem dos tons\.

 \*/

int pinoAudio = 12;

int pinosLeds\[4\] = \{ 2, 4, 6, 8 \};

int pinosBotoes\[4\] = \{ 3, 5, 7, 9 \};

 

// Indica se um botão foi pressionado durante o loop principal\.

int botao\_pressionado = 0;

// Flag indicando se o jogo acabou\.

int perdeu\_o\_jogo = false;

 

void setup\(\) \{

  // Definindo o modo dos pinos dos Leds como saída\.

  for \(int i = 0; i <= 3; i\+\+\) \{

    pinMode\(pinosLeds\[i\], OUTPUT\);

  \}

 

  // Definindo o modo dos pinos dos Botões como pullup interno\.

  for \(int i = 0; i <= 3; i\+\+\) \{

    pinMode\(pinosBotoes\[i\], INPUT\_PULLUP\);

  \}

 

  // Definindo o modo do pino de Áudio como saída\.

  pinMode\(pinoAudio, OUTPUT\);

 

  // Inicializando o random através de uma leitura da porta analógica\.

  // Esta leitura gera um valor variável entre 0 e 1023\.

  randomSeed\(analogRead\(0\)\);

\}

 

void loop\(\) \{

  // Se perdeu o jogo reinicializamos todas as variáveis\.

  if \(perdeu\_o\_jogo\) \{

    int sequencia\[100\] = \{\};

    rodada\_atual = 0;

    passo\_atual\_na\_sequencia = 0;

    perdeu\_o\_jogo = false;

  \}

 

  // Toca um som de início para anúnicar que o jogo está começando quando é a primeira rodada\.

  if \(rodada\_atual == 0\) \{

    tocarSomDeInicio\(\);

    delay\(500\);

  \}

// Chama a função que inicializa a próxima rodada\.

  proximaRodada\(\);

  // Reproduz a sequência atual\.

  reproduzirSequencia\(\);

  // Aguarda os botões serem pressionados pelo jogador\.

  aguardarJogador\(\);

 

  // Aguarda 1 segundo entre cada jogada\.

  delay\(1000\);

\}

 

// Sorteia um novo item e adiciona na sequência\.

void proximaRodada\(\) \{

  int numero\_sorteado = random\(0, 4\);

  sequencia\[rodada\_atual\+\+\] = numero\_sorteado;

\}

 

// Reproduz a sequência para ser memorizada\.

void reproduzirSequencia\(\) \{

  for \(int i = 0; i < rodada\_atual; i\+\+\) \{

    tone\(pinoAudio, tons\[sequencia\[i\]\]\);

    digitalWrite\(pinosLeds\[sequencia\[i\]\], HIGH\);

    delay\(500\);

    noTone\(pinoAudio\);

    digitalWrite\(pinosLeds\[sequencia\[i\]\], LOW\);

    delay\(100\);

  \}

  noTone\(pinoAudio\);

\}

 

// Aguarda o jogador iniciar sua jogada\.

void aguardarJogador\(\) \{

  for \(int i = 0; i < rodada\_atual; i\+\+\) \{

    aguardarJogada\(\);

    

  // verifica a jogada  

  if \(sequencia\[passo\_atual\_na\_sequencia\] \!= botao\_pressionado\) \{

      gameOver\(\); // perdeu

   \}

   

   // para o jogo se perdeu

    if \(perdeu\_o\_jogo\) \{

      break;

    \}

     passo\_atual\_na\_sequencia\+\+;

  \}

 

  // Redefine a variável para 0\.

  passo\_atual\_na\_sequencia = 0;

\}

 

void aguardarJogada\(\) \{

  boolean jogada\_efetuada = false;

  while \(\!jogada\_efetuada\) \{

    for \(int i = 0; i <= 3; i\+\+\) \{

      if \(\!digitalRead\(pinosBotoes\[i\]\)\) \{

        // Dizendo qual foi o botao pressionado\.

        botao\_pressionado = i;

 

        tone\(pinoAudio, tons\[i\]\);

        digitalWrite\(pinosLeds\[i\], HIGH\);

        delay\(300\);

        digitalWrite\(pinosLeds\[i\], LOW\);

        noTone\(pinoAudio\);

 

        jogada\_efetuada = true;

      \}

    \}

    delay\(10\);

  \}

\}

 

void gameOver\(\) \{

    // GAME OVER\.

    for \(int i = 0; i <= 3; i\+\+\) \{

      tone\(pinoAudio, tons\[i\]\);

      digitalWrite\(pinosLeds\[i\], HIGH\);

      delay\(200\);

      digitalWrite\(pinosLeds\[i\], LOW\);

      noTone\(pinoAudio\);

    \}

 

    tone\(pinoAudio, tons\[3\]\);

    for \(int i = 0; i <= 3; i\+\+\) \{

      digitalWrite\(pinosLeds\[0\], HIGH\);

      digitalWrite\(pinosLeds\[1\], HIGH\);

      digitalWrite\(pinosLeds\[2\], HIGH\);

      digitalWrite\(pinosLeds\[3\], HIGH\);

      delay\(100\);

      digitalWrite\(pinosLeds\[0\], LOW\);

      digitalWrite\(pinosLeds\[1\], LOW\);

      digitalWrite\(pinosLeds\[2\], LOW\);

      digitalWrite\(pinosLeds\[3\], LOW\);

      delay\(100\);

    \}

    noTone\(pinoAudio\);

 

    perdeu\_o\_jogo = true;  

\} 

  

 

void tocarSomDeInicio\(\) \{

  tone\(pinoAudio, tons\[0\]\);

  digitalWrite\(pinosLeds\[0\], HIGH\);

  digitalWrite\(pinosLeds\[1\], HIGH\);

  digitalWrite\(pinosLeds\[2\], HIGH\);

  digitalWrite\(pinosLeds\[3\], HIGH\);

  delay\(500\);

  digitalWrite\(pinosLeds\[0\], LOW\);

  digitalWrite\(pinosLeds\[1\], LOW\);

  digitalWrite\(pinosLeds\[2\], LOW\);

  digitalWrite\(pinosLeds\[3\], LOW\);

  delay\(500\);

  noTone\(pinoAudio\);

\}

- __PROFESSOR__: Lembrando que, nessa aula, os alunos não farão a escrita do código\.

Recursos

- Protoboard, Resistores, Botão, leds, jumpers e Arduino\.

Tarefas

- Não a tarefas\.

