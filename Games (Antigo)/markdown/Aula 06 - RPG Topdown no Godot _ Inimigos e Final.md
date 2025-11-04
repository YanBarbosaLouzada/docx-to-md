# __PLANO DE AULA__

Aula 15 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Inimigos\.

Objetivos

- Construindo Inimigo;
- Programação\.

Estratégias e atividades

- Detectando inimigo na área de colisão\.
	- Vá para cena Character \(personagem principal\);
	- Clique em AttackArea, em seguida em NODE que está localizado ao lado direito de inspetor;
	- Selecione a opção Body\_entered e depois, selecione o character e clique em connect;
	- Agora passe a alteração do script do character que pode ser  encontrado no github\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454765514700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454768514400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454772677100.png)

- Criando a cena do inimigo\. 
	- Crie uma nova cena com o node > characterrbody2d renomeie para slime;
	- Adicione dentro, uma sprite 2D, e dentro dela adicione o asset do inimigo;
	- Em animation, dentro de sprite 2D, coloque Hframes em 7 e o Vframes em 5\.
- Adicionando um novo nó para o slime\.
	- Adicione o animation player para o slime;
	- Adicione dentro de animation player, a animação idle e clique na chavinha do frame 0 até 4, mude o relógio para 0\.4 e coloque a animação em loop;
	- Adicione agora a animação walk, mude o frame para 7 e clique na chavinha até virar 13, mude o relógio para 0\.6 coloque a animação em loop;
	- Adicione a animação de death, mude o frame para 28 e clique na chavinha até virar 33, mude o relógio para 0\.5\.
- Adicionando slime no grupo enemy de colisor\.
	- Clique no slime, vá até node Groups e adicione o grupo enemy;
	- Agora adicione a collisionshape2d para o slime > no inspetor troque o shape dela para um retângulo e a ajuste corretamente;
	- Ainda no inspetor do collisionshape2d > visiblity > show behind > ative\-o\.
- Adicione uma area2D e renomeie para DetectionArea\.
	- Dentro dela agora adicione uma collisionshape2d e mude o shape para um círculo \(Faça do tamanho da área que deseja que seu slime siga o player\)\.
	- Ainda no inspetor do collisionshape2d > visiblity > show behind > ative\-o\.
- Criando Script para slime\.
	- Crie um script\. Depois de criado, selecione DetectionArea, clique em node e em body\_entered, selecione o slime e depois connect, faça o mesmo para body\_exited;
	- Agora faça o mesmo para AnimationPlayer do slime e conecte o  \_animation\_finished no slime\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454774671500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454776672300.png)

- Criando Grupo para personagem e slime\.
	- Vá para a cena do personagem e clique em character > node > groups > adicione um grupo chamado character;
	- Agora faça o mesmo para o slime, mas chame o grupo de enemy\.
- Criando animação de morte para personagem\.
	- Vá até a cena do personagem, clique em animationplayer e adicione uma nova animação chamada death;
	- Adicione os frames 54, 55, 56 mude o relógio para 1;
	- Agora vá para o animationtree > crie uma nova blendSpace2d > chame de death > troque o blend para 3 pontinhos e clique no lápis\. Coloque a animação death em todas as extremidades < ^ > v\.
- Imagem demonstrativa:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454780055800.png)

- Nesta imagem mostra todos os lugares onde você irá clicar,após criar a cena do inimigo de acordo com o passo a passo da aula:
	- Relógio\[Animação\];
	- Loop\[Animação\];
	- Frame\[Animação\];
	- Animação\[Fique atento as animações que nao tem loop\];
	- Hierarquia\[Adicione Componentes\] \.
- Passe os scripts para os alunos\.

Recursos

- Computador, internet, Godot instalado\.

Observação

- O projeto utiliza o Godot 4\.0 [https://godotengine\.org/download/windows/](https://godotengine.org/download/windows/)
- Será um jogo estilo RPG visto de cima\.
- Se os projetos dos alunos apresentarem muitos erros basta clonar a branch da próxima aula no git e passar para os computadores da escola\.

Tarefas

- Desafio para casa:
	- Pesquisar como fazer a câmera focar apenas em nosso personagem e fazer na próxima aula\.

