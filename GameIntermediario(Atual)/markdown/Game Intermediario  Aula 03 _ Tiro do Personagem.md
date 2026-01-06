# __PLANO DE AULA__

Aula 03 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Fazendo ação de tiro do personagem\.

Objetivos

- Fazer animação;
- Fazer scripts\.

Estratégias e atividades

- Criando animação de attack\.
	- Primeiramente, abra o animation e crie uma nova animação chamada Attack;
	- Arraste todas as animações de attack para a telinha;
	- Mude o sample para 5\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587982940200.png)

- Criando animator de Attack\.
	- Abra o __animator__, clique em __parameters__ e crie um novo parâmetro __chamado attack do tipo trigge__r;
	- Conecte a animação __attack__ __com o idle__ e vice e versa \(botão direito > make transition\)\.
	- Nas configurações da seta que aponta para attack, faça como na imagem a seguir \(basta clicar em cima da seta\);

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587985942700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587987942600.png)

- 
	- Nas configurações da seta que aponta para idle, faça como na imagem a seguir\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587989953300.png)

- Criando bola de fogo\.
	- Crie um objeto vazio na cena, para isso você deve clicar com o botão direito em __hierarquia __e em __create empty__, renomeie para Fireball;
	- Crie outro e renomeie para __FireballHolder __e arraste o FIreball para dentro dele;
	- Duplique 9 vezes o Fireball e desative todos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587991943200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587993958600.png)

- Criando animator controller para fireball\.
	- Na pasta animation, clique com o botão direito em um lugar vazio e vá até Create > Animator Controller renomeie para Fireball\.
- Criando animation idle para fireball\.
	- Primeiro para abrir o animation, vá até window > animation > animation;
	- Depois clique em cima de fireball e create;
	- Coloque o nome da animação de Fireball\_idle;
	- Por fim, arraste todas as animações de Fireball idle para a telinha e mude o samples para 20\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587995943000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)

- Criando a animation explosion para fireball\.
	- Crie uma nova animação e renomeie para Fireball\_Explode;
	- Faça o mesmo processo da animação idle;
	- Na última animação da fireball explode, clique com o botão direito em cima e selecione a opção __add animation__ __event__ e mude a function para deactivate\(\)\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)

- Configurando animator de fireball\.
	- Volte ao animator de fireball e conecte o idle no explode \(basta clicar com o botão direito make transition\);
	- Crie também um parâmetro chamado explode do tipo trigger;
	- Agora para configurar esta transição, clique na seta e use configurações da imagem\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)

- Crie um novo script chamado Projectile e também passe as alterações dos outros scripts para as crianças… Tem comentários indicando cada aula\.
- Finalizando aula 
	- Crie um __create empty__ dentro do player e coloque na frente de onde irá sair o fogo… Depois de arrumar, arraste ele para dentro do fire point no player\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)

- 
	- No player, adicione todos esses componentes\. ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)
	- Na bola de fogo, adicione todos esses componentes;
	- No box collider ative o is trigger;
	- No rigidbody2d troque o gravity scale para 0;
	- No animator arraste o animator do fireball para dentro do controller;
	- Por fim, no script, coloque a speed da bola de fogo\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727587997942400.png)
	- Na hierarquia duplique 9 vezes a bola de fogo;
	- Selecione todas e desative;
	- Arraste para dentro do script \(Player\_attack\) componente que está no player\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588013813900.png)

Recurso

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- O que é um jogo em Unity:
	- Pesquisar e entender o que é necessário para criar um jogo na Unity\.
	- Descobrir os diferentes tipos de jogos que podem ser feitos na Unity\.

