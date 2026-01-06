# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773792192400.png)

# __PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Computador

Ferramenta\(s\): GDevelop baixado no computador

Conteúdos

- GDevelop: Jogo de Plataforma \- Mynder’s Mission\.

Objetivos

- Criando o Menu;
- Controles Mobile;
- Publicação\.

Estratégias e atividades

Chegou a hora de finalizarmos o projeto Mynder’s Mission\! Para iniciar ou sair do jogo, criaremos um menu\. Além disso, vamos adicionar a opção de controles mobile para o jogador que estiver em um dispositivo touch screen \(tela de toque\)\. Por último, vamos aprender a como publicar o jogo e deixá\-lo disponível para jogar online\.

__START__

Um bom menu de jogo deve imediatamente transmitir ao jogador o tipo de experiência que ele terá\. Vamos criar um menu que capture e transmita a atmosfera do nosso jogo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773792192400.png)

- Vamos criar um nova cena e defini\-la como a cena inicial:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773808757000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773810765300.png)

- Defina a cena Menu como a __cena inicial__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773812773200.png)

- Agora podemos alterar a __cor de fundo__ do Menu:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773812773200.png)

 

- Adicionamos um novo objeto do tipo __Sprite__ que chamaremos de __Título__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773814782100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773816791000.png)

- Vamos adicionar também dois botões: __Jogar__ e __Sair\.__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773818799400.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773818799400.png)__

- __Ajuste __os elementos na tela como preferir\. Aqui temos um exemplo de como os objetos podem ser distribuídos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773820808300.png)

Agora vamos aos Eventos para programar as ações do menu:

- Quando o botão __JOGAR__ for clicado, alteramos para a cena __Fase 1__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773824231500.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773825151400.png)__

- Já o botão __SAIR__ irá fechar o jogo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773827938700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773827938700.png)

Com nosso menu funcionando, vamos voltar para a cena __Fase 1__ para criar o __Sistema de Controles Mobile__:

- Primeiro iremos adicionar um objeto do tipo __Multitouch Joystick__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773829945900.png)

- Escolha um modelo de __joystick__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773831954000.png)

- Posicione o Joystick na cena, alterando sua camada para__ Interface__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773833962000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773835969400.png)

Para os __botões de ação \(Pulo e Disparo\)__, vamos criar nosso próprio design de botão:

- Crie um objeto do tipo __botão__ e ao invés de escolher um __modelo pré\-definido__, vamos __criar do zero__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773835969400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773837977100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773840991600.png)

Botões possuem três principais estados:

- __Idle:__ O estado normal do botão;
- __Hovered:__ Quando posicionamos o cursor em cima do botão;
- __Pressed:__ Quando pressionamos o botão\.

Vamos fazer uma versão para cada estado do __botão A__:

-  Começaremos pelo estado __Idle__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773841817800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

- Para o estado __Hovered__, vamos utilizar a __mesma imagem__, porém um pouco mais escura\. Ao editar o Sprite no Piskel, clique em __New__ para não sobrescrever a imagem de idle:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

- Para __Pressed__, vamos deixar a cor __ainda mais escura__, para que seja visível quando o jogador está apertando o botão:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

- Agora vamos __duplicar__ o botão A, criando o botão B e arrastando ambos os botões para a cena:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

A resolução __640 x 480__ funciona para jogos executados no computador ou navegadores, mas quando falamos de dispositivos mobile, podemos utilizar uma proporção __16:9__ \(__640 x 320__\):

- Para alterar a resolução, vamos acessar o __Gestor de Projeto__ e as __Propriedades__ nas __Configurações do Jogo__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773844605500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

- Ajuste o __joystick__ e os __botões__ de acordo com a nova resolução:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

Agora vamos aos __Eventos__ ajustar a programação para os novos controles:

- Adicione um novo __Grupo de Eventos__ chamado __Controles Mobile:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

- Faça o mesmo para o __lado esquerdo__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

- Quando o botão A for __pressionado__, o personagem irá __saltar__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

Por fim, vamos __acionar__ o disparo com o __botão B__:

- Para que a ação de __disparar__ funcione com ambos os controles \(tecla X e botão B\), vamos utilizar o __operador relacional OU__, que executa a ação se uma das condições for verdadeira:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773858840000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773875437900.png)

Clique em __Visualizar__ e veja que já é possível jogar pelos controles mobile\.

Para testarmos, vamos aprender a como gerar uma __build executável__ do game e também como __publicá\-lo__ em plataformas digitais:

- Clique em __Compartilhar__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773877852500.png)

-  No GDevelop temos diversas plataformas de publicação, como a gd\.games \(Plataforma digital do GDevelop\), Computador \(PCs e Notebooks\) e dispositivos móveis:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773877852500.png)

- Primeiro vamos gerar um arquivo __\.APK \(Android\)__ ou __\.IOS \(IPhone\)__ para instalar o game em dispositivos móveis:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)

- O GDevelop tem uma __limitação diária__ de __2 \(duas\) publicações__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)

- Aguarde o GDevelop gerar o \.APK e __baixe__ após a conclusão: 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)

- Envie para um __dispositivo Android__ e __instale__ o aplicativo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)

Vamos publicar o jogo na plataforma __gd\.games__ para jogar online:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773879861800.png)

__Copie o link__ e acesse o game\. Você pode __compartilhar__ esse link para amigos testarem seu jogo antes do lançamento:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773890922400.png)

Inclua __informações__ como capa, categoria e descrição e publique seu jogo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773892108500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773894116100.png)

Parabéns por concluir o projeto do jogo __Mynder’s Mission__\! Agora é a sua vez de aprimorar o game e criar novos desafios, adicionando novas funcionalidades\. Além disso, você pode usar o conhecimento adquirido até aqui para desenvolver seu próprio jogo do zero e publicá\-lo para jogar com seus amigos\!

Recursos

- GDevelop, internet, Google e computador\.

Observação

Tarefas

Agora que nosso projeto está completo, faça um relatório com os seguintes tópicos:

- Principais características/mecânicas trabalhadas durante este projeto;
- Pontos positivos: O que você mais gostou de fazer? Qual parte do projeto foi mais interessante?
- Pontos negativos: O que você menos gostou de fazer? O que poderia ser diferente? 

Envie uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), traga em um pendrive ou em seu Google Drive/One Drive\.

