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

1. Explicar sobre Web e como Web é importante para o mundo, não apenas se resumindo a sites\.
2. Criar conta no site [Github](https://github.com/)\. Cada aluno terá um gmail, onde ele vai criar a conta\. É extremamente importante que o aluno tenha sempre acesso ao gmail, pois se ele perder a senha vai perder a conta do Github\.
3. Ativar a autenticação de 2 fatores do Github no [Extensão chrome](https://chromewebstore.google.com/detail/2fa-authenticator-app/gmohoglkppnemohbcgjakmgengkeaphi?hl=pt-br), desta forma sempre que o aluno estiver logado com o gmail dele poderá ver o número de autenticação\.
4. Após criar a conta no site, o professor explicará o que é Git e Github, e quais as vantagens de se criar um Github\.
5. Entendendo sobre Criptografia: nesta parte o aluno irá entender sobre criptografia, e porque é importante criptografar o código\.  


- __Criptografia:__
	- Chave pública: A chave pública tem como tarefa desembaralhar o código criptografado, pois ela sabe como traduzir o código para o original\.
	- Chave privada: A chave privada criptografa o código e faz com que o arquivo se “embaralhe”, fazendo com que apenas quem sabe a sequência possa traduzir\.

Exemplo de criptografia:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600207031200.png)

1. Criar o Config dentro de C:\\Users\\nomeDoUsuario\\\.ssh \(caso não tenha uma pasta chamada \.ssh, crie uma\.
	1. Como o Windows não permite mais criar um executável por questões de segurança, disponibilizamos o arquivo para configurar múltiplas chaves ssh neste [link](https://drive.google.com/drive/folders/10l1Bk1Hs9XEgI1t65k0Uwaf5G9108iZs?usp=share_link), nele existe um arquivo chamado __config__\.
	2. Como funciona este arquivo: é importante primeiro entender sobre como o Github funciona e interage com a ferramenta Git, baixada para iniciar a aula\. Entendendo a URL de um repositório:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600210034500.png)
	3. Agora, o importante é entender que a ideia central do Git é ter uma única chave ssh no computador, porém nós estamos usando o computador da escola, então para isto será criado um arquivo de configuração\. Esse arquivo que está no link acima, tem vários templates de chaves ssh:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600213032500.png)  
Se repararmos, nele existem algumas informações importantes\. A primeira é o host, se lembrarmos a URL do Github pede um host, então com isto podemos customizar os hosts dos alunos\.

  
O segundo argumento importante é o IdentityFile que mostra onde está salvo a chave ssh do aluno, contendo a pasta \.ssh/nomeDaChaveNãoPublica

1. Criar a chave ssh:
	1. Dentro da pasta \.ssh clique com o botão direito e vá em __Open Git Bash Here__:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600216034000.png)
	2. Clique nele e digite: 	  
Lembre\-se de alterar o gmail para o gmail do Github e o id\_rsa\_NomeDoAluno\. Caso o aluno vá fazer esse processo em casa, ele não precisará de ter também o arquivo de config, a única coisa que ele precisará fazer em casa é baixar o Git Bash e digitar:  
  
ssh\-keygen \-t ed25519 \-C "[your\_email@example\.com](mailto:your_email@example.com)"  
  
Após isto, será criada a chave ssh\. Dê enter várias vezes\. Se você reparar verá que foram criadas duas chaves: uma \.pub e uma sem extensão, a com \.pub você irá abrir em um bloco de notas:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600218031300.png)
	3. Reparando bem, você irá usar as duas chaves \(na escola\) e em casa o aluno só irá precisar da \.pub que vai estar no passo
	4. Agora, abra o arquivo de config e coloque o nome da chave, criando um host pro aluno parecido com este exemplo:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600222033500.png)  
São alteradas apenas duas partes: o nome do Host e o IndentityFile que é o caminho para o arquivo da chave\. Por isto o nome tem que ser igual\. Depois é só dar ctrl \+ S e ir para o último passo:
	5. Abra o arquivo com \.pub clicando no botão direito do mouse e abrindo com o bloco de notas, dê Ctrl \+ A e Ctrl \+ C para copiar e vamos até o Github para salvar a chave\. Clique no ícone do lado direito da tela e vá em settings:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600229055300.png)  
Após isso vá em SSH and GPC keys e adicione uma nova chave ssh:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600230054700.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600232054900.png)  
Agora que adicionamos a chave ssh, podemos ir para o código da aula, pois o Github já está configurado\.  
  


1. Crie uma pasta no computador e abra\-a no Visual Studio Code:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600234251500.png)  

2. Opções legais para ensinar aos alunos\. O *file*, na aba superior é onde você pode abrir os arquivos e ir até as pastas\. Existe uma opção chamada extensões, onde o aluno pode instalar as extensões visuais do Visual Studio Code\. Vou instalar a Fortnite no exemplo, porque gosto da cor roxa, mas o aluno pode procurar várias, exemplos de nomes:
	1. Dark
	2. Fortnite
	3. Naruto theme
	4. Panda Theme
	5. Dracula
	6. Monokai
3. Exemplo Fortnite:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600239252800.png)
4. Para garantir que o projeto seja sempre salvo, clique na opção __Auto Save__ do VS Code: File > Auto Save

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600248779100.png)  


