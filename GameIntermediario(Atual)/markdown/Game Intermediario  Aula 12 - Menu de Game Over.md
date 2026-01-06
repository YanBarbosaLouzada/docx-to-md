# __PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- GameOver

Objetivos

- Menu de Game Over

Estratégias e atividades

- Intro
	- Baixe os assets da fonte e do game over sound 
- Game Over Scenario
	- Agora vamos criar a tela de game over para isso precisamos criar dentro de canvas um objeto vazio chamado GameOverScreen\.
	- Dentro GameOverScreen vamos criar o Background\(image\) e mudar sua cor para vermelho e aumentar a transparência, agora vamos criar um Text com o nome de DED e dentro dele vamos escrever GameOver\.
		- Dentro do Text que criamos adicione os componentes e use as configurações que irei passar depois\.
	- Crie agora o SelectionArrow\(image\)
		- Dentro do SelectionArrow que criamos adicione os componentes e use as configurações que irei passar depois\.
	- Crie agora um create empty com o nome de Options e dentro dele crie um text chamado Restart 
		- Dentro do Restart  que criamos adicione os componentes e use as configurações que irei passar depois\.
	- Duplique duas vezes esse Restart e renomeie para Main Menu e Quit

Game Over

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588852244200.png)

SelectionArrow

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588854564400.png)

Restart

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588856575300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588858563000.png)

Organize assim

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588861554300.png)

- Scripts
	- Houve alteração no script do PlayerRespawn e uma pequena mudança no do health
	- Crie os scripts SelectionArrow\(Arraste para o SelectionArrow\) e UIManager\(Arraste para o UICanvas\)
	- Após ter passado os scripts volte na animação de morte do player e troque a função de respawn para Check Respawn\(\)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588864552400.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588865889200.png)
- Agora para cada opção\(Restart,Main Menu e Quit\) mude para a função respectiva\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588867888100.png)

- 
	- Faça isso para todos e no final desative o GameOverScreen\.

Recurso

- Computador, internet, unity

Observação

- Os assets e scripts estão disponíveis no github;
- Link para o download da unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Trazer um canvas\(foto\) do jogo que mais gosta de jogar\.

