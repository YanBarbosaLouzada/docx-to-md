# __PLANO DE AULA__

Aula 22 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- ToolBox/Chão invisível que mata\.

Objetivos

- Criar chão invisivel;
- Aprender ToolBox\.

Estratégias e atividades

- Criando chão invisível que mata\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780456949698300.png)

- No script, escreva:

local Invisivel = script\.Parent

local function onTouch\(hit\)

	local character = hit\.Parent

	local humanoid = character:FindFirstChildOfClass\("Humanoid"\)

	if humanoid then

		humanoid\.Health = 0

	end

end

Invisivel\.Touched:Connect\(onTouch\)

- Aprendendo a mexer com ToolBox\.
	- Abra a toolbox\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780456965233200.png)

- Marketplace é onde você pode pesquisar coisas prontas para pôr no seu jogo\.
- Recent ficam guardados os tools que você pegou\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780456968241400.png)

- Basta pesquisar na barra de pesquisa e arrastar para sua tela\.
- Deixe agora os alunos se divertirem com os seus jogos e toolbox\.

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 
- O chão invisível é útil para quando você cair de um lugar ele vai estar flutuando para te matar\.

Tarefas

- Baixar GameMaker: [https://gamemaker\.io/pt\-BR/download](https://gamemaker.io/pt-BR/download) 

