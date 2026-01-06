![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772756374700.png)

# __PLANO DE AULA__

Aula 02 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): GDevelop baixado no computador

Conteúdos

- GDevelop: Jogo de Boat\.

Objetivos

- Utilização de Assets\.
- Mecânica de Colisões\.
- Sistema de Pontuação\.

Estratégias e atividades

Na aula de hoje, iremos criar o __Jogo do Boat__, um game onde um barco deve desviar de pedras em seu caminho enquanto atravessa um rio\.  Vamos aprender o que são__ assets __e como utilizá\-los para enriquecer nossos projetos\. Também aprenderemos sobre __colisões__ entre objetos, uma mecânica essencial no desenvolvimento de jogos\.

__START__

Vamos criar um novo projeto chamado __Jogo do Boat__ com a resolução __1280 x 720:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772756374700.png)__

Primeiro vamos adicionar os assets\. __Assets__ são todos os recursos que utilizamos em nosso jogo\. Podem ser imagens \(jogos 2D\), modelos tridimensionais \(jogos 3D\), áudio, animações, scripts, fontes e muitos outros elementos, que podem ser criados do zero ou ser baixados prontos em pacotes de assets\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772756374700.png)

Para começar, vamos adicionar o objeto __Bote__\. Lembre\-se de ir até o painel __Objetos __e clicar em __Adicionar um novo objeto__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772756374700.png)

O barco contém três imagens: reto, esquerda e direita\. Para adicioná\-los, selecione a opção __Importar Imagens__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772772342800.png)

Vá até a pasta dos assets e selecione as imagens do barco,  uma de cada vez, adicionando assim três animações::

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772772342800.png)

__Renomeie__ as animações com os respectivos nomes e __aplique__ as alterações:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772772342800.png)

Vamos prosseguir com a programação do movimento do Boat na aba __Eventos__\. 

Antes da programação em si, vamos criar um __Grupo de Eventos__, que é uma forma de organizar melhor nossos eventos\. Clique em __Adicionar__ \-> __Grupo de Eventos__\.

Vamos chamá\-lo de __Movimento e Animação:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772778478500.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772778478500.png)__

Nosso primeiro comando terá a seguinte lógica:

- Quando pressionarmos a __tecla esquerda__, o Boat deverá se __mover para a esquerda__ e devemos alterar também sua __animação__ para __esquerda:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772778478500.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772778478500.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772778478500.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)__

- Repita o processo para a __direita__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)

- Precisamos indicar que, ao não estar apertando nenhuma tecla, o bote volte para a animação __reto\.__ Para isso, usamos as mesmas condições de pressionamento de tecla, porém, __invertemos a condição__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)__

Agora, vamos adicionar o objeto __Pedra__ e iniciar sua programação:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)

- Primeiro, vamos __criar um temporizador__ no__ início da cena__, que será responsável por criar as pedras ao longo do tempo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772788023800.png)

- Para criar as pedras de forma aleatória, vamos usar o comando __RandomInRange __para criar um número aleatório entre __1 e 3 segundos__\. Quando o temporizador for maior que esse número, iremos criar novas pedras:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772803691400.png)

- Quando essa condição for atendida, utilizaremos o comando __Criar Objeto__, especificando a __posição__ onde a pedra será criada\. Para tornar o jogo mais desafiador, vamos __aleatorizar__ a posição da pedra no __eixo X__, fazendo com que ela apareça em qualquer lugar entre os cantos esquerdo e direito da tela:
- Precisamos __resetar__ o temporizador, para que outra pedra seja gerada e assim sucessivamente:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772806316100.png)

- Por último, vamos aplicar a todas as pedras uma __força__ no __eixo Y__, fazendo com que a pedra gerada se movimente na direção do barco, simulando a correnteza:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772808323300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772808323300.png)

Voltando à cena, vamos alterar a __cor de fundo__ da cena para azul, simulando um rio:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772808323300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772808323300.png)

Arraste o __barco__ até a cena e __centralize\-o__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772808323300.png)

Teste o jogo, clicando no botão __Visualizar__ no topo da cena\. O barco já pode ser controlado e as pedras são geradas aleatoriamente, resta agora detectarmos quando acontece a colisão entre esses objetos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772808323300.png)

