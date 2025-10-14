# __PLANO DE AULA__

Aula 28 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): GameMaker

Conteúdos

- Scripts e Personagem Atacando\.

Objetivos

- Criar o ataque do personagem\.

Estratégias e atividades

- Criando sprite do personagem:
	- Crie uma nova sprite e renomeie para __spr\_personagem\_atacando\_direita__;
	- Clique em importar e importe a imagem do personagem atacando para a direita;
	- Clique em editar imagem > imagem > converter para quadros, use a imagem como exemplo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457639902700.png)

- 
	- Mude o fps para 12 e seu ponto de origem para o pé do personagem;
	- Mude a colisão para que não fique muito grande, use a imagem como exemplo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457641903800.png)

- Criando sprite do personagem atacando para a esquerda:
	- Duplique a sprite do personagem atacando para a direita e renomeie para __spr\_personagem\_atacando\_esquerda__;
	- Depois clique em editar imagem > imagem > espelhar;
	- Coloque o ponto de origem no pé do personagem\.
- Criando sprite hitbox:
	- Crie uma sprite chamada __spr\_hitbox__;
	- Redimensione as propriedades \(tamanho\) para:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457643905900.png)

- 
	- Agora, clique em editar imagem e adicione um círculo preenchido:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457645904500.png)

- 
	- Mude o ponto de origem para o centro;
	- Mude a colisão de acordo com a imagem a seguir:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457646904800.png)

- Criando o objeto hitbox:
	- Crie um objeto chamado __obj\_hitbox__;
	- Coloque a __spr\_hitbox__;
	- Adicione os eventos __criar, alarme0__ e __colisão > obj\_inimigo\_cebola__;
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457648905000.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457650906700.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457651905700.png)
	- Desative o ‘visível’ deste objeto\.
- Criando script:
	- Clique na pasta script com o botão direito do mouse e selecione a opção script\. Renomeie para __scr\_personagem__;
	- Neste script vamos trazer toda a programação de movimentação do nosso player\. Você encontra no github da escola\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457653906500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457654904300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457656906100.png)

Agora atualize a etapa e create do personagem

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457657904100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457660905500.png)

- Criando script:
	- Crie outro script e mude o nome dele para __scr\_fim\_da\_animacao__ para checar se nossa animação de ataque acabou\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457663906000.png)

- Após terminar as alterações do personagens vamos adicionar as do inimigo

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457665905500.png)

- Agora chegamos ao fim da aula

Recursos

- Computador, internet e GameMaker\.

Observação

- Esta aula foi feita em uma outra versão do GameMaker, peço que instale no computador das crianças [https://gamemaker\.io/pt\-BR/download](https://gamemaker.io/pt-BR/download)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457670904600.png)

Tarefas

- Jogar na sua casa jogos de plataforma\. Anote referências e traga para a próxima aula\.

