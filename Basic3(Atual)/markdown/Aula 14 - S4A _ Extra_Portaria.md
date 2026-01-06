# __ PLANO DE AULA__

Aula 13 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): S4A instalado no computador

Conteúdos

- Servo Motor
- Botao

Objetivos

- Lógica de programação;
- Aprender novos componentes\.

Estratégias e atividades

1\. Introdução ao sistema

Explique aos alunos:

- Cada __servomotor__ será uma cancela\.  

- Cada __botão__ será o “porteiro” abrindo a cancela correspondente\.  

- Quando pressionado → a cancela abre  

- Quando solto → a cancela volta a fechar  


Isso imita o funcionamento real\.

2\. Materiais

- Arduino UNO  

- 2 Servos \(SG90 ou similar\)  

- 2 Botões de pressão \(push buttons\)  

- 4 resistores de 10kΩ \(pull\-down\)  

- Protoboard  

- Jumpers  


3\. Montagem dos Servos

__Conexão de cada servo:__

- __Vermelho__ → 5V  

- __Marrom/Preto__ → GND  

- __Amarelo/Laranja \(Sinal\)  
__
	- Servo 1 → Pino 9  

	- Servo 2 → Pino 10  


4\. Montagem dos Botões

Cada botão deve ser ligado assim:

- Um terminal → pino digital  

- Outro terminal → GND  

- Resistor de 10k entre pino digital e GND \(pull\-down\)  


__Pinos sugeridos:__

- Botão 1 → Pino 2  

- Botão 2 → Pino 3![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774759028500.png)

Para o Codigo:

\#include <Servo\.h>  

// Inclui a biblioteca que permite controlar motores do tipo servo,

// que são motores que giram para posições específicas \(como abrir/fechar uma cancela\)\.

Servo cancela1;  

Servo cancela2;  

// Aqui criamos dois "objetos" do tipo Servo, que representarão as duas cancelas\.

int botao1 = 2;  

int botao2 = 3;  

// Definimos que o primeiro botão está ligado na porta digital 2,

// e o segundo botão na porta digital 3 do Arduino\.

void setup\(\) \{

  cancela1\.attach\(9\);

  cancela2\.attach\(10\);

  // Conectamos os servos às portas 9 e 10\.

  // O Arduino precisa saber em qual porta cada motor está ligado\.

  pinMode\(botao1, INPUT\_PULLUP\);

  pinMode\(botao2, INPUT\_PULLUP\);

  // Aqui configuramos os botões como entradas usando "INPUT\_PULLUP"\.

  // Isso significa que:

  // \- Sem apertar o botão → o sinal fica em HIGH \(alto\)\.

  // \- Apertando o botão   → o sinal vai para LOW \(baixo\)\.

  // Isso evita interferência elétrica e facilita a leitura\.

  cancela1\.write\(0\);   // fechada

  cancela2\.write\(0\);   // fechada

  // No início, as duas cancelas são posicionadas em 0 graus, ou seja, fechadas\.

\}

void loop\(\) \{

  // O loop roda o tempo todo repetidamente, sem parar\.

  // IMPORTANTE:

  // Como estamos usando INPUT\_PULLUP, o Arduino entende que:

  // LOW = botão apertado

  // HIGH = botão solto

  if \(digitalRead\(botao1\) == LOW\) \{

    cancela1\.write\(90\);  // abre

    // Se o botão 1 for apertado, a cancela 1 gira para 90 graus \(posição de aberta\)

  \} else \{

    cancela1\.write\(0\);   // fecha

    // Se o botão 1 não estiver apertado, a cancela volta para a posição fechada

  \}

  if \(digitalRead\(botao2\) == LOW\) \{

    cancela2\.write\(90\);  // abre

    // A mesma lógica acima, mas agora para a segunda cancela

  \} else \{

    cancela2\.write\(0\);   // fecha

  \}

\}

Recursos

- S4A instalado, Servo Motor, internet e computador\.

Observação

- Não há observação\.

Tarefas

- Veja este video: [https://www\.youtube\.com/watch?v=VitG0Sq6kNY](https://www.youtube.com/watch?v=VitG0Sq6kNY)

