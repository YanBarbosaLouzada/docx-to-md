# __PLANO DE AULA__

Aula 08 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Inimigo Pt 1\.

Objetivos

- Criação de inimigos\.

Estratégias e atividades

- Sprites e animações inimigas\.
	- Para fazer o inimigo precisamos importar seus assets se ainda não foi importado;
	- Crie um creaty empty e mude o nome dele para __MeleeEnemy__, dentro dele adicione os componentes: __Box collider__ com o is trigger ativo, __Animator__, __Sprite Renderer__ com a layer do player, troque também a layer e tag do objeto para enemy;
	- Crie as seguintes animações para o inimigo: Idle, Hurt, MeleeAttack, RangedMelee, Run;
	- Dentro do controller do meleeEnemy crie todos esses parâmetros:

 		![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588491020700.png)

- 
	- 
		- Depois faça toda a esquematização do animator controller com base na imagem a seguir e as aulas passadas\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588492984600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588495984800.png)

Não esqueça de desativar o loop na animação Die, no ranged Attack adicione uma função na terceira animação clicando neste ícone ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588498982900.png) e mude a função para DamagePlayer\(\)\.

- IA inimiga corpo a corpo\. 
	- Crie um script com nome __MeleeAttack__, arraste para o inimigo, passe o script para as crianças e por fim coloque as dependências no script;
	- Depois arraste o inimigo para pasta de prefabs\.
- Patrulhamento 
	- Crie três pontos vazios:
		- EnemyPatrol: Deve estar no centro do sprite do inimigo\.
	- LeftEdge e RightEdge:
		- Posicionados nas extremidades da área de patrulha do inimigo\.
	- Certifique\-se de que:
		- LeftEdge e RightEdge estão dentro de EnemyPatrol\.
	- Crie um script com nome EnemyPatrolm, passe os scripts para crianças e depois adicione as dependências do script\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588498982900.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588498982900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588507458600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588507458600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588512458700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588514812200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727588514812200.png)

Recurso

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Github;
- Link para o download da Unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	- Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

Tarefas

- Diferença entre 2D e 3D na Unity:
	- Pesquisar e entender as diferenças fundamentais entre jogos em 2D e 3D na Unity;
	- Descobrir como os desenvolvedores trabalham com cada um desses tipos de jogos\.

