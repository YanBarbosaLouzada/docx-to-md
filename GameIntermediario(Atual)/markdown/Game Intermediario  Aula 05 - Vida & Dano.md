# __PLANO DE AULA__

Aula 05 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Sistema de vida e dano\.

Objetivos

- Criar sistema de vida e dano\.

Estratégias e atividades

- Sort layers 
	- Para criar sort layers, você deve clicar em cima do player e depois deve abrir o Sprite Renderer > Additional Settings > Sort Layer > Add Sorting layer;
	- Adicione todas essas layers e deixe\-as nesta ordem da imagem\.

		BackGround/ForeGround/Player/Ground

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588198677300.png)

- 
	- Agora vá para Grid, e no tilemap renderer, mude no Additional Settings > Sorting Layer > Mude de acordo com a grid que você está…

		Ground > Ground Cenario > Cenario Player > Player

Wall > ForeGround\.

- Prefabs Fireball
	- Para criar o prefab da Fireball basta arrastar a FireBall para a pasta que você irá criar com o nome de prefab\.
	- Depois não esqueça de duplicar e volte\-as para o componente de player\_attack\.
- Componente de vida 
	- Vamos criar uma pasta chamada __health __e dentro dela vamos colocar um novo script chamado health;
	- Passe o script para os alunos;
	- Coloque o script no player;

 

- Canvas
	- Abra a hierarquia e clique com o botão direito\. Selecione UI > Canvas e renomeie para UICanvas;
	- Clique sobre o UICanvas e crie um objeto vazio \(Create Empty\)\. Renomeie para Healthbar\. Dentro de Healthbar, clique com o botão direito, vá em UI > Image, e renomeie para HealthbarTotal;
	- No HealthbarTotal, adicione o recurso gráfico do coração chamado HealthBar, arrastando\-o para dentro de Image > Source Image\. Os recursos estão disponíveis no drive da escola;
	- Agora, configure para exibir apenas 3 corações\. Para isso, clique em Image > Type e selecione Filled\. Em Fill Method, escolha Horizontal\. Configure Fill Amount para 0\.3 e marque a caixa Preserve Aspect\. Em seguida, clique em Set Native Size;
	- Antes de duplicar o HealthbarTotal, altere a cor do coração para preto\. Após isso, duplique o objeto e renomeie para HealthbarCurrent\. Agora, retorne a cor para vermelho\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588198677300.png)

	HealthbatCurrent

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588198677300.png)

HealthTotal

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588211895400.png)

- Canvas \(Script\) 
	- Crie um novo script e chame\-o de Healthbar;
	- Arraste para o HealthBar e passe o script para as crianças;
	- Não esqueça depois de arrastar as dependências do script para ele\.
- Animações de dano e morte
	- Clique em cima do player e depois entre em animation como já foi ensinado nas aulas passadas;
	- Crie a animação hurt e die, depois clique crie no animator e crie dois parâmetros do tipo trigger \(Die e Hurt\)\.
- Armadilha
	- Crie um creat empty e renomeie para saw dentro dele coloque os componentes…
		- No box collider ative o is trigger;
		- No Sprite Renderer coloque a layer como a do player;
		- Crie um script com nome Enemy\_Sideways;
		- No animator arraste o animator controller do saw \(Vamos criar aqui em baixo\)\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588214812200.png)

- 
	- Na pasta de animações crie uma nova pasta, renomeie para traps e depois crie um animator controller dentro dela e renomeie para Saw;
	- Crie uma animação para Saw e depois renomeie para Saw;
	- Adicione todos os frames da serra girando;
	- Adicione dentro Animator o animator controller do saw;
	- Por último passe o script do enemy para as crianças\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588216955200.png)

- Coleta de vida
	- Vamos criar um create empty e renomear para HealthCollectable e dentro dele vamos adicionar os componentes;
		- No Sprite Renderer coloque a layer como a do player e adicione a imagem do coração que esta disponível no asset do document;
		- No Box collider, ative os is trigger;
		- Crie e adicione um novo script com nome de HealthCollectable\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588219956500.png)

- 
	- Finalize exibindo o coração na tela e disponibilize o script para os alunos, certificando\-se de incluir as dependências tanto do script anterior quanto do script do coração\.
- Estrutura do projeto até o presente momento

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588220955100.png)

Recurso

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Componentes básicos da Unity:
	- Pesquisar sobre os componentes fundamentais na criação de jogos na Unity, como GameObjects, Scripts, Colliders, etc;
	- Entender o papel de cada componente no desenvolvimento do jogo\.

