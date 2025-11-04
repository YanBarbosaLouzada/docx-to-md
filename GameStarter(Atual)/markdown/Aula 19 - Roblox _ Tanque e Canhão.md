# __PLANO DE AULA__

Aula 19 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Tanque e Canhão\.

Objetivos

- Criar Modelo do Tanque
- Criar Canhão;
- Programação\.

Estratégias e atividades

- Criando um Canhão que atira:
	- Construindo o Canhão:
		- Use algumas Parts para modelar um canhão simples\. Uma Part cúbica para a base e uma cilíndrica para o tubo\.
	- Adicionando Script ao Canhão:
		- Com o tubo do canhão selecionado, clique com o botão direito, escolha Insert Object, e selecione Script\.
	- Coloque as duas partes como âncora no painel edit acima para que não caia por conta da gravidade\.
- Insira o seguinte código no script:

local cannonTube = script\.Parent

local projectileTemplate = Instance\.new\("Part"\)  \-\- Esta será a bola que o canhão dispara\.

projectileTemplate\.BrickColor = BrickColor\.new\("Really black"\)

projectileTemplate\.Shape = Enum\.PartType\.Ball

projectileTemplate\.Size = Vector3\.new\(2, 2, 2\)  \-\- Ajuste o tamanho conforme necessário\.

projectileTemplate\.Anchored = false

projectileTemplate\.CanCollide = true

local fireRate = 2  \-\- Tempo em segundos entre cada tiro\.

local function fireCannon\(\)

    local projectile = projectileTemplate:Clone\(\)

    projectile\.Position = cannonTube\.Position \+ \(cannonTube\.CFrame\.lookVector \* 3\)  \-\- Começa 3 studs à frente do tubo\.

    projectile\.Velocity = cannonTube\.CFrame\.lookVector \* 50  \-\- Ajuste a velocidade conforme necessário\.

    

    \-\- Adicionar uma função para lidar com o contato da bola com o jogador\.

    projectile\.Touched:Connect\(function\(hit\)

        local character = hit\.Parent

        local humanoid = character:FindFirstChildOfClass\("Humanoid"\)

        

        if humanoid then

            humanoid\.Health = 0  \-\- Mata o jogador\.

        end

    end\)

    

    projectile\.Parent = workspace

    \-\- Remova o projétil após 5 segundos para evitar que muitos objetos se acumulem\.

    game:GetService\("Debris"\):AddItem\(projectile, 5\)

end

while wait\(fireRate\) do

    fireCannon\(\)

end

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio   
[https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Pesquisar estilos de jogos Obby e dizer qual é o mais famoso desse estilo hoje em dia\. Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com)\.

