# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600820858100.png)

# __PLANO DE AULA__

Aula 13 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Armas \- Parte 1

Objetivos

- Configurar sistema de armas\.

Estratégias e atividades

Chegou a hora de criarmos um sistema de armas para o personagem, que permitirá coletar e escolher diferentes tipos de armas\.

__START__

Vamos ajustar o Player e prepará\-lo para estar equipado com armas\. Primeiro, adicionaremos o pacote __Animation Rigging__, uma ferramenta que permite criar, modificar e controlar__ rigs de animação__ diretamente no editor\. Um __rig__ é uma __estrutura esquelética__ que pode ser associada a um modelo 3D, facilitando a animação de personagens ou objetos complexos\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600825164900.png)

Baixe e importe o pacote __Animation Rigging __através do Package Manager:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600829163200.png)

Selecione o objeto Player e vá até o menu __Animation Rigging__, clique em __Rig Setup__ e depois em __Bone Renderer Setup:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600832179000.png)__

Agora o __esqueleto__ do personagem deve aparecer da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600836163900.png)

Perceba que dentro do objeto Player foi criado um novo objeto __Rig 1\.__ Nele adicionaremos todas as __constraints__, que são as estruturas usadas para mover e apontar o esqueleto do personagem quando ele estiver atirando, por exemplo__\.__

Vamos adicionar as seguintes __constraints__ como objetos filhos do __Rig 1__:

- __Spine\_Aim: __Representa o corpo do personagem e controlará o giro da coluna quando estiver apontando a arma\.
- __Hand\_Aim: __Representa a mão que está segurando a arma e deve girar junto com ela para a direção do alvo\.
- __Second\_Hand: __Representa a posição da mão que não está com a arma e pode estar apoiando \(no caso de um rifle\)\.

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600839520200.png)__

Vamos configurar primeiro o movimento de mira do personagem\. Para isso, adicionaremos um objeto vazio dentro da cabeça do Player, com uma certa distância à sua frente\. Este será seu __alvo__ \(Aim Target\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600841526600.png)

Na constraint __Spine\_Aim__ dentro de __Rig 1__, adicione o componente __Multi\-Aim Constraint__ e configure\-o da seguinte forma:

- __Constrained Object__ deve ser a parte do esqueleto do personagem que irá girar e apontar para o alvo\.
- __Source Objects__ deve ter o objeto __Aim Target__ que acabamos de criar\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600843534000.png)

Na constraint __Hand\_Aim__, adicione também o componente __Multi\-Aim Constraint__, com algumas diferenças em sua configuração:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600843534000.png)

Note que agora o __Constrained Object__ deve ser a mão direita \(mão que segura a arma\)\.

Antes de prosseguirmos, vamos adicionar ao Player um objeto que servirá como referência para a arma\. Baixe na Unity Asset Store um pacote de modelos 3D de armas de sua preferência,, como no exemplo abaixo: 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600847231300.png)

Aproveite para baixar também o pacote __War FX__, que possui vários __efeitos visuais__, como explosões, impactos de munição, entre outros que serão úteis no nosso sistema de arma\.

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600854923700.png)

Vamos criar um objeto dentro da mão do Player chamado __WeaponSlot__\. Qualquer arma implementada será adicionada neste objeto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600856931000.png)

Agora adicione o modelo 3D da arma dentro de WeaponSlot:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600856931000.png)

Por último, precisamos configurar a segunda mão \(que não segura a arma\) como apoio\. Adicione dentro da Mão direita, depois de WeaponSlot, dois objetos vazios chamados __Second\_Hand\_target__ e __Second\_Hand\_hint__ e configure\-os de forma que o Player posicione o braço para apoiar a arma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600864901300.png)

No objeto __Second\_Hand__ dentro de __Rig 1__, adicione o componente __Two Bone IK Constraint__ e configure da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600868873500.png)

Para que a visão do jogador esteja em primeira pessoa enquanto mira, vamos adicionar uma __Cinemachine Virtual Camera__ dentro da __cabeça__ \(__head__\) do Player:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600870881900.png)

Posicione a câmera de modo que fique __atrás__ do Player, __por cima__ dos ombros:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600875807000.png)

Adicione o componente __Cinemachine 3rd Person Aim__ e configure a câmera da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600875807000.png)

Por último, vamos configurar os controles para o personagem equipado\. Na Input Actions __Controls__, adicione a Action Map __Equipped __e as Actions __Aim__ \(para mirar\) com botão direito do mouse e __Shoot __\(para atirar\) com botão esquerdo do mouse, ambas com Action Type __Value:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600875807000.png)__

Na próxima aula, iremos implementar as __mecânicas__ configuradas até aqui e criar a classe __Weapons__\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Sem tarefa

