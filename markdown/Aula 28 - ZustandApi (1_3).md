# __PLANO DE AULA	__

Aula 28 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- ZustandApi \(1/3\)

Objetivos

- Aprender sobre o Zustand e como ele funciona\.

Estratégias e atividades

- Instalar e entender o Zustand\.

1. Vamos adicionar uma nova biblioteca, chamada Zustand\. Então vamos começar instalando\-a:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602952934800.png)
2. O Zustand nada mais é que um Redux sem configurações, o que deixa ele um projeto maravilhoso\. Vamos começar criando um contador:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602954932000.png)  


Repare que ele tem um create que serve para criar a store, e duas funções que interagem com o estado, o próprio Zustand sabe o que é uma função e o que é um estado, podendo interagir entre si\.

1. O outro reducer que vamos fazer é um para a nossa carteira:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602956933700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602958931800.png)
2. Agora nós vamos criar um projeto que pegue o valor do real em tempo atual, e converta de acordo com o gasto que estamos fazendo\. Exemplo: se nós gastarmos 10 dólares ele converte pra 47\.89 reais pra salvar na carteira\. Mas a segurança do nosso login ainda não está muito legal, então vamos criar uma função para validar a senha:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602960936800.png)
3. Vamos adicionar a navbar a nova rota de carteira:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602962933200.png)
4. Vamos criar um CSS para o popup roxo também:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602964932400.png)
5. Vamos também colocar a nossa função de validação no loginPage:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602966935500.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602969932700.png)
6. Agora vamos criar a página de carteira:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602971950500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602973935200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602976934800.png)
7. E não podemos esquecer do CSS:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602978933900.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602980933000.png)
8. Lembre\-se de adicionar ao router o carteiraPage:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602982933200.png)
9. E prontinho, a nossa carteira já está com o corpo montado e o contador funcionando:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602984934200.png)
10. Para finalizar vamos subir o código no Github\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602986932700.png)

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602988933700.png)
- Professor: por se tratar de uma API de animes, ela é como se fosse o Google\. Muito cuidado com o que o aluno for pesquisar\! Ele tem acesso a internet pois é uma aula de web 🙂
- Contexto, por ser algo novo pode ser meio difícil, então caso tenha dúvidas indico este video:[ https://www\.youtube\.com/watch?v=OLtpJLQLOeM](https://www.youtube.com/watch?v=OLtpJLQLOeM) 

Tarefas

- Descobrir como os contextos podem ser úteis\. E de desafio tentar fazer o contexto começar vazio sem ser com o mockNotes\.
- Resposta:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602990934300.png)

