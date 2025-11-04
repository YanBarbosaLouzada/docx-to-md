# __PLANO DE AULA__

Aula 09 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Animação personagem\.

Objetivos

- Criar animações de ataque;
- Programação;
- Colisão de ataque\.

Estratégias e atividades

- Criando animações de ataque \.
	- Duplique a animação de __idle\_down__, renomeie para attack\_down\. Modifique os frames 1 \- 36/2 \- 37/3 \- 38/3 \- 39\. Agora delete os frames que sobraram\. mude o relógio da animação para 0\.4 e desmarque o loop \(as setas devem ficar brancas\);
	- Agora para __attack\_right__\. Duplique a animação de attack\_down, mude os frames para 1 \- 42/2 \- 43/3 \- 44/4 \- 45;
	- Agora para __attack\_left__\. Duplique a animação de __attack\_right__, mude o position para 0\.5 positivo e marque o flipH como true;
	- Agora para __attack\_up__\. Duplique a animação de attack\_down, mude os frames para 1 \- 48/2 \- 49/3 \- 50/4 \- 51\.
- Selecione o animationTree\.
	- Crie um novo blendspace2d, renomeie para attack e clique para abrí\-lo\. Mude o blend para 3 pontos, selecione o lápis e adicione as animações como na última aula\.
- Adicionando um timer para evitar bugs\.
	- Adicione um novo no chamado timer e renomeie para AttackTimer;
	- No inspetor mude o Waittime para 0\.4s e marque o one shot;
	- Agora com o  AttackTimer selecionado, clique em node do lado do inspetor e clique em cima de timeout\(\), selecione o character na tela que aparecer e em connect\.
- Agora passe as mudanças do script do player aos alunos\.
- Adicionando tecla de atalho\.
	- Entre em project settings > inputmap;
	- Adicione um add new action e chame de attack;
	- Clique no \+ do lado esquerdo da lixeira e escolha o botão que desejar que ataque\.
- Adicionando dependências no inspetor do Character\.
	- Selecione o character e use estas configurações\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952744506100.png)__

- Adicionando um novo nó\.
	- Adicione um novo nó chamado area2D e mude o nome para AttackArea;
	- Adicione um novo nó dentro de AttackaArea chamado collisionshape2D e muda o nome para collision;
	- E no inspetor do collision em shape, mude a collision para __rectangle __e no __disabled __deixe marcado\.
- Adicionando hitbox na animação de attack\_down\.
	- Selecione a animação attack\_down, depois na hierarquia selecione o colisor e ajuste ele para que fique debaixo do pé do personagem \(o Transform position Y normalmente fica 12\);
	- Agora clique na chavinha \(depois de ter arrumado o colisor\) do __shape__, __Transform position__ e __disabled marcado \(azul\)__;
	- Agora mude a barra azul para __0\.1__ e clique com o botão direito do mouse __em cima da barra azul__, na __mesma linha do disabled__, e insira uma key com o value dela sem marcação;
	- Agora faça o mesmo para__ 0\.3__ e deixe o value marcado como __on__;
	- Se tudo deu certo é para ficar assim:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952750528700.png)

__		__

- Adicionando hitbox na animação de attack\_up\.
	- Mesma coisa do down, só que ajuste a colisão para cima e clique na chave do __Shape, Transform Position e Disabled \(marcado\)__;
	- Depois insira as chaves na linha \(0\.1 e depois 0\.3\) do disabled e coloque a primeira desativada e a segunda ativa;
	- Se não conseguir editar a colisão vá até animationTree e desative no inspetor o active\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261952752536900.png)__

- Adicionando hitbox na animação de attack\_left e right\.
	- Ajuste a colisão para os lados respectivos e clique na chave do __Shape, Transform Position e Disabled \(marcado\)__;
	- Depois insira as chaves na linha \(0\.1 e depois 0\.3\) do disabled e coloque a primeira desativada e a segunda ativa;
	- Se não conseguir editar a colisão vá até animationTree e desative no inspetor o active\.
- Teste seu jogo, não esqueça de ativar o __active__ do animationTree e também ativar em __DEBUG__ \(deixar colisores visíveis\) do lado de Project\.

Recursos

- Computador, internet, Godot instalado\.

Observação

- O projeto utiliza o Godot 4\.0 [https://godotengine\.org/download/windows/](https://godotengine.org/download/windows/)
- Será um jogo estilo RPG visto de cima\.
- Se os projetos dos alunos apresentarem muitos erros basta clonar a branch da próxima aula no git e passar para os computadores da escola\.

Tarefas

- Sem tarefa\.

