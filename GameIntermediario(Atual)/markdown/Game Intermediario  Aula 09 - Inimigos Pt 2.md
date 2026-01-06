# __PLANO DE AULA__

Aula 09 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Inimigo Pt 2\.

Objetivos

- Fazer o inimigo Ranged\.

Estratégias e atividades

- Mudanças no script do projétil\.
	- Passe o script para as crianças\.
- Mudanças no script do Health\.
	- Passe o script para as crianças\.
- Criando Ranged Enemy Holder \(create empty\)\.
	- Alterando Enemy Melee para Enemy Ranged\.
		- Para isso você deve pegar a prefab do MeleeEnemy desvinculada da prefab, mudar o nome para RandegEnemy… apague o script do MeleeEnemy\.
	- Adicionando Firepoint \(create empty\)\.
		- Você deve colocar ele na frente do seu inimigo igual fizemos o com o player\. 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588597624200.png)

- Criando Script do Ranged Enemy\.
	- Passe o script para as crianças;
	- Adicione o script dentro do RangedEnemy e depois adicione suas dependências script\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)

- Adicionando Fireballs Holder\.
	- Adicione a prefab da Fireball dentro do FireballsHolder \(mude o nome para EnemyFireball\) e desvincule da prefab \(clique com o botão direito em cima da prefab > prefab > Unpack, mude também o script de projectile para o enemy projectile\.
	- Adicione as Fireballs no script do Ranged Enemy\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)

- Animation RangedAttack\.
	- Na animation RangedAttck add a função RangendAttack nas animações\.
- Criando Script  EnemyFireballHolder\.
	- Passe o script para as crianças;
	- Adicione o script dentro do FireballsHolder e suas dependências\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)

- Mudanças no script Enemy Projectile\.
	- Passe o script para as crianças\.
- Para que o nosso atirador ande e atire basta colocar ele dentro do EnemyPatrol e colocar as dependências dentro do script patrol\.
- No Health, não esqueça de colocar dentro do componente o EnemyPatrol e RangedEnemy\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)

- Desabilitando Inimigos
	- Vá na function de Die do personagem principal e do enemy, adicione uma função no final de cada animação e coloque ela para ser “desactive”\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588598658600.png)

Recurso

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Plataformas para as quais a Unity pode exportar jogos:
	- Pesquisar sobre as plataformas para as quais os jogos podem ser exportados a partir da Unity \(PC, consoles, dispositivos móveis, etc\.\);
	- Descobrir as vantagens e desvantagens de desenvolver para diferentes plataformas\.

