# __PLANO DE AULA__

Aula 18 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Acelerador/Trampolim\.

Objetivos

- Criar Acelerador;
- Criar Trampolim\.

Estratégias e atividades

- Abrindo o Roblox Studio:
	- Inicie o Roblox Studio e selecione um novo projeto Baseplate\.
- Criar uma conta com o gmail das crianças
- Colocando e Modificando um Bloco:
	- No painel Insert, clique com o botão direito em Part;
	- Você verá um bloco \(Parte\) no meio de sua tela;
	- Usando as ferramentas no painel tools, mova, redimensione e gire o bloco;
	- No painel edit, modifique as propriedades da Parte, como cor, material, âncora \(deixar o bloco fixo\) e etc\.
- Criando o Bloco Acelerador:
	- Insira uma nova Parte como feito anteriormente;
	- Redimensione e posicione onde você deseja que o acelerador esteja;
	- Adicionando Script ao Acelerador;
	- Com a Parte selecionada, clique com o botão direito, escolha Insert Object, e selecione Script;
	- No script, insira o seguinte código:

\-\- Obtém a parte \(objeto\) onde o script está anexado

local part = script\.Parent

\-\- Define um multiplicador de velocidade

local speedMultiplier = 2

\-\- Este bloco de código é executado quando algo toca na parte

part\.Touched:Connect\(function\(hit\)

    \-\- Verifica se o que tocou na parte é um personagem

    local character = hit\.Parent

    local humanoid = character:FindFirstChildOfClass\("Humanoid"\)

    

    \-\- Se o que tocou for um personagem \(humano\)

    if humanoid then

        \-\- Aumenta a velocidade de caminhada do personagem

        humanoid\.WalkSpeed = humanoid\.WalkSpeed \* speedMultiplier

        

        \-\- Espera por 5 segundos

        wait\(5\)

        

        \-\- Retorna a velocidade de caminhada do personagem ao valor original após 5 segundos

        humanoid\.WalkSpeed = humanoid\.WalkSpeed / speedMultiplier

    end

end\)

- Criando o Bloco Trampolim:
	- Insira uma nova Parte como antes;
	- Redimensione e posicione onde você quer que o trampolim esteja;
	- Adicionando Script ao Trampoline e Configuration:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261953771075600.png)

No script, insira:

local trampoline = script\.Parent

trampoline\.Velocity =Vector3\.new\(0,trampoline\.Configuration\.BounceSpeed\.Value, 0\)

trampoline\.SurfaceGui\.Enabled = false

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Criar uma conta no Roblox se não tiver\.

