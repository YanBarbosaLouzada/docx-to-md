# __PLANO DE AULA__

Aula 21 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Plataforma explosiva;

Objetivos

- Criar plataforma explosiva;
- Programação\.

Estratégias e atividades

-  Criando plataforma explosiva\.
	- Primeiro crie uma part \(bloco quadrado\);
	- Agora renomeie para ExplosionPart e depois adicione um script a ela;
	- No script você vai escrever:

local explosionPart = script\.Parent

explosionPart\.Transparency = 1

local function Explode\(\)

	

	local explosion = Instance\.new\("Explosion"\)

	explosion\.Parent = explosionPart

	explosion\.Position = explosionPart\.Position

end

while true do

		explosionPart\.Transparency = 1

		wait\(3\)

		explosionPart\.Transparency = 0

		

		local light = Instance\.new\("PointLight"\)

		light\.Parent = explosionPart

		light\.Brightness = 100

		light\.Range = 10

		light\.Color = Color3\.new\(1, 0, 0\.0156863\)

		

		

		

		wait\(math\.random\(1,5\)\)

		

		game:GetService\("Debris"\):AddItem\(light,0\.01\)

		

		Explode\(\)

	

 end

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

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261954101683200.png)

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Sem tarefa\.

