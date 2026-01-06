# __ PLANO DE AULA__

Aula 13 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): S4A instalado no computador

Conteúdos

- Servo motor\.

Objetivos

- Lógica de programação;
- Aprender novos componentes\.

Estratégias e atividades

- Hoje vamos aprender sobre o servo motor, que é como o "músculo" de um robô ou de outros brinquedos que se movem\. Imagina que você tem um amigo robô, e ele precisa levantar o braço quando você aperta um botão no controle\. O servo motor é o que ajuda o braço do robô a ir para cima quando você quer, e parar quando você diz "chega"\.
	- A maioria dos servo motores funciona com uma faixa específica de tensão, como 4\.8V a 6V, por exemplo\.
	- A maioria dos servo motores padrão pode girar em torno de 180 graus\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774652712100.png)

- Vamos começar a montagem, identificando os pinos: positivo, negativo e o pino 8\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774656733100.png)

- Agora, configuraremos a lógica para que, ao pressionar a tecla "A", o servo motor pare; ao pressionar a tecla "B", ele gire no sentido horário; e ao pressionar a tecla "C", ele gire no sentido anti\-horário\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774659579300.png)

- Ótimo, concluído o exercício anterior, você pode apagar toda programação\! Isso foi um teste \(risos\)\.
- Na nova programação, atribuímos um ângulo específico ao servo motor, de modo que ele se ajustará ao ângulo fornecido em resposta à instrução dada\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774661579300.png)

- 
	- Lembre\-se de que o servo motor pode atingir um ângulo de até 180 graus\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774663458200.png)

- A seguir, utilizaremos o potenciômetro para que ele possa controlar o ângulo do servo motor\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774665458700.png)

- Antes de começar, criaremos duas variáveis: uma chamada "sensor" e outra chamada "Angulo"\.
	- A variável "sensor" sempre capturará o valor em que o potenciômetro se encontra;
	- A variável "Angulo" será responsável por arredondar os valores capturados pelo sensor;
	- Por fim, o servo motor sempre utilizará as informações contidas na variável "Angulo"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774667457100.png)

Recursos

- S4A instalado, Servo Motor, internet e computador\.

Observação

- Não há observação\.

Tarefas

- Veja este video: [https://www\.youtube\.com/watch?v=VitG0Sq6kNY](https://www.youtube.com/watch?v=VitG0Sq6kNY)

