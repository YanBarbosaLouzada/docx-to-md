# __PLANO DE AULA__

Aula 04 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Tilemap;
- Sistema de Câmera\.

Objetivos

- Criar sistema de câmera e tilemap\.

Estratégias e atividades

- Primeiro vamos precisar criar nosso tilemap, para isso precisamos clicar em window > 2D > Tile Pallet\.
	- Agora com o tile aber, vamos clicar em Create New Pallet, renomeie para Ground e salve em uma pasta chamada Tiles;
	- Faça isso para Ground, Wall e Cenário\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588109602800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588113180000.png)

- Editando assets\.
	- Em Pixel Adventure 1 > assets > Terrain, selecione o terrain que tem todos os blocos;
	- Após clicar nele, vá até o inspetor e mude os pixel por unit para 16;
	- Sprite mode para multiple;
	- Por fim clique no sprite editor;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588114179200.png)

- 
	- Dentro do sprite editor, clique em slice e mude o type para grid by cell size;
	- Mude o pixel size para 16x16;
	- Clique em apply\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588116180400.png)

- 
	- Configurando Tile Pallette\.
		- Nós fizemos a configuração dos assets, agora vamos arrastar esse asset para dentro do tile pallet Ground e Wall;

		![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588118185800.png)

- 
	- No cenário vamos arrastar o asset que está dentro de items > checkpoint > Start, mas antes precisamos colocar a mesma configuração que fizemos no inspetor do asset passado;
	- Então clique no Start \(idle\), vá até o inspetor e mude os pixel por unit para 16;
	- Sprite mode para multiple;
	- Clique no sprite editor;
	- Dentro do sprite editor, clique em slice e mude o type para grid by cell size;
	- Mude o pixel size para 16x16;
	- Clique em apply;
	- Por fim, volte no tile pallet de cenário e arraste este item para dentro dele\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588120240600.png)

- Adicionando componentes
	- Na sua Hierarchy deve ter aparecido algo chamado grid e dentro dela deve ter o ground, wall e cenário, caso não tenha basta você duplicar o que está dentro e alterar o nome;
	- Em cada grid \(ground, wall e cenário\), você deve adicionar um componente chamado tilemap collider 2D e alterar a layer de acordo com a grid;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588120240600.png)

- Agora vamos desenhar\.
	- Tudo o que for referente ao ground siga o exemplo da foto…
	- Para wall só devemos selecionar wall onde está escrito Ground;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588120240600.png)

- 
	- Para pintar/desenhar selecione o pincel ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588120240600.png)e depois selecione o bloco que você deseja;
	- Se quiser apagar selecione a borracha ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588120240600.png)\.
- Terminamos o nosso mapa, agora vamos fazer alterações na câmera?
- Criando scripts Door e CameraController\.
	- Passe o script para as crianças\.
- Crie um objeto vazio e chame ele de Door\.
	- Se quiser organizar seu projeto, você pode criar um create empty e trocar seu nome para level, dentro dele criar outro create empty e chamar de Room1 dentro dele você pode guardar e desativar o ground e wall que criamos antes de fazer o tilemap;
	- Guarde também o Door;
	- Adicione estes componentes ao Door, por fim ative o is trigger do box collider 2D\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588120240600.png)

- Coloque a door na tela onde deseja que a câmera mude para outra cena\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588131863200.png)

- Criando novo nível depois de ter feito tudo isso, duplique o Room1 e renomeie para Room2\.
	- Você deve arrastar o Door do Room2 para o final da tela 2\.
- Coloque os respectivos scripts dentro de Door e Main Camera
	- Coloque as coisas que se pede dentro de do script dor e main camera\. 

\(Room1\)				  \(MainCamera\)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588131863200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588131863200.png)

- Crie uma tag para Main Camera chamada MainCamera\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588131863200.png)

- Não esqueça de ver se a tag está correta no seu lugar\.

Recurso

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Como funciona a física na Unity:
	- Pesquisar sobre a física usada na Unity para simular movimento e interações\.
	- Descobrir como os objetos se comportam dentro do mundo criado na Unity\.

