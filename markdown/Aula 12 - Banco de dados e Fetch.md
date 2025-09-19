# __PLANO DE AULA__

Aula 12 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Banco de dados e fetch\.

Objetivos

- Ensinar os alunos sobre como o mundo real funciona;
- Criar um banco de dados no *firebase* e fazer a conexão\.

Estratégias e atividades

- Continuar o site da semana passada, criando agora uma tabela para ver as pessoas\.
- O que é um banco de dados\.
- Aprender sobre requisições\.

1. Hoje vamos finalmente salvar nossos usuários em algum lugar\. Para isso é importante entender como vai funcionar o projeto das próximas aulas\. O nosso site vai ser um site que irá enviar requisições para o banco de dados fazendo com que ele consiga informações salvas:  
  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911544757300.png)

1. Mas por que isto é importante? Sempre que nós damos f5 no site, ele recarrega as variáveis e com isto nós podemos entender que, para pegar as informações salvas em algum lugar, este lugar se chama __banco de dados__\. Existem 2 tipos de banco de dados os relacionais e os não relacionais:

  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911544757300.png)

1. Ambos são importantes\. Para que o nosso projeto funcione, vamos utilizar um banco não relacional chamado *firebase*\. Logue no site [https://firebase\.google\.com/?hl=pt\-br](https://firebase.google.com/?hl=pt-br) com o seu Gmail\. Vamos criar um projeto:
	1. Clique para ir para o console:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911547616200.png)
	2. Crie um projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911547616200.png)
	3. Dê o nome do projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911547616200.png)
	4. Pode desativar o Google Analytics:  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911547616200.png)

- 
	1. Vamos criar um *RealtimeDatabase*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911547616200.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911547616200.png)
	2. Escolha a região mais perto, no meu caso é os EUA, ou seja, nosso banco de dados ficará nos Estados Unidos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911561287200.png)
	3. Vamos criar as configurações de segurança:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png)
	4. Vualá\! Temos nosso banco de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png)
	5. Vá nas regras de uso e faça com que permita *visualizar e editar o banco de dados*, coloque ambos como *true* e clique em publicar \(pode ignorar os avisos de falta de segurança, estamos estudando, não publicando o site da NASA\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png) 
	6. Agora, o nosso banco de dados virou uma URL:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png)
	7. Vamos criar a estrutura HTML do nosso site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png)

1. Nosso site servirá para podermos cadastrar pessoas no banco de dados\. Este é o CSS do nosso site\. Lembre\-se que os alunos podem editar e customizar o CSS da maneira que achar melhor usando as ferramentas aprendidas e o Bootstrap:  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png)

1. Vamos criar uma variável com a constante salvando a URL do nosso banco de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911563294400.png)
2. Com isto, nós vamos entender um novo conceito das funções chamado *assincronismo*\. Nada mais é que criar um “espere” dentro da função fazendo com que o nosso código espere até algo ser executado antes de passar pra próxima linha:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911576755700.png)
3. No código para criar este *“delay”*, usamos a palavra *await*, e ela só pode ser usada em funções que tem a palavra *async* no começo\. Vamos usar o *fetch* para pegar os dados da URL e depois esperar serem convertidos para JSON:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911577981800.png)
4. Vamos formatar os objetos que vem do banco e transformá\-los em um *array de objetos*, para poder colocar na tela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911579988700.png)
5. E para finalizar, precisamos chamar esta função no final do get para poder pegar os dados sempre que o site for criado:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911581996500.png)
6. Agora que já vinculamos o nosso próprio site ao banco de dados, só nos resta aguardar para na próxima aula criarmos o post e cadastrarmos as pessoas\.
7. Para finalizar vamos subir o código no Github\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911584003300.png)	

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911586011800.png)

- Assistir o vídeo do Dev Soltinho sobre *promises* antes da aula pode facilitar entender como elas funcionam:  
[Como usar Async/Await? Promises no JavaScript? Você NUNCA MAIS VAI ERRAR](https://www.youtube.com/watch?v=q28lfkBd9F4)

Tarefas

- Pesquisar diferentes nomes de banco de dados e os mais usados no mundo\. Montar uma apresentação e enviar para o email [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com) ou para seu professor via Discord\.

