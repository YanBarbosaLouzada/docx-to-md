# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774027467900.png)

# __PLANO DE AULA__

Aula 07 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Computador

Ferramenta\(s\): Godot Engine

Conteúdos

- Godot Engine

Objetivos

Estratégias e atividades

Introdução

__START__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

Conteúdos

- Introdução à Godot Engine\.

Objetivos

- Criar projeto;
- Conhecendo a interface da Godot;
- Nodes \(Nós\) e Scenes \(Cenas\);

Estratégias e atividades

Seja bem\-vindo a __aula experimental__ do curso de __Desenvolvimento de Games__ da Mynds\. Nesta aula, vamos entender o que é uma __Game Engine__ \(motor de jogo\) e conhecer a __Godot Engine__, um poderoso motor de jogo utilizado para desenvolvimento de jogos 2D e 3D\.

START

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774031484800.png)

Game Engine ou Motor de jogo é uma ferramenta que facilita o desenvolvimento de jogos, fornecendo meios para a criação de personagens, criação de mapas, mecânicas de jogos, criação de áudio, criação de interfaces e tudo que é necessário para se criar um jogo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774031484800.png)

Como exemplo de Game Engines famosas, temos a __Unreal Engine__, para jogos realistas e complexos, a __Unity Engine__, que permite a criação de um simples jogo 2D até um jogo 3d, mais avançado e também temos uma opção mais leve, porém muito poderosa, que é a __Godot Engine__, um motor de jogo completamente gratuito, de código aberto, que pode ser usado por qualquer pessoa:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774036608000.png)

Vamos começar __baixando__ a Godot em seu site oficial: __https://godotengine\.org/__

- Para os nossos projetos, utilizaremos a __Godot 4\.1\-stable__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774038616700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774042091200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774044101300.png)

- Baixe a versão para __Windows__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774044101300.png)

- Após baixar o arquivo, vamos iniciar a Godot:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774046110300.png)

Ao iniciar a Godot, somos apresentados ao __Project Manager__, a tela inicial onde podemos __criar um novo projeto__ ou __gerenciar projetos salvos__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774048119700.png)

- Clique em __\+ New Project__ para criarmos nosso primeiro projeto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774048119700.png)

Ao criarmos um novo projeto, temos as propriedades:

- __Project Name:__ Aqui damos um nome ao nosso projeto;
- __Project Path:__ A pasta onde o projeto será salvo no computador;
- __Renderer:__ A Godot pode ser usada para projetos simples e mais complexos e em diversas plataformas, por isso, precisamos indicar qual o nível de recursos gráficos do nosso projeto\. Usaremos o Renderer __Mobile__, que oferece equilíbrio entre desempenho e qualidade gráfica\.
- __Version Control Metadata:__ A Godot permite utilizarmos um sistema de controle de versão, como o Git, para evitar erros, corrigir falhas e permitir o trabalho em equipe\.

Após incluir todas as informações necessárias, clique em __Create & Edit__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774048119700.png)

Agora vamos conhecer a __interface__ da Godot Engine:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774048119700.png)

- __Painel Scene:__ Aqui iniciamos uma nova cena e gerenciamos um cena aberta;
- __Painel FileSystem: __Aqui vemos todos os arquivos do nosso projeto, como as cenas criadas, scripts, imagens e áudios;
- __Painel Current Scene: __Aqui temos a cena atual, onde editamos nosso jogo e vemos todos os seus elementos;
- __Output: __Aqui temos informações importantes sobre o jogo, como avisos de erros e modificações importantes em tempo de execução;
- __Inspector: __Aqui vemos as propriedades de um elemento do jogo, como por exemplo a posição, tamanho e escala de um objeto;
- __Menu Superior: __Aqui alternamos a nossa área de trabalho entre 2D \(para jogos simples em duas dimensões\), 3D \(para jogos mais complexos em três dimensões\), Scripts \(para programação do jogo\) e AssetLib \(para acessar objetos e modelos prontos da comunidade\);

Vamos começar criando uma nova __cena 2D__ no Painel __Scene__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774092269400.png)

- Para salvar a cena, vamos até o menu __Scene__ \-> __Save Scene__ \(Um modo mais rápido de salvar é utilizando o atalho__ CTRL S__\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774092269400.png)

- Para manter nosso projeto organizado, antes de salvar a cena vamos__ criar__ uma pasta __“Scenes”__ e salvar a cena dentro dela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774092269400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774092269400.png)

- Altere o nome da Cena para __Cena\_1__ e clique em __Save \(Salvar\)__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774092269400.png)

Podemos visualizar no painel __File System__ a pasta __Scenes__ e o arquivo da __Cena\_1__ dentro dela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774092269400.png)

Agora que temos a cena criada, vamos entender o que são __Nodes \(Nós\)__ e como são utilizados pela Godot:

- Um Node \(ou Nó\) é um objeto fundamental na Godot, que pode ser um personagem, um inimigo, um obstáculo, uma luz, um elemento de cenário, um botão, um áudio, um texto ou qualquer objeto do jogo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774107031400.png)

- Na Godot, os objetos são chamados de __Nós__ porque os projetos são estruturados como uma __árvore__ com várias __ramificações__\. Cada cena representa uma árvore que pode conter múltiplos Nós, e cada Nó pode, por sua vez, conter outros Nós, formando uma hierarquia:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774108886200.png)

Os nós podem ser de diversos tipos e cada um possui propriedades diferentes\. Vamos começar com um nó do tipo__ CharacterBody2D__ que nos permite movimentá\-lo como um personagem pela cena:

- Clique no símbolo__ \+ __no painel __Scene__ e pesquise pelo nome CharacterBody2D:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774108886200.png)

- Um Node do tipo Characterbody2D não funciona sozinho\. Precisamos adicionar pelo menos dois nós importantes dentro dele: um __Sprite2D__ e um __CollisionShape2D__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774114528400.png)

- Começando pelo __Sprite2D__, vamos até o painel __Inspector__ e podemos ver diversas informações sobre este nó em específico:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774114528400.png)

- Vamos alterar a __Textura__ do Sprite utilizando o arquivo__ icon\.svg__ que vem por padrão na Godot:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774118182000.png)

Selecione agora o Node __CollisionShape2D__ e repare que agora o Inspector tem outras propriedades, como __Shape \(forma\):__

- Selecione __RetangleShape2D:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774118182000.png)__

- Ajuste a forma retangular no formato do sprite do personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774118182000.png)

- Agora vamos selecionar o Node__ CharacterBody2D__ novamente e ativar a opção __Move__ para movimentar o personagem até o centro da tela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774125424300.png)

Com o personagem em cena, vamos clicar em __Run__ para ver a cena funcionando:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774125424300.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774125424300.png)__

Finalizamos a primeira aula do módulo __Game Starter__\. Utilize os conhecimentos adquiridos até agora e adicione alguma nova funcionalidade ao personagem\.

Recursos

- Computador, internet, Godot instalado\.

