# __PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

Conteúdos

- Tipo de jogo: Infinity Run;
- Criar nó;
- Criar Cena;
- Comunicação de Scripts\.

Objetivos

- Gerando obstáculos e colisores parte 2\.

Estratégias e atividades

- Crie uma nova cena > other e pesquise por node:
	- Após criar sua nova cena, renomeie para PipeSpawner\. 
- Criando um novo nó:
	- Na cena ground pesquise por __Timer __e renomeie para SpawnTime, dentro dele vamos mudar o wait time para 2 e vamos criar um script para ele\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455658335100.png)

- Crie uma nova __cena2D __e renomeie para __PipePair__:
	- Dentro dela crie um novo nó e pesquise por __Area2D__ e renomeie para __TopPipe__\. Depois duplique este nó e renomeie para __BottomPipe__, e dentro de cada um dos dois adicione um novo nó e pesquise por sprite2D e um CollisionShape2D\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455661512000.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455664512600.png)__

- Dentro do sprite do TopPipe arraste o asset do cano e vamos configura lo agora:
	- Lembre\-se de arrumá\-lo na cena e ajustar os colisores\.
- Em__ Transform Do TopPipe__:
	- __Rotation mude para 180°__;
	- __Position mude para \-300__\.
- Agora dentro do sprite do BottomPipe arraste também o asset do cano e vamos configurá\-lo:
	- Lembre\-se de arrumá\-lo na cena e ajustar os colisores\.
- Em__ Transform do BottomPipe__:
	- __Position y mude para 300__\.

	

- Crie um novo nó dentro de PipePair Area2D e renomeie para scored:
	- Dentro deste nó adicione um CollisionShape2D e ajuste ela assim: 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455675521600.png)

- Crie um script do Pipepair:
	- Use os códigos da aula09 no github\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455676521500.png)

- Agora vamos emitir o sinal do TopPipe, BottomPipe e Scored:
	- Clique em __TopPipe__, depois em __node __\(do lado do inspetor\) em seguida em __body\_entered __e clique em __pick __e escolha __\_on\_body\_entered __e depois __connect__\.
- Agora em __BottomPipe __clique em __node > body\_entered > pick > \_on\_body\_entered > connect__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455678523500.png)

- Agora em __Scored __clique em __node > body\_entered > pick > \_on\_point\_scored > connect__\.
- Script PipeSpawner:
	- Lembra do script que criamos então agora é a hora de colocarmos as coisas dentro dele entre no github e copie os códigos\.
- Instancie a scene PipeSpawner na cena main\.
- Agora para não criar um pipe a mais vamos colocar um novo nó em __pipe\_pair __chamado __visibleOnscreenNotifer 2D __depois vamos clicar neste nó e vamos em __node > screen\_exited > connect__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455681700600.png)

Recursos

- Computador, internet, Godot instalado\.

Observação

- Nada a observar\.

Tarefas

- Pesquisar jogos de plataforma estilo infinity run e trazer pelo menos o nome de um jogo e em qual plataforma ele foi feito\.

