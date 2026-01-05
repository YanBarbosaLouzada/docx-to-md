# __ PLANO DE AULA__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Github e HTML\.

Objetivos

- Criar Conta Github;
- Entender como a Web funciona, o que é a Web e quais as vantagens de usar o Github\. Se ambientar com o Github\.

Estratégias e atividades

1. Agora vamos começar com um projeto usando 2 frameworks um para backend e outro para o frontend, mas o que um framework faz?  Ele é como se fosse um conjunto de padrões que nos permitem desenvolver de uma maneira muito rápida\. Vamos agora instalar nosso primeiro framework o Nestjs\.
2. Para isto vamos instalar o nestjs no terminal com o comando igual está na documentação oficial ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344776048200.png)
3. Agora vamos criar o nosso nestjs na pasta do nosso projeto vamos criar um projeto chamado backend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344776048200.png)
4. Após isso repare que irá criar toda uma estrutura no projeto![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png)
5. No git bash \(aonde colocamos os commits para subir ao github\) vamos digitar um comando pra remover a pasta \.git que é criada junto com o projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png)
6. Agora vamos instalar um super compilador pro nosso projeto recarregar bem rápido:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png)
7. Na documentação tem um exemplo do que precisa alterar no arquivo nest\-cli\.json:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png)
8. O  nosso nest\-cli irá ficar assim:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png)
9. Tente agora alterar um arquivo no app\.service\.ts e veja a velocidade de recarregar os dados\.
10. Vamos instalar o prisma e inicializar ele, rode este comando dentro de backend:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png)
11. Crie um esquema do prisma para poder ter um exemplo do usuário![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344782313700.png) 
12. Crie agora um \.env dentro da pasta backend e coloque essas configurações:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344791489400.png)
13. Agora é só rodar o comando pro banco de dados carregar:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344792718800.png)
14. Como o banco de dados é um sqlite instale esta extensão no vscode![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344794727100.png)
15. Depois disto nós podemos ir diretamente no banco de dados e visualizar os dados dos usuários:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344794727100.png)
16. Agora vamos instalar as bibliotecas que vamos usar para criptografar as senhas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344797455400.png)
17. Vamos usar os dados do nestjs para poder usar o framework para ele criar os nossos dados, dentro da pasta backend rode estes comandos:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344797455400.png)
18. Repare que foram criados estes tipos de arquivos:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344801175700.png)
19. Na  documentação existe um template de código para conectar o prisma:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344801175700.png)
20. E com uns ajustes o backend prisma\.service:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344805436900.png)
21. Vamos agora criar a receita dos módulos do usuário:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344807930200.png)
22. Agora o controller do user:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)
23. Agora o serviço para fazer as consultas no banco de dados\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)
24. Pronto agora é apenas mandar as requests no localhost:PORTA\_ESCOLHIDA\. E para rodar a porta é só entrar no main\.ts e colocar dentro do listen:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)
25. Criar o gitignore e agora subir o código ao github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)

Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias a ferramenta Git\.
- Na hora de explicar pros alunos sobre criptografia, vale a pena mostrar um pedaço deste vídeo \(em torno de 4 minutos\) sobre criptografia do cellbit:  
[CICADA 3301 \- PARTE 1 \- CELLBIT](https://www.youtube.com/watch?v=Ep5qn8pLCMA)
- Links Extras de estudo sobre o Github:  
[O QUE É GIT E GITHUB? \- definição e conceitos importantes 1/2](https://youtu.be/DqTITcMq68k?si=0gEyQuywjrcMM4jI)  
[COMO USAR GIT E GITHUB NA PRÁTICA\! \- desde o primeiro commit até o pull request\! 2/2](https://youtu.be/UBAX-13g8OM?si=9LqJceHGIfj-osHz)

Tarefas

- Instalar o Visual Studio Code em casa e tentar montar um site simples com o código parecido:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344809312500.png)

