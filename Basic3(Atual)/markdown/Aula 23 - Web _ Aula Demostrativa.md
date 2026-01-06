# __PLANO DE AULA__

Aula 20  | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

__Tipo da atividade:__ Online  
__Ferramenta\(s\):__ VS Code, HTML, CSS

__Recursos:__ Navegador\.

__Conteúdo:__ 

Nesta aula, o aluno aprenderá:

- Instalar o Visual Studio Code\.  

- Instalar extensões essenciais \(Live Server, Prettier, Color Highlight, HTML CSS Support\)\.  

- Criar o primeiro projeto web\.  

- Estruturar um arquivo HTML\.  

- Aplicar estilos usando CSS\.  

- Criar uma página simples com __um card__ e __background bege__\.  


## <a id="_heading=h.ge5tdkf6cc3w"></a>__🖥️ Instalação do Visual Studio Code__

1. Acesse o site oficial:[ https://code\.visualstudio\.com/  
](https://code.visualstudio.com/)
2. Clique em __Download__\.  

3. Instale o programa mantendo as opções sugeridas\.  

4. Recomenda\-se marcar:  

	- "Adicionar ao PATH"  

	- "Abrir com Code"  


## <a id="_heading=h.luu2dbi5w8if"></a>__🔌 Extensões Essenciais __

Abra o VS Code → Ícone de Extensões__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775392331600.png)__ → Pesquise e instale:

- __Live Server__ – Atualiza a página automaticamente\.  

- __Prettier__ – Formata o código\.  

- __Color Highlight__ – Mostra cores no CSS\.  

- __HTML CSS Support__ – Autocomplete HTML/CSS\.  


## <a id="_heading=h.p529ia3nsxgf"></a>__📁 Criando o Projeto__

1. Crie a pasta __meu\-site__\.  

2. Crie os arquivos:  

	- index\.html  

	- style\.css  

3. Abra no VS Code\.  


## <a id="_heading=h.itbnmreriumb"></a>__🌐 Estrutura HTML__

- <\!DOCTYPE html>
- <html lang="pt\-BR">
- <head>
-     <meta charset="UTF\-8">
-     <meta name="viewport" content="width=device\-width, initial\-scale=1\.0">
-     <title>Meu Primeiro Site</title>
-     <link rel="stylesheet" href="style\.css">
- </head>
- <body>
-     <div class="card">
-         <h1>Bem\-vindo\!</h1>
-         <p>Este é o meu primeiro card estilizado\.</p>
-     </div>
- </body>
- </html>

## <a id="_heading=h.jjhy53joep4q"></a>__🎨 Estilizando com CSS__

- body \{
-     background\-color: \#f5f1e6;
-     font\-family: Arial, Helvetica, sans\-serif;
-     margin: 0;
-     padding: 0;
-     display: flex;
-     justify\-content: center;
-     align\-items: center;
-     height: 100vh;
- \}
- \.card \{
-     background: white;
-     padding: 20px;
-     border\-radius: 12px;
-     box\-shadow: 0 4px 10px rgba\(0, 0, 0, 0\.1\);
-     text\-align: center;
-     max\-width: 300px;
- \}

## <a id="_heading=h.5vxiy29xn9yr"></a>__▶️ Executando com Live Server__

1. Clique com o botão direito no arquivo __index\.html__\.  

2. Selecione __Open with Live Server__\.  

3. O navegador abrirá automaticamente\.  


## <a id="_heading=h.dyg4m8qxv2kt"></a>__⭐ Atividade Final__

Personalize seu card:

- Altere a cor do fundo\.  

- Adicione uma imagem\.  

- Modifique a fonte\.  


