# __PLANO DE AULA__

Aula 04 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Animação personagem\.

Objetivos

- Criar Animações;
- Criar novos nodes;

Estratégias e atividades

- Criando animação Idle\_down\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952251564100.png)

- Agora selecione o sprite2D\.
	- Cheque no __inspetor __em __animation __se o __frame__ está em __0 __se estiver clique na chavinha ao lado![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952257115100.png) e também se certifique que a barra azul da animação está em zero ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952259979600.png)\. Clique nesta chave > em create > clique nela mais 5 vezes, e no relógio ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952261985600.png) ao lado deixe em 0\.6 e marque o botão de loop ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952263993100.png)\.
	- Imagem exemplo:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952266001000.png)__

- 
	- Arraste a barra azul para __0__ selecione __sprite2d __e desta vez vamos clicar na chavinha do transform > __position__\.
	- E também vamos fazer isso no Offset > __Flip H__\.
	- Imagem exemplo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952267007300.png) 	

- Agora vamos fazer uma animação nova chamada idle\_right\.
	- Selecione o sprite2d e no animation > __frame__, mude para __6 __e clique na chavinha mais 5 vezes, mude o relógio para 0\.6 marque o botão de loop\.
	- Agora o mesmo para flip H e Position\.

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952271021500.png)

- Agora vamos duplicar a animação idle\_right e renomear para idle\_left\.

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952273028400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952275036200.png)

- Agora vamos criar uma nova animação chamada idle\_up\.
	- Mude o frame para 12 e clique na chave > mude o relógio para 0\.6 > clique em loop\. __O flip H deve ser desativado e o Position deve voltar a ser \-0\.5\.__
- Agora vamos duplicar a animação idle\_down e chamá\-la de walk\_down\.
	- Selecione cada quadradinho e mude o value __do 1 para 18__, __2 para 19__, __3 para 20__, __4 para 21__, __5 para 22__, __6 para 23__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952279051800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952281061200.png)

- Agora vamos duplicar a animação idle\_up e chamá la de walk\_up\.
	- Selecione cada quadradinho e mude o value do __1 para 30__, __2 para 19__, __31 para 20__, __32 para 33__, __5 para 34__, __6 para 35__\.
- Agora vamos duplicar a animação idle\_left e chamá la de walk\_left\.
	- Selecione cada quadradinho e mude o value do __1 para 24__, __2 para 25__, __3 para 26__, __4 para 27__, __5 para 28__, __6 para 29__\.
- Agora vamos duplicar a animação walk\_left e chamá la de walk\_right\.
	- Selecione cada quadradinho e mude o value do __1 para 18__, __2 para 19__, __3 para 20__, __4 para 21__, __5 para 22__, __6 para 23__\.
	- __Não esqueça de retirar o fliph e voltar o positon para 0\.5\. Clique onde as setas apontam e mude o value\.__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952287090500.png)__

- Adicione um novo no chamado __animation tree__\.
	- No inspetor em tree root vamos adicionar o animationnodestatemachine\.
	- Em anim player vamos linkar o nosso animation\.
- Pós o vínculo\.
	- Onde está escrito start e end clique com o botão direito, adicione o __blendspace2d __e mude o nome para __idle__\.__ __Clique no lápis ao lado\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952291108200.png)

- Deixe como a imagem acima\.
	- Para adicionar os idles, clique com o botão direito > add animation > idle\_right por exemplo\.
- Agora volte para a tela que tem o Start e o End e faça o mesmo para walk Siga o passo a passo como o do idle\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952294654900.png)

- Clique em CharacterBody2D > use esta configuração\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952296663300.png)__

- Agora em animationplayer\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952298671200.png)

- Por último, em animation tree\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952300677900.png)

Recursos

- Computador, internet, Godot instalado\.

Observação

- O projeto utiliza o Godot 4\.0 [https://godotengine\.org/download/windows/](https://godotengine.org/download/windows/)
- Será um jogo estilo RPG visto de cima\.

Tarefas

- Sem tarefa\.

