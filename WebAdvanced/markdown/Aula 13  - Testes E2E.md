# __ PLANO DE AULA__

Aula 28 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Validações

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Agora vamos fazer testes end to end, mas o que seria um teste end to end? Um teste end to end é o teste mais próximo do que o cliente irá usar, então teremos um bot que ao invés de testar nosso código testa a aplicação já pronta\.![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344531680200.png)
2. Para isto usaremos uma biblioteca chamada cypress, instalaremos ela no frontend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344533680500.png)
3. Agora que a lib já está instalada vamos entender o funcionamento da biblioteca:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344535682800.png)
4. Vamos agora abrir o cypress:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344538682500.png)
5. Vemos que agora irá abrir um navegador:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344540688300.png)
6. E nossa como isto é mágico certo? Agora nosso site irá rodar dentro de um navegador de testes\.Podendo inclusive escolher o navegador:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344553131400.png)
7. Esta é a tela inicial do projeto:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344557128000.png)
8. Vamos criar uma spec de testes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344562673500.png)
9. Chamaremos ela de login:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344562673500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344562673500.png)
10. Veremos que agora nosso código contém um enorme projeto dentro do nosso frontend:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344570308000.png)
11. Lá dentro contém nosso teste gerado pelo script:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344570308000.png)
12. Vamos rodar via cypress para entender o que irá acontecer ao rodar iremos para esta tela em um navegador chrome com todos os testes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344576655600.png)
13. Temos também uma tela de runs:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344576655600.png)
14. Se quisermos debugar também podemos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344576655600.png)
15. Ao clicarmos em specs no nosso primeiro teste ele irá carregar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344576655600.png)
16.  Agora nosso primeiro teste cypress está funcionando:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344576655600.png)
17. Mas porque ele está funcionando? Vamos analisar o código fornecido:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344589972800.png)
18. Veja entramos no site example\.cypress\.io vamos trocar para localhost:3000:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344589972800.png)
19. Automaticamente o navegador irá redirecionar ao nosso projeto:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344592652400.png)
20. Vamos agora pegar um texto que esteja na página inicial:
	1. Tela inicial:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344594659500.png)
	2. Teste:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344596666500.png)
	3. E veremos se passou:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344598673900.png)
21. Agora que o tutorial começou vamos tentar utilizar um teste de logar,primeiro adicionamos um data\-testid e em seguida dizemos ao cypress para entrar:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344600679600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344600679600.png)
22. E agora ao entrarmos no nosso navegador cypress veremos o teste funcionando:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344603522700.png)
23. E pronto agora iremos subir ao github

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344603522700.png)

  
  
  
  
  
  
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


