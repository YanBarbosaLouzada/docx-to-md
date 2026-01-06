# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773005754100.png)

# __PLANO DE AULA__

Aula 03 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Computador

Ferramenta\(s\): GDevelop baixado no computador

Conteúdos

- GDevelop: Jogo de Plataforma \- Mynder’s Mission\.

Objetivos

- Criação do Projeto e Pacote de Assets;
- Movimentação Básica;
- Ajustes Iniciais da Cena\.

Estratégias e atividades

Até aqui, exploramos diversos aspectos do desenvolvimento de jogos no GDevelop, como a criação de objetos, uso de comportamentos, movimentação, controle de animações, colisões e manipulação de cenas\. Agora, chegou a hora de aplicarmos todos esses conceitos na criação de um jogo de plataforma, onde utilizaremos esses elementos e muito mais\.

START

Nosso projeto se chamará __Mynder’s Mission__, um jogo de plataforma onde o robô Mynder deve superar os desafios dentro de um laboratório tomado por inimigos e restaurar o sistema:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773009645700.png)

Vamos criar um novo projeto e ajustar a resolução para __640 x 480:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773011647700.png)__

Começamos pelas configurações iniciais:

- Primeiro, vamos alterar o nome da cena\. Clique no ícone do __Gestor de Projeto__ e em __Cenas__, renomeie a cena para __Fase 1:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773013647200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773015645900.png)

 

- Baixe o pacote de assets __Sci Fi Lab__ disponível na __Loja de Ativos__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773018645000.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773020645700.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773023645800.png)__

- Agora, todos os objetos deste __pacote__ estão disponíveis na aba de objetos, como personagens, inimigos, obstáculos, itens e peças de cenário\. Para organizá\-los, vamos criar __Pastas__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

- Mas nosso personagem principal é o __Mynder__, então vamos criá\-lo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

Vamos adicionar todas as animações do Mynder uma a uma:

- __Idle: __Parado \- Frame__ 1__;
- __Run: __Movimentando \- Frame __2__;
- __Shoot: __Atirando \- Frame __3__;
- __Death: __Morrendo \- Frame__ 4__ a__ 8__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

Antes de adicionar o Mynder em cena, precisamos de um cenário inicial\. Para facilitar a construção do cenário, vamos ativar as linhas de grade:

- No canto superior direito, clique no __símbolo da grade \#__ e depois em __Mostrar grade__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

- Agora, vamos utilizar o __GroundTile__, um sprite em grade que podemos redimensionar, facilitando a criação do chão:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

- Adicione ao GroundTile o comportamento de __Plataforma__, para que ele seja tratado como um chão que o Mynder pode pisar e se movimentar:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)

Agora podemos adicionar o __Mynder__ na cena\.

- Adicione o comportamento __Personagem de Plataforma__ para que possamos controlar o Mynder\.\. Teste a cena clicando em __Visualizar__ e perceba que o personagem cai, pode se movimentar pelo chão \(setas direcionais\) e pode pular\(tecla espaço\):

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)__

- Para que as __animações básicas__ do Mynder funcionem corretamente, vamos adicionar outro comportamento chamado __PlatformerCharacterAnimator__\. Assim, as animações __Idle__ e __Run__ já funcionam e o personagem é __invertido horizontalmente__ sempre que mudamos de direção:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773025645800.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773041467900.png)__

Agora que nosso personagem já tem a movimentação básica, vamos fazer alguns ajustes nas __Camadas__ em nossa cena:

- No GDevelop, a exibição dos elementos é definida pela__ ordem Z__\. Assim, um elemento com ordem Z de __valor 1__ está à frente de outro objeto com ordem Z de__ valor 0__, porém, sua utilização é útil para uma interação simples entre dois ou mais objetos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773044540600.png)

Outro modo de separar os objetos em __planos diferentes__ é a utilização de __Camadas\. __Pois, desta forma, podemos aplicar __configurações específicas__ para um grupo de objetos:

- Por padrão, temos a __Camada base__ \(onde boa parte do nosso jogo funcionará\) e uma __Cor de fundo__, que pode ser alterada:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773046607200.png)

- Vamos criar a camada __Interface__, onde ficarão alguns elementos visuais como a __barra de vida__\. Criaremos também a camada __Fundo__, onde ficará o plano de fundo do nosso cenário\. Note que a __ordem entre as camadas__ foi alterada\. A interface fica acima das outras, enquanto o Fundo fica por último:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773049815600.png)

Concluímos a primeira aula do projeto Mynder’s Mission\. Na próxima aula, vamos focar na criação da interface do jogo e no desenvolvimento do sistema de vida do personagem\. Além disso, aprenderemos a criar elementos de cenário, obstáculos e portas, aprimorando ainda mais a aventura do Mynder\!

__ __

Recursos

- GDevelop, internet, Google e computador\.

Observação

Tarefas

- Agora que completamos a base do projeto Mynder’s Mission, vamos pensar em novos desafios que o Mynder pode enfrentar ao longo do jogo\. Considere ideias para obstáculos, inimigos ou enigmas que possam enriquecer o projeto\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

