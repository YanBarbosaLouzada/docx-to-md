# __PLANO DE AULA__

Aula 25 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Inputs\.

Objetivos

- Interação com mouse e teclado\.

Estratégias e atividades

__Input__ significa entrada de dados\. No caso dos jogos, são os comandos que o jogador envia — como apertar uma tecla, clicar com o mouse ou tocar na tela\.

START

No Roblox Studio, podemos detectar esses comandos e fazer o jogo reagir a eles com __scripts__\.

### <a id="_heading=h.9x8cvfx7igxj"></a>__Conhecendo o UserInputService__

O UserInputService é uma ferramenta do Roblox que permite capturar os comandos do jogador\. Com ele, podemos detectar quando uma tecla é pressionada e fazer algo acontecer\.

### <a id="_heading=h.j8bem0lv1y1s"></a>__Exemplo Prático: Fazer o jogador pular com a tecla “P”__

Vamos criar um script que faz o personagem pular toda vez que o jogador aperta a tecla __P__\.

### <a id="_heading=h.hy9de4ljryzj"></a>__Passo a Passo__

#### <a id="_heading=h.nhh73du5rp9u"></a>__1\. Abra seu projeto no Roblox Studio\.__

Pode ser um projeto novo com o template *Baseplate*\.

#### <a id="_heading=h.fsusp2vfes7"></a>__2\. Crie um Script Local:__

- Clique em __StarterPlayer__ > __StarterPlayerScripts  
__
- Clique com o botão direito e escolha __Insert Object > LocalScript  
__
- Use __LocalScript__, pois ele é necessário para capturar inputs do jogador\!

#### <a id="_heading=h.q80azwcz4yhv"></a>__3\. Copie este código no LocalScript:__

\-\- Ativa o serviço de input

local UserInputService = game:GetService\("UserInputService"\)

local player = game\.Players\.LocalPlayer

local character = player\.Character or player\.CharacterAdded:Wait\(\)

local humanoid = character:WaitForChild\("Humanoid"\)

\-\- Detecta quando uma tecla é pressionada

UserInputService\.InputBegan:Connect\(function\(input, gameProcessed\)

	if gameProcessed then return end \-\- ignora se o input for usado pelo sistema

	if input\.KeyCode == Enum\.KeyCode\.P then

		\-\- Faz o personagem pular

		humanoid:ChangeState\(Enum\.HumanoidStateType\.Jumping\)

	end

end\)

### <a id="_heading=h.jcnp4h3ix7dd"></a>__Explicação do Código:__

- UserInputService: captura as entradas do teclado\.  

- InputBegan: evento que detecta quando uma tecla é pressionada\.  

- input\.KeyCode == Enum\.KeyCode\.P: verifica se a tecla apertada foi a __P__\.  

- humanoid:ChangeState\(Jumping\): faz o personagem pular programaticamente\.  


### <a id="_heading=h.qlu8l7iqbzy"></a>__Desafio:__

Altere o script para que outras teclas façam ações diferentes:

- Tecla __R__: o personagem diga algo no chat\.  

- Tecla __L__: o personagem perca um pouco de vida\.  


Quer um exemplo dessas ações também?

__O que o aluno deve saber ao final:__

- Como detectar quando uma tecla é pressionada\.  

- Como usar o UserInputService com LocalScript\.  

- Como aplicar uma ação a partir de um comando do teclado\.

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

