# __PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 2

Tipo da atividade: Online

Ferramenta\(s\): GDevelop baixado no computador

	                                

Conteúdos

-  GDevelop: Jogo do pong\.

Objetivos

- Trabalhar lógica de programação;
- Conhecer o jogo Pong;
- Variáveis no GDevelop\.

Estratégias e atividades

- Explicar a história do pong:
	- O Pong é um dos primeiros videogames e marcou o início da indústria de jogos eletrônicos\. Foi criado por Nolan Bushnell e lançado pela Atari em 1972\. O jogo simulava uma partida de tênis de mesa, com dois jogadores controlando raquetes virtuais e tentando rebater uma bola de um lado para o outro na tela\.
	- Pong foi um sucesso imediato nos fliperamas e ajudou a estabelecer os videogames como uma forma popular de entretenimento eletrônico\. Sua jogabilidade simples e intuitiva o tornou acessível a pessoas de todas as idades\. O jogo também desempenhou um papel importante na popularização dos consoles de videogame caseiros, quando a Atari lançou uma versão doméstica do Pong em 1975\.
	- O sucesso do Pong abriu caminho para a indústria de jogos eletrônicos, levando ao desenvolvimento de uma ampla variedade de jogos e sistemas de videogame ao longo dos anos\. Portanto, Pong é considerado um marco na história dos videogames e um símbolo do início dessa indústria multimilionária\.
	- https://www\.youtube\.com/watch?v=fiShX2pTz9A
- Estarei disponibilizando um arquivo contendo os recursos gráficos \(assets\)\. Coloque nos computadores dos alunos: [https://drive\.google\.com/file/d/1sDR\-q\-KWE6v1JWYoktw\-O\-moKtfztOWA/view?usp=drive\_link](https://drive.google.com/file/d/1sDR-q-KWE6v1JWYoktw-O-moKtfztOWA/view?usp=drive_link)
- Este jogo será para dois jogadores, ou seja, ambas as barras precisarão se mover\. Uma delas será controlada com as teclas WASD e a outra com as setas\. É importante observar que as barras só podem realizar movimentos para cima e para baixo\. Lembre\-se de que tudo o que fizermos na barra1, replique na barra2\.
	- Procederemos com a abertura da "behavior" da barra1 e adicionaremos o movimento "Top\-down”;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697255997600.png)

- 
	- Será necessário remover todos os "checks", visto que ele deve movimentar\-se somente para cima e para baixo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697257740000.png)  


- Faça a mesma coisa para a barra2\.
- Ao executarmos o jogo, observaremos que não há resposta, devido à remoção de todas as funções da Barra1 e da Barra2\. Será necessário utilizar as teclas "W" e "S" para direcionar a barra1 verticalmente\. Para a barra2, deve\-se usar as setas direcionais para cima e para baixo\.
	- Abra o Events;
	- Add > Event Group > Movimento;
	- Add a new event;
	- Add condition;
	- Key pressed > W;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697262340500.png)

- 
	- Add action;
	- Barra1 > Simulate up key press\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697262340500.png)

- Agora temos que fazer o mesmo processo para ele ir para baixo, porém vamos trocar a tecla pressionada para S e ele simulará para baixo = down\.
	- Ficará assim;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697265276100.png)

- Realize o mesmo procedimento para a Barra2, alterando apenas as teclas para "UP" e "Down"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697267291300.png)  
  
  


- Ao testar o jogo, observamos que, ao movimentar\-se verticalmente, a barra ultrapassa os limites visuais\. Existe uma barreira invisível\. Devemos configurar as barras para reconhecer e não ultrapassar essa barreira\.
	- Abra o Events;
	- Add > Event Group > Limite;
	- Add a new event;
	- Add action;
	- Barra1 > Separate > Barreira;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697267291300.png)

- 
	- Faça o mesmo para a barra2;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697267291300.png)  


- Concluído o ajuste da barra, procederemos com a bola\. Quando o jogo iniciar é essencial que ela tenha movimentação\.
	- Abra o Events;
	- Add > Event Group > Movimento bola;
	- Add a new event;
	- Add condition;
	- At the beginning;![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697267291300.png)  
  
  

	- Add action;
	- Bola > Add a force \(angle\);
	- O Ângulo tem que ser aleatório, por isso coloque aqueles números;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697267291300.png)  


- A bola está andando, porém quando a bola encosta na barra, ela atravessa, para fazer com que ele não atravessa e rebata, vamos abrir a behavior da bola e pesquisar por bounce\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Abra o Events;
	- Add > Event Group > Rebater;
	- Add a new event;
	- Add action;
	- Bola > bounce off another object > Barra1;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Faça a mesma coisa para a barra2 e a barreira;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- Será necessário configurar para que, ao ultrapassar a barra1, o ponto seja atribuído à barra2 e o jogo recomece\. Iniciaremos pela criação de variáveis denominadas Pontuação1 e Pontuação2\.
	- Clique na “Carinha” no canto esquerdo;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Selecione a Global variables;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- Crie os pontos dos players\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Será necessário programar de modo que, caso a bola ultrapasse \-100 em X, o jogo reini	cie e a variável Player2 receba 1 ponto\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Abra o Events;
	- Add > Event Group > Pontos;
	- Add a new event;
	- Add Condition;
	- Bola > X position <= \-100;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Add action;
	- Change the scene;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- 
	- Add action;
	- Change number variable\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697276212200.png)

- Procederemos de forma similar quando a bola ultrapassar o Player2, contudo, alteraremos o valor de X e atribuiremos 1 ponto à variável do Player1\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697291992100.png)  


-  Agora vamos fazer com que esses pontos apareçam na nossa tela, para isso será necessário adicionar um “TEXT” ao nosso jogo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697294001900.png)

- Deixe essa configuração\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697294001900.png)

- Crie para o player2 a mesma coisa\.
- Coloque os TEXT dentro do jogo\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697294001900.png)
- Agora vamos fazer com que este texto sempre atualize com as informações das variáveis\.
	- Abra o Events;
	- Add > Event Group > Texto;
	- Add a new event;
	- Add Action;
	- PontosPlayer1 > Modify the text > ToString\(GlobalVariable\(PontosPlayer1\)\);

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697294001900.png)

- 
	- Replique para o PontosPlayer2\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702697294001900.png)  
  
  
Recursos

- GDevelop, internet, Google e computador\.

Observação

- Deixei disponível o jogo completo, caso surja alguma duvida: https://drive\.google\.com/file/d/1GyHVbmPcqOIfHiDXg11plqrL6KFRBzaD/view?usp=drive\_link

Tarefas

- Em sua residência, tente recriar o jogo que desenvolvemos durante nossa atividade em sala de aula, mas substitua as sprites\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/Onedrive\.

