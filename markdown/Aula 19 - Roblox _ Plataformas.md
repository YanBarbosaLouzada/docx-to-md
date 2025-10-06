# __PLANO DE AULA__

Aula 19 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Plataforma explosiva;
- Plataforma que cai\.

Objetivos

- Criar plataforma explosiva;
- Criar plataforma que cai;
- Programação\.

Estratégias e atividades

-  Criando plataforma explosiva\.
	- Primeiro crie uma part \(bloco quadrado\);
	- Agora renomeie para ExplosionPart e depois adicione um script a ela;
	- No script você vai escrever:

local explosion = Instance\.new\("Explosion",game\.Workspace\)

explosion\.Position = game\.Workspace\.ExplosionPart\.Position

ARRUMAR NA APOSTILA

\-\- Referencia o bloco

local ExplosionPart = script\.Parent

\-\- Função para criar uma explosão

local function explode\(part\)

	\-\- Cria uma nova instância de uma explosão

	local explosion = Instance\.new\("Explosion"\)

	explosion\.Position = part\.Position \-\- Define a posição da explosão para a posição do bloco

	explosion\.Parent = game\.Workspace \-\- Define o pai da explosão como o Workspace

end

\-\- Loop infinito

while true do

	\-\- Muda a cor do bloco para branco

	ExplosionPart\.BrickColor = BrickColor\.new\("Bright white"\)

	wait\(1\)

	\-\- Muda a cor do bloco para vermelho

	ExplosionPart\.BrickColor = BrickColor\.new\("Bright red"\)

	\-\- Gera um tempo de espera aleatório entre 1 e 5 segundos

	local randomWaitTime = math\.random\(1, 5\)

	\-\- Espera pelo tempo aleatório gerado

	wait\(randomWaitTime\)

	\-\- Chama a função de explosão no bloco

	explode\(ExplosionPart\)

end

- Para montar uma plataforma que explode randomicamente, clonar vários desse explosion part e colocar dentro de um group\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780456467876700.png)

- Criando plataforma que cai\.
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

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780456475039200.png)

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Sem tarefa\.

