# __PLANO DE AULA__

Aula 10 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

Conteúdos

- Tipo de jogo: Infinity Run;
- Importar assets;
- Criar um nó;
- Configuração do Projeto;
- Criar Cena\.

Objetivos

- Preparando o projeto;
- Programação inicial do personagem\.

Estratégias e atividades

- PARA ESTE PROJETO USE O GODOT 4\.1
- Importando assets:
	- Após criar seu projeto no Godot, vá até as pastas e arraste até lá sua pasta com os assets disponibilizados\.
- Criando um nó principal:
	- Vá até o Create__ Root Node__ e clique em other node e após abrir a caixa de pesquisa procure por __Node__, e dê Enter, renomeie o que foi criado para __main__\.
- Salvando o projeto:
	- Aperte__ Ctrl \+ S __e crie uma nova pasta com o nome__ Scenes__\.
- Definindo como cena principal:
	- Vá até onde estão seus arquivos e clique na pasta Scenes que foi criada, depois com o botão direito em__ main __clique em __set as main Scene__\.
- Definindo dimensões da tela:
	- Em __Project__ clique em __Project Settings > Display > Window, __defina __Viewport Width 288__ e __ViewportHeight 512__\. __Depois em Stretch > mode __mude para__ viewport__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455265210500.png)

- Criando nova Cena:
	- Em __Scene __> __New Scene__
- Criando novo nó:
	- Pesquisamos por__ Character Body 2D__ e mudamos o nome para__ Bird, __depois clicamos com o botão direito em cima de__ Bird__ e pesquisamos por __Sprite 2D__ e em seus arquivos arraste o asset __yellowbird\-midflap\.png __para dentro do __Sprite 2D__, depois mude em__ Texture o filter para Nearest\.__

__	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455269213700.png)__

- Adicionando colisor:
	- Em Bird pesquise por __collision shape 2D__ e dentro dela mude para o shape para __capsule Shape 2d__ e arrume de acordo com o sprite do bird\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455272364500.png)

- Adicionando Animação:
	- Em Bird\(Node\) pesquise por __AnimationPlayer__\.
- Adicionando Inputs:
	- Em __Project Settings__ > __InputMap __>__ add new action__:__ __adicione uma ação nova chamada jump, e no símbolo de mais \(\+\) ao lado direito clique e pesquise pela tecla space\. 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455275369500.png)

- Adicionando o bird na Scene main:
	- Abra a cena__ main__ e depois clique com o botão direito e procure por __instantiate child scene __e clique na cena bird\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455277365500.png)

- Criando o Script:
	- Clique uma vez em bird e depois uma vez em __script __\(uma folha com um pequeno \+ ao lado de filter nodes\)\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455279367000.png)
- Adicionando uma câmera:
	- Na cena \(main\) clique com o botão direito em main e procure por câmera 2D\.
- Escrevendo o Script:
	- Copie o script do bird no github\. Entender o código e explicar para os alunos o passo\-a\-passo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455280535800.png)

- Criando o BackGround:
	- Na cena \(main\) pesquise por __sprite 2D__ e renomeie para Background depois arraste o asset Background para dentro de texture e por fim mova esse nó para cima de Bird\.
- Adicionando animação \(idle\):
	- Em bird clique no Nó animation player e lá embaixo \(“Terminal”\) vai aparecer uma frase __animation __clique nela e adicione uma nova animação __idle__\.
	- Depois clique em __Add Track > Property Track > sprite 2D > position__\. Clique com o botão direito na linha azul criada e adicione uma chave e então mova a linha para 0,5 e insira uma nova chave\.
	- Clique na última chave criada e mude o valor dela no inspetor para __y = \-10px__\.
	- E não se esqueça de colocar a animação em looping \(fica no lado direito do terminal de animação\)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455283538200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455284536300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455287539400.png)

- Adicionando animação \(flap\_wing\):
	- Em bird clique no Nó animation player e lá embaixo \(“Terminal”\) vai aparecer uma frase __animation __clique nela e adicione uma nova animação __flap\_wing__\.
	- Depois clique em __Add Track > Property Track > Sprite2D > Texture__\.
	- Clique com o botão direito na linha azul criada e adicione uma chave __0\.0 \(__Dentro desta chave coloque o yellowbird\-downflap\.png__\)__\. Agora arraste a barra para __0\.1 \(__Dentro desta chave coloque o yellowbird\-midflap\.png__\)__ e insira uma nova chave\. Por último para __0\.2 \(__Dentro desta chave coloque o yellowbird\-upflap\.png__\)__\.
	- E não se esqueça de colocar a animação em looping \(fica no lado direito do terminal de animação\)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455288962400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455289964100.png)

Recursos

- Computador, internet, Godot instalado\.

	

Observação

- Nada a observar\.

Tarefas

- Jogar flappy bird no celular\.

OBS\.: é um exemplo de jogo infinity run que usaremos na aula\.

