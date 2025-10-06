# __PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

Conteúdos

- Tipo de jogo: Infinity Run;
- Comunicação de Scripts;
- Criar Cena;
- Criar nó\.

Objetivos

- Gerando obstáculos e colisões\.

Estratégias e atividades

- Crie uma nova __cena 2D__:
	- Após criar sua nova cena, renomeie para ground\.
- Criando um novo nó:
	- Na cena ground pesquise por __área 2D__ e renomeie para Ground1\. Faça isso novamente e renomeie para Ground2:

	

- Criando um __Sprite 2D__ e um __Collision Shape2D__ dentro do Ground1 e do Ground2:
	- Dentro dos dois Sprites coloque o asset __base\.png__ e coloque uma ao lado da outra na sua cena para fazer a parte de cima do jogo;
	- Lembre\-se de ajustar os colisores na parte verde do sprite \(__base\.png__\)\.

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455481052500.png)

- Crie um script para o ground e Altere o do player:
	- Use o script que está no github na branch \(Aula 02\);
	- Vale lembrar que o script do player também sofre alterações\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455487054000.png)

bird\.gd

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455496196200.png)

- Instanciando o Cena \(ground\) como um filho da main:
	- Volte para a cena main e clique com o botão direito em __main > instantiate child Scene > cena ground __e ajuste como o print\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455504320600.png)__

- Na Cena \(Ground\):
	- Clique no __Ground1 __e do lado do inspetor tem o __node__ clique nele e procure __body\_entered \(body:node 2D\) __clique com o botão direito > __conectar__\.
	- Dentro dessa nova caixa aberta em Receiver method renomeie para __\_on\_body\_entered__ e clique em __connect__\.
	- Agora clique no Ground 2 e faça a mesma coisa, só que agora __não__ troque o nome para__ \_on\_body\_entered__ mas sim clique na caixa __escolher \(change\)__ ao lado e procure por \___on\_body\_entered __que você já havia criado\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780455507322200.png)

Recursos

- Computador, internet, Godot instalado\.

Observação

- Nada a observar\.

Tarefas

- Trazer seus próprios assets feitos no Aseprite:  
BackGround\.png

Passarinho\.png \(com a animação de asa para cima e para baixo\)

Canos/Pipes\.png

