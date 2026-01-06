# __PLANO DE AULA__

Aula 09 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 2

Tipo da atividade: Online

Ferramenta\(s\): GDevelop baixado no computador

Conteúdos

- GDevelop: apresentação da plataforma\.

Objetivos

- Download do GDevelop;
- Conhecer a Game Engine;
- Compreender o conceito de "Behavior";
- Compreender “Condição” e “Reação”;
- Lógica de programação\.

Estratégias e atividades

- Hoje vamos aprender uma nova Game Engine: o GDevelop\.
	- GDevelop é um software de código aberto, o que implica que seu código\-fonte está acessível a qualquer indivíduo\. Esta característica é altamente vantajosa, uma vez que possibilita que programadores desenvolvam novas ferramentas e as incorporem ao GDevelop\.
- Link para download > [https://gdevelop\.io/download](https://gdevelop.io/download)
- Clique no “Windows”

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696207346800.png)

- Antes de procedermos com qualquer ação, é importante realizar a configuração do GDevelop para que esteja operando no idioma inglês\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696209317100.png)

- Após a conclusão da instalação e a alteração do idioma para inglês, procederemos clicando na opção__ "Build"__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696212055200.png)

- Para iniciar um novo projeto, é necessário seguir os seguintes passos: primeiramente, clique em "Create a project", em seguida, atribua um nome ao projeto\. Por fim, clique em "GDevelop Cloud" e siga os procedimentos para criar uma conta\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696212055200.png)

- O aluno tem que fornecer o nome que deseja exibir na conta, o e\-mail e a senha\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696212055200.png)
- Feito isso, basta criar o projeto\.  

- Vamos dividir a interface do GDevelop em partes distintas para melhor compreensão e organização\.
	- Parte 1: Nesta seção, teremos controle sobre as propriedades dos objetos, como ajustar altura, largura, posição e selecionar a camada em que eles ficarão posicionados\.
	- Parte 2: Esta área será dedicada à interface de desenvolvimento do jogo, onde incluiremos todas as imagens e criaremos a interface do jogo\.
	- Parte 3: Neste segmento, serão catalogados todos os objetos do jogo, como personagens, inimigos, terreno, cenário, entre outros\.
	- Parte 4: Ativar o jogo para visualização, a fim de avaliar seu progresso\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696212055200.png)

- Iniciaremos a incorporação das imagens no nosso jogo diretamente a partir da __"Assets Store"__ do GDevelop\. Será necessário pegar o personagem e o chão\.
	- Avise aos alunos que não dá para pegar as imagens que são pagas\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696212055200.png)  


- No exemplo em questão, optei por selecionar as imagens da Dungeon\. A escolha das imagens a serem utilizadas fica a critério tanto do professor quanto dos alunos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696212055200.png)

- Escolha o personagem e clique em__ “Add to the scene”__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)

- Após importar a imagem, clique em __“Back"__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)

- Agora, procederemos à busca pela imagem do chão e executaremos o mesmo processo\.
- Vamos adicionar o personagem ao nosso jogo, arrastando\-o e posicionando\-o dentro da cena\. 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)  
  


- Para aumentar o tamanho do personagem, dispomos de duas opções: podemos aumentar a largura \(Width\) e a altura \(Height\) diretamente no canto esquerdo ou ajustar as dimensões pelo quadrado\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)

- A mesma coisa será aplicada no chão\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)
- O nosso jogo ficará com a seguinte aparência aproximada\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)

- Vamos realizar uma prévia do nosso jogo para observar os resultados\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)
	- É natural que não ocorra qualquer ação, uma vez que ainda não realizamos nenhuma programação\.
- Agora, procederemos à programação para que nosso personagem inicie o movimento, utilizando as Behavior\.
	- No GDevelop, as "Behaviors" são componentes pré\-programados que oferecem uma funcionalidade específica, destinados a acelerar o processo de desenvolvimento de jogos\. Geralmente, esses comportamentos são criados com base em padrões amplamente utilizados em programação\. Para ilustrar, considere que muitos desenvolvedores iniciam suas carreiras criando jogos de plataforma\. Nesse sentido, existem comportamentos pré\-definidos disponíveis para lidar com aspectos como movimento de plataformas e interações do personagem, como caminhar e pular pelo cenário;
	- Clique __2 vezes__ em cima do __personagem__;
	- Vamos em__ Behavior__ > __Add a behavior__;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696227151400.png)

- 
	- Selecione o __“Platformer Character”__;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696242901300.png)

- 
	- Agora basta clicar em __”Apply”__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696242901300.png)  


- Vamos realizar uma prévia do nosso jogo para observar os resultados\.
- Observamos que o personagem caiu devido à ausência da Behavior de 	“platform” no chão \(Platform torna o chão sólido\)\.
	- Clique 2 vezes no chão;
	- Behavior;
	- Platform\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696242901300.png)

- Vamos realizar uma prévia do nosso jogo para observar os resultados\.
	- É perceptível que agora tudo ocorreu conforme o planejado;
	- __Observação:__ Para andar com o personagem basta utilizar as setas do teclado\.
