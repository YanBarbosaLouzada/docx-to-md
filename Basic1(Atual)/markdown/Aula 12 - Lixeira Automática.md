# __PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 1

Tipo da atividade: Offline 		

Ferramenta\(s\): Sensor ultrassônico, servo motor, caixa, tampa, fita ou cola quente, fio dental, Arduino e um pesinho\.

Conteúdos

- Lixeira\.

Objetivos

- Trabalhar com coordenação motora;
- Aprender novos componentes\.

Estratégias e atividades

- O que é um Sensor Ultrassônico?
	- Um sensor ultrassônico é como um "ouvinte mágico" que usa ondas sonoras que não conseguimos ouvir para medir distâncias\. É como um amigo que consegue dizer a que distância algo está dele, usando sons que são como ecos mágicos\. Podemos usá\-lo para criar objetos inteligentes que "sentem" o mundo ao seu redor\!

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543863671900.png)

- O que é um Servo Motor?
	- Um servo motor é como um braço robótico pequenino que pode se mover para onde quisermos\. É como um assistente pessoal que obedece aos nossos comandos e pode girar de um lado para o outro\. Podemos usá\-lo para fazer nossos projetos se movimentarem de maneiras legais e divertidas\!

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543867685400.png)

- O que é o Arduino?
	- O Arduino é como um cérebro mágico para inventores, permitindo que eles criem projetos eletrônicos incríveis sem precisar serem expertos em magia \(ou programação\)\.
- O mundo mágico do Arduino:
	- Coração Eletrônico: O Arduino é como o coração de muitos projetos mágicos\. Ele pode entender e seguir comandos especiais, fazendo coisas surpreendentes acontecerem\.
	- Código Mágico: Para dar vida ao Arduino, usamos um código mágico\. É como um conjunto de instruções que diz ao Arduino o que fazer\. Você pode pensar nisso como poções mágicas que dão vida às nossas invenções\.
	- Amigo dos Componentes: O Arduino ama trabalhar com outros componentes eletrônicos\. Sensores, luzes, motores \- todos podem ser amigos do Arduino e juntos criar algo extraordinário\.
	- Conectividade Mágica: O Arduino pode se conectar ao nosso computador, permitindo\-nos enviar novos comandos e atualizar nossas invenções com ainda mais magia\.
- Porque é importante:
	- Invenções Personalizadas: Com o Arduino, podemos criar nossas próprias invenções personalizadas\. Desde robôs até luzes controladas por gestos, o céu é o limite\!
	- Aprendizado Mágico: É uma ferramenta mágica para aprender sobre eletrônica e programação\. Você pode começar com feitiços simples e, com o tempo, tornar\-se um verdadeiro mestre\.
	- Comunidade de Magos: Muitos inventores compartilham seus códigos e ideias, formando uma comunidade mágica que ajuda uns aos outros a realizar projetos incríveis\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702543873700800.png)

\.

- __PROFESSOR:__ Instrua aos estudantes que realizaremos a criação de uma lixeira\. Para facilitar a compreensão do circuito, disponibilizarei um vídeo para o professor:
	- __OBS\.:__ Faça a montagem do circuito nessa aula\.
	- __OBS\.: __O código está na observação ao final da página\.
	- [https://www\.youtube\.com/watch?v=g32x\-fCgWKU](https://www.youtube.com/watch?v=g32x-fCgWKU)
- __PROFESSOR: __Reproduza o que foi ensinado no vídeo sobre a Lixeira\. Lembre\-se de que não é necessário criar o código junto com os alunos, apenas explique o que é o Arduino\.

Recursos

- Sensor ultrassônico, servo motor, caixa, tampa, fita ou cola quente, fio dental, Arduino e um pesinho\.

Observação

- Link também do código: [https://github\.com/pontocomdev/Lixeira\_Inteligente/blob/master/LixeiraInteligente\.ino](https://github.com/pontocomdev/Lixeira_Inteligente/blob/master/LixeiraInteligente.ino)

\#include <Servo\.h>   //Biblioteca do Servo Motor

Servo servo;     

int trigPin = 5;    

int echoPin = 6;   

int servoPin = 7;

int led= 10;

long duration, dist, average;   

long aver\[3\];  

void setup\(\) \{       

    Serial\.begin\(9600\);

    servo\.attach\(servoPin\);  

    pinMode\(trigPin, OUTPUT\);  

    pinMode\(echoPin, INPUT\);  

    servo\.write\(0\);         //Inicia com a tampa fechada

    delay\(100\);

    servo\.detach\(\); 

\} 

void measure\(\) \{  

 digitalWrite\(10,HIGH\);

digitalWrite\(trigPin, LOW\);

delayMicroseconds\(5\);

digitalWrite\(trigPin, HIGH\);

delayMicroseconds\(15\);

digitalWrite\(trigPin, LOW\);

pinMode\(echoPin, INPUT\);

duration = pulseIn\(echoPin, HIGH\);

dist = \(duration/2\) / 29\.1;    //Obtem a distancia

\}

void loop\(\) \{ 

  for \(int i=0;i<=2;i\+\+\) \{   //verifica a distancia

    measure\(\);               

   aver\[i\]=dist;            

    delay\(10\);              //adiciona um atraso as medições

  \}

 dist=\(aver\[0\]\+aver\[1\]\+aver\[2\]\)/3;    

if \( dist<50 \) \{

//Mude os valores de acordo com a sua necessidade

 servo\.attach\(servoPin\);

  delay\(1\);

 servo\.write\(0\);  

 delay\(3000\);       

 servo\.write\(150\);    

 delay\(1000\);

 servo\.detach\(\);      

\}

Serial\.print\(dist\);

\}

Tarefas

- Não há tarefas\.

