# __PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Interface do jogo\.

Objetivos

- Entender o que é uma GUI \(Graphic User Interface\)
- Criar elementos de interface\.

Estratégias e atividades

Na aula de hoje, vamos entender o que é uma interface e como utilizar seus elementos em jogos para fornecer feedback visual ao jogador, enriquecendo a jogabilidade e aumentando a imersão\.

START

Quando falamos de interface no desenvolvimento de jogos, estamos nos referindo à GUI \(Graphic User Interface\), ou Interface Gráfica do Usuário\. Ela é composta por elementos visuais que exibem informações importantes para o jogador durante a partida, como barras de vida, pontuação, mapas e setas indicando o caminho, textos contendo diálogos ou missões entre outros elementos visuais\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953133313100.png)

Vamos começar pelos __Assets__, os recursos que precisamos para a criação da interface\. Primeiro, vamos importar \(ou criar\) a imagem da barra de vida:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953147578400.png)

É importante que a imagem tenha uma área vazada transparente para inserirmos a barra de vida no fundo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953149585600.png)

Após criar a imagem, vamos importar no nosso projeto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953151594000.png)

Assim como quase todos os elementos do nosso jogo, a interface é uma cena que será instanciada na cena principal\. Vamos criar uma nova cena do tipo interface\. Altere o tipo do nó para __Canvas Layer__, que é o nó responsável por manter os elementos na tela \(na frente da câmera\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953153601700.png)

Dentro da HUD, vamos adicionar dois nós do tipo Sprite2D\. O primeiro irá conter a imagem da barra de vida que importamos antes:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953153601700.png)

O segundo Sprite 2D se chamará __LifeBar__\. Não precisamos importar uma imagem e sim criar um retângulo para simular a barra\. Uma forma simples de fazer isso é criando um __Canvas Texture __no lugar da textura:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953159135200.png)

Precisamos fazer alguns ajustes no CanvasTexture:

- No Inspector, vá até __offset __e desmarque a opção __centered__, assim podemos diminuir a barra de vida da direita para a esquerda;
- Ajuste o Canvas Texture na posição mais próxima possível da área vazada\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953161142900.png)

- Para alterar a cor da barra, ainda no Inspector, vá até __Visibility__, em seguida __Modulate__ e altere a cor:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953165209400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953165209400.png)

Agora que temos a cena pronta, vamos criar um novo __script __para controlar a interface:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953169224400.png)

Insira a interface na cena principal e teste:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953183013900.png)

Agora podemos fornecer informações para o jogador, deixando o jogo mais dinâmico e 

rico visualmente\. Até a próxima aula\!

Tarefas

- Desafio para casa:
	- Tente criar outro elemento de interface, como por exemplo uma barra de stamina e adicione na interface\.

