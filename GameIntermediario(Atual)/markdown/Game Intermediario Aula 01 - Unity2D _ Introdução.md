# __PLANO DE AULA__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Introdução à Unity e Movimentação\.

Objetivos

- Criar o primeiro projeto;
- Apresentar plataforma;
- Iniciar o projeto 2D\.

Estratégias e atividades

- Crie o projeto na versão 2020\.2\.1\.f1\.
- Para iniciar o projeto, siga estes passos: 
	- Clique na seta ao lado de "New" e escolha a versão mais próxima ou idêntica àquela que foi recomendada;
	- Em seguida, selecione o tipo de projeto, que, no nosso caso, será um projeto 2D;
	- Por fim, atribua um nome ao projeto\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590271908800.png)

- Explicando um pouco sobre a interface da Unity:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590273923200.png)

- Colocando uma movimentação básica e chão para o personagem\.
	- Adicionando o player: Clique com o botão direito em __hierarchy__ > __2D object__ > __Sprites__ > __Square__;
	- Adicionando componentes no player: Clique em __Add Component__ e adicione os seguintes componentes\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590276879400.png)
	- Adicionando o chão: Clique com o botão direito __em cima do player__ e selecione duplicar;
	- Crie outro objeto para o chão chamado __Ground__ e adicione um__ Box Collider:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590278879700.png)\.

- 
	- Distribua os __Objetos na cena__ da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590280878800.png)

- 
	- Para mudar de cor basta ir no Inspector do componente que deseja mudar a cor, depois clicar em sprite renderer > color\.
- Organizando projeto
	- Criando as pastas: Assets, Animation e Sprites\.
	- Para criar a pasta basta ir até a aba __Project__ > clicar com o botão direito na pasta __Assets__ > __Create__ > __Folder__:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)__

- Criando Script\.
	- Clique com o botão direito dentro da pasta __scripts__ > __Create__ > __C\# Script__;
	- Renomeie o Script para __Player\_Movement __e adicione este Script:

EDITOR DA APOSTILA > SUBSTITUA A IMAGEM ANTERIOR PELA IMAGEM ABAIXO

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)

- Dê o play e veja seu jogo criando vida\.
- Agora vamos personalizar este jogo
	- Vá até a pasta__ assets __que pode ser encontrada no Drive do Game Intermediary e baixe todos os assets que vamos precisar para este jogo\.
- Adicionando sprite\_idle no player\.
	- Agora, no __painel Hierarchy__, clique no objeto chamado __'Player'__, e no painel Inspector, encontre a seção __'Sprite Renderer'__\. Dentro dela, você pode alterar a imagem do sprite, assim como na imagem de exemplo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)

- Ajuste o Box Collider do player\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)

- Fazendo animação
	- Abrindo aba de animação;
	- Clique em ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png) e depois clique em Animation e selecione o animation e o animator;
	- Clique em player primeiro e depois clique no animation dentro dele;
	- Haverá um botão escrito ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)no qual você deve clicar e adicionar uma nova animação “Idle”;
	- Se tudo ocorreu corretamente deve estar aparecendo assim:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)
	- Vamos agora adicionar o “Sample”\. Caso não esteja aparecendo, basta clicar nos três pontinhos e marcar a opção __Show Sample Rate__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590281879600.png)

- Adicionando animação idle\.
	- Selecione as animações de ‘parado’ que importamos e __arraste __todas para dentro de __animation __e depois altere o __Sample __para __8__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590298003400.png)

- Criando uma nova animação \(run\)\.
	- Clique na seta do lado de ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590298003400.png) e selecione__ create new clip__,__ __salve a animação como __Run__\.
	- Selecione as animações de __walk __que importamos e __arraste __todas para dentro de __animation \(Run\) __e depois altere o __Sample __para __8__\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590302412100.png)
- Arrumando eventos do __animator__\.
	- Clique no player e entre dentro da aba animator, se tudo estiver certo estará assim:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590304420600.png)

- 
	- Você deve fazer uma conexão para que o player possa alterar da animação __run para idle__ e vice e versa\. Para fazer essa conexão você deve clicar com o botão direito em cima de IDLE, selecionar a opção__ Make Transiton__ e conectar com o __run__;
	- Faça a mesma de __run para idle__; 
	- Quando você clica na seta e olha no inspetor tem uma opção chamada __Has exit time__\. Você deve deixá\-la desativada para as duas setas\. Se tudo estiver certo o que você deverá ver é isso:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590304420600.png)

- Vamos agora adicionar uma condição para que possamos trocar de animação\. 
	- Vá até __'Parameters'__ e crie um novo parâmetro clicando no botão de __adição \(\+\)__ e selecione a opção __'bool'__;
	- __Renomeie este parâmetro para 'run';__
	- Após criar essa condição, __clique na seta que aponta para 'run'__ e, no painel 'Inspector', procure a seção 'Conditions', onde você deve __clicar no botão de adição \(\+\) e adicionar 'Run' com o valor 'True'__;
	- Na seta que aponta para 'idle', defina 'Run' como 'False'\."

Idle > run					    Run > idle

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590307161000.png)	   ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590309169100.png)

- Adicionando animação jump\.
	- Para adicionar a animação jump, temos que fazer o mesmo passo a passo do run para criar uma nova animação;
	- Depois, renomear para jump e por fim arrastar as animações para dentro da tela e mudar o sample para 6\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590311177400.png)

- Arrumando o __animator__\.
	- Primeiro vamos adicionar novos parâmetros\. Um vai se chamar __grounded__ e vai ser do tipo__ bool, __o segundo vai ser do tipo __trigger __e vai se chamar __jump__;
	- Agora faça essas ligações do:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590311177400.png)

- 
	- 
		- Na seta que vai de any state para jump, use estas configurações\(clique nela e olho no inspetor\)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590313184400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590315712200.png)

- 
	- Na seta que vai de jump para idle, use estas configurações \(clique nela e olho no inspetor\);

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590316712300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590317712000.png)

- 
	- Clique duas vezes em cima na animação jump e desative o loop\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590319713100.png)

- Criando tag __Ground__\.
	- Para criar uma tag devemos clicar no objeto que desejamos e clicar em tag > add tag; 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590321712100.png)

- 
	- Clicar no \+ e adicionar uma nova tag com nome Ground, em seguida volte no objeto e coloque a tag\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590322712700.png)

- Passe o restante do script para as crianças:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727590323711600.png)

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Instalar Unity em casa\.

