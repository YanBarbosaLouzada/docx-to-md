# __ PLANO DE AULA__

Aula 18 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Testes

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje vamos mergulhar um pouco mais a fundo em eventos de validação, checando se o usuário ao se registrar está obedecendo às seguintes regras:
	1. Nome precisa ter mais de 3 letras\.
	2. Email precisa ser válido 
	3. Idade precisa ser maior que 12
	4. Senha precisa ter mais de 6 letras, um número e um caractere especial\.
	5. Os campos de senhas são iguais\.
2. Para cada uma dessas validações erradas irá exibir um texto do input na tela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343651395800.png)
3. Vamos começar criando uma função de validate e um state para armazenar todos os erros\. Note que no email nós usamos um tipo de validação chamada regex que nada mais é que uma conta matemática para ajudar a manipular textos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343653396300.png)
4. Agora vamos mostrar na tela os erros nos respectivos lugares:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343655396400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343656400000.png)
5. Vamos agora adicionar nos erros data\-testid para coletar os erros:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343659099700.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343661154600.png)
6. Agora vamos precisar criar testes para validar se o usuário digitar coisas que o formulário não permite, esperar que o erro apareça\.
7. Correção do formulário com senha nova:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343664150500.png)
8. testando nome inválido:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343666149600.png)
9. Testando email:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343667155000.png)
10. Testando para idade inválida:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343669155100.png)
11. Testando para senha inválida:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343671150100.png)
12. E para finalizar as senhas quando não são iguais:  
 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343672150800.png)
13. Agora como desafio os alunos devem tentar verificar se quando digitam cada dado correto de uma vez se a mensagem não aparece\. Dica: podemos usar o \.not para descrever algo como, é esperado que o error confirm não esteja no documento:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343674150900.png)
14. Não esqueça de subir no github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343675150300.png):  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


