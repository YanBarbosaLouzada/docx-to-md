# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780452999794600.png)

# __PLANO DE AULA__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

Conteúdos

- Introdução à Godot Engine\.

Objetivos

- Criar projeto;
- Conhecendo a interface da Godot;
- Nodes \(Nós\) e Scenes \(Cenas\);
- Movimentação simples\.

Estratégias e atividades

Seja bem\-vindo ao __Game Starter__, o módulo inicial do curso de __Desenvolvimento de Games__ da Mynds\. Nesta aula, vamos entender o que é uma __Game Engine__ \(motor de jogo\) e conhecer a __Godot Engine__, um poderoso motor de jogo utilizado para desenvolvimento de jogos 2D e 3D\.

START

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453004794300.png)

Game Engine ou Motor de jogo é uma ferramenta que facilita o desenvolvimento de jogos, fornecendo meios para a criação de personagens, criação de mapas, mecânicas de jogos, criação de áudio, criação de interfaces e tudo que é necessário para se criar um jogo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453007795800.png)

Como exemplo de Game Engines famosas, temos a __Unreal Engine__, para jogos realistas e complexos, a __Unity Engine__, que permite a criação de um simples jogo 2D até um jogo 3d, mais avançado e também temos uma opção mais leve, porém muito poderosa, que é a __Godot Engine__, um motor de jogo completamente gratuito, de código aberto, que pode ser usado por qualquer pessoa:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453010929700.png)

Vamos começar __baixando__ a Godot em seu site oficial: __https://godotengine\.org/__

- Para os nossos projetos, utilizaremos a __Godot 4\.1\-stable__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453016929700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453018928100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453023117500.png)

- Baixe a versão para __Windows__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453025117500.png)

- Após baixar o arquivo, vamos iniciar a Godot:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453028118000.png)

Ao iniciar a Godot, somos apresentados ao __Project Manager__, a tela inicial onde podemos __criar um novo projeto__ ou __gerenciar projetos salvos__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453030251000.png)

- Clique em __\+ New Project__ para criarmos nosso primeiro projeto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453031245100.png)

Ao criarmos um novo projeto, temos as propriedades:

- __Project Name:__ Aqui damos um nome ao nosso projeto;
- __Project Path:__ A pasta onde o projeto será salvo no computador;
- __Renderer:__ A Godot pode ser usada para projetos simples e mais complexos e em diversas plataformas, por isso, precisamos indicar qual o nível de recursos gráficos do nosso projeto\. Usaremos o Renderer __Mobile__, que oferece equilíbrio entre desempenho e qualidade gráfica\.
- __Version Control Metadata:__ A Godot permite utilizarmos um sistema de controle de versão, como o Git, para evitar erros, corrigir falhas e permitir o trabalho em equipe\.

Após incluir todas as informações necessárias, clique em __Create & Edit__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453033251800.png)

Agora vamos conhecer a __interface__ da Godot Engine:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453035245100.png)

- __Painel Scene:__ Aqui iniciamos uma nova cena e gerenciamos um cena aberta;
- __Painel FileSystem: __Aqui vemos todos os arquivos do nosso projeto, como as cenas criadas, scripts, imagens e áudios;
- __Painel Current Scene: __Aqui temos a cena atual, onde editamos nosso jogo e vemos todos os seus elementos;
- __Output: __Aqui temos informações importantes sobre o jogo, como avisos de erros e modificações importantes em tempo de execução;
- __Inspector: __Aqui vemos as propriedades de um elemento do jogo, como por exemplo a posição, tamanho e escala de um objeto;
- __Menu Superior: __Aqui alternamos a nossa área de trabalho entre 2D \(para jogos simples em duas dimensões\), 3D \(para jogos mais complexos em três dimensões\), Scripts \(para programação do jogo\) e AssetLib \(para acessar objetos e modelos prontos da comunidade\);

Vamos começar criando uma nova __cena 2D__ no Painel __Scene__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453039245800.png)

- Para salvar a cena, vamos até o menu __Scene__ \-> __Save Scene__ \(Um modo mais rápido de salvar é utilizando o atalho__ CTRL S__\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453040379300.png)

- Para manter nosso projeto organizado, antes de salvar a cena vamos__ criar__ uma pasta __“Scenes”__ e salvar a cena dentro dela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453042379600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453044380600.png)

- Altere o nome da Cena para __Cena\_1__ e clique em __Save \(Salvar\)__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453045380900.png)

Podemos visualizar no painel __File System__ a pasta __Scenes__ e o arquivo da __Cena\_1__ dentro dela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453047382100.png)

