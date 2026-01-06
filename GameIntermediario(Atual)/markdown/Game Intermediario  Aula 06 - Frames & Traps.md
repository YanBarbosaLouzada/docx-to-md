# __PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Aprimorando sistema de frames;
- Traps\.

Objetivos

- Aprimorar sistema de frames;
- Criar mais traps\.

Estratégias e atividades

- Create layers and prefabs
	- Crie uma layer para o enemy e o player e coloque cada uma no lugar;
	- Arraste o Saw, Health Collected para aba de prefabs, para que se torne uma prefab\.
- Alteração no script health
	- Passe a alteração do script health, estão todas comentadas como aula 06\.
- Spikes
	- Crie um script com nome de Enemy Damage e depois passe\-o para as crianças;
	- Precisamos criar também um create empty com o nome de spikes, onde vai se localizar o script que terminamos agora e o box collider com o is trigger ativo \(Ajuste ele no espinho\)… Depois disso precisamos adicionar os assets do spike dentro do spikes basta pesquisar spikes na aba e arrastar para dentro de Spikes \(objeto\)\.
	- Coloque a tag e layer \(Enemy\) dentro de Spikes \(objeto\) e dentro do asset que arrastamos para dentro do Spike;
	- Mude a layer do sprite renderer para player\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588315635700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588315635700.png)

- Firetrap
	- Crie um objeto vazio \(Empty Object\) na hierarquia do Unity\. Renomeie o objeto para "Firetrap"; 
	- Adicione os componentes necessários: Adicione um Box Collider e ative a opção "Is Trigger";
	- Adicione um Animator e um Sprite Renderer:
		- Defina a sprite padrão para o Firetrap no Sprite Renderer \("Fire \(idle\)"\)\. Ajuste o Box Collider conforme necessário;
		- Defina a tag como "Enemy" e a layer do Sprite Renderer como "Player"\. 
		- Configurar as animações:
			- Crie duas animações dentro do Firetrap: "Idle" e "Activated";
			- Para "Idle", adicione a animação sem fogo e para "Activated", adicione a animação com o fogo ativo;
			- Crie um parâmetro chamado "activated" do tipo bool\. 
		- Configure as transições das animações: 
			- Da animação "Idle" para "Activated": Quando o parâmetro "activated" for verdadeiro \(true\);
			- Da animação "Activated" para "Idle": Quando o parâmetro "activated" for falso \(false\)\. 
		- Configurar o Animator:
			- Arraste o componente Animator para dentro do objeto Firetrap no Inspector\. Certifique\-se de que o Animator Controller esteja vinculado ao Animator\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588315635700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588315635700.png)

Recurso

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Como adicionar efeitos sonoros na Unity:
	- Pesquisar sobre o uso de áudio na Unity, incluindo como adicionar música e efeitos sonoros aos jogos;
	- Descobrir como os sons são implementados e controlados dentro do ambiente da Unity\.

