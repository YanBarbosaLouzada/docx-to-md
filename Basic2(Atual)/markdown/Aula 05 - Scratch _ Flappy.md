# __PLANO DE AULA__

Aula 05 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 2

Tipo da atividade: Online

Ferramenta\(s\): Scratch dentro do Google Chrome

	                                

Conteúdos

- Flappy com Scratch\.

Objetivos

- Lógica de programação;
- BroadCast;
- Entender sobre a Gravidade;

Estratégias e atividades

- Mostrar o jogo que vamos replicar: https://www\.youtube\.com/watch?v=fQoJZuBwrkU
- Abra um projeto \(Aula 17\)\.
- Abra o Costumes do Scratch e apague a primeira imagem\.
- Vamos criar dois tubos, semelhantes aos tubos do jogo Flappy Bird\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695550644200.png)
- Clique na lupinha para deixa a imagem afastada\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695552646500.png)

- Apague o Scratch\.
- Clique no quadrado e depois escolha a cor verde\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695554645400.png)
- Desenhe dois tubos\.
	- Deixe a imagem no máximo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695556645400.png)

- Aprimore visualmente a apresentação, tornando\-a mais agradável esteticamente\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695562030400.png)

- Inclua o Cat Flying e ajuste o tamanho dele para 60\.
	- Se o gato ficar excessivamente grande, faça o ajuste no tamanho do cano\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695564039300.png)

- Mude o nome da Sprite para “Cano”\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695566038800.png)

- Vamos garantir que o cano se mova consistentemente para a esquerda, emulando o comportamento do jogo Flappy Bird\.
	- Configure a posição inicial do cano para começar em X = 300 quando o jogo for iniciado;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695568041100.png)

- 
	- Repita até que:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695571038400.png)

- 
	- A posição do X  < do que \-260;

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695572038600.png)

- 
	- Adicione \-3 a X\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695574039400.png)
- Clique na bandeira para verificar se está funcionando\.
- Vamos implementar uma variação na posição do cano para evitar sua constante ocorrência no mesmo local\.
	- Será necessário ajustar a coordenada Y para um valor aleatório\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695576041000.png)

- Crie uma variável chamada “Pontos”\.
- Vamos adicionar pontos sempre que o Cat passar pelo cano\.
	- Quando clicar na bandeira;
	- Para sempre;
	- Se a posição X = \-1;
	- Adicione 1 à pontos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695608464400.png)

- Acesse o código do personagem "Cat" para que possamos implementar uma mecânica de descida semelhante à do Flappy Bird\.
	- Quando clicar na bandeira;
	- Vá para X: 0 e Y: 0;
	- Sempre;
	- Adicione \-4 à Y\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695620229300.png)

- Vamos implementar a funcionalidade na qual, ao pressionar a tecla espaço, o meu personagem se deslocará para cima\.
	- Quando a bandeira for clicada;
	- Sempre;
	- Se tecla espaço for pressionada então;
	- Deslize por 0\.2 segundos, até X: 0 e Y: posição Y \+ 30\.
		- Não estamos atribuindo um valor específico à coordenada X, pois não temos a intenção de permitir movimentos horizontais para a esquerda ou para a direita\.
		- No eixo Y, estou obtendo a posição atual e adicionando um valor de \+30\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695622231900.png)
- Vamos desenvolver o código para que o personagem perca\.
	- Quando a bandeira for clicada;
	- Sempre;
	- Se tocado no cano então;
	- Pare tudo\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695624230200.png)
- Adicione o fundo para o nosso jogo ficar visualmente mais agradável\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695626230500.png)
- Vamos adicionar o plano de fundo de "derrota"\.
	- Link para download: https://drive\.google\.com/drive/folders/1Nreiww3Q6\-Jt0uFTiuX\-upM2RJFtYAlC
	- Clique em Stage > Backdrops;![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695631264700.png)
	- Agora vamos subir a imagem de YouLose\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695633273200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695633273200.png)

- Agora vamos adicionar a tela de vitória\.
	- Faça o mesmo da tela de derrota\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695635280300.png)

- Vamos criar uma transmissão \("Broadcast"\) de modo que, quando o objeto "Cat" colidir com o objeto "cano", os elementos desapareçam e exibam a tela de vitória ou derrota\.
	- Podemos dizer que broadcast se resume ao processo pelo qual é transmitida ou difundida uma informação, ao mesmo tempo, para diversos receptores diferentes;
	- Vamos enviar uma mensagem dentro do objeto "Cat" para outros elementos, como o objeto "cano" e o plano de fundo \("Backdrop"\);

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695637287200.png)

- 
	- Mude o nome para “Lose”;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695637287200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695639296600.png)

- 
	- Quando receber a mensagem “Lose”;![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695641307200.png)
	- Esconder imagem;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695642965800.png)

- 
	- Se apenas configurarmos a opção "hide" \(esconder\), ocorrerá um erro, pois quando o objeto "cano" desaparecer após o contato com o "Cat", ao clicarmos na bandeira ele não aparecerá\. Portanto, é necessário também incluir a opção "show" \(mostrar\) para que ele possa reaparecer adequadamente\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695644621400.png)

- 
	- Vamos replicar a mesma programação no objeto cano\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695646469000.png)

- Na programação do fundo, realizaremos a mesma ação, embora o bloco de código seja diferente\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695648518300.png)

- Para concluir, é necessário reiniciar os pontos quando clicarmos na bandeira\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702695649518200.png) 

Recursos

- Scratch, internet, google e computador\.

Observação

- Caso julgue necessário, pode ajustar a largura do cano, aumentando ou diminuindo conforme o desejado\.
- Caso os alunos terminem, dê um desafio no qual apareça a tela de Vitória\.

Tarefas

- Faça um jogo usando a__ gravidade__ dentro do Scratch\. Enviar uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), trazer em um pendrive ou em seu Google Drive/One Drive\.

