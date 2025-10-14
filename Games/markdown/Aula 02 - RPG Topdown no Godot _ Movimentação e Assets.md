# __PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Movimentação do player e Assets\.

Objetivos

- Criar um novo projeto 2D;
- Movimentação do player;
- Baixando Assets\.

Estratégias e atividades

- Instalando dependências:
	- Entre neste link [https://game\-endeavor\.itch\.io/mystic\-woods](https://game-endeavor.itch.io/mystic-woods) e baixe a versão gratuita dos assets;
	- Clique na pasta nova e abra com o winrar \(só clicar duas vezes\) e deixe aberta por enquanto
- Crie um novo projeto 2D\.
- Configurando resolução do jogo\.
	- Clique em __project settings > display > window e mude o viewport width __para __320 __e __viewport height __para __180__;
	- Para a próxima configuração marque a opção __advanced settings__;
	- Ainda em Window mode o __window width override__ para __1280 __e o__ window height override__ para __720__;
	- Window > Stretch > __mode__ muda de para __canvas\_items__\.
- Adicionando os sprites no jogo\.
	- Crie todas essas pastas;
	- Dentro de tilesets coloque as pastas floors e walls\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453375808500.png)

- Arraste os asstes que foram abertos no winrar para as determinadas pastas:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453377813000.png)

- Configurando textura do nosso projeto\.
	- Project settings > Rendering > Textures > Texture Filter mude para Nearest\.
- Iniciando nossa progamação do personagem
	- Clique no ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453381018300.png) para Adicionar um novo nó a esta cena que ainda não nomeamos;
	- Adicione primeiro todos estes nos CharcterBody2D, Sprite2D e CollisionShape2D;
	- Clique em sprite 2D e arraste o player\.png para dentro de textura\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453383891500.png)__

- Ainda com o Sprite2D selecionado, use estas configurações para o Sprite2D;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453386142700.png)

- Salvando a cena aperte ctrl \+ S e salve a cena, você também pode criar um pasta chamada cena para salvar cenas futuras\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453388144900.png)

- Agora com o __CollisionShape2d__ selecionado use está configurações\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453389557200.png)

- Adicionando script no player\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453391555300.png)
	- E depois clique em criar e pronto… você também pode criar uma pasta chamada scripts para guardar os scripts\.
- Scripts disponíveis no Github \(Aula 11\)\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453393556300.png)

- Configurando Inputs\.
	- Project Settings > InputMap\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453394556900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453396556300.png)

- Se tudo deu certo deve ficar assim\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453397554300.png)

- Agora seu player já está andando\.

Recursos

- Computador, internet, Godot instalado\.

Observação

- O projeto utiliza o Godot 4\.0 [https://godotengine\.org/download/windows/](https://godotengine.org/download/windows/)
- Será um jogo estilo RPG visto de cima\.

Tarefas

- Jogar um jogo do estilo RPG que estamos fazendo e contar sua experiência, e o que tirou de inspiração do jogo\.

