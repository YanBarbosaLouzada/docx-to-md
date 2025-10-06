# __PLANO DE AULA__

Aula 21 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Roblox

Conteúdos 

- Elevador/Plataforma Flutuante\.

Objetivos

- Gerar terrenos e entender ferramentas\.

Estratégias e atividades

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

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1759780456688224900.png)

Recursos

- Computador, internet e Roblox Studio\.

Observação

- Link para download do Roblox Studio: [https://create\.roblox\.com/](https://create.roblox.com/) 

Tarefas

- Desafio para a sala de aula, descobrir como aumentar a distância que a plataforma vai para frente e arrumar na próxima aula\.

