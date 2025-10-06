# __PLANO DE AULA__

Aula 13 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Tipo de jogo: Infinity Run;
- Criar nó;
- Criar Cena;
- Comunicação de Scripts\.

Objetivos

- Finalizando projeto;
- Criando pontuação;
- Criando GameManager\.

Estratégias e atividades

- Crie um novo __nó \(node\)__ na cena__ main__ > pesquise por __Game__:
	- Renomeie para __GameManager__ e mova ele para cima de __BackGround__ e depois crie um script para ele\.
		- Observe que __ocorreram mudanças nos outros scripts__ se atente\-se a isso no github\.

Bird\.gd

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455883161900.png)

pipe\_spawn\.gd  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455887163500.png)  


- Continuando na __main__, Mova o __bird__ para baixo do __PipeSpawner__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455889161300.png)

- Criando uma nova cena:
	- Crie uma nova Cena > Other > CanvasLayer\.	
- Crie um novo nó \(node\):
	- Pesquise por MarginContainer e use essas configurações\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455893335100.png)__

- Adicionando outros nós:
	- Adicione todos esses nós na hierarquia e os organize assim:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455895335500.png)
- __PointsLabel:__
	- A font e o asset que temos em font precisamos somente arrastá\-la:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455896336100.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455897333600.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455899333900.png)__

- __VBoxContainer:__
	- Usando o botão __do lado__ de visualizar centralizamos:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455900558400.png)__

Para ficar assim:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455909725200.png)__

- __Texture Rect:__
	- Arraste o asset gameover para dentro de texture:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455910725500.png)__

- __Button:__
	- A font e o asset que temos em font precisamos somente arrastá\-la:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455912725500.png)  
__

- __Não se esqueça de esconder o VboxContainer:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455914725200.png)__
- Criando o script de UI:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455915726100.png)

- Comunicação do botão:
	- Clique no botão vá em __node__ e __pressed__ e depois__ conectar__\.__ __
	- Isso vai gerar a comunicação e este trecho do script:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455917724800.png)__

- Instanciando UI:
	- Vá na cena __main__ e com o botão direito em cima dela__ instancie__ a cena__ UI__\.

__	__

Recursos

- Computador, internet, Godot instalado\.

Observação

- Nada a observar\.

Tarefas

- Pesquisar o que é uma HUD de um jogo e dar exemplo de pelo menos dois jogos\.