Em desenvolvimento de jogos, os objetos detectam a colisão entre si a partir de __colisores__ e no caso do desenvolvimento de jogos 2D, colisores são formas geométricas simples, como quadrados, círculos, triângulos ou até mesmo formas mais complexas como polígonos\. 

Quando criamos um objeto no GDevelop, um colisor é automaticamente criado com base na imagem escolhida \(ou criada\), mas nós iremos criar nossos próprios colisores:

- Para acessar o colisor do barco, vamos até as configurações do objeto e clicar na opção __Editar máscaras de colisão:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)__

- Primeiro vamos editar a imagem do barco __reto__\. Clique em __Use uma máscara de colisão personalizada__, pois vamos editar nossa máscara manualmente:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)__

- __Desmarque __as opções de compartilhar as máscaras de colisão, pois vamos fazer alterações nas três imagens separadamente\. Com o __clique do mouse__ os __edite os pontos__ da máscara de modo a contornar o barco\. Note que não precisamos incluir os remos na máscara:

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)

- Repita o processo para as __outras imagens do barco__ e para a __pedra__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)

Antes de programar as colisões, vamos criar um __sistema de pontuação__ para que, a cada pedra superada, o jogador ganhe um ponto e se colidir com qualquer pedra, o jogo reinicie e a pontuação seja zerada\.

Para __criar__ ou __manipular__ um valor, seja ele um número, texto ou boleano \(verdadeiro ou falso\), utilizamos __variáveis\.__ No GDevelop, podemos criar __variáveis globais__ que podem ser utilizadas em qualquer cena, durante todo o jogo\. Para a pontuação, criaremos uma váriavel global do tipo __número__:

- Clique no ícone do __Gestor de Projeto__ no canto superior direito da tela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)

- Selecione a opção __Variáveis Globais:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)__

- Crie uma variável do tipo __número__ com valor __0 \(zero\):__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772819480900.png)__

Agora que já temos a variável Pontuação, precisamos criar um objeto para mostrá\-la ao jogador:

- Utilizaremos um objeto do tipo __Texto__\. Podemos chamá\-lo de __Texto\_Pontuação:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772835309200.png)

- Ajuste as __propriedades__ do texto como fonte, cor e tamanho como desejar:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772835309200.png)

- Arraste o objeto__ Texto\_Pontuação__ para a cena, em uma posição que não atrapalhe o jogador:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772835309200.png)

Para finalizar, vamos programar o sistema de pontuação na aba __Eventos__:

- Primeiro, garantimos que o objeto __Texto\_Pontuação__ seja atualizado o tempo todo com o valor da variável __Pontuação__, assim, sempre que alterarmos a variável, o valor atualiza na tela também:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772835309200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772835309200.png)

- Quando uma pedra ultrapassa o final da tela, ou seja, a posição __720__ no __eixo Y__, o jogador ganha um ponto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772835309200.png)

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772846730100.png)

- Precisamos também __excluir __a pedra em seguida, para que somente um ponto seja computado:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772846730100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772848738900.png)

- Por último, sempre que o barco __colidir__ com a pedra, a potuação é zerada e o jogo __reinicia__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772850959700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772852968300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772854976800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702772856984500.png)

Assim, reiniciamos a cena e a pontuação será zerada, finalizando assim o nosso jogo do Boat\. 

Que outros recursos poderíamos incluir em nosso projeto? A partir deste ponto, tente criar mais desafios e diferentes funcionalidades\. Altere e melhore o cenário, adicione novos barcos, torne o jogo mais atraente e divertido\! 

Recursos

- GDevelop, internet, Google e computador\.

Observação

- Caso o professor possua alguma dúvida, disponibilizei o jogo completo para referência: [https://drive\.google\.com/file/d/1b5HSnSnbfU7NVW0b6nazNg4DVXcEu4U9/view?usp=share\_link](https://drive.google.com/file/d/1b5HSnSnbfU7NVW0b6nazNg4DVXcEu4U9/view?usp=share_link)

Tarefas

- Tente reproduzir o jogo que desenvolvemos durante nossa atividade em sala de aula, modificando os ASSETS e adicionando mais coisas\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

