# __PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): S4A instalado no computador

Conteúdos

-  Nave game\.

Objetivos

- Lógica de programação\.

Estratégias e atividades

- Olá alunos, hoje vamos desenvolver um jogo de nave no S4A\. Para desenvolver esse jogo, precisamos primeiro fazer a montagem do circuito\.
- Neste circuito iremos utilizar o joystick e o pushbutton já vistos antes\.

  
	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774576225900.png)

- O push button será utilizado para dar o tiro da nave
- Analogico será utilizado para controlar a nave

Agora vamos para a programação do nosso jogo:

- A primeira coisa a ser feita é o download dos assets disponíveis na pasta do Basic 03\.
- Após baixar os nossos assets vamos agora dar vida ao nosso jogo\.

Para começar precisamos criar algumas variáveis que iremos utilizar ao longo do desenvolvimento do projeto:

- __Variáveis __

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774578195200.png)

Precisamos agora começar com a programação do arduino que será o responsável por pegar os valores digitais do analógico e do push button\.

- Programação do __arduino __

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774580193000.png)

- A variável botão tiro está sendo responsável por guardar se o botão está sendo clicado ou não\. \( 1 = Clicado 0 = Não clicado \)
- A variável X e Y está sendo responsável por guardar os valores de X e Y do analogico 
- A variável Start é responsável por guardar se o jogo começou ou não\. \(1 = True 0 = False\)
- A variável Atirando é responsável por guardar se nossa nave está atirando ou não \(1 = True 0 = False\)

Agora vamos fazer nosso __Personagem __

- Primeiro adicione o sprite da nave no seu jogo, depois faça a programação a seguir dentro da nave\.
- Programação da __Nave__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774582195100.png)

- Nesta programação damos movimento ao nosso personagem a partir do valor do X e Y
- As Variáveis X nave e Y nave servem para guardar o valor da posição da nave

Agora vamos criar o tiro do nosso personagem, não esqueça de pegar o sprite na pasta\.

- Este tiro vai servir para destruir os meteoros 
- Programação do __Tiro__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774584194900.png)

- Nesta programação a estamos checando se a variável Botão Tiro  é igual a 1 e Atirando é igual 0\. Caso essas condições sejam atendidas mudaremos o valor do atirando para 1\.
- E depois fazemos com que esse tiro se mova para frente caso atirando seja 1 e senão ele fica escondido dentro da nave\.

Agora vamos montar o __meteoro __que vai servir para matar a nossa nave:

- Primeiro precisamos pegar o sprite e colocar no jogo\.
- Depois precisamos fazer a programação\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774586600400.png)

- Nesta programação fazemos a movimentação do nosso meteoro, o sistema de pontos caso o meteoro passe pelo personagem sem bater, o sistema de spawn de meteoros, o sistema de morte do personagem e o sistema de som quando destruímos o meteoro\.
- Basicamente toda vez que o meteoro passa na nave ou é destruído ele ressurge no canto direito da tela\.

Agora vamos programar o Big Meteoro 

- A programação deste meteoro é basicamente, porém ele só __será criado a partir de 10 pontos__\. 
- Programação do__ Big Meteoro__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774588600600.png)

Agora para finalizarmos nosso projeto vamos montar um cenário e colocar o Sprite do Start na tela 

- Primeiro vamos fazer a programação de quando deve estar aparecendo o start na tela
- Programação do __START__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774590600800.png)

- Agora vamos para a montagem do nosso palco ou cenário como preferir
- __Clique no Palco \-> Fundos de tela \-> Editar__
- Agora faça seu cenário espacial 

Alunos agora terminamos nosso jogo e agora olha como ele ficou 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774591600200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702774593873300.png)

Agora você já pode se divertir com seu jogo\.

Recursos

- S4A instalado, internet e computador\.

Observação

- Nada a observar\.

Tarefas

- Sem tarefa\.

