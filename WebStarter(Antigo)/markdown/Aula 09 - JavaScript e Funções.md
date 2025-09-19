# __PLANO DE AULA__

Aula 09 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- JavaSscript e funções\.

Objetivos

- Ensinar os alunos sobre como o mundo real funciona;
- Apresentar o site [https://fonts\.google\.com/](https://fonts.google.com/);
- Conhecer o [https://getbootstrap\.com/docs/5\.3/getting\-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/);
- Usar o [https://color\.adobe\.com/pt/trends](https://color.adobe.com/pt/trends)\.  


Estratégias e atividades

- Estilizar o site e aprender sobre JavaScript\.
- O que é uma linguagem de programação\.
- Aprender sobre JavaScript e as tags: 
	- <script> </script>

1. Hoje vamos fazer o nosso primeiro deploy online\.
2. __O que é uma linguagem de programação?__

Vamos começar a entender o que foi que aprendemos até agora, HTML e CSS\. O HTML é uma linguagem de marcação, ou seja, nós marcamos o site e definimos uma estrutura, já o CSS é apenas estilização, então apesar de termos possibilidade de criar animações, nós não podemos no CSS programá\-las\.

1. __Mas o que é programação?__

A programação nada mais é que criar passos lógicos que o computador ou o seu projeto vai fazer, e com isto, criar diferentes tipos de coisas e situações inusitadas\. E para isto usaremos o JavaScript\.

1. __Mas como usar o JavaScript?__

Existem muitos meios diferentes, o primeiro será __no final__ __do <body>__, colocar uma tag chamada <script> </script> e tudo dentro dela já será rodado em JavaScript\.

1. A primeira coisa, e provavelmente a que mais irá usar em uma construção de site, é o comando* console\.log\(\) *onde ele mostra na tela um o conteúdo que deseja visualizar, também podemos editar para ter errors:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601092355700.png)
2. Para visualizar, é importante que nós abramos o arquivo HTML no site\. Ao abrir o site, clicar com o botão direito do mouse e ir na opção *“inspecionar”*, abrí\-lo e se direcionar ao console:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601094328500.png)
3. Agora, vamos começar com os tipos de variáveis\. Existem diferentes tipos de variáveis\. __Mas o que é uma variável?__ Ela nada mais é que uma informação que queremos guardar dentro de uma palavra, aqui estão os tipos\.

As vezes precisamos colocar variáveis em um texto, nesse caso nós usamos crases \(\`\`\) para podermos indicar que colocaremos variáveis lá dentro com *$\{nomeDaVariavel\}*\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601096319500.png)  
Elas podem variar desde textos até objetos e outras estruturas\.

1. Existe também, uma coisa chamada *holding *no JavaScript, que são tipos diferentes de estruturas de variáveis\. Pense comigo, existem informações que são pra sempre com o mesmo valor\. Exemplo de uma informação que nunca irá mudar como o nome de um anime ou desenho, porém o número de episódios muda\. Então existem no total 3 tipos de holding no JavaScript: 1\) As __Constantes__ que como o próprio nome já diz, o valor dela é fixo e não muda\. 2\) A __Variável__ que o valor e pode mudar; 3\) A __Let__ que depois de usada ela irá sumir\. E por que isso importa? Como todo programa, seu site precisa gastar um espaço da memória do computador para rodar\. Este espaço pode ser guardado em bytes ou gigabytes, então para eliminar peso desnecessário, nós usamos a __Let__ muitas vezes\.   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601098318400.png)
2. Agora, para compararmos os valores de variáveis, nós usamos tanto variáveis do mesmo tipo \(texto, número\) quanto de tipos diferentes e aqui está alguns tipos de exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601099318200.png)  
O resultado no console do inspecionar \(sempre lembre\-se de dar F5 depois de alterar o JavaScript se não o projeto não carrega o código alterado\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601101320200.png)
3. __Funções:__ nada mais são que tarefas pré programadas\. Vamos criar uma função chamada Cliquei, que mostra quantas vezes clicamos no número:  
  
Vou deixar abaixo outro jeito de criar funções, se divirta tentando fazer o Cliquei como uma arrow function:

  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601102318600.png)  
Mas agora como chamamos a função em um botão, lembre\-se sempre de colocar os parênteses pois eles simbolizam que a função foi clicada\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601104317900.png)  
  
Agora, clique no botão do site e repare no console:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601105328100.png)

1. Funções também podem receber coisas\. Ao receber, elas são atribuídas a uma variável que está dentro do parênteses:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601107318200.png)  

2. E por último, a função também pode estar atribuída a retornar uma variável:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601108318300.png)
3. Existem perguntas inteligentes que podemos criar no código, as chamamos de condicionais, com situações de se ou se não\. Também conhecidos como if e else\.  ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601110319000.png)
4. Para finalizar, vamos subir o código no Github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601111319100.png)

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601113317700.png)

Tarefas

- Pesquisar usos do JavaScript\. Monte uma apresentação e envie para o e\-mail [myndstechschool@gmai\.com](mailto:myndstechschool@gmai.com) ou via Discord para seu professor\.

