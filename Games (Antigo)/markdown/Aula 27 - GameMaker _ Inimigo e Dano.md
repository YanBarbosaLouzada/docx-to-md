# __PLANO DE AULA__

Aula 27 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): GameMaker

Conteúdos

- Primeiro inimigo e causando dano no player\.

Objetivos

- Primeiro inimigo;
- Causar dano no player\.

Estratégias e atividades

- Crie uma nova sprite para o inimigo:
	- Renomeie para __spr\_cebola\_andando\_direita__;
	- Clique em importar e importe o inimigo ‘cebola’;
	- Agora clique em editar imagem > imagem \(do lado direito de ajuda\) > converter para quadros, e ajuste de acordo com a imagem a seguir:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457533750000.png)
	- Mude o fps da cebola para 8 para que se mova mais lentamente e o ponto de origem para centro inferior\.
- Fazendo o inimigo andar para a esquerda:
	- Duplique o sprite da cebola andando para a direita e renomeie;
	- Depois clique em editar imagem > imagem > espelho > todos os quadros\.
- Arrumando máscara de colisão:
	- Volte para os sprites do inimigo e faça isso para os dois\. Clique em máscara de colisão, mude o modo para manual o tipo para retângulo e ajuste a colisão somente para o corpo do inimigo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457537752200.png)

    

- Criando um objeto para o inimigo cebola:
	- Crie o objeto e renomeie para __Obj\_inimigo\_cebola__;
	- Coloque a sprite da cebola andando para a direita;
	- Vamos adicionar um evento CRIAR e uma ETAPA\.
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457539903700.png)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457541903500.png)
	- Dentro do objeto do inimigo, entre na opção de máscara de colisão e coloque para que ‘sempre use a da do inimigo andando para a direita’;![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457542903800.png)
	- Coloque o objeto inimigo na sua cena\.
- Criando uma parede para o inimigo:
	- Crie uma sprite para esta parede e renomeie para __spr\_parede\_inimigo__;
	- Clique em editar imagem e coloque uma cor sólida que preencha toda a imagem da sprite;
	- Crie um objeto para esta parede e renomeie para __obj\_parede\_inimigo__, coloque a sprite da parede inimigo dentro do objeto;
	- Adicione os eventos CRIAR e ETAPA;
	- Coloque esta parede na cena de uma forma que o nosso inimigo encoste nela e vire para o lado contrário;
	- Por fim, volte ao objeto e desmarque a opção visível\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457544901300.png)

- Fazendo player tomar dano:
	- Dentro do objeto player, adicione os eventos: Alarme0 e Colisão > obj\_inimigo\_cebola\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457546904000.png)

- Passe os scripts para as crianças\.

Recursos

- Computador, internet e GameMaker\.

Observação

- Esta aula foi feita em uma outra versão do GameMaker, peço que instale no computador das crianças [https://gamemaker\.io/pt\-BR/download](https://gamemaker.io/pt-BR/download)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780457547903400.png)

Tarefas

- Sem tarefa\.

