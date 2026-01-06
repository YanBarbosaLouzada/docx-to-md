# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599493517100.png)

# __PLANO DE AULA__

Aula 03 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Manipulação de Terreno e Cenário\.

Objetivos

- Utilizar ferramentas de manipulação de Terreno
- Editando o Cenário;

Estratégias e atividades

Vamos começar criando um novo terreno na cena, clicando em __3D Object > Terrain__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599501628400.png)

Para adicionar mais recursos de terreno, vamos baixar o pacote__ Terrain Sample Asset Pack__, disponível na __Unity Asset Store__:

__*Dica para o professor: Baixe e importe este pacote antecipadamente no computador dos alunos\!* __

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599505177800.png)

Após fazer o download,__ importe__ o pacote no__ Package Manager:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599507609900.png)__

Agora temos as ferramentas necessárias para manipular o terreno\. Primeiro, altere o tamanho do terreno clicando em __Terrain Settings:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599507609900.png)

Vá até__ Mesh Resolution \(On Terrain Data\)__ e altere as opções: __Terrain Width \(Largura\) \-> 2000__ e __Terrain Length \(Comprimento\) \-> 2000\.__ 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599507609900.png)

Verifique agora se o terreno está em uma__ altura inferior à da cidade__, a fim de evitar __sobreposições__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599507609900.png)

Para iniciar a manipulação do terreno, clique em __Paint Terrain__ e selecione a opção __Stamp Terrain__ \(Carimbo de Terreno\)\. Utilize os diferentes pincéis para criar __áreas montanhosas__ ao redor da cidade, assim como__ áreas mais planas__, como praias e planícies:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599507609900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599520923300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)

Vamos adicionar uma textura de grama ao terreno\. Faremos isso através de__ Layers __\(Camadas\): Ainda em __Paint Terrain__, selecione agora a opção __Paint Texture__ e crie uma __nova Layer__, selecionando a textura __grass__ \(grama\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)

Além da textura de grama, podemos incluir também__ Meshes 3D__ de __grama__ e __árvores__:

Vá até a opção __Paint Details__ e depois em__ Add Detail Mesh:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)__

Altere as configurações do mesh da grama, como__ largura__,__ altura__ e__ densidade:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)__

Vamos baixar o pacote de árvores __World Space Trees__ e configurá\-las em __Paint Trees__ e depois em__ Add Tree:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599524940900.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599538734000.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599538734000.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599538734000.png)__

Para simular__ água __\(lago ou rio\), vamos criar um __3D Cube__ e aplicar uma textura que se movimenta, alterando sua posição em relação ao objeto\.

Baixe o __Simple Water Shader__ e crie um novo material que utilizará a textura\. Salve este material em uma pasta chamada __Materials__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599549851100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599555497700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599555497700.png)

Para__ movimentar__ o objeto e a textura, vamos criar um__ script “Water”__ e configurar da seguinte forma:

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using UnityEngine;__

__public class Water : MonoBehaviour__

__\{__

__    public Renderer waterRenderer;__

__    public float scrollSpeed = 0\.02f;__

__    public float amplitude = 0\.1f;__

__    public float frequency = 1f;__

__    private Vector3 originalPosition;__

__    void Start\(\)__

__    \{__

__        originalPosition = transform\.position;__

__    \}__

__    void Update\(\)__

__    \{__

__        float yOffset = amplitude \* Mathf\.Sin\(Time\.time \* frequency\);__

__        transform\.position = originalPosition \+ new Vector3\(0, yOffset, 0\);__

__        float offset = Time\.time \* scrollSpeed;__

__        Vector2 offsetVector = new Vector2\(offset, offset\);__

__        waterRenderer\.material\.SetTextureOffset\("\_MainTex", offsetVector\);__

__    \}__

__\}__

Adicione o __Scrip__t ao objeto __Water__ que configuramos anteriormente e sinalize a referência ao __Mesh Renderer__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599558950300.png)

Por fim, marque a opção __Is Trigger__ no componente__ Box Collider__, permitindo que o jogador entre no objeto, proporcionando a sensação de mergulhar na água:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599558950300.png)

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Sem tarefa\.

