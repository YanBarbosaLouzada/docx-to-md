# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599068154200.png)

# __PLANO DE AULA__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Introdução à Unity 3D\.

Objetivos

- Criar o primeiro projeto;
- Apresentar plataforma;
- Iniciar o projeto 3D;
- Mapeamento de Controles\.

Estratégias e atividades

Crie o projeto na versão 2022\.3\.22f1\.

Para iniciar o projeto, siga estes passos: 

- Clique na seta ao lado de __New__ e escolha a versão mais próxima ou idêntica àquela que foi recomendada;
- Em seguida, selecione o tipo de projeto, que, no nosso caso, será um projeto 3D;
- Por fim, atribua um nome ao projeto\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599068154200.png)

Vamos acessar o site __Mixamo__ para selecionar o personagem que será utilizado no jogo\. É importante escolher um personagem__ humanóide__, para manter a consistência com o padrão de jogo que estamos desenvolvendo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599084009700.png)

Para salvar o personagem, selecione o formato de arquivo __FBX for Unity__, pois é altamente compatível e otimizado para uso na Unity Engine\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599084009700.png)

Vamos salvar o personagem em uma pasta chamada __Player__, onde estará seu modelo 3D \(adquirido no mixamo\)\. Para visualizar o personagem corretamente, selecione seu modelo na pasta e  extraia seus materiais e texturas clicando em __Extract Textures__ e__ Extract Materials__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599089705800.png)

Precisamos configurar o personagem como um tipo__ humanóide__ e criar um avatar a partir do seu modelo para que as animações funcionem corretamente\. Ao final, clique em __Apply__ para confirmar as alterações:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599091577000.png)

Após a criação do projeto, é hora de obtermos os __assets iniciais__, os quais incluem as estruturas que compõem a cidade utilizada no jogo\.

Após fazer o download dos assets, abra a cena que já inclui a cidade do jogo pré\-montada em: __Assets > Starter Assets > Buildin > Town Constructor Pack > Scenes > City__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599093584600.png)

Agora que temos a cena da cidade aberta, podemos posicionar nosso personagem no ponto inicial do jogo\. Para isso, vamos adicionar o __modelo 3D__ do nosso personagem em cena e renomeá\-lo para __Player__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599095591600.png)

A cena já está equipada com uma câmera principal, no entanto, para o nosso projeto, vamos utilizar a __Cinemachine Free Look__, uma câmera que acompanha o movimento do nosso personagem, proporcionando uma experiência semelhante a jogos como __GTA \(Grand Theft Auto\)__ e __Assassin's Creed__\.

Para verificar se a Cinemachine já está instalada, acesse a aba __Window > Package Manager__ e procure por 'Cinemachine'\. Caso não esteja instalada, clique em 'Instalar' para adicionar ao projeto\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599099882200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599099882200.png)

Com a cinemachine instalada, agora podemos criar a Free Look Camera na cena:

Clique com o botão direito no painel __Hierarchy__: __Cinemachine > FreeLook Camera__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599099882200.png)

Nossa câmera principal agora possui um símbolo que indica estar sendo controlada pela cinemachine\. Agora passamos a trabalhar somente com a__ Freelook Camera__ e nossa primeira configuração será indicar qual objeto ela irá seguir, através da opção __Follow__\. No caso, será o nosso __Player__\. 

Devemos também indicar para qual objeto a câmera irá apontar, com a opção__ LookAt__\. Para isso, iremos criar um __objeto vazio \(Create Empty\)__ próximo da cabeça do nosso personagem e chamá\-lo de__ Head__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599099882200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599099882200.png)

Por fim, iremos configurar o mapeamento de controles\. Na Unity, chamamos estas ações de __Input Actions__\. Vamos começar criando um novo Input Actions e chamá\-lo de __Controls__:

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599111739500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599111739500.png)

Selecione o Input Actions Controls e, no Inspector, marque a opção __Generate C\# Class__ para que os controles possam ser configurados através de script:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599115646900.png)

Agora, vamos abrir o nosso Input Actions __Controls__ para mapear os controles básicos de movimentação do personagem:

 

- Primeiro definiremos um __Action Map __chamado __Player__, utilizado para especificar qual objetivo deste conjunto de controles\. Posteriormente criaremos Input Maps diferentes para navegação no menu, tela de pause e etc\.
- Depois, temos as __Actions__, que são as ações mapeadas, como movimentar, correr e atacar\. Nossa primeira ação será __Move\.__ Marque a opção __Action Type__ como __Value __e __Control Type__ como __Vector2 \(coordenadas X e Y\)__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599118146000.png)

Em __Move__, agora podemos indicar quais as __entradas__ que controlam estas ações:

- Crie uma __Binding__ \(vínculo\) para separar diferentes tipos de controles \(Teclado, Joystick, Mouse\), vamos chamá\-la de __Keyboard__ \(teclado\)\.
- Dentro de Keyboard, indique todos os controles que representam as quatro direções \(AWSD\)\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599118146000.png)

Para controlar a câmera, vamos criar outra __Action__ chamada __Camera__ e repetir o processo de Move, mas agora utilizando o __movimento do mouse \(delta\)__ como controle:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599118146000.png)

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefa

- Instalar a versão __2022\.3\.22f1__ da __Unity Engine__ em casa\.

