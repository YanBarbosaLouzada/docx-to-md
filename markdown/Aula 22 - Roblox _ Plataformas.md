# __PLANO DE AULA__

Aula 22 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Plataforma que cai\.
- Plataforma flutuante\.

Objetivos

- Criar plataforma que cai\.
- Criar plataforma flutuante\.
- Programação\.

Estratégias e atividades

Criando plataforma que cai\.

- 
	- Primeiro crie uma part \(bloco quadrado\) coloque Âncora nela;
	- Agora renomeie para Platcair e depois adicione um script a ela;
	- No script você vai escrever:

\-\- Vamos chamar isso de "plataforma"

local platform = script\.Parent

\-\- Guarda a posição inicial da plataforma

local initialPosition = platform\.Position

\-\- Define quanto tempo a plataforma espera antes de começar a cair

local waitTime = 2  \-\- 2 segundos

\-\- Define quanto tempo a plataforma espera antes de voltar à sua posição original após cair

local resetTime = 5  \-\- 5 segundos

\-\- Define a velocidade com que a plataforma vai cair\. Você pode pensar nisso como o quão rápido ela desce\.

local fallingSpeed = \-10  \-\- Ela desce 10 unidades por segundo\. 

\-\- Esta função serve para redefinir a posição da plataforma para o topo após cair\.

local function resetPlatform\(\)

    platform\.Velocity = Vector3\.new\(0, 0, 0\)  \-\- Para a plataforma, faz ela parar de se mover\.

    platform\.Anchored = true  \-\- Faz com que a plataforma fique fixa no lugar\.

    platform\.Position = initialPosition  \-\- Coloca a plataforma de volta na posição inicial\.

end

\-\- Esta função faz a plataforma começar a cair\.

local function startFalling\(\)

    platform\.Anchored = false  \-\- Libera a plataforma para que ela possa cair\.

    platform\.Velocity = Vector3\.new\(0, fallingSpeed, 0\)  \-\- Faz a plataforma cair para baixo com uma velocidade constante\.

    wait\(resetTime\)  \-\- Espera um tempo antes de redefinir a plataforma\.

    resetPlatform\(\)  \-\- Chama a função para colocar a plataforma de volta no topo\.

end

\-\- Esta função é chamada quando um jogador toca na plataforma\.

local function playerTouched\(\)

    wait\(waitTime\)  \-\- Espera um tempo antes da plataforma começar a cair\.

    startFalling\(\)  \-\- Chama a função para fazer a plataforma cair\.

end

\-\- Este bloco de código é executado quando um personagem \(jogador\) toca na plataforma\.

platform\.Touched:Connect\(function\(hit\)

    local character = hit\.Parent

    local humanoid = character:FindFirstChildOfClass\("Humanoid"\)

    

    \-\- Verifica se o que tocou na plataforma é um jogador

    if humanoid then

        playerTouched\(\)  \-\- Chama a função para fazer a plataforma começar a cair\.

    end

end\)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261954202308700.png)

- Plataforma Flutuante\.
	- Coloque um bloco \(part\) para ser a plataforma \(renomeie como desejar\), ative a âncora nela e crie um script para ela;
	- Antes de escrever o script você coloca duas plataformas onde você deseja que ela te leve \(ancore elas também\)\.
	- No script, coloque:

\-\- Vamos chamar esta coisa de "plataforma"

local platform = script\.Parent

\-\- Definimos onde a plataforma começa

local startPosition = platform\.Position

\-\- E onde ela vai terminar \(no nosso caso, vai se mover para a direita\)

local endPosition = Vector3\.new\(50, platform\.Position\.Y, platform\.Position\.Z\) \-\- Você pode mudar esse número se quiser

\-\- Ajustamos a velocidade da plataforma

local speed = 0\.01 \-\- Você pode fazer a plataforma ir mais rápido ou mais devagar mudando esse número

\-\- Inicializamos uma variável de tempo

local t = 0

\-\- Agora, repetimos o seguinte para sempre

while true do

    \-\- Aumentamos o valor de 't' com a velocidade

    t = t \+ speed

    \-\- Movemos a plataforma de acordo com 't', fazendo\-a ir do início ao fim suavemente

    platform\.Position = startPosition:Lerp\(endPosition, t\)

    \-\- Quando a plataforma chega ao seu destino \(t = 1\), fazemos ela voltar ao início

    if t >= 1 then

        \-\- Trocamos as posições de início e fim para que a plataforma volte

        startPosition, endPosition = endPosition, startPosition

        t = 0

        \-\- Esperamos um pouco antes de começar a mover a plataforma novamente

        wait\(2\) \-\- Espera por 2 segundos antes de se mover de novo

    end

    \-\- Esperamos um pouco antes de atualizar a posição novamente

    wait\(0\.03\)

end

- Criando Elevador\.
	- Coloque um bloco \(part\) para ser a plataforma \(renomeie como desejar\), ative a âncora nela e crie um script para ela;
	- Antes de escrever o script você coloca duas plataformas onde você deseja que ela te leve \(ancore elas também\)\.
	- No script coloque:

\-\- Defina o elevador

local elevator = script\.Parent

\-\- Configure a posição inicial e final do elevador

local startPosition = elevator\.Position

local endPosition = Vector3\.new\(elevator\.Position\.X, elevator\.Position\.Y \+ 50, elevator\.Position\.Z\) \-\- Vai subir 50 unidades\. Você pode mudar isso se quiser\.

\-\- Configure a velocidade do movimento do elevador

local moveSpeed = 3\-\- Velocidade do elevador

\-\- Configure o tempo de espera antes do elevador começar a se mover

local waitTime = 5 \-\- Tempo de espera antes do movimento

\-\- Inicialmente, o elevador vai subir

local direction = 1

\-\- Este é um loop que faz o elevador se mover para cima e para baixo repetidamente

while true do

	\-\- Espere por um certo tempo antes de iniciar o movimento

	wait\(waitTime\)

	

	\-\- Determine para onde o elevador deve ir \(para cima ou para baixo\)

	local goal = direction == 1 and endPosition or startPosition

	

	\-\- Continue movendo o elevador até que ele chegue ao seu destino

	while \(elevator\.Position \- goal\)\.magnitude > 1 do

		elevator\.CFrame = elevator\.CFrame:Lerp\(CFrame\.new\(goal\), moveSpeed \* 0\.01\) 

		wait\(0\.03\)

	end

	

	\-\- Mude a direção para que o elevador vá na direção oposta na próxima vez

	direction = \-direction

end

Imagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261954209871700.png)

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Sem tarefa\.

