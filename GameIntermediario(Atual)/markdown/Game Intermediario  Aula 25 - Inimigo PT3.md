# __PLANO DE AULA__

Aula 25 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

Objetivos

- Montar um inimigo / sistema de vida 

Estratégias e atividades

- Agora vamos montar a barra de vida do nosso inimigo e implantar um sistema de dano básico para testar\.
	- Crie um canvas para o inimigo, clique com o botão direito do mouse ui\-> canvas, para facilitar desative por enquanto o do player 
	- Dentro do canvas do inimigo você irá colocar um slider e um Text para fazermos da mesma forma do player
- Agora vamos configurar o__ inspetor do canvas__
	- Troque o rendermode para world space
	- Mude a order in layer para 10
	- Use essas informações para react transforme
		- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589678915800.png)
- Agora as mudanças no inspetor do slider 
	- Mude o nome dele para HealthSlider 
	- Mude o Value para 1
	- Agora dentro do background deixe ele um vermelho mais para preto ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589681484800.png)
	- Agora dentro do Fill area \-> area mude a cor para um vermelho mais brilhante ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589686585600.png)
	- Ajuste o Fill área para que ele fique com a barra vermelha completa até o final
- Agora as mudanças no inspetor do text 
	- Mude o text input para skeleton 
	- Mude o Text Style C3
	- Mudar cor para vermelho 
	- No outline mude o thickness para 0\.16
- Posicione tudo em cima da cabeça do esqueleto 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589691585400.png)

- Agora escreva o WaypointID\.cs e faça alterações no player, playercontroller e monster 
- Coloque o WaypointID nos pontos onde seu skeleton se move\.

Recurso

- Computador, internet, unity\.

Observação

- Os assets e scripts estão disponíveis no github;
- Link para o download da unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	-  Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com)\.
- Avise as Crianças que o GDD será usado no TCC 

Tarefas

- Continue fazendo o seu GDD em casa\.

