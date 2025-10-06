# __PLANO DE AULA__

Aula 14 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

	                                

Conteúdos

- Construindo Terreno\.

Objetivos

- Tile Map;
- Construir Terreno;
- Trabalhando com colisão de terreno\.

Estratégias e atividades

- Crie uma nova cena\.
	- Pesquise no other por __node tilemap__ e renomeie para Terrain\.
- Configurando terrain\.
	- No inspetor de __terrain__ use estas configurações:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454614394500.png)
- Adicionando tilemap\.
	- Ainda dentro do inspetor do __terrain__, clique tileset;![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454616391000.png)
	- Depois disso abra sua pasta onde estão guardados os assets do tilemap e arraste a grama\. Clique em __Yes__\.

__		![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454618393100.png)__

- Criando terreno base \(plains\.png\)\.
	- Faça o mesmo: arraste e depois troque nome para __terrain__ e clique em nó; 
	- Após isso selecione com o botão esquerdo do mouse apenas as montanhas e o chão\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454625584600.png)
- Depois no inspetor de __terrain__ use a configuração da imagem abaixo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454630708400.png)

- Selecionado propriedades\.
	- Clique em ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454632710100.png), depois em ‘paint properties’ e selecione terrains;
	- Em terrain set passe o terrain set 0;
	- Terrain passamos o grass\_path;
	- E a agora pinte apenas as terras \(caso pinte errado, com o botão direito do mouse ele retorna o pixel normal\);
	- Se tudo deu certo é para ficar assim:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454633709700.png)
- Salvando cena\.
	- Aperte Ctrl \+ S para salvar a cena e salve dentro da pasta onde está salvando as cenas\.
- Criando uma nova cena para construir o terreno\.
	- Clique em Node 2D \(Scene2D\) após criar a nova cena e mude o nome para level;
	- Agora vamos __instanciar __nosso __terreno __e o __character __dentro desta nova cena\. Basta__ clicar no botão que fica do lado do \+__ para isso\. Em seguida, __selecione __a cena __terrain __e depois a __character__\.
	- Selecione o __terrain__ na hierarquia e depois selecione lá embaixo onde abriu o terminal __Terrains__, e comece a pintar\.
	- Para pintar somente a grama, vá em __tiles__, depois clique em __grass__, e selecione o bloco\.
- Pintando com grama\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454637709700.png)
- Pintando buracos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454638711200.png)

- Adicionando mais coisas no tilemap\.
	- Vá para a cena de terrain > selecione o terrain > no inspetor, clique em tileset > terrain sets > crie um novo elemento podemos chamá\-lo ciff\_path\. Vamos colocar a cor dele como preta\.
	- Agora vá em paint > em terrain vamos mudar de grass\_path para cliff\_path\. Pinte todos os terrenos de baixo\.
	- Se tudo estiver certo é para ficar assim:

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454640864300.png)

- Criando layers\.
	- Selecione __terrain__ e faça no inspetor como na imagem abaixo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454641865300.png)

- Volte para cena Level\.
	- Quando colocar a montanha, selecione na layer cliff\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454643865900.png)

- Adicionando colisores\.
	- Vá novamente para cena do __terrain__ > no inspetor clique em tileset\. Procure por Physics Layers e clique em add;
	- Clique em Paint > Paint Properties > Physics Layer 0 e com o botão esquerdo do mouse marque a montanha \(desenho abaixo\);
	- Imagem exemplo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780454646865200.png)

- Agora você pode adicionar mais coisas se quiser, todas serão feitas basicamente da mesma forma\.

Recursos

- Computador, internet, Godot instalado\.

Observação

- O projeto utiliza o Godot 4\.0 [https://godotengine\.org/download/windows/](https://godotengine.org/download/windows/)
- Será um jogo estilo RPG visto de cima\.
- Se os projetos dos alunos apresentarem muitos erros basta clonar a branch da próxima aula no git e passar para os computadores da escola\.

Tarefas

- Sem tarefa\.

