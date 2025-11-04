# __PLANO DE AULA__

Aula 26 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): GameMaker

Conteúdos

- Colocando Sprites e Criando a vida\.

Objetivos

- Trocar Sprites;
- Colocar sistema de vida\.

Estratégias e atividades

- Diminuindo cenário:
	- Clique em Room1 dentro de cenas e abra o inspetor\. Mude sua largura para 720 e altura para 480\.
- Criando um novo sprite:
	- Renomeie esse novo sprite para __spr\_parado\_direita__;
	- Agora importe o asset do nosso personagem para a direita clicando no __importe__;
	- Depois clique em __edite imagem__ > em __imagem __\(em cima do lado direto de ajuda\) > __converter para quadros__;
	- Use as informações da imagem a seguir:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457380020000.png)

- 
	- Coloque o ponto de origem no pé do personagem;
	- Ajuste o fps da imagem para 4\.
- Adicionando o sprite parado esquerda:
	- Renomeie para __spr\_parado\_esquerda__;
	- Depois clique em __edite imagem__ > em __imagem __\(em cima do lado direto de ajuda\) > espelho > todos os quadros\.
- Adicionando sprite andando:
	- Crie uma nova sprite, e renomeie para __spr\_andando\_direita__;
	- Importe o asset do personagem andando para direita;
	- Depois clique em __edite imagem__ > em __imagem __\(em cima do lado direto de ajuda\) > converter para quadros;
	- Use as configurações da imagem a seguir:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457391167300.png)

- 
	- Troque o fps para 10\.
	- Coloque a origem no pé do personagem\.
- Duplicando sprite do personagem andando\_direita:
	- Mude o nome para __spr\_andando\_esquerda__;
	- Duplique como o sprite de parado e espelhe ele, como fizemos anteriormente\.
- Voltando ao objeto do player:
	- Clique no objeto do player e troque o sprite para o player __spr\_parado\_direita__\.
- Criando objeto controle:
	- Clique com o botão direito na pasta objeto, adicione um novo objeto e renomeie para __Obj\_Controle__;
	- Adicione um evento chamado desenhar gui;
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457395166800.png)
	- Arraste este objeto para cena como na imagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457397166900.png)x

- Criando sprite de Vida:
	- Crie uma nova sprite, renomeie para __spr\_vida__ e adicione o asset do coração nela;
	- O ponto de origem fica na esquerda superior\.

Recursos

- Computador, internet e GameMaker\.

Observação

- Está aula foi feita em uma outra versão do GameMaker, peço que instale no computador das crianças [https://gamemaker\.io/pt\-BR/download](https://gamemaker.io/pt-BR/download)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457401324500.png)

Tarefas

- Pesquisar e entender sprites e como elas são montadas\. Traga sua pesquisa em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com)\.

