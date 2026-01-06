# __PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 2

Tipo da atividade: Online

Ferramenta\(s\): Scratch dentro do Google Chrome

	                                

Conteúdos

- Corrida com Scratch\.

Objetivos

- Lógica de programação;
- Entender melhor a “Vida” do player;

Estratégias e atividades

- Abra um projeto \(Aula 17\)\.
- Nesta aula, será necessário a incorporação de quatro elementos distintos: um representando o carro, outro representando o obstáculo, um terceiro responsável pela contagem de pontos e, por fim, o plano de fundo\. A seleção das imagens correspondentes a cada um desses elementos ficará a cargo do professor responsável por esta aula, em conjunto com os alunos\. As imagens utilizadas fora do ambiente do Scratch estarão disponíveis no drive para referência: [https://drive\.google\.com/drive/folders/1\_uY2tmtVzHwhphf6S169U8zzcZAjk8eG](https://drive.google.com/drive/folders/1_uY2tmtVzHwhphf6S169U8zzcZAjk8eG)
- Inclua todas as imagens que iremos utilizar\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695745933700.png)
- Iniciaremos a programação do veículo, permitindo o seu movimento\.
	- Quando a tecla … for pressionada;
	- Adicione … a X;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695760156400.png)

- Se julgar necessário, é recomendável reduzir o tamanho do objeto proporcionalmente\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695761900100.png)

- Vamos criar um comportamento onde a banana gere constantemente um clone de si mesma, e esse clone se desloque para baixo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695761900100.png)

- Observamos que a banana principal permanece no nosso jogo sem se mover, apenas criando clones\. Precisamos ocultar essa banana para que ela não prejudique a estética visual do nosso jogo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695765876900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695765876900.png)

- A banana continua aparecendo sempre no mesmo local\. Vamos modificar isso para que ela escolha uma posição X aleatória\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695765876900.png)

- Vamos configurar para que, quando a banana encostar nas bordas do nosso jogo, ela desapareça\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695765876900.png)

- Crie uma variável chamada vida\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695765876900.png)

- Vamos implementar a funcionalidade de modo que, caso a banana encoste no carro, você perca 1 vida e o clone da banana seja removido\.
	- Se tocando em Carro então;
	- Mude \-1 a Vida;
	- Apague este clone;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695765876900.png)

- Crie a variável Pontos\.
- Abra a programação do plano de fundo e vamos configurar para que, quando a bandeira seja clicada, os valores dos pontos e da vida sejam definidos como um valor específico\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695776316000.png)

- Vamos implementar a funcionalidade para que, ao clicar na bandeira, o cenário seja alterado para a pista\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695779832300.png)

- Se a nossa quantidade de vidas for igual a zero, é necessário alterar o plano de fundo para a tela de "Derrota"\.
	- Sempre;
	- Se Vida < 1 então;
	- Mude para o cenário Lose;
	- Pare todos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695779832300.png)

- Vamos configurar para que o carro também desapareça quando a quantidade de vidas chegar a zero\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695779832300.png)

- Agora será necessário adicionar os pontos\. 
	- A programação será a mesma, com a única diferença sendo a manipulação dos pontos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695779832300.png)

Recursos

- Scratch, internet, google e computador\.

Observação

- Caso julgue necessário, pode ajustar os tamanhos dos objetos\.
- Caso os alunos terminem, dê um desafio no qual a vida aumente\.

Tarefas

- Não há tarefas\.

