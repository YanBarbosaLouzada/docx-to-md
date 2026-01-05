# __ 	 PLANO DE AULA__

Aula 01 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\): Node API

Conteúdos

- Criação de uma API com Node

Objetivos

- Criar Repositório
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Vamos começar criando uma pasta com o projeto do semestre, e dentro dela criar uma pasta chamada backend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969678726900.png)
2. Mas o  que é o backend? Ele nada mais é que o coração de um projeto, TUDO online precisa de um backend, a principal tarefa do backend é processar as informações e enviar para o frontend mostrar pro usuário, então se for para resumir, a tarefa do frontend é a tela de um projeto, é aonde você clica, tudo que o usuário pode interagir é o frontend, já o backend é quem cuida do trabalho sujo\. Sempre validando as informações, salvando os projetos, criando requisições etc\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969680727400.png)
3. Agora vamos começar a criar um pacote backend do nosso projeto , ele irá ser um servidor NodeJs que compila o código javascript e coloca em uma porta do computador\. Dentro da pasta backend digite npm init \-y:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969682728800.png)
4. Dentre ele irá criar um arquivo de configuração vazio chamado package\.json:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969684729000.png)
5. O nodejs utiliza um sistema chamado NPM que permite você ir até o site [https://www\.npmjs\.com/](https://www.npmjs.com/) para poder baixar as bibliotecas, vamos começar instalando as bibliotecas muito importantes para o desenvolvimento do projeto usando *npm install nome\-da\-lib1 nome\-da\-lib2 etc…*:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969685728600.png)
6. Se reparar agora ele irá criar uma pasta chamada node modules e um package\-lock\.json\. O package\-lock contém todas as informações das versões da biblioteca e o node\_modules são os arquivos salvos da biblioteca\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969687729400.png)
7. Vamos criar uma pasta chamada src com um arquivo javascript dentro e mostrar na tela uma mensagem:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969688728500.png)
8. Para rodar o projeto vamos digitar node caminho/ate/o/arquivo\.js:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969689728800.png)
9. Agora vamos criar um setup para ter dentro do código que se atualize sozinho para isto vamos instalar o nodemon digitando npm install nodemon:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969693276800.png)
10. Vamos criar um script chamado dev para olhar todas as configurações dentro de src:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969693276800.png)
11. Agora para rodar este script precisamos digitar npm run dev:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969703636700.png)
12. Vamos colocar o type no package\.json para setup do projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969703636700.png)
13. Este setup permite que nós usemos import e export igual funciona no react, facilitando entender os processos:  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969707598900.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969708607200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969708607200.png)
14. Agora que vimos que já está tudo okay, vamos começar a criar uma tela de apresentação da api criando um index\.html:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)
15. Para servir esta porta devemos criar um mini servidor:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)
16. Agora se formos até localhost:4444 veremos uma landing page da nossa api:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)
17. Mas o intuito do backend não é servir as páginas html, sim é possível, porém, vamos usar isto para criar uma api que busque os dados 
18. De desafio agora vocês devem incrementar o /public do projeto e hospedar uma página linda com html e css nele\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)
19. Agora para subir pro github vamos criar um gitignore para tirar os arquivos pesados inúteis ao projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)
20.  Agora crie um repositório no github e suba o projeto:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)

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
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634969710947800.png)

