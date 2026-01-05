# __ PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React

Conteúdos

- Login api

Objetivos

- Criar Repositório
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Vamos  começar instalando a biblioteca de criptografia e o de tokens:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970527438400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970527438400.png)
2. Criar um módulo de usuário:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970544025100.png)
3. Vamos criar agora os controllers, de registrar o usuário e de logar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970546023700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970548023600.png)  

4. Vamos agora criar um controller token que irá funcionar como um middleware do projeto\. A ideia do middleware é criar validações e permissões de acesso a nossa api:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970550021500.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970552022700.png)
5. Para utilizar este token é necessário colocar ele como um middleware nas rotas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970554022000.png)
6. Agora vamos criar as rotas de login e registro do app:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970556022900.png)
7. E não podemos esquecer de importar as rotas:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970557039900.png)
8. Repare que nós colocamos o middleware em quase todas as rotas dos produtos menos a rota do get ou seja, se formos no insomnia e tentarmos acessar os dados![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970559022400.png)
9. Entretanto o get ainda tem permissão:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970560887700.png)
10. Agora vamos nos registrar no app:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970561887800.png)
11. Repare que a senha ficou encriptografada graças ao bcrypt, agora o login tentará ver se a senha bate os hashs e se for aprovado irá colocar o jwt:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970563888700.png)
12. Agora que o jwt já está funcionando, como usamos esse token misterioso? vamos precisar colocar ele nos headers da requisição para isso vamos no criar do projeto:  
	
13. Porque isto é importante? O maior motivo é que apenas o cliente do nosso projeto terá permissão de enviar e se comunicar com a api\. Fazendo com que seja mais seguro se conectar com nosso projeto\.  

14. Para finalizar vamos subir ao github o projeto:  
  
 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634970564886900.png)

Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.
- Na hora de explicar pros alunos sobre criptografia, vale a pena mostrar um pedaço deste vídeo \(em torno de 4 minutos\) sobre criptografia do cellbit:  
[CICADA 3301 \- PARTE 1 \- CELLBIT](https://www.youtube.com/watch?v=Ep5qn8pLCMA)
- Links Extras de estudo sobre o Github:  
[O QUE É GIT E GITHUB? \- definição e conceitos importantes 1/2](https://youtu.be/DqTITcMq68k?si=0gEyQuywjrcMM4jI)  
[COMO USAR GIT E GITHUB NA PRÁTICA\! \- desde o primeiro commit até o pull request\! 2/2](https://youtu.be/UBAX-13g8OM?si=9LqJceHGIfj-osHz)

Tarefas

- sem tarefa  


