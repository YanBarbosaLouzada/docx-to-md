# __ PLANO DE AULA__

Aula 22 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Testes

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Antes de entrarmos no código de testes dos animes\. Muitas vezes nós temos receio e não entendemos o que vamos testar, existe duas maneiras mais conhecidas sobre testes:
	1. Caminho Primário e Caminho Secundário\.
	2. Coverage\.
2. O Caminho Primário nada mais é do que criar testes de situações de tudo que o usuário vai utilizar em nosso site e vai conseguir fazer seguindo todas as instruções\.
3. Caminho Secundário é o usuário fazer tudo que não pode, digitar a senha no email\. clicar onde não deve, digitar errado, fazendo com que o app reaja aos erros\.
4. Agora o nosso foco da aula: Coverage\.O coverage \(ou cobertura de código\) é uma métrica importante em testes de software, que indica a extensão em que o código\-fonte de um projeto é executado durante a execução dos testes\. Em outras palavras, o coverage mede quais partes do código foram "cobertas" pelos testes e quais partes não foram testadas\. O Jest, que é uma popular ferramenta de testes em JavaScript, oferece suporte integrado para medir essa cobertura\. 
5. O coverage tem 4 testes:
	1. Cobertura de Linha \(Line Coverage\):  
__O que é__: Mede o percentual de linhas de código que foram executadas durante os testes\.  
__Exemplo__: Se um arquivo tem 100 linhas de código e 80 dessas linhas são executadas pelos testes, a cobertura de linha é de 80%\.
	2. Cobertura de Função \(Function Coverage\):  
__O que é__: Mede o percentual de funções ou métodos que foram chamados durante os testes\.  
__Exemplo__: Se um arquivo contém 10 funções e 8 delas são chamadas durante os testes, a cobertura de função é de 80%\.
	3. Cobertura de Bloco \(Block Coverage\):  
__O que é__: Mede o percentual de blocos básicos de código que foram executados\. Um bloco básico é uma sequência de declarações ou expressões sem ramificações\.  
__Exemplo__: Dentro de um loop ou uma estrutura condicional, cada ramo ou iteração é considerado um bloco\.
	4. Cobertura de Condição/Ramo \(Branch Coverage\):  
__O que é__: Mede o percentual de todos os ramos de controle \(como if, else, switch case\) que foram executados\.  
__Exemplo__: Se um if tem um else, cada caminho \(if e else\) é um ramo\. Se o if é executado mas o else não, a cobertura de ramo não é 100%\.
6. Configurando o jest para poder ter o coverage,vamos começar pelo package\.json:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344004601100.png)
7. Agora vamos alterar o jest\.config\.js:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344005603200.png)
8. Para finalizar vamos também alterar babel\.config\.js  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344007603600.png)
9. Agora ao rodar o comando npm run coverage temos o seguinte resultado:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344009173600.png)
10. Isto nos mostra como o projeto falta ser testado, e inclusive nos mostra as linhas que estão faltando serem testadas\. Agora vamos criar testes do AnimesCard\.jsx, primeiro vamos adicionar data\-testid no AnimesCard:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344011223400.png)
11. Vamos criar agora um factory:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344013222100.png)
12. E implementar um teste para validar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344015222700.png)
13. Agora ao iniciar o coverage:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344017222100.png)
14. Vamos agora implementar 100% de coverage no AnimesList\.jsx, para isto iremos Atualizar os arquivos de AnimesList\.jsx, animesCard\.jsx e os 2 testes:  

	1. AnimesCard:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344019234200.png)
	2. AnimesList:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344021222600.png)
	3. AnimesList\.test\.js:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344022224200.png)
	4. AnimesCard\.test\.js:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344024253800.png)
	5. anime\.factory\.js:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344026223300.png)
15. Agora como desafio para o fim da aula, devem tentar criar um teste para suprir o coverage do formulário do anime, repare que o animeCard e o anime List está 100% já:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344026223300.png)
16. Não esqueça de subir ao github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344028678700.png)  
  
  
  
   
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


