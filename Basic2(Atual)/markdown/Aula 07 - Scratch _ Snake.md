# __PLANO DE AULA__

Aula 07 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 2

Tipo da atividade: Online

Ferramenta\(s\): Scratch dentro do Google Chrome

	                                

Conteúdos

- Snake com Scratch\.

Objetivos

- Trabalhar lógica de programação\.

Estratégias e atividades

- Mostrar o jogo que vamos replicar: https://www\.youtube\.com/watch?v=DekS8Pgb1qc
- Abra um projeto \(Aula 17\)\.
- Apague o Scratch\.
- Vamos começar a desenhar a snake\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695937834900.png)

- Vamos fazer a cabeça dele\.
	- Primeiro, selecione a cor desejada, no meu caso, escolhi verde\. Em seguida, escolha a cor da borda, que será preta\. Por fim, clique no círculo e desenhe\-o no jogo\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695939841600.png)
- Agora vamos criar o corpo dele\. Para isso, clique com o botão direito sobre a imagem e selecione a opção "Duplicar"\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695939841600.png)

- Agora, volte para a cabeça dele e desenhe os olhos![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695944115300.png)
- Arrume o tamanho do snake\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695946124300.png)

- Vamos fazer com que a nossa snake gire a cabeça\.
	- Quando clicar na bandeira;
	- Sempre;
	- Se tecla … pressionada, então;
	- Aponte para a direção;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695948132000.png)

- 
	- Realizamos o direção para cima; agora, precisamos replicá\-lo para as outras direções\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695950141000.png)

- Será necessário programá\-lo para que ele possa se mover\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695950141000.png)

- Quando clicarmos na bandeira, quero que ele retorne à posição central\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695952149000.png)

- Será necessário criar o alimento da snake\. Fica a critério dos alunos escolherem o que será o alimento\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695954158400.png)

- Mude o tamanho\.
- Vamos configurar para que o alimento apareça aleatoriamente em qualquer lugar do mapa\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695956165000.png)

- Agora é necessário programar para que, quando a snake tocar na maçã, ela apareça em outro local\.
	- Sempre;
	- Se encostar em … então;
	- Vá para X: número aleatório entre \-200 e 200 e Y: número aleatório entre \-150 e 150

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695959924600.png)

- A partir deste ponto, será necessário que nossa serpente comece a crescer\.
	- Vamos criar uma variável chamada “tamanho”;
	- Quando clicarmos na bandeira;
	- Mude tamanho para 0\.5\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695961935100.png)

- Vamos fazer com que a nossa cobra comece a crescer quando comer o alimento\.
	- Quando bandeira for clicada; 
	- Sempre;
	- Mude para a fantasia corpo \(Pois é o corpo que vai crescer\);
	- Crie clone do ator \(Isso fará com que crie o corpo da cobra\);
	- Mude para a fantasia cabeça \(Depois quero que a cabeça apareça\);
	- Espere 0\.1 segundo \(Para dar um efeito no Snake\);
	- Mova 5 passos \(Para ela andar\);

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695963943800.png)

- Se testarmos o jogo, a cobra ficará infinitamente crescendo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695965953600.png)

- Para interromper o crescimento da cobra, é necessário implementar a seguinte programação:
	- Quando começar o meu clone;
	- Espere … segundos;
	- Apagues este clone\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695965953600.png)

	

- Implementamos a seguinte programação: 
	- Quando a cobra consumir a comida, seu tamanho aumentará\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695967965300.png)

- Vamos implementar a seguinte funcionalidade: se a cabeça da cobra entrar em contato com seu próprio corpo, o jogador perderá o jogo\.
	- Quando bandeira for clicado;
	- Sempre;
	- Se a cor … está tocando na cor \.\.\. então;
	- Para todos;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695969972800.png)

- 
	- Vamos arrumar as cores;
	- Selecione esta opção;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695971982200.png)

- 
	- Deixe exatamente na cor vermelha;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695973990000.png)

- 
	- Faça a mesma coisa na segunda cor

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695975740300.png)

- 
	- Se o personagem não perder ao entrar em contato com seu próprio corpo, o mesmo procedimento deve ser aplicado às cores, alterando apenas a posição que foi inicialmente definida\.
- Agora, vamos programar para que, caso a snake entre em contato com as paredes, o jogador seja derrotado\.
	- Selecione a opção Paint no BackGround;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695975740300.png)

- 
	- Clique no Quadrado > Convert to Bitmap;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695977747500.png)

- 
	- Clique no quadrado, coloque a cor da borda e deixe como Outlined;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695979756000.png)

- 
	- Faça o quadrado agora

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695981764200.png)

- Dentro da programação da cobra, vamos implementar a lógica em que, se a cobra entrar em contato com a cor da borda, o jogo será encerrado\. Esta programação será semelhante àquela aplicada ao corpo da cobra\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695983772800.png)

Recursos

- Scratch, internet, google e computador\.

Observação

- Caso julgue necessário, pode ajustar os tamanhos dos objetos\.
- Caso os alunos terminem, dê um desafio no qual apareça a tela de Vitória e Derrota\.
- Se você desejar visualizar o jogo criado durante esta aula, aqui está o link para acessá\-lo: [https://drive\.google\.com/drive/folders/1FfIf1a6IC\_QpyaiMLn4rX\_zaoKM6wOXM](https://drive.google.com/drive/folders/1FfIf1a6IC_QpyaiMLn4rX_zaoKM6wOXM)

Tarefas

- Desenvolva um jogo no Scratch com base no mesmo conceito de crescimento da serpente, similar ao jogo "Snake"\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

