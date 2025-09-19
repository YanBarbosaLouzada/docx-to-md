# __PLANO DE AULA__

Aula 20 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- React Timers e Animações\.

Objetivos

- Ensinar sobre React;
- Aprender a instalar bibliotecas;
- Configurar um *package\.json*\.

Estratégias e atividades

- Criar um App que consome API\.

1. Hoje vamos instalar e deixar o site bonito, isso é muito importante\. Para isto, vamos criar estes arquivos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602085535500.png)
2. Vamos exibir um aviso no canto da tela que diz o que está acontecendo, mas vamos começar com como ficará o site no final:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602087536300.png)
3. Começaremos pelos *animes card*\. Ele será o quadrado azul, onde contém as informações, repare que ele também usa outro componente chamado *GenreIcon* que é aqueles ‘cardzinhos’ pequenos azuis:  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602092534400.png)
4. O arquivo *GenreIcon* receberá o nome que precisa mostrar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602094534300.png)
5. Agora vamos estilizar o *GenreIcon*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602096535400.png)
6. Para estilizar o card é um pouco diferente:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602098537000.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602099536800.png)
7. E agora precisamos implementar o card criado no App\.js \(não esqueça de importar\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602100535900.png)
8. Vamos criar o popup, que é aquele aviso verde na imagem de cima\. O arquivo *popup\.js* é bem tranquilo e ele recebe como props uma mensagem e uma cor, ficando assim:  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602102822900.png)
9. E o CSS do popup terá cores dinâmicas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602103836100.png)  
O ‘success’ será chamado quando der certo a chamada API e o ‘warning’ quando não funcionar\.
10. Agora, como implementar no App\.js? Primeiro vamos criar uma função para mostrar e esconder o popup usando o *setTimeout* para poder esconder depois de um tempo, sempre que a API for finalizada o código do componente vai ser renderizado e mostrado na tela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602105824000.png)
11. Porém, agora como vamos chamar o popup na tela?  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602107822600.png)
12. E vualá\! Funcionando:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602108824000.png)
13. Para simular um erro, apague um pedaço da URL do *geturl api*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602113821200.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602115823400.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602116823500.png) 
14. Para finalizar, vamos subir o código no Github\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602117824200.png)	

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602119823000.png)

- Professor: por se tratar de uma API de animes, ela é como se fosse o Google\. Muito cuidado com o que o aluno for pesquisar\! Ele tem acesso a internet pois é uma aula de web 🙂
- Como funcionam os timers? Faça esse código com os alunos no navegador, a função *setTimeout* faz algo acontecer depois do tempo que é passado no segundo argumento:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130602121822000.png)

Tarefas

- Fazer um código usando o *setTimeout* para a próxima aula\. Não se esqueça de salvar no seu Github\.

