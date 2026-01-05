# __PLANO DE AULA__

Aula 23 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Contexto API e ícones React

Objetivos

- Aprender sobre contextos e como usar ícones no React\.

Estratégias e atividades

- Terminar um CRUD local que usa o contexto para salvar as anotações\.
- Instalar e entender o ReactIcons\.

1. Hoje vamos finalizar a página de anotações\. Mas para isso, vamos precisar alterar algumas coisas, porque o contexto agora precisa conversar constantemente entre o formulário e os cards, como mostra o exemplo abaixo:  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969100336400.png)

1. Vamos começar criando a função de editar e trazendo paro nosso contexto a anotação que o formulário vai criar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969102338000.png)
2. Agora vamos enviar para os componentes que estão utilizando o provider:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969103338000.png)
3. Agora o FormNote\.jsx vai utilizar as funções do contexto pra criar o note, repare que ele agora checa se está editando ou não para poder trocar o texto do botão:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969105336700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969106335600.png)
4. Vamos editar um pouco o CSS do AllNotes\.css:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969107337200.png)
5. Para poder deixar o projeto dos cards bonitos, vamos instalar uma biblioteca chamada react\-icons:  


__Professor:__ abra o link com os alunos e ensine\-os a escolher os ícones [React Icons](https://react-icons.github.io/react-icons/)   


Vamos primeiro instalar a lib no projeto \(o i é uma abreviação para install\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969109893300.png)

1. Agora, como usar a lib? No site desta, tem várias opções de ícones para utilizarmos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969111158400.png)
2. Eu escolhi o BsFillTrashFill\. Repare que ele começa com as letras “bs”, então a importação dele será no “react\-icons/bs” sempre é as duas primeiras letras do ícone, para mudar o tamanho dele você pode alterar o fontSize e a cor com o color\. Usando as funções meu novo card ficou assim:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969113156800.png)

1. Não esqueça do CSS:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969115158800.png)
2. Agora vejamos como ficou:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969117156700.png)
3. Se clicarmos na lixeira, some o card e se clicarmos no editar, repare que por estarmos usando o contexto o formulário irá reagir na hora:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969119158600.png)

 

1. Para finalizar, vamos subir o código no Github\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969121157100.png)

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador, como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969123158000.png)
- Professor: por se tratar de uma API de animes, ela é como se fosse o Google\. Muito cuidado com o que o aluno for pesquisar\! Ele tem acesso a internet pois é uma aula de web 🙂
- Contexto, por ser algo novo pode ser meio difícil, então caso tenha dúvidas indico este video: [https://www\.youtube\.com/watch?v=OLtpJLQLOeM](https://www.youtube.com/watch?v=OLtpJLQLOeM) 

Tarefas

- Descobrir como os contextos podem ser úteis\. E de desafio, tentar fazer o contexto começar vazio sem ser com o mockNotes,
- Resposta:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969125158200.png)

