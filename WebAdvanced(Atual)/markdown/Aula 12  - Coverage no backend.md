# __ PLANO DE AULA__

Aula 27 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Validações

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Agora vamos fazer a validação do coverage, para isto vamos criar um script no package e analizar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344405701700.png)
2. Ao rodar este código veremos o seguinte:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344408980900.png)
3. Vamos começar pelo productController\.test\.js as 3 linhas que ele diz que não foram testados são estas 3 validações:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344410989300.png)
4. Para criar os testes disto vamos consertar agora criando testes para estes campos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344412988600.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344414989000.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344417000700.png)	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344419001200.png)
5. E agora ao rodar o coverage novamente:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344420989300.png)
6. Vamos agora criar testes para o pokemonController, para a próxima aula voltarmos ao código e comentar o que não estamos usando:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344421988600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344424032300.png)
7. Para finalizar vamos melhorar o connection to database:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344426868500.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344428868700.png)
8. E agora nosso coverage está com 100%:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344430868600.png)
9. Antes de subir ao github coloque os dados do coverage para serem ignorados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344431867400.png)
10. Agora vá em configurações ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344433867700.png)
11. Depois procure actions e vá até secrets and variables do actions:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344434868500.png) 
12. Crie tanto em secret quanto em variable seu dbUrl para configurar o setup do mongo![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344436879600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344437877600.png)
13. Agora vamos também colocar o “config” do dotenv tanto em connection quanto no teste:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344438868400.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344440868600.png)
14. Agora o que falta é nós setarmos no jest\.config um limite que chamamos de coverageThreshold : ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344441868300.png)
15. Para o ci precisamos dizer que existirá uma variável de ambiente:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344442869500.png)
16. E para o backend mudaremos o processo, iremos criar um arquivo \.env e manter o projeto funcional, agora temos testes unitários tanto no frontend quanto no backend, com um adicional de coverage no backend:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344444928100.png)
17. Vamos agora sempre que rodarmos o coverage ,o nosso CI\-CD nos avisará se o coverage de um dos 4 itens cair para abaixo de 100 ou 80%,usarei 100% para verem que começa a alertar quando os códigos estão errados:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344446937500.png)
18. Analisando o ci cd veremos que ambos passaram com 100% de segurança em nosso backend:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344446937500.png)
19. Não esqueça de subir ao github:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344448945400.png)

  
  
  
  
  
  
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


