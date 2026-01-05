# __ PLANO DE AULA__

Aula 20 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Testes

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Vamos agora aprender a imitar uma resposta da api, para criação e manipulação de dados, instalaremos a lib responsável por isto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343834670700.png)
2. __npm i jest\-preview msw@1__
3. Agora que instalamos essas 2 libs, vamos entender o que elas fazem:
	1. MSW funciona como um mock de um servidor ele simula requisições que usamos nos testes\.
	2. jest\-preview cria uma tela de teste para que possamos visualizar e debugar os testes em um outro servidor
4. Vamos abrir os 4 terminais do projeto:
	1. Frontend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343836675400.png)
	2. backend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343837676000.png)
	3. frontend testes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343838675900.png)
	4. Vamos configurar agora o do jest\-preview:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343839675700.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343840677100.png)
5. Agora vamos mudar um pouco o pokemonList:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343842475900.png) 		  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343844533300.png)
6. Agora vamos criar 2 variáveis para “mockar” os dados que o axios irá retornar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343845533200.png)
7. Para poder pegar os dados de cima é preciso abrir o navegador e entrar na url:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343847533700.png)
8. Agora 	vamos entrar no pokemon 1 para pegar os dados e mockar o primeiro pokemon escolhido:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343848533300.png)
9. Vamos salvar ela em uma variável para ser usada no teste:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343852048800.png)
10. Agora vamos entender o novo modelo de testes:  
começaremos criando o servidor e montando as apis falsas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343855048200.png)
11. Agora vamos criar o teste e aprender a usar o jest\.preview\(\), repare que o projeto no localhost:3336 irá ter a tela de loading:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343857051100.png)
12. E o motivo disto é que o teste contém um jest\.preview\(\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343859049400.png)
13. Agora vamos entender o que este preview\.debug\(\) faz, com isto podemos tirar “prints” da tela no momento que tem o teste, por isso vamos validar se o axios irá mostrar os itens corretos na tela adicionando um segundo preview\.debug\(\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343860048700.png)
14. E agora no preview do projeto mostrará os itens na tela:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343862121000.png)
15. Agora vamos criar um teste para procurar os dados do bulbasaur nos testes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343862121000.png) 
16.  Agora vamos criar o teste para verificar os dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343864127200.png)
17. Para testar o modal precisamos colocar os test id no modal:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343866134800.png)
18. E também nas vizualizações:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343868142000.png)
19. Agora como teste tente colocar mais testes para validar os dados do modal, e para finalizar, vamos subir no github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343868142000.png)  
  
  
  
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


