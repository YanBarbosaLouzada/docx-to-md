# __PLANO DE AULA__

Aula 29 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): GameMaker

Conteúdos

- Arremessando Projéteis e Grupos de Organização\.

Objetivos

- Criar projétil arremessável;
- Criar grupos de organização;
- Criar um novo inimigo\.

Estratégias e atividades

- Criando um novo inimigo:
	- Crie uma sprite e renomeie para __spr\_tomate\_atacando__\. Importe o tomate atacando para a direita;
	- Clique em editar imagem > imagem > converter para quadros, use estas configurações:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457830248900.png)

- 
	- Mude o ponto de origem para a boca do tomate;
	- Mude o fps para 6\.
- Criando objeto inimigo:
	- Crie um novo objeto e renomeie para __obj\_inimigo\_tomate__;
	- Coloque a sprite do tomate;
	- Adicione eventos __alarm0__ e __create__
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457833678000.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457838749600.png)
- Criando objeto parente:
	- Crie um novo objeto e renomeie ele para __parente\_inimigo__;
	- Depois clique em ‘pai’ e arraste o objeto dos dois inimigos do nosso jogo para dentro da caixa que foi aberta;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457841412900.png)

- 
	- Volte ao objeto do personagem e no hitbox, e troque o inimigo para parente inimigo;

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457845567700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457847827800.png)

coloque este script dentro de parent\_inimigo que vai estar no hitbox![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457849923400.png)

- 
	- Adicione o evento __criar__, __etapa__, __alarm1 __e __desenhar__;\(No objeto pai\)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457851690700.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457852699900.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457853699600.png)
	- Dentro do objeto ‘cebola’, substitua a etapa\. Basta clicar com o botão direito em cima da etapa que vai estar meio apagada e selecionar ‘substituir’\.
	- Depois altere os script do create e do etapa do inimigo cebola
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457855700100.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457856698900.png)
- Criando projétil:
	- Crie uma nova sprite e renomeie para __spr\_tomate\_projetil__;
	- Importe a imagem do projétil e mude o ponto de origem para o centro\.
- Criando objeto projétil:
	- Crie um novo objeto e renomeie para __obj\_tomate\_projetil__;
	- Coloque o sprite do projétil no objeto;
	- Adicione o evento CRIAR e COLISÃO com__ obj\_chao__\.
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457858699400.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457859700800.png)
- Adicionando eventos no personagem:
	- Volte ao objeto personagem e adicione o evento\. Colisão > obj\_tomate\_projetil e depois faça com o parente\_inimigo
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457861857300.png)

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457862855500.png)

- Mudança no create do personagem adicione no script 
	- inv\_tempo = 180;
- Adicionando duas sprites de morte:
	- Crie uma sprite e renomeie para __spr\_cebola\_morrendo__, importe a imagem e depois separe em quadros: editar imagem > imagem > separar em quadros;
	- Mude o fps para 10 e o centro de origem para o pé da cebola;
	- Crie outra sprite e renomeie para __spr\_tomate\_morrendo__, importe a imagem e depois separe em quadros: editar imagem > imagem > separar em quadros;
	- Coloque o ponto de origem na boca do tomate e o fps muda para 10\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457864908000.png)

- Por fim, passe os scripts dos eventos de cada objeto para as crianças e lembre\-se de colocar o inimigo tomate \(objeto\) na tela do jogo \(Room1\)\.

Recursos

- Computador, internet e GameMaker\.

Observação

- Esta aula foi feita em uma outra versão do GameMaker, peço que instale no computador das crianças [https://gamemaker\.io/pt\-BR/download](https://gamemaker.io/pt-BR/download)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457866907600.png)

Tarefas

- Pesquisar sobre herança e sobre orientação a objeto\. Monte uma apresentação e traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com)\.

