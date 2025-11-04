# __PLANO DE AULA__

Aula 22 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Contexto API\.

Objetivos

- Aprender sobre contextos\.

Estratégias e atividades

- Criar um CRUD local que usa o contexto para salvar as anotações\.

1. Hoje vamos aprender como criar um contexto\. O contexto nada mais é que um jeito diferente de salvar os estados\. Para ele funcionar, nós precisamos entender sobre como funcionam os Contextos\. Eles são camadas de código que podem armazenar os estados, fazendo com que todos os componentes dentro dele não precisem ficar passando os dados como props, podem pegar direto do contexto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602345569800.png)

1. Agora, vamos entender o que será feito\. Nós vamos criar um contexto para a nossa página de anotações\. Ele será responsável por interagir tanto o formulário quanto os cards:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602346574200.png)  
 
2. Primeiro de tudo, vamos criar funções em JavaScript que vão nos ajudar como *helpers*:
	1. A primeira é para criar as datas no formato do Brasil, então é só chamar a função, e temos o horário de Brasília\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602348572700.png)
	2. E para finalizar, vamos criar uma função para gerar um ID aleatório:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602349574800.png)
3. Agora, o contexto lembra muito um componente em React, porém a diferença é  que ele permite outros componentes acessarem o estado e funções para manipular os estados, com isto nós vamos criar uma função para adicionar uma anotação e outra para deletar, e por fim vamos adicionar o contexto e o provider:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602351572500.png)
4. Repare que além de usarmos as funções *helpers* também tem um *mockNotes*, que é para nós podermos validar os testes, não esqueça de importar e exportar os dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602354783800.png)
5. Vamos agora, criar a página das anotações:
	1. Adicione uma rota para o Componente da página lá no *router\.js*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602357783500.png)
	2. Crie uma página e lembre\-se de adicionar o *Provider* para poder compartilhar os dados entre os componentes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602359783400.png)
	3. NotesPage\.css:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602361781700.png)
	4. Vamos criar o* FormNote*, começando criando uma anotação dentro do formulário, e pegando a função de adicionar lá do nosso contexto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602362783500.png)

O código do retorno é um formulário que interage com o *noteCreated*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602364783200.png)

- 
	1. Vamos deixá\-lo mais bonitinho, editando o CSS:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602366785500.png)
	2. E ficou assim:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602368783900.png)

1. Agora, vamos criar a parte de mostrar as anotações:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602369786200.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602371783200.png)
	1. Vamos criar cada anotação separada:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602373783600.png)
	2. E agora, criamos anotações, porém faltou algo, não é mesmo? Cadê nosso link lá na navbar?![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602375783300.png)
	3. Agora, vamos criar o link na navbar:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602377782300.png) ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602379784200.png)
2. Para finalizar, vamos subir o código no Github\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602382934700.png)	

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602384949800.png)

- Professor: por se tratar de uma API de animes, ela é como se fosse o Google\. Muito cuidado com o que o aluno for pesquisar\! Ele tem acesso a internet pois é uma aula de web 🙂
- Contexto, por ser algo novo pode ser meio difícil, então caso tenha dúvidas indico este video: [https://www\.youtube\.com/watch?v=OLtpJLQLOeM](https://www.youtube.com/watch?v=OLtpJLQLOeM) 

Tarefas

- Descobrir como os contextos podem ser úteis\.
- Desafio: tentar fazer o contexto começar vazio sem ser com o mockNotes\.
- Resposta:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602387937200.png)

