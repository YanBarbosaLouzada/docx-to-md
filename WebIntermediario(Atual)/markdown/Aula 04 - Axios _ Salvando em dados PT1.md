# __PLANO DE AULA__

Aula 19 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Axios e seu formato para salvar em dados\.

Objetivos

- Ensinar sobre React;
- Aprender a instalar bibliotecas;
- Configurar um *package\.json*\.

Estratégias e atividades

- Criar um App que consome API\.

1. Hoje vamos instalar uma biblioteca no nosso projeto, então, no VS Code, clique em *terminal* e vá em *new terminal*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968120946100.png)
2. Para instalar a biblioteca temos que digitar: *npm install nomeDaLib*\.  
A que vamos utilizar se chama *axios*, então vamos instalar e depois ir no *package\.json* para ver se o projeto instalou corretamente:  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968123949800.png)
3. Vamos criar um dado mockado que, na verdade, significa uma simulação de algo que vamos pegar na API, então a primeira coisa a fazer agora é baixar o arquivo que o professor deixou separado e por em um arquivo:  
[Mock anime](https://drive.google.com/file/d/1JofN8tT4jps6YRMr95Qo1YB5W0EAfJxb/view?usp=drive_link)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968126589800.png)

1. Renomeie o App\.js para *appExemplo*, porque agora vamos de fato criar o App\.js do nosso projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968128667000.png)
2. Vamos começar usando o dado mockado, o nosso projeto tem um *input* e um *botão*, então quando digitarmos queremos salvar o que foi digitado em um input e o quando clicarmos no botão enviar para a API de animes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968130667700.png)
3. Para simular a chamada da API, vamos usar o dado mockado para exibir os animes\. O input enquanto muda chama a função do *handleInputChange* e o botão chama o “buscar anime”\. Após isso, criamos uma pergunta, se é um array que está vindo da API, caso esteja vamos mapear e exibir o título do anime:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968132667600.png)

1. Agora que já fizemos o App mostrar os títulos, vamos criar uma função que usa a biblioteca *axios* para procurar os dados da API\. Esta função retorna 3 coisas, se está carregando os dados, se deu algum erro, e obviamente os dados dos animes:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968134667000.png)

1. Agora vamos usar isto no App\.js:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968136666400.png)
2. Para finalizar, vamos subir o código no Github\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968138666800.png)	

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634968140667800.png)
- Professor: por se tratar de uma API de animes, ela é como se fosse o Google\. Muito cuidado com o que o aluno for pesquisar\! Ele tem acesso a internet pois é uma aula de web 🙂

Tarefas

- Tentar editar o CSS dos textos em casa\. Não se esqueça de subir o arquivo com as modificações para o Github\.

