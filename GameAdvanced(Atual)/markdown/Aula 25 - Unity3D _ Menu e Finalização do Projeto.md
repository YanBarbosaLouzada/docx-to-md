# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603203302300.png)

# __PLANO DE AULA__

Aula 25 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Menu e Build\.

Objetivos

- Criação do Menu e Finalização do Projeto\.

Estratégias e atividades

Estamos na reta final do desenvolvimento do nosso jogo de mundo aberto na Unity\! Nesta última aula, vamos aprender a criar um __menu inicial__ completo e exportar o __arquivo executável__, permitindo que você jogue o game diretamente no seu computador\.

Vamos criar uma __nova cena__ para o menu\. Esta será a cena principal quando iniciarmos o jogo:

- Clique em __File__ \-> __New Scene__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603219149900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603221157600.png)

- Para salvar a cena, clique em __File__ \-> __Save__ \(ou utilize o atalho __CTRL S__\) e renomeie como Menu, dentro da pasta Scenes:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603221157600.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603221157600.png)

O Menu do jogo é uma__ interface__, onde podemos iniciar um novo jogo ou carregar um jogo salvo, fazer ajustes como mapeamento de controles, configurações gráficas e também acessar outros modos de jogo\. Vamos criar um novo __Canvas__ para inserir nossos elementos de interface do menu:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603221157600.png)

- Renomeie o Canvas como __Menu__ e marque a opção de visualização __2D__ para visualizar melhor os elementos na tela:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603221157600.png)

Para manter a __identidade visual __do jogo, vamos adicionar um __fundo escuro__ ao menu\.

- Insira uma nova__ Image__ dentro do Canvas Menu:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603235033500.png)

- Renomeie para __Background__ e ajuste no tamanho da __tela inteira__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603239203700.png)

O menu deve passar uma atmosfera do que encontraremos em nosso jogo\.

- Neste exemplo, vamos buscar por __elementos__ da cidade para compor uma cena __urbana__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603239203700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603239203700.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603239203700.png)

- Para visualizar melhor a montagem da cena, vamos voltar ao ambiente 3D e desabilitaremos o fundo do menu por enquanto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603251112400.png)

- Vamos montar a __cena__ que se repetirá durante o menu:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603251112400.png)

- Utilize as __partes modulares__ da cidade para simular um pequeno trecho onde vamos fazer algumas __sequências__ de câmera:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603251112400.png)

- Quanto mais detalhes adicionarmos à cena, como luzes, objetos e veículos, mais rica e imersiva ela se tornará:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603259153200.png)

Após a montagem da cena, vamos criar uma nova __timeline__:

- Crie um novo objeto vazio chamado __Timeline\_Controller__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603259153200.png)

- Na timeline, clique em__ Create __e dê o nome de __Menu\_Scene__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603263264000.png)

- Arraste a __câmera__ para a timeline e criando uma nova__ Animation Track__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603263264000.png)

- Crie movimentos __horizontais__ \(panorâmica\) ou movimentos__ verticais__ \(tilt\), altere o __zoom__ e adicione __câmeras adicionais __para criar uma sequência que mostra a cidade de vários ângulos\. Observe um exemplo do que pode ser feito:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603266899400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603266899400.png)

- Após a montagem da cena, iremos fazer com que a cena se repita alterando a opção __Wrap Mode__ do __Playable Director__ para __Loop__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603274200700.png)

- Agora podemos reativar o__ fundo__ e diminuir sua __opacidade__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603274200700.png)

- Para a composição do menu, vamos criar um novo __TextMeshPro__ para o título:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603274200700.png)

- Vamos criar também dois botões para as ações de__ Iniciar Jogo__ e __Sair__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603274200700.png)

- Nosso menu ficou assim:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603282586800.png)

Para finalizar o menu, vamos criar um __script__ que irá conter as __ações dos botões__:

- Selecione o Canvas__ Menu__ e crie um novo __script__ chamado __Menu:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603306827300.png)__

Script do Menu:

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using UnityEngine;__

__using UnityEngine\.SceneManagement;__

__public class Menu : MonoBehaviour__

__\{__

__    public void StartGame\(\)__

__    \{__

__        SceneManager\.LoadScene\(1\);__

__    \}__

__    public void Exit\(\)__

__    \{__

__        Application\.Quit\(\);__

__    \}__

__\}__

- No __botão Iniciar Jogo__, insira a __função StartGame\(\)__ no evento __OnClick\(\):__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603316574000.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603319561500.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603321867800.png)__

- Repita o mesmo processo para o __botão Sair__, chamando a função __Exit\(\):__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603323869800.png)__

Para que a Unity carregue a cena corretamente, vamos configurar a __sequência__ de cenas:

- Clique em __File __\->__ Build Settings__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603325869400.png)

- Clique em __Add Open Scenes__ para inserir a cena __Menu__ como__ inicial__ \(__0__\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603328228000.png)

- Abra a __cena do jogo__ novamente e adicione como a __cena 1:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603329971700.png)__

Por fim, vamos criar um __arquivo executável__ do jogo para poder jogá\-lo no computador:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603332137900.png)

Aguarde até que a Unity termine a __criação da Build__ e teste o jogo:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603334146800.png)__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708603347370300.png)__

Finalizamos o nosso projeto, e agora contamos com uma base sólida para expandir e desenvolver um jogo de mundo aberto\. A estrutura que criamos serve como ponto de partida para adicionar novos elementos, como missões, veículos, personagens e sistemas dinâmicos, permitindo que o jogo cresça e evolua em escala e complexidade\.

Obrigado e até a próxima\!

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Sem tarefa\.

