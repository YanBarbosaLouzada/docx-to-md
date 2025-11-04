# __PLANO DE AULA__

Aula 26 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Interface\.

Objetivos

- Criar uma GUI\.

Estratégias e atividades

Em jogos, utilizamos uma interface para fornecer ao jogador informações importantes e feedback do estado atual do jogo\.

START

UI vem do inglês __User Interface__ \(Interface do Usuário\)\. No Roblox, usamos UI para mostrar informações na tela, como:

- Pontuação  

- Vida do jogador  

- Mensagens  

- Botões e menus  


Tudo isso é criado com __objetos de interface__, como *TextLabel*, *ImageLabel*, *TextButton* e outros\.

### <a id="_heading=h.25ob9uytyca0"></a>__Exemplo Prático: Mostrar uma mensagem na tela__

Vamos criar uma interface com uma mensagem que aparece quando o jogador entra no jogo\.

### <a id="_heading=h.3bq2rdu0q3re"></a>__Passo a Passo__

#### <a id="_heading=h.i3h047q8lzkp"></a>__1\. Crie uma ScreenGui__

- Vá até __StarterGui  
__
- Clique com o botão direito > __Insert Object__ > __ScreenGui  
__

O ScreenGui é o "container" principal da interface\. Tudo que estiver aqui vai aparecer na tela do jogador\.

#### <a id="_heading=h.y3lpcxzrdy3"></a>__2\. Adicione um TextLabel__

- Clique com o botão direito em ScreenGui > __Insert Object__ > __TextLabel  
__

Um TextLabel mostra um texto fixo na tela\.

#### <a id="_heading=h.2hau8waa4vcy"></a>__3\. Ajuste o visual do texto:__

- Com o TextLabel selecionado, vá no painel __Properties__:  

	- Text: "Bem\-vindo ao jogo\!"  

	- TextSize: 30  

	- BackgroundTransparency: 1 \(pra deixar o fundo invisível\)  

	- Position: \(0\.3, 0, 0\.05, 0\) *\(pode ajustar onde quiser\)  
*

### <a id="_heading=h.45nigh3taj7l"></a>__Agora vamos controlar via script\!__

Vamos esconder o texto depois de 5 segundos\.

#### <a id="_heading=h.tnxo3t7d1e7y"></a>__Crie um LocalScript:__

- Clique com o botão direito no __TextLabel__ > __Insert Object__ > __LocalScript  
__

#### <a id="_heading=h.aqcxzj12snc2"></a>__Escreva o seguinte código:__

local texto = script\.Parent

wait\(5\) \-\- espera 5 segundos

texto\.Visible = false \-\- esconde o texto

### <a id="_heading=h.33yfgm7aju1u"></a>__Explicação do Código:__

- script\.Parent: se refere ao TextLabel, que é o "pai" do script\.  

- wait\(5\): espera 5 segundos\.  

- Visible = false: esconde o texto da tela\.  


### <a id="_heading=h.yut31cfhrpxv"></a>__Desafio:__

- Altere o texto e o tempo de espera\.  

- Crie outro TextLabel que apareça __quando o jogador apertar uma tecla__ \(use junto com o UserInputService da aula anterior\)\.  

- Experimente adicionar um __TextButton__ e fazer ele executar uma ação\.  


__O que o aluno deve saber ao final:__

- Como criar e posicionar elementos de UI \(como TextLabel\)\.  

- Como alterar propriedades do UI via script\.  

- Como usar LocalScript para interações visuais com o jogador\.

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

