# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602551544600.png)

# __PLANO DE AULA__

Aula 22 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Timeline e Cutscenes

Objetivos

- Criação de Cenas com Timelines\.

Estratégias e atividades

Agora que o nosso jogo base está concluído, vamos aprender o que são cutscenes e a ferramenta Timeline e como podemos utilizá\-la para adicionar uma cena inicial antes de assumir o controle do personagem\. Nesta etapa, aprenderemos a manipular os objetos para criar uma cena de introdução\.

__START__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602551544600.png)

Por muitos anos, as cutscenes em jogos eram criadas em softwares externos e reproduzidas antes ou depois de uma fase, ou no início do jogo\. Hoje, no entanto, utilizamos cenas em tempo real, que se integram de forma mais fluida à jogabilidade, tornando a experiência mais imersiva e contínua\.

Na Unity, contamos com a ferramenta Timeline, que possibilita criar sequências de ações para objetos e câmeras, permitindo a construção de cutscenes que podem ser até mesmo interativas\. Vamos começar criando a timeline para nossa cena inicial:

- No painel __Window__, clique em __Sequencing__ \-> __Timeline__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602551544600.png)

- Crie um novo objeto vazio, que será responsável por controlar a cutscene inicial\. Vamos chamá\-lo de __Timeline\_Controller:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602551544600.png)__

- Selecione o objeto __Timeline\_Controller__ e crie uma nova timeline:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602567193900.png)

Para criar nossa cena, vamos utilizar objetos do próprio mundo do jogo, como o player, o carro e algumas câmeras\. Para aprendermos como utilizar a timeline, vamos fazer uma cena como exemplo, com um título para o jogo, mas fique a vontade para criar sua própria introdução\.

Primeiro vamos montar a introdução na sequência: a frase “Mynds presents” \(Mynds apresenta\) e depois o título do jogo “Underground”:

- Crie um novo painel na HUD chamado __Starter\_Scene__\. Altere a __SourceImage__ para __Square__ e mude a __cor de fundo__ para __preto__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602573127700.png)

-  Dentro do painel, crie um__ TextMeshPro__ com o texto __“Mynds Presents”__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602573127700.png)

- Vamos criar também um novo __TextMeshPro__ na HUD que será responsável pelo título do jogo: __Underground__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602577536000.png)

Além dos elementos de HUD, precisaremos também de duas__ câmeras__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602577536000.png)

Vamos chamá\-las de Cutscene\_Camera e Cutscene\_Camera2:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)

Agora que temos todos os elementos da cena, vamos voltar à timeline e criar uma nova __Track__, que são faixas onde cada elemento da cena será trabalhado:

- Crie uma nova __Animation Track__ \(Faixa de Animação\) para o fundo escuro __Starter\_Scene__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)

- Uma forma mais rápida de adicionar um objeto diretamente é arrastando o objeto até a timeline\. Vamos fazer isso com o TextMeshPro __Presents:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)__

- Vamos incluir também o TextMeshPro __Underground:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)__

Vamos começar escondendo os Texts __Presents__ e __Underground:__

- Clique em __Start Recording__ \(Iniciar Gravação\)\. A partir desse momento, qualquer alteração no objeto será alterada na timeline\. Vamos alterar a __opacidade da cor__ do texto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602582588300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602598356700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)

- Mova a __paleta__ até o __frame 100__ e volte o valor da __opacidade__ para o __máximo__, assim o texto irá aparecer gradualmente:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)__

Podemos ver uma prévia ao clicarmos no símbolo __Play__\. Perceba que o texto surge com uma __animação da opacidade__, que foi de __0__ a __255__ em __100__ frames\.

- Mova a paleta por mais __100 frames__ \(até o __frame 200__\) e insira o valor da opacidade como __255__ novamente\. Depois, mova mais __100 frames__ \(__frame 300__\) e volte a opacidade para __0__\. Assim, o texto surge, permanece por um tempo e depois desaparece:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)

Agora vamos animar o Text __Underground__, que começa transparente e se mantém assim até o__ frame 400__, aparecendo totalmente no __frame 500__\. Depois de mais 100 frames \(__frame 600__\) irá desaparecer:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)

Vamos fazer com que o fundo escuro desapareça antes do título, revelando a cidade do jogo:

- Mova a paleta até o __frame 550__ e indique a __opacidade__ do fundo no máximo\. Depois avance __100 frames__ \(__frame 650__\) e mude a opacidade para__ 0__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)

A partir de agora vamos trabalhar com as câmeras e elementos do cenário, como o player e um carro\.

Trabalhar com câmeras em cutscenes se assemelha a dirigir a cena de um filme, onde precisamos posicioná\-las e criar sequências de movimento:

- Vamos começar posicionando a câmera no alto, para capturar um plano amplo da cidade:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602600537100.png)

- A câmera fará um movimento vertical para baixo \(posteriormente, mostraremos a chegada do veículo do jogador neste momento\)\. Crie uma nova __Animation Track__ para a __Cutscene\_Camera__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602614153100.png)

- Clique em __Starting Recording__ e mova a paleta até o __frame 420__\. Altere a posição da câmera no __eixo Y__\. Esta será a posição inicial da câmera\.

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602614153100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602619128400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602619128400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602619128400.png)

Observe que agora a câmera se move para baixo e, para definir até onde queremos exibir a imagem dessa câmera específica, é necessário adicionar uma __Activation Track__ \(Faixa de Ativação\), que é uma faixa responsável por ativar ou desativar um objeto em cena:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602619128400.png)

- Deixe a câmera __ativa__ até o __frame 600__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602619128400.png)

Ao final a cena deve terminar com algo parecido com isso:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602619128400.png)

Na próxima aula iremos fazer a segunda parte da cena, com uma transição para o início do jogo\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Sem tarefa\.

