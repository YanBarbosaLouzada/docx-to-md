# __PLANO DE AULA__

Aula 07 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Traps Pt 2\.

Objetivos

- Criar mais traps\.

Estratégias e atividades

- Arrow Trap
	- Crie um script com nome de ArrowTrap e outro com nome de Enemy Projectile, depois passe\-o para as crianças;
	- Crie todos esses create empty e organize\-os assim:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588399267100.png)

- Arrow Trap Componente:
	- Dentro do componente Arrow Trap, adicione o script Arrow Trap\.
- Sprite e Sprite Renderer:
	- Crie um sprite e adicione um Sprite Renderer;
	- No Sprite Renderer, altere a camada \(layer\) para "player";
	- Arraste o sprite "Fire \(idle\)" que fizemos anteriormente, ao final da última aula, para o Sprite Renderer\.
- Firepoint:
	- No Firepoint, altere o ícone selecionado para um prisma;
	- Escolha na tela o local de onde deseja que as flechas saiam\.
- Arrow Holder:
	- No Arrow Holder, adicione a flecha \(Arrow\) que está disponível nos assets do drive;
	- Para adicioná\-la, clique no asset, mude o modo de sprite para "multiple", vá para Sprite Editor > Slice > Slice > Apply;
	- Escolha a flecha desejada após essa etapa;
	- Coloque a flecha dentro do Sprite Renderer do arrow e mude a camada para "player"\.
- Configurações adicionais para a flecha \(Arrow\):
	- Adicione um Box Collider com a opção "is trigger" ativada;
	- Adicione um Rigidbody2D;
	- Aplique o script do Enemy Projectile;
	- Altere a tag e a camada para "enemy";
	- Arraste a arrow para aba de prefab;
	- Duplique nove vezes a arrow como fizemos e depois arraste para dentro do script ArrowTrap;
	- Por fim, desative o prefab da arrow\.

Arrow 					Arrow Trap

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588403160500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588405142800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588407124700.png)

- Spikehead
	- Criação do SpikeHead:
		- Crie um objeto vazio \(Create Empty\);
		- Renomeie\-o para "SpikeHead"\.
	- Componentes no SpikeHead:
		- Adicione os seguintes componentes dentro do SpikeHead;
		- Box Collider com "Is Trigger" ativado;
		- Rigidbody 2D;
		- Sprite Renderer\.
	- Configurações no Sprite Renderer:
		- No Sprite Renderer;
		- Adicione o sprite do "SpikeHead Idle";
		- Altere a camada para "player"\.
	- Script SpikeHead:
		- Crie um novo script chamado "SpikeHead";
		- Associe este script ao SpikeHead que criou\.
	- Transforme esse inimigo em prefab:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588409125600.png)

Recurso

- Computador, internet e Unity

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Interação do jogador com a Unity:
	- Pesquisar sobre como os jogadores interagem com os jogos feitos na Unity, seja por meio de controles, mouse, teclado ou até mesmo dispositivos móveis\.

