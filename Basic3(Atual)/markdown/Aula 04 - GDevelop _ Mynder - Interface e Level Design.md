# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773199257400.png)

# __PLANO DE AULA__

Aula 04 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Computador

Ferramenta\(s\): GDevelop baixado no computador

Conteúdos

- GDevelop: Jogo de Plataforma \- Mynder’s Mission\.

Objetivos

- Interface;
- Sistema de Vida;
- Elementos de Cenário\.

Estratégias e atividades

Na aula de hoje, vamos criar um __sistema de vida__ para o Mynder e o primeiro elemento de__ interface__: a barra de vida\. Além disso, vamos aprender sobre elementos de __cenário__, como obstáculos, itens e portas e como interagir com eles\.

START

Na última aula, criamos a camada Interface\. Vamos adicionar um novo objeto nesta camada, do tipo Sprite e importar a imagem da __Barra de Vida__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773201268100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773203274800.png)

- Arraste a imagem para a cena e altere para a camada __Interface__ no painel __Propriedades:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773203274800.png)__

- Agora mesmo que o personagem se movimente, os elementos da interface permanecem na mesma posição\. Para visualizar isso, vamos adicionar ao Mynder o comportamento__ SmoothPlatformerCamera__, que fará a __câmera__ seguir o personagem de forma suave:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773208512800.png)

- Agora vamos editar o fundo, utilizando o __TilesetPiece19__\. Devemos cobrir toda a área da cena e lembre\-se de incluir o objeto na camada do __Fundo__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773210536800.png) 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773213521600.png)

Já temos a imagem da barra de vida, mas para que ela funcione como uma barra que pode aumentar e diminuir, criaremos um novo objeto do tipo __Barra de Recursos:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773214551600.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773216521100.png)__

- Vamos renomear o objeto para __HP__ e arrastá\-lo para a cena\. Ajuste a imagem da __Barra de Vida__ para se adequar ao HP:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773218521700.png)__

- Ao editarmos o objeto __HP__, podemos configurar as informações da barra de recursos:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773220520800.png) __

Já temos a barra de vida, mas precisamos atualizar seu valor constantemente com a vida do personagem:

- Vamos adicionar o comportamento __Health__ ao Mynder e assim temos um __Sistema de Vida__ completo com Health Points \(Pontos de Vida\), Damage \(Dano\), Armor \(Armadura\) e Shield \(Escudo\);
- __Damage cooldown__ é o tempo antes do personagem perder pontos de vida novamente, para evitar bugs e ataques imprecisos\.
- Em __Starting health \(Vida Inicial\)__ e __Maximum health \(Vida Máxima\)__, o valor de __100__ é o mesmo da barra de vida \(HP\)\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773222521700.png)__

Para testarmos o __Sistema de Vida__, precisamos de elementos que causem __dano__ ao personagem\. Vamos para a etapa de __Level Design__, onde criaremos o cenário do jogo\.

Ao inserir um elemento, ajuste seu tamanho à __grade__ para manter a consistência do cenário:

- O __cenário inicial__ deve ser construído para que o jogador __aprenda__, então os desafios devem ser __gradativos__, ou seja, inicie com obstáculos simples que vão exigir apenas movimentação básica e saltos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773225522000.png)

- Depois que o jogador já se acostumou com os obstáculos iniciais, vamos aumentar um pouco o desafio\. Crie __espinhos__ que causarão dano ao Mynder, caso toque neles:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773227521600.png)

- Aumentamos um pouco mais a dificuldade inserindo um obstáculo que se move e exige mais habilidade do jogador\.
- Insira o objeto __Saw \(Serra\)__\. Em Rotação, __gire 90°__ para apontar para cima:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773229519700.png)

- Adicione o comportamento __EllipseMovement__ à Serra, com o __valor 80__ apenas no __eixo X__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773232521300.png)

Assim como os obstáculos, podemos ter outros tipos de interação com o cenário, como __portas__ para acessar outras áreas:

- Vamos criar um novo objeto chamado __Door __\(Porta\) e inserir a imagem da porta da pasta de Assets e depois posicioná\-lo na cena:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773234520900.png)__

Agora que o cenário está montado, podemos começar a __programar__ para que tudo funcione corretamente:

- Vamos até a aba __Eventos__\. Primeiro, vamos garantir que a __barra de vida \(HP\)__ do Mynder seja atualizada de acordo com os__ Health Points__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773236520800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773238521500.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773240521800.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773241521600.png)__

- Sempre que o Mynder __colidir__ com um __espinho__, aplicamos uma quantidade de __dano__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773241521600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773241521600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773247270300.png)

- Vamos repetir o processo para a __cerra__, aumentando o __valor de dano__ aplicado:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773249278400.png)

Por fim, devemos verificar quando a __vida__ do personagem chega a __0 \(zero\)__, decretando a __derrota__ do jogador:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773251299100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773251299100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773254110500.png)

Quando esta __condição__ é atendida, temos uma série de__ ações__ para executar:

- Primeiro, desativamos a __movimentação__ do Mynder e a __troca automática de animações__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773256117700.png) 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

- Depois, ativamos a animação __Death__ e depois de alguns segundos __reiniciamos a cena__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

Estamos quase lá\! Com a primeira fase pronta e um sistema de vida funcional, só falta escolher uma__ trilha sonora__ épica que combine com o clima de batalha do nosso jogo:

- Vamos pesquisar na __loja de recursos__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773257624800.png)

- Experimente ouvir os diferentes sons disponíveis e escolha o que lhe agradar \(mas lembre\-se de que o som deve combinar com a __atmosfera__ do jogo\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773273424500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773273424500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773276725400.png)

Concluímos a segunda aula do projeto Mynder’s Mission e já temos a primeira fase com obstáculos e um sistema de vida\. Na próxima aula, vamos tornar a jornada do Mynder mais desafiadora, criando inimigos pelo cenário\. Para que ele possa enfrentar esses novos desafios, vamos desenvolver um sistema de combate\!__ __

Recursos

- GDevelop, internet, Google e computador\.

Observação

Tarefas

- Na próxima aula iremos criar inimigos\! Crie ideias de um ou mais inimigos que poderíamos ter no jogo\. Planeje, desenhe ou até mesmo tente criar esse inimigo no GDevelop em casa\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\. No caso de desenho ou escrita à mão, trazer na próxima aula\. 

