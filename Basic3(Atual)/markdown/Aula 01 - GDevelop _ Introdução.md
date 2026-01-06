‘![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772525529700.png)

# __PLANO DE AULA__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): GDevelop

Conteúdos

- GDevelop: Introdução\.

Objetivos

- Lógica de programação\.

Estratégias e atividades

Este volume marca o início da jornada no desenvolvimento de jogos com

__GDevelop__, uma poderosa Game Engine que capacita a criação de jogos através

da programação visual\. Prepare\-se para mergulhar nesse universo empolgante e

aprender a construir suas próprias experiências interativas\!

Vamos começar instalando o GDevelop no computador\. Vá até o site do GDevelop: [https://gdevelop\.io/pt\-br](https://gdevelop.io/pt-br)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772525529700.png)

Clique em __download__ e escolha a plataforma __Windows__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772540453800.png)

Baixe e execute o instalador\. Escolha o local para a instalação e aguarde até que o programa termine a instalação:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772542232000.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772542232000.png)

Agora vamos conhecer a interface do GDevelop e suas principais ferramentas\. Logo em sua tela inicial vemos diversas opções de gerenciamento dos jogos criados e projetos da comunidade, mas, de início, vamos focar em dois menus principais::

- __Iniciar:__ Ao abrir o GDevelop, a tela de início exibe tutoriais básicos e templates para começar a desenvolver jogos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772547226500.png)

- __Construir: __Aqui podemos conferir jogos prontos, iniciar o nosso projeto ou abrir um projeto existente:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772547226500.png)

Vamos__ criar__ o nosso primeiro projeto e suas configurações iniciais:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772547226500.png)

Na tela __Novo Projeto__, configure da seguinte forma:

- Defina a __resolução__ que melhor se encaixa no nosso projeto\. Como o jogo será executado no computador, utilizaremos __full HD 1920 x 1080\.__
- O nome do projeto será__ Aula 1 __e é assim que iremos encontrá\-lo posteriormente\.
- O GDevelop permite salvar o projeto na nuvem, mas vamos __salvá\-lo no computador\.__ Escolha uma pasta fácil de lembrar\.
- Marque a opção __Otimizar para Pixel Art__, pois vamos trabalhar em um projeto__ 2D\.__
- Por último, desmarque a __opção de autenticação__, pois nosso projeto inicial não será __online\.__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772547226500.png)__

Agora que criamos nosso projeto, vamos entender melhor a interface da __cena__ no GDevelop\. A cena é a base de um jogo e pode representar uma fase ou parte dela, um menu ou um puzzle\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772558897000.png)

Como identificado na__ figura acima__, temos:

- __Cena:__ A cena é o espaço principal onde o jogo acontece\. É aqui que você cria e organiza todos os elementos visuais e interativos do jogo\.
- __Objetos:__ Os objetos são os elementos que compõem a cena\. Eles podem ser personagens, inimigos, plataformas, itens colecionáveis, botões de menu, entre outros\.
- __Propriedades:__ As propriedades permitem personalizar os atributos da cena e dos objetos nela contidos\. Isso inclui posição, tamanho, rotação, animações, comportamentos específicos, entre outros\.
- __Camadas:__ As camadas permitem organizar visualmente os elementos da cena em diferentes níveis\. Você pode ter uma camada para o fundo, outra para os elementos de jogo principais e outra para a interface do usuário\.

Vamos __criar um objeto__ e adicionar um __sprite__ \(imagem\) a ele:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772561127100.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772561127100.png)

Vamos chamá\-lo de __Jogador__\. Poderíamos importar uma imagem qualquer ou até um conjunto de sprites, como animações, mas o GDevelop permite __desenhar__ o nosso próprio objeto através do __Piskel__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772566009300.png)

Para a nossa aula inicial, o personagem será um simples __quadrado\.__ Utilize o __balde de tinta__ para pintar toda a área da imagem\. Clique em __Salvar__ e depois em __Aplicar__ para confirmar as alterações:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772566009300.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772566009300.png)__

Agora que criamos nosso objeto __Jogador__, vamos arrastá\-lo até a cena\. Clique em __Visualizar__ e observe que já conseguimos ver nosso personagem em cena:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772566009300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772566009300.png)

Mas o jogador ainda não faz nada\. Por enquanto ele é apenas uma imagem estática, sem qualquer tipo de ação\. No GDevelop, podemos controlar as ações dos objetos por meio de __Eventos \(Events\)__ e __Comportamentos \(Behaviors\)\. __

Vamos começar pelos eventos\. Vá até a aba __Eventos__ para criarmos nosso primeiro comando:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)

__Eventos__ são utilizados para definir a lógica do jogo, determinando como os objetos devem se __comporta__r em resposta a certas __condições\.__ Um evento é composto por duas partes principais: a __condição__ e a __ação:__

- __Condição:__ é a parte do evento que verifica se um determinado critério é atendido\. Se a condição for verdadeira, a ação associada a ela será executada\.
- __Ação:__ é o que acontece quando a condição é satisfeita\. Pode ser qualquer coisa que modifique o estado do jogo, como mover um objeto, mudar uma animação, aumentar uma pontuação, ou reproduzir um som\.

Nosso primeiro comando irá executar a __ação de mover__ o jogador quando a __condição de uma tecla pressionada__ for atendida:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)__

Se visualizarmos a cena, já conseguimos mover o jogador ao pressionar a tecla D\. Vamos repetir o processo para mover o jogador para a esquerda com a tecla A:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)

Note que agora aplicamos uma __força negativa__ no eixo X de __\-200\.__

Outro modo de atribuir ações aos objetos é utilizando __Comportamentos \(Behaviors__\)\. Ao incluir um comportamento específico a um objeto, podemos configurá\-lo e até mesmo utilizar eventos que só aquele comportamento possui\. Vamos adicionar o comportamento __Personagem de Plataforma__ ao Jogador:

- Clique dentro do objeto__ Jogador__ e vá até __comportamentos\. __Clique em __Adicionar um comportamento__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)

- Escolha o comportamento __Personagem de Plataforma:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772575542500.png)__

- Agora podemos alterar vários atributos do jogador, como aceleração, gravidade, velocidade do salto\. Por enquanto vamos apenas aplicar o comportamento\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772591873000.png)

Visualize a cena e perceba que o jogador cai, pois agora ele é afetado pela gravidade\. Precisamos criar outro objeto que servirá como uma superfície para o jogador pisar:

- Crie um novo objeto chamado __Chão__ e pinte de uma cor diferente da cor do jogador\. Como dito anteriormente, utilize o painel de Propriedades à esquerda para alterar a escala \(largura e altura\) do objeto\. É possível fazer alterações de posição e tamanho diretamente com o mouse:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772591873000.png)

- Adicione o comportamento__ Plataforma__ ao objeto Chão:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772596091200.png)

Visualize a cena e note que agora o jogador cai somente até encostar no chão e consegue se mover a partir das setas do teclado:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772596091200.png)__

Com isso, concluímos a base do nosso primeiro projeto\. Agora é a sua vez de personalizar e explorar todas as possibilidades: aprimore o cenário adicionando mais detalhes e elementos, personalize o personagem e teste novos comportamentos e eventos\. 

Lembre\-se, a criatividade é a chave para um projeto de sucesso, então não tenha medo de experimentar e inovar\. Bom desenvolvimento\!

Tarefa

- Em sua residência, faça a instalação do GDevelop em seu computador\. Além disso, tente reproduzir o jogo que desenvolvemos durante nossa atividade em sala de aula, modificando os ASSETS e adicionando mais coisas\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