Agora que temos a cena criada, vamos entender o que são __Nodes \(Nós\)__ e como são utilizados pela Godot:

- Um Node \(ou Nó\) é um objeto fundamental na Godot, que pode ser um personagem, um inimigo, um obstáculo, uma luz, um elemento de cenário, um botão, um áudio, um texto ou qualquer objeto do jogo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453049381900.png)

- Na Godot, os objetos são chamados de __Nós__ porque os projetos são estruturados como uma __árvore__ com várias __ramificações__\. Cada cena representa uma árvore que pode conter múltiplos Nós, e cada Nó pode, por sua vez, conter outros Nós, formando uma hierarquia:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453050619300.png)

Os nós podem ser de diversos tipos e cada um possui propriedades diferentes\. Vamos começar com um nó do tipo__ CharacterBody2D__ que nos permite movimentá\-lo como um personagem pela cena:

- Clique no símbolo__ \+ __no painel __Scene__ e pesquise pelo nome CharacterBody2D:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453053621400.png)

- Um Node do tipo Characterbody2D não funciona sozinho\. Precisamos adicionar pelo menos dois nós importantes dentro dele: um __Sprite2D__ e um __CollisionShape2D__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453056619500.png)

- Começando pelo __Sprite2D__, vamos até o painel __Inspector__ e podemos ver diversas informações sobre este nó em específico:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453059785500.png)

- Vamos alterar a __Textura__ do Sprite utilizando o arquivo__ icon\.svg__ que vem por padrão na Godot:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453062785000.png)

Selecione agora o Node __CollisionShape2D__ e repare que agora o Inspector tem outras propriedades, como __Shape \(forma\):__

- Selecione __RetangleShape2D:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453075202500.png)__

- Ajuste a forma retangular no formato do sprite do personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453081727600.png)

- Agora vamos selecionar o Node__ CharacterBody2D__ novamente e ativar a opção __Move__ para movimentar o personagem até o centro da tela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453083726200.png)

Com o personagem em cena, vamos clicar em __Run__ para ver a cena funcionando:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453085728300.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453087727600.png)__

Já aprendemos sobre as principais ferramentas e como incluir um personagem, mas para que ele ganhe vida, precisamos __programar__ seu funcionamento\. Na Godot, iremos programar com a linguagem __GDScript__:

- Selecione o Node __CharacterBody2D__ e vamos criar um __script__ para ele:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453090117900.png)

- Crie uma pasta específica para __Scripts__: 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453092125100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453093125800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453095126500.png)

- Ao abrir o script, já temos o comando __extends CharacterBody2D__, que nos permite utilizar os comandos e bibliotecas específicas daquele Node:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453097127400.png)

- Como nosso objetivo é movimentar o personagem, vamos criar uma __variável__ para guardar o valor da velocidade:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453100127300.png)

Na __GDScript__, temos duas funções principais:

- __\_ready\(\):__ Inicializar variáveis e objetos\. Executa comandos no __primeiro frame__ do jogo;
- __\_process\(delta\):__ Comandos em__ looping __durante a execução do jogo, como por exemplo a movimentação do jogador\.

Vamos usar a propriedade __velocity__ dentro da função __\_ready\(\)__\. Quando falamos de objetos 2D, temos dois eixos de movimento:

- Eixo __X__: movimento horizontal \(esquerda e direita\);
- Eixo__ Y__:  movimento vertical \(cima e baixo\)\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453104052300.png)

Primeiro vamos alterar o valor da velocidade horizontal do personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453105050300.png)

Apenas alteramos o valor da __velocidade__, mas precisamos utilizar um __comando__ chamado __move\_and\_slide\(\)__ para __movimentar__ o personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453116309000.png)

Perceba que ao testarmos o jogo, o personagem se movimenta para a direita\. Mas se aplicarmos uma força __negativa__ ao valor de speed, o personagem vai para a __esquerda__\.  

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453118309300.png)

Podemos utilizar __condições__ para acionar comandos, como por exemplo o __pressionamento de teclas__\. Vamos alterar o script para controlar o personagem pelas setas do teclado:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780453121630300.png)

Teste e veja que agora o personagem se movimenta apenas quando pressionamos as __setas esquerda__ e __direita\.__

__Desafio: Tente movimentar o personagem para cima e para baixo com as setas repetindo o processo anterior\.__

Finalizamos a primeira aula do módulo __Game Starter__\. Utilize os conhecimentos adquiridos até agora e adicione alguma nova funcionalidade ao personagem\.

Recursos

- Computador, internet, Godot instalado\.

Observação

Tarefas

- Instalar Godot 4\.1 em casa\.

