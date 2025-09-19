# __PLANO DE AULA__

Aula 11 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Dom em tela\.

Objetivos

- Ensinar os alunos sobre como o mundo real funciona;
- Usar o  [https://fonts\.google\.com/](https://fonts.google.com/);
- Usar o [https://getbootstrap\.com/docs/5\.3/getting\-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/);
- Usar o [https://color\.adobe\.com/pt/trends](https://color.adobe.com/pt/trends)\.  


Estratégias e atividades

- Continuar o site da semana passada criando agora uma tabela para ver as pessoas\.
- O que é dom?
- Aprender sobre novas tags:
	- <table>;
	- <thead></thead>;
	- <tbody></tbody>\.

1. Hoje vamos fazer uma tabela no HTML\. Para isso precisaremos aprender algumas tags:
	1. <table> conteúdo da tabela</table>
	2. <thead> cabeçalho </thead>
	3. <tbody> corpo da tabela </tbody>
	4. <tr> table row, ou linha horizontal da tabela </tr>
	5. <td> item da tabela </td>
2. Construir o HTML e CSS do novo form:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911453317800.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911455330700.png)
3. JS customizado para esta aula, para cadastrar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911455330700.png)
4. Agora, vamos observar o HTML da tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911458873700.png)

Repare que o código é muito simples\. É apenas um topo da tabela e o CSS\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911461330500.png)

1. Então, como nós vamos colocar nela as pessoas que adicionarmos? Com o JavaScript\. Por isso, é extremamente importante olhar o ID que colocamos no *tbody* da tabela\. Vamos criar agora uma função chamada *updateTabl*e, onde ela irá cada vez que for chamada, criar o *tbody* baseado na lista de pessoas que temos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911461330500.png)  
Nesta função, nós criamos um elemento chamado *"tr”*, e usamos a função *innerHTML* para editar o HTML contido no table\. O *dom *nada mais é que o domínio do JavaScript dentro de um site, fazendo com que nós consigamos manipular a tela usando JavaScript\.

  
Mas quando devemos chamar esta função? Sempre após adicionar uma pessoa \(linha 28\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911461330500.png)

1. Agora, vamos ver como fica quando cadastramos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911461330500.png)
2. Para finalizar, vamos subir o código no Github\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911461330500.png)

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911461330500.png)

Tarefas

- Sem tarefa\.

