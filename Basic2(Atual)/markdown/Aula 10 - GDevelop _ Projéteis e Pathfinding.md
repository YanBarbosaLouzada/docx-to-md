# __PLANO DE AULA__

Aula 10 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 2

Tipo da atividade: Online

Ferramenta\(s\): GDevelop baixado no computador

	                                

Conteúdos

-  GDevelop Projéteis e Pathfinding\.

Objetivos

- Trabalhar lógica de programação\.

Estratégias e atividades

- Estarei disponibilizando um arquivo contendo os recursos gráficos \(assets\)\. Coloque nos computadores dos alunos:  [https://drive\.google\.com/file/d/17IJZPUpqz8HPwogJKsyEZcH9WmRr7KCe/view?usp=drive\_link](https://drive.google.com/file/d/17IJZPUpqz8HPwogJKsyEZcH9WmRr7KCe/view?usp=drive_link)   

- Iniciaremos a programação com a implementação do movimento do personagem\. Para alcançar esse objetivo, procederemos à configuração dos comportamentos acessando a seção de "Behavior"\.
	- A funcionalidade denominada "Top\-down movement" possibilita a movimentação do personagem em todas as direções\.
	- Recomenda\-se desmarcar a opção de “rotate”, pois, caso contrário, o personagem ficará girando conforme andamos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696444054600.png)

- Neste momento, procederemos com a programação da câmera para que ela siga continuamente o jogador\. A lógica da programação é a seguinte: a câmera permanecerá centrada no personagem o tempo todo\. Portanto, não será necessário adicionar qualquer condicional, uma vez que essa ação ocorrerá de forma constante e ininterrupta\.
	- Abra o Events;
	- Add > Event Group > “Player”;
	- Add action > Center the camera;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696642549000.png)

- Caso observemos que o personagem está atravessando as paredes, faremos os ajustes necessários\. A lógica de programação a ser aplicada consiste em garantir que o personagem permaneça separado das paredes o tempo todo\.
	- Add action > Player > Separate > Parede;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696751637300.png)

- 
	- Ficará assim\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696751637300.png)  
  
  
  


- Prosseguiremos agora com a implementação da capacidade de disparo do nosso personagem\. Para alcançar esse objetivo, iremos adicionar uma “Behavior" de "Fire bullet"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696751637300.png)

- Pesquise por “Fire”:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696757000400.png)

- Após a adição da “Behavior”, é o momento de realizar a programação\. 
	- Na condição, configuramos o seguinte: "Ao clicar com o botão esquerdo do mouse";
	- Add condition > mouse button release > Left;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696759025400.png)

- 
	- Na reação: Player > Fire bullets toward a position;
	- 1: Estou definindo o ponto de origem da bala, que será no centro do jogador, tanto em relação ao eixo X quanto ao eixo Y;
	- 2: Especificando qual objeto será;
	- 3: Indicando a direção para a qual o tiro será direcionado, que corresponde à posição apontada pelo cursor do mouse, tanto em X quanto em Y;
	- 4: Configurando a velocidade do disparo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696782027200.png)  


- A próxima etapa a ser abordada diz respeito à gestão da colisão entre os elementos de fogo e os inimigos\. Nesse cenário, é necessário assegurar a destruição simultânea tanto do elemento de fogo quanto do inimigo envolvido\.
	- Clique em “Add a new event”;
	- Add condition;
	- A lógica será de que quando meu tiro colidir com o inimigo;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696791927800.png)

- 
	- O tiro seja deletado e o inimigo também;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696791927800.png)

- 
	- Ficará assim;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696793938200.png)  


- Agora, proceda com a programação que garantirá a exclusão do projétil quando colidir com uma parede\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696795944900.png)  


-  Será necessário fazer com que os inimigos apareçam pelo mapa de forma contínua\. Para isso, precisamos estabelecer um temporizador, onde, se o tempo exceder 3 segundos, ele será reiniciado, criando, assim, inimigos de forma aleatória\.
	- Add new event;
	- Add condition > Timer;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696797951600.png)

- 
	- Add action;
	- Inimigo > Create;
	- Em ambos os eixos, tanto o X quanto o Y, é crucial utilizar valores aleatórios, uma vez que a fixação de valores constantes poderia permitir a ocorrência de um "Spawn Kill";

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696799958700.png)

- 
	- Vamos reiniciar o timer;
	- Add Action;
	- Start \(or reset\) a scene timer\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696801965400.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696801965400.png)  


- Se realizarmos um teste no jogo, será evidente que ele não funcionará corretamente\. É necessário que o cronômetro seja acionado assim que o jogo se inicia\.
	- Add new Event;
	- Add condition;
	- At the beginning of the scene;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696801965400.png)

- 
	- Add Action;
	- Start \(or reset\) a scene timer\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696807604400.png)

- Faremos agora com que nosso inimigo sempre nos siga, para isso, vamos adicionar um “behavior” de Pathfinding a ele\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696809611400.png)

- Acesse a seção de programação, onde iremos garantir que o inimigo nos siga incessantemente durante todo o jogo\.
	- Add action;
	- Inimigo >  Move to a position\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696809611400.png)

- Ao iniciar o jogo, identificamos três problemas: o primeiro refere\-se ao tamanho reduzido dos inimigos que surgem, o segundo diz respeito à inversão de sua imagem, e o terceiro o inimigo atravessa paredes\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696814074000.png)

- Para interromper a rotação dele, é necessário que acessamos as configurações de comportamento \(Behavior\) e removamos a marcação da opção de rotação\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696814074000.png)

- Abra os eventos para aumentar o tamanho dele\. Vamos configurar para que o tamanho do meu personagem seja para sempre, uma largura__ \(width\)__ de 140 e uma altura __\(height\)__ de 155\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696817729200.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696819736100.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696821743400.png)

- Para evitar que ele atravesse as paredes, é necessário acessar as “behaviors” da parede e marcar a opção 'obstacle for pathfinding'\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696823493700.png)

- Para concluir o jogo, é essencial que implementemos a condição de vitória\. Vamos criar uma nova fase que será exibida na tela de vitória\. \(Aula 23, na folha 22\)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696825501900.png)

-  Retorne à cena principal e adicione a bandeira\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696825501900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696828363400.png)

- A programação será, quando o personagem encostar na Flag, mude de scene\.
	- Add new event;
	- Add condition;
	- Player > Collision > Flag;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696830379500.png)

- 
	- Add action;
	- Change the scene;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696832389500.png)  
  


Recursos

- GDevelop, internet, Google e computador\.

Observação

- Quando os alunos terminarem, solicite que personalizem a tela de 'Win'\.
- Jogo finalizado para consulta:: https://drive\.google\.com/drive/folders/1Cw8\-6l2gD1g0apKdW04cnAz4L6BImZ3K?usp=drive\_link

Tarefas

- Em sua residência, tente recriar o jogo que desenvolvemos durante nossa atividade em sala de aula, mas substitua as sprites e criando novos inimigos\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

