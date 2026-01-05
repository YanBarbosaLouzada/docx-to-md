# __ PLANO DE AULA__

Aula 21 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  

1\. Faker\.js

1. O que é?
	1. Biblioteca para gerar dados falsos \(como nomes, URLs, números aleatórios, etc\.\)\.
	2. Útil para criar mocks dinâmicos e variados\.
2. Como usar no seu código?
	1. Você usa o Faker para

Conteúdos

- Testes

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Vamos começar agora a usar novos modelos de mocks, vamos agora começar a utilizar uma nova lib chamada faker\. Ela é responsável por criar itens falsos para podermos executar![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343910018600.png)
2. __npm install @faker\-js/faker \-\-save\-dev__
3. Se formos ao github \([https://github\.com/faker\-js/faker](https://github.com/faker-js/faker)\) do faker veremos exemplos de usos, lembrando que criaremos “factories” que nada mais é que são dados falsos criados para usarmos no projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343910018600.png)
4. Agora que entendemos que  o faker é um tipo diferente de dados, vamos utilizar do faker para criar “mocks” com os novos formatos, o primeiro será o do pokémon que iremos visualizar:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343926689800.png)
5. Entendendo que a tarefa do faker é colocar dados falsos precisamos então ter estes dados no nosso projeto, isto é usado tanto para popular bancos de dados quanto para validar testes do projeto, vamos precisar passar na lista de pokémons o nosso modelo de pokémons para poder ter uma comparação, validando o dado, com isto vamos poder passar para a função factory que 	criará os dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343928688600.png)
6. Agora vamos dar uma editada para validar os dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343929688700.png)
7. Indo nos arquivos agora podemos criar variáveis com as informações que mostram no projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343931704600.png)
8. Nós podemos agora mockar na resposta da api estes dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343932687700.png)
9. Alterando o primeiro teste,repare que agora nós pegamos a quantidade de pokémons baseada no dado mockado, usando o pokemon\.results\.length:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343934687800.png)
10. Melhorando o segundo teste, para pegarmos todos os valores gerados pelo projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343936688300.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343938686300.png)
11. Como desafio  e tarefa tentar criar factories para criar um teste do Anime List, na próxima aula o professor irá mostrar a resposta de como criar factories e mockar os dados, lembrando que este é a estrutura que o animes responde:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343940688300.png)
12. Para finalizar subir ao github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343942497800.png)  
  
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