1. Agora, vamos criar um arquivo chamado index\.html:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600250780400.png)
2. Este primeiro ícone irá criar um arquivo, chamaremos de index\.html\. Repare que se eu digitar __\!__ ele vai me dar um template para poder programar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600252782100.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600254780800.png)
3. Vamos entender como funciona o HTML:

HTML é uma linguagem de marcação, então ele não serve para poder “programar” sites, ele apenas mostra uma estrutura e nós seguimos essa estrutura\. Vamos começar com o início, todo site é dividido em duas partes, o __<head> </head>__ e o __<body> </body>__\. Dentro do __head __nós vamos colocar tudo que não é referente às informações que não fazem parte do corpo do site, como por exemplo, nomes, informações extras como links ou meta\-dados, Já dentro do __body__, nós colocamos o corpo do site, como as imagens, os botões entre todas as outras coisas que existem em um site\.

1. Tags: se você reparar, a maioria das palavras no html começam com < e terminam com > isso se chama marcação, toda palavra no html que for ser parte do nosso site vai ser desta maneira:  
<tag>Conteudo que não faz parte do html </tag> 
2. Vamos abrir o site no navegador, clique no index\.html com o botão direito e clique nesta opção: CopyPath![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600257779800.png)
3. Cole no navegador, que irá abrir uma tela em branco com o nome Document na parte superior:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600259781400.png)
4. Vamos começar alterando o nome do site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600262780000.png)  
Ao dar F5 e reiniciar o site verá que o título mudou:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600263781000.png)
5. Agora vamos às Tags que aprenderemos na aula de hoje:
	1. __<h1> </h1>__  
É o título maior do site\. A onde ele sempre terá o maior tamanho por padrão\.
	2. __<h2> </h2>__   
É o subtítulo\. A mudança entre ele e o título é o tamanho da letra\.
	3. __<hr/>__  
Linha de separação onde faz uma linha no site\.
	4. __<img src="\./nomeDaImagem\.png" alt="descrição">   
__Tag de imagem onde nós precisamos colocar onde ela está salva\. Ou seja, ‘\./’ representa que está salva na mesma pasta do projeto\. Ao final, é o nome do arquivo de imagem que queremos mostrar\.
6. Então este código:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600266779100.png)
7. Vira este site:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600269788900.png)
8. Vamos postar este site no Github\. Se você digitar na parte superior, na URL, __repo\.new__, onde se coloca os sites, você irá parar nesta tela:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600279778500.png)
9. As únicas coisas que são preciso fazer nesta tela são: o nome do repositório e clicar no botão de Create Repository, então irá aparecer esta tela:  


![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600281779000.png)

1. É importante saber que este site que estamos usando o Github\.com é como se fosse uma pasta online, onde podemos salvar o projeto que estamos utilizando\. Cada “salve” que damos no nosso código nós chamamos de commit\.
2. Abra o Git Bash Here na pasta onde está salvo o seu código:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600284781900.png)
3. Comandos do Git:
	1. git config \-\-global user\.email "[myndstutorial@gmail\.com](mailto:myndstutorial@gmail.com)": configura seu email para os commits![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600286781600.png)
	2. git config \-\-global user\.name "MyndsTutorial": configura o nome do usuário que vai aparecer no commit, é obrigatório ser o nome do Github:  ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600289794300.png)
	3. git config \-\-global push\.autoSetupRemote true: este comando__ desativa a opção de upstream facilita os__ __push__:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600291779200.png)
	4. git init: inicia uma pasta chamada \.git que serve para salvar seus arquivos\. Esta pasta é obrigatória para poder salvar o código:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600293078200.png)
	5. git status: ele mostra para você a situação atual do projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600294078900.png)  
Repare que ele diz que nós precisamos adicionar as modificações feitas no código\.
	6. git add \.: este comando significa que vamos adicionar todas as modificações:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600295078300.png)
	7. git commit \-m “salvando o site da primeira aula”: este comando serve para salvar o código e guardar uma mensagem com o salve:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600297078700.png)
	8. git push <link do repositório>: este código serve para enviar o link do repositório, porém é extremamente importante lembrar que quando estiver na escola você precisa configurar o host\. Para pegar o link do repositório você coloca em __ssh e copia__:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600298077500.png)  
Agora é só dar o comando e:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600300078500.png)  
Repare que mesmo eu dando “yes”, foi negado o acesso e isso é porque eu não coloquei o host que configurei lá atrás no ‘config’, então na escola é necessário:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600304859900.png)  
E repare que agora deu tudo certo, e temos agora um site online:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600307859700.png)  
Mas agora como funciona para pegar este site online e colocar no nosso computador de casa?
	9. Primeiro copiamos o link do repositório:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600310858300.png)
	10. E depois na nossa pasta nova, clonamos o projeto com o comando:  
__git clone <link\-do\-repositorio>__  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600313032800.png)  
Agora temos a nossa pasta clonada em outro computador\.

De lembrete mais importante sobre o Github, lembrem\-se:  


Chave ssh com \-nomeDoAluno só na escola\.  


Em casa não precisa ter o \-nomeDoAluno, porque o comando do tutorial já faz automaticamente a configuração\.

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
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130600316030300.png)

