# __PLANO DE AULA__

Aula 20 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Ponte Ativável\.

Objetivos

- Criar Ponte Ativável;
- Programação\.

Estratégias e atividades

Criando uma ponte\.

- 
	- Crie duas parts, e mude o nome para gatilho e plataforma;
	- Crie um grupo para duas partes gatilho e plataforman\(basta selecionar as duas e clicar em groups\), renomeie este grupo \(model\) para ponte\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261954022465700.png)

No script, digite:

\-\- Imprime uma mensagem para configurar a ponte

print\("Configurando a Ponte"\)

\-\- Define o objeto como o objeto atual \(onde o script está\)

local objeto = script\.Parent

\-\- Obtém a plataforma e o gatilho dentro do objeto

local plataforma = objeto\.Plataforma

local gatilho = objeto\.Gatilho

\-\- Define a plataforma para ser quase invisível e impossível de colidir no início

plataforma\.Transparency = 0\.9  \-\- Quase invisível

plataforma\.CanCollide = false  \-\- Não pode ser tocada ou colidida

\-\- Esta função desativa a ponte

local function desativaPonte\(\)

	plataforma\.Transparency = 0\.9  \-\- Torna a plataforma quase invisível novamente

	plataforma\.CanCollide = false  \-\- Impede que os jogadores colidam com ela

end

\-\- Esta função ativa a ponte

local function ativaPonte\(\)

	print\("Ativando Ponte\!"\)  \-\- Imprime uma mensagem dizendo que a ponte está sendo ativada

	plataforma\.Transparency = 0  \-\- Torna a plataforma visível

	plataforma\.CanCollide = true  \-\- Permite que os jogadores colidam com ela

	wait\(3\)  \-\- Espera por 3 segundos

	desativaPonte\(\)  \-\- Chama a função para desativar a ponte novamente após 3 segundos

end

\-\- Esta função é chamada quando algo toca no gatilho

local function blindao\(colisao\)

	local humano = colisao\.Parent:FindFirstChild\("Humanoid"\)  \-\- Verifica se um jogador tocou no gatilho

	if humano then

		ativaPonte\(\)  \-\- Se um jogador tocar no gatilho, a ponte é ativada

	end

end

\-\- Conecta a função "blindao" ao evento "Touched" do gatilho

gatilho\.Touched:connect\(blindao\)

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio   
[https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Pesquisar estilos de jogos Obby e dizer qual é o mais famoso desse estilo hoje em dia\. Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com)\.

