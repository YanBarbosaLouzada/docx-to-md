# __ PLANO DE AULA__

Aula 03 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\): Node api

Conteúdos

- Banco de dados

Objetivos

- Criar Repositório
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Vamos começar agora a utilizar bancos de dados no projeto\. O banco de dados nada mais é que um lugar seguro onde guardamos as informações que estamos usando no projeto, e registros que são importantes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970101042000.png)
2. O uso de banco de dados se deve por causa que as linguagens de programação não foram criadas com intuito de guardar as informações apenas manipulá\- las para fins específicos\.
3. Vamos começar a criar um banco de dados, que é onde as informações do carrinho ficarão salvas\. Para isto vamos ao site do [mongodb](https://account.mongodb.com/account/login):
	1. Sempre logue pelo Gmail, é o método mais tranquilo\. Após isso, vamos criar um banco de dados __gratuito__:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970103044300.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970105046700.png)
4. Caso já tenha criado um banco anteriormente, pode criar um novo projeto também:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970106044700.png)
5. Vamos criar um usuário:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970108045200.png)
6. E habilitar a internet:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970109854100.png)
7. Agora é só clicar em __conectar__ e ir pegar o código do __driver nodejs__:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970111901700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970113901400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970115902000.png)
8. Agora que já configuramos tudo vamos começar a fazer o código da conexão com o banco de dados\. Primeiro vamos instalar a lib do mongoose e de segurança:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970117901100.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970118902600.png)
9. Agora vamos criar uma variável de ambiente\. Variáveis de ambiente são informações secretas que não queremos compartilhar com o github, com isto vamos criar um arquivo chamado \.env e um chamado exemplo\.env, onde um será o oficial que colocaremos no gitignore para não enviar e outro será o exemplo que iremos enviar:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970119902400.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970120902000.png)
10.  Agora vamos copiar a url que o mongodb dá para dentro da pasta\. Esta url será apagada então vocês precisam pegar a url de vocês\. Lembre\-se de depois do \.net/ colocar a palavra aulas para ter um banco das aulas:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970121902700.png)
11. Vamos criar um arquivo de configuração:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970123902100.png)
12. Agora vamos permitir que o nosso servidor use:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970124902600.png)
13. E o nosso terminal estará assim:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970126904400.png)
14. Agora vamos criar os módulos\.Nós vamos criar uma loja então vamos começar criando coisas simples como um produto, cada produto irá ter um nome, uma quantidade, um preço, e uma descrição:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970126904400.png)
15. Para nós criarmos as funções de crud iremos criar um novo controller e uma nova rota: ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)
16. Não esqueça de importar as rotas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)
17. Agora para finalizar vamos testar o projeto no insomnia: 
	1. Create product  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)
	2. Edit Product: ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)
	3. Get products:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)
	4. Delete product:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)
18. Agora que o crud já está funcionando, já está tudo bem e funcionando, devemos subir o código ao github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970129003400.png)

  
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


