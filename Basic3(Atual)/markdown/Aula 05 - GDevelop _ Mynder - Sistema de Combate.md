# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773492694300.png)

# __PLANO DE AULA__

Aula 05 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Computador

Ferramenta\(s\): GDevelop baixado no computador

Conteúdos

- GDevelop: Jogo de Plataforma \- Mynder’s Mission\.

Objetivos

- Criando Inimigos;
- Sistema de Combate;
- Coleta de Itens\.

Estratégias e atividades

Para enfrentar novos desafios, Mynder receberá um __sistema de combate__ e __coleta de itens__, que o ajudarão em sua jornada\.

START

Em jogos de plataforma, inimigos são basicamente obstáculos que se movem, podendo ter diferentes ações e reagir ao jogador\. Além de contribuírem para a progressão do jogo, os inimigos ajudam a aumentar gradualmente a dificuldade, proporcionando uma experiência de jogo envolvente e desafiadora\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773497555000.png)

Nosso primeiro inimigo irá seguir o Mynder sempre que estiver a uma certa distância\. Além disso, irá __disparar projéteis__ que podem ferir nosso personagem:

- Selecione o __Droid1__ e arraste até a cena\. Vamos adicionar um comportamento chamado __Pathfinding \(Buscar Trajetória\)__ que faz o inimigo seguir uma posição automaticamente:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773497555000.png)

- Altere a __Aceleração__ para __50__ e __Velocidade máxima__ para __100__ e desmarque a opção__ Rotacionar objeto__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773499563300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773501571400.png)

- Para evitar que o inimigo fique preso, como em paredes, por exemplo, podemos sinalizar outros objetos como __Obstáculos para a trajetória__\. Vamos fazer isso com o __GroundTile__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773503642900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773505662700.png)

- Além de seguir o personagem, o inimigo também irá disparar projéteis\. Vamos automatizar esse processo com o comportamento __Fire bullets__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773507669600.png)

Agora vamos aos __Eventos__ programar seu funcionamento:

- O inimigo inicia o ataque sempre que a __distância__ até o Mynder for menor que __200 pixels__, perseguindo o __Mynder:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773509368600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773509368600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773512843600.png)

- Ativamos também o __disparo dos projéteis\.__ Ajuste os valores corretamente para que o projétil saia da arma do inimigo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773514851700.png)

O inimigo já persegue e dispara corretamente, mas ainda precisamos__ inverter__ o inimigo quando muda de direção\. Note que o projétil também parece sair do nada, pois está acima do sprite do inimigo\. Vamos alterar sua __ordem Z__ para consertar isso:

- Sempre que a __posição X__ do__ Droid1 __for maior que a __posição X__ do __Mynder__, ele é invertido e vice\-versa \(repita o processo para o outro lado\):

 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773516859700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773516859700.png)

- Quando o inimigo __disparar o projétil__, altere a __ordem Z__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773519973200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773521980200.png)

- Teste o jogo e perceba que o inimigo segue o personagem, atirando em sua direção:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773523987300.png)

- Vamos adicionar um novo __Grupo de Eventos__ chamado __Dano__ e incluir o espinho e a serra\. Seguindo a mesma lógica, __aplicamos dano__ ao Mynder sempre que colidir com um projétil:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773526130800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773527129800.png)

- Vamos __destruir__ o projétil após a colisão com Mynder:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773529131400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773530637100.png)

Quando o projétil não atinge o Mynder, ele continua o movimento infinitamente e nunca será destruído, o que pode gerar um desempenho ruim quando temos vários projéteis em cena:

- Para evitar isso, iremos utilizar o comportamento __Destruir quando fora da tela:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773532644900.png)__

- Vamos definir uma__ margem de 100 pixels__, para que ele seja destruído depois que ultrapassar a tela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773532644900.png)

Para que o Mynder consiga combater o inimigo, vamos adicionar uma mecânica parecida de disparo, porém, ao invés de usar um sprite como projétil, vamos criar um objeto do tipo __Emissor de Partículas__ para obter um efeito diferente:

- Crie um novo objeto do tipo Emissor de Partículas e escolha um modelo de partícula que preferir:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773535533200.png)

- Altere o nome para __Disparo__ e a as cores iniciais e finais para __verde:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773537540000.png)

- Altere o __tempo__ de vida das partículas: __mínimo__ \-> __0,3__ e __máximo__ \-> __0,1__
- Altere o __tamanho__ das partículas: __inicial__ \-> __50__ e __final__ \-> __5__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773539547500.png)__

Vamos adicionar ao Mynder o comportamento __Fire bullet__, para que ele possa disparar, assim como o inimigo:

- Altere o atributo __Firing cooldown__ para disparar a cada __1 segundo:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773541845700.png)

Agora que já criamos o sistema de disparo, vamos para a programação nos Eventos:

- Primeiro criamos um novo __Grupo de Eventos__ para o __Disparo__ e detectamos quando o jogador aperta a tecla __X__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773543853900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773545566500.png)

- Também precisamos conferir se o Mynder não está morto antes de disparar:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773547575200.png)

- Devemos alterar a __direção do disparo__ e a __direção da emissão__ da partícula, de acordo com a direção do personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773549576300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773551057400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773553056900.png)

- Lembre\-se de alterar a __ordem Z__ do disparo para__ 0__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773554058300.png)

- Faça o mesmo quando o personagem __não está invertido__, invertendo os ângulos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773556055800.png)

O disparo está quase pronto, restando apenas alterar a animação do personagem atirando:

- Quando Mynder __disparar__, alteramos para animação __Shoot:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773558056200.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773560055600.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773562056100.png)__

- Quando a animação termina, retornamos para a animação __Idle:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773564067600.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773565055700.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773567075800.png)__

- Agora que o disparo está pronto, vamos incluir o comportamento __Health__ ao inimigo e __aplicar dano__ quando ele for atingido:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773569078300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773570079100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773571077200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773573075700.png)

- __Destrua o Disparo__ quando atingir o inimigo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773575077100.png)

Se a __vida__ do inimigo chegar a __0__, ativamos a animação __Death \(Morte\)__, impedimos que ele __dispare__ e __se mova__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773575077100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773575077100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773575077100.png)

- Quando a animação estiver finalizada, __destruímos__ o objeto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773581504100.png)

Assim terminamos o sistema de combate, mas para finalizar vamos adicionar um __item__ que pode ser __coletado__ ao longo do caminho e __aumenta a vida__ do Mynder:

- Utilizaremos o objeto __Vat__ que tem a figura de um __refil__\. Vamos renomear o objeto como __Recarga__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773583510300.png)

- Sempre que o personagem __colidir__ com a __Recarga__, a vida __aumenta__, desde que seja menor ou igual a __100__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773585517200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773587524500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773587524500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773589532100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773591839400.png)

- E __destruímos__ o item Recarga assim que é coletado:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773593686200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702773595339100.png)

Concluímos o sistema de combate e coleta de itens\. Agora, sua tarefa é criar mais fases com diferentes inimigos e obstáculos\. Utilizando o conhecimento adquirido até agora, pense em como podemos alternar entre as fases ao chegar em um portal\.

Desenvolva com entusiasmo e criatividade\!

Recursos

- GDevelop, internet, Google e computador\.

Observação

Tarefas

- Agora que nosso jogo está quase completo, que funcionalidades diferentes poderíamos implementar nele? Pense em novas ideias para enriquecer o projeto e envie uma apresentação para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com), traga em um pendrive ou em seu Google Drive/One Drive\. No caso de desenho ou escrita à mão, trazer na próxima aula\. 