- Para tornar nosso jogo mais envolvente, vamos adicionar dois elementos: um inimigo e um portal\.
	- __Observação: __Execute a mesma ação que realizamos anteriormente para adicionar o chão e o personagem\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696242901300.png)

- Observamos que o nosso inimigo está virado de costas para nós; vamos corrigir essa situação\.
	- Clique 2 vezes no inimigo;
	- Edit with Piskel;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696242901300.png)

- 
	- Flip Vertically;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696252267000.png)

- 
	- Temos que fazer tudo isso em todas as imagens;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696254275200.png)

- 
	- Clique em __“Save”__;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696254275200.png)

- 
	- Apply;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696258750800.png)

- Agora, procederemos à configuração para reiniciar o jogo caso o personagem entre em contato com o inimigo\. Para fazer isso, clique na opção "Events"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696260757900.png)

- Clique em "Add" e em seguida selecione "Event Group"\. Isso nos permitirá criar um grupo de eventos que nomearemos como "Personagem"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696262763400.png)

- Agora, simplesmente clique em__ "Add New Event"__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696264770500.png)

- Se repararmos agora temos um__ “Add Condition” = Condição__ e um__ “Add Action” = Reação\.__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696264770500.png)__

- 
	- __Condição:__ Uma condição é como se fosse uma pergunta que fazemos a um computador ou a um personagem em um jogo\. É como dizer: "Se algo acontecer, o que você fará?"\.
	- __Reação:__ A reação é o que acontece em seguida, dependendo da resposta à pergunta ou da condição\. É a ação que o computador ou o personagem toma com base no que aconteceu\.
	- __Exemplo:__ Imagine que estamos brincando de esconde\-esconde\. A condição é: "Se alguém me encontrar escondido, o que vou fazer?" A reação seria: "Se alguém me encontrar, vou correr e tentar chegar à base\."\.
	- Em jogos ou computadores, usamos condições e reações para fazer personagens se moverem, atacarem inimigos quando estão próximos, ou até mesmo para mudar a música de fundo quando algo emocionante acontece\. É uma maneira de ensinar ao computador ou ao personagem o que fazer em diferentes situações, como se fosse um conjunto de regras\.
- Clique em __“Add Condition”__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696264770500.png)

- Agora, vamos progredir para a programação que envolve a lógica da seguinte condição: "Se o meu jogador colidir com o BigZombie\.\.\."\.
	- Selecione o Player;
	- Pesquise “Collision”;
	- Selecione o inimigo\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696264770500.png)
- Agora, avançaremos para a lógica da ação, que consistirá em: "Reiniciar o jogo"\.
	- Clique no “Add Action”;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696264770500.png)

- 
	- Pesquise “Change the scene”;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696264770500.png)

- Realize uma prévia do nosso jogo para observar os resultados\.
	- Caso o jogador não consiga pular sobre o inimigo, vamos aumentar o __“Jump Speed” __do jogador dentro da Behavior\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696274856800.png)

- Agora, é necessário proceder com a programação do portal para que o personagem possa concluir o nível e avançar\. Isso requer a criação de uma nova "Scene" \(cena\)\.
	- Clique no canto esquerdo;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696276865200.png)

- 
	- Selecione “Add Scene”;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696276865200.png)

- Vamos incluir um texto com a palavra "Win" na nossa nova cena\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696276865200.png)

- 
	- 1: Insira o nome do texto;
	- 2: Aumente o tamanho do texto;
	- 3: Escolha a cor do texto;
	- 4: A frase que irá aparecer\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696282222300.png)

- 
	- Arraste o texto para dentro da Scene;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696284230400.png)

- Agora, prosseguiremos com a programação para permitir que o personagem avance de fase e exiba a mensagem "YOU WIN" na tela\.
	- __OBSERVAÇÃO:__ Peça aos alunos tentarem fazer sozinhos;
	- Clique em__ “Events”__;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696286239700.png)

- 
	- Selecione __“Add a new Event”__;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696286239700.png)

- 
	- Clique em __“Add condition”__;__	__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696290871800.png)

- 
	- A lógica da condição será: "Se o meu jogador colidir com o Porta\.\.\.";

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696290871800.png)

- 
	- Selecione o__ “Add action”__;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696290871800.png)

- 
	- A lógica da ação será: "Mudar de Scene";

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696290871800.png)

- Realize uma prévia do nosso jogo para observar os resultados\.  


Recursos

- GDevelop, internet, Google e computador\.

Observação

- Frequentemente, os alunos inadvertidamente deixam o jogo em execução, e quando tentam realizar a visualização prévia, encontram a mensagem "Update"\.
	- Para solucionar essa questão, basta fechar o jogo que está em execução\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702696290871800.png)

Tarefas

- Em sua residência, faça a instalação do GDevelop em seu computador, conecte à sua conta e explore a ferramenta\. Além disso, tente reproduzir o jogo que desenvolvemos durante nossa atividade em sala de aula\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

