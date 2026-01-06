# __PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária:  Basic 2

Tipo da atividade: Online

Ferramenta\(s\): GDevelop baixado no computador

	                                

Conteúdos

-  GDevelop: Jogo da Nave\.

Objetivos

- Trabalhar lógica de programação\.

Estratégias e atividades

- Estarei disponibilizando um arquivo contendo os recursos gráficos \(assets\)\. Coloque nos computadores dos alunos:  [https://drive\.google\.com/file/d/1MSqG6zNTi9DqXjT0Vbu57GH1Z3sI4JRL/view?usp=drive\_link](https://drive.google.com/file/d/1MSqG6zNTi9DqXjT0Vbu57GH1Z3sI4JRL/view?usp=drive_link)
- Iniciaremos a implementação de um efeito em nosso jogo, com o propósito de conferir a ilusão de movimento ao fundo\. Este efeito é conhecido como "Offset"\.
	- Abra a programação da Fase 1;
	- Add > Event Group;
	- Action;
	- Fundo > Y offset;  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696928767900.png)  


- Procederemos com a configuração que permitirá o deslocamento do nosso personagem pelo mapa\. Para realizar este processo, é necessário acessar a seção "Behavior" e selecionar a opção "Top\-down movement"\.
	- Lembre\-se de tirar o Rotate\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697022783400.png)  


- Vamos implementar a funcionalidade de disparo para o nosso __personagem__\. Para isso, adicionaremos a mesma “Behavior” que empregamos em nossa última aula, ou seja, o comportamento "Fire Bullet"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697024790700.png)  


- Abra a programação da fase\. Na programação, vamos programar para que, ao pressionar a tecla de espaço, ocorra um único disparo, do projétil\.
	- Add > Event Group > Tiro;
	- Add a new event > Add Condition;
	- Key pressed > Space;
	- Trigger Once;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697026783700.png)

- 
	- Action;
	- Player > Fire bullet toward an angle;
	- 1: Onde a bala vai ser spawnada;
	- 2: Objeto que vai ser a bala;
	- 3: Ângulo que a bala vai sair e velocidade\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)  


- Será necessário fazer com que os inimigos apareçam pelo mapa de forma contínua\. Para isso, precisamos estabelecer um temporizador, onde, se o tempo exceder determinado segundos, ele será reiniciado, criando, assim, inimigos de forma aleatória\.
	- Add > Event Group > Enemy;
	- Add condition;
	- Value of a scene timer;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)

- 
	- Add action;
	- Inimigo1 > Create an object;
	- 1: Ele spawnar em um posição aleatória entre 0 a 1500;
	- 2: Ele aparece acima do mapa, em uma posição que não é visível aos jogadores, a fim de criar a sensação de que ele surgiu de cima;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)

- 
	- Se reproduzirmos o jogo, notamos que nada ocorrerá, pois nosso adversário está sendo gerado, contudo, ele surge no topo do mapa\. Necessitamos adicionar uma força a ele para promover seu movimento;
	- Add action;
	- Inimigo1 > Add a force \(angle\);

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)

- 
	- Vamos reiniciar o timer;
	- Add Action;
	- Start \(or reset\) a scene timer;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)  


- Se realizarmos um teste no jogo, será evidente que ele não funcionará corretamente\. É necessário que o cronômetro seja acionado assim que o jogo se inicia\.
	- Add new Event;
	- Add condition;
	- At the beginning of the scene;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)

- 
	- Add Action;
	- Start \(or reset\) a scene timer\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697077395100.png)

- Concluído\. Neste momento, nosso inimigo está sendo gerado e locomovendo\-se\.  
  


  
  
  
  


- Se observarmos atentamente, notamos que precisamos realizar a mesma programação tanto para o inimigo 2 quanto para os asteroides\. Portanto, é possível utilizar a combinação de teclas CTRL \+ C e CTRL \+ V\. Será necessário apenas efetuar a alteração dos objetos correspondentes\.
	- Clique no começo;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697093074200.png)

- 
	- CTRL \+ C e CTRL \+ V;
	- Mude os nomes;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697093074200.png)

- 
	- Faremos a mesma coisa pro asteroide;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697093074200.png)

- 
	- Modifique os parâmetros relacionados aos segundos de maneira a evitar a geração simultânea de todos os elementos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697100262800.png)

- Agora procederemos à implementação de uma funcionalidade na qual, ao ocorrer o contato do projétil com os inimigos e os asteroides, o projétil será removido, bem como os inimigos e asteroides\.
	- Add > Event Group > Destruição;
	- Add condition;
	- Tiro > Collision > Inimigo1;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697100262800.png)

- 
	- Add action;
	- Inimigo1 > Delete;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697100262800.png)

- 
	- Delete o tiro também\.
- Utilizaremos a mesma coisa do CTRL \+ C e o CTRL \+ V\. Apenas vamos mudar os valores\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697106291100.png)

- Agora, é necessário implementar a funcionalidade na qual o jogo será reiniciado quando um asteroide ou inimigo entrar em contato com o jogador\.
	- Add > Event group > Reiniciar;
	- Add new event;
	- Add condition;
	- Player > Collision > Inimigo1;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697108298900.png)

- 
	- Add action;
	- Change the scene > Fase1;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697108298900.png)

- Utilizaremos a mesma coisa do CTRL \+ C e o CTRL \+ V\. Apenas vamos mudar os valores\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697108298900.png)

Recursos

- GDevelop, internet, Google e computador\.

Observação

- Caso os alunos terminem a atividade, solicite que eles criem uma tela de derrota\.

Tarefas

- Em sua residência, tente recriar o jogo que desenvolvemos durante nossa atividade em sala de aula, mas substitua as sprites\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/Onedrive\.

