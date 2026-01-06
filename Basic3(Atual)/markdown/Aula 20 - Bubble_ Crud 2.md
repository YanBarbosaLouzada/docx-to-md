# __PLANO DE AULA__

Aula 21| Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: Online

Ferramenta\(s\): Site https://bubble\.io/

Conteúdos

- Aprender a cadastrar diferentes itens no site\.

Objetivos

- Apresentação do banco de dados e interação com ele\.

Estratégias e atividades

Conteúdos

- Aprender a cadastrar diferentes itens no site\.

Objetivos

- Apresentação do banco de dados e interação com ele\.

Estratégias e atividades

- Vamos agora, criar a função deletar\. Para isto vamos criar um componente que mostrará o nome de cada um dos já cadastrados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775169580200.png)
- Repare que ele irá pedir algo sobre o banco de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775171552800.png)
- Vamos colocar uma ordenação e dizer que ele irá buscar no banco de dados:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775173556100.png)
- Agora, na simulação, repare que ele já deixa setado qual é o item do anime que irá aparecer:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775176194100.png)
- Agora vamos colocar o título do anime\. Para isto precisamos entender que o existe algo chamado dado dinâmico, que é uma representação de o que pode vir mas não seu valor, exemplo sabemos que vai vir o nome do banco de dados mas não temos como saber exatamente qual nome está lá:
- Arraste um texto para seu repeating grou;
	- Clique para editar o texto que está aparecendo e depois clique ao lado que está escrito Insert Dinamic Data
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775178193100.png)
	- Use estas configurações \( Current cell’s Anime’s Name \)
	- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775180193000.png)
- E quando nós clicarmos pra ver a página, veremos já um anime:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775181200200.png)
- Para podermos deletar, vamos adicionar ao lado do texto um ícone de lixeira:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775183217200.png)
- No workflow, vamos customizar para quando clicarmos no ícone, deletar um item do banco de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775186192600.png)
- E agora nós já conseguimos deletar um item do current cells que significa anime atual:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775188192600.png)
- Agora é só clicar na lixeira e consultar o banco de dados:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775190193200.png)
- E veremos que realmente deleta em tempo real:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)  
  

- Vamos criar a função mais complexa que é a de editar\. Começaremos criando um *popup* e colocando o tipo dele “anime”:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)
- Para mexermos na página ou no popup podemos escolher quais itens vamos ver em tela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)
- No popup, vamos precisar mexer para que cada input venha com o initial content do item que clicamos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)
- Além de deixar o initial content com os valores do parent group anime, vou adicionar um ícone de fechar no canto superior direito:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)
- Quando clicarmos no ícone, vamos esconder o componente popup editar:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)
- E quando clicarmos no ícone de editar, vamos mostrar o popup editar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)
- Vamos também precisar enviar os dados do item que clicamos:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775192192200.png)  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775208003000.png)
- Agora quando clicarmos, aparecerá o anime que clicamos no popup para editarmos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775208003000.png)
- Para finalizar, vamos programar o botão de editar para quando clicarmos nele editar o item e fechar o popup\. Uma dica muito boa é renomear os inputs para ficarem fáceis de achar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775208003000.png)
- Repare que o código agora ficará fácil de achar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775208003000.png)
- Não se esqueça de fechar o popup:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775208003000.png)
- E agora os animes editados aparecem:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767702775208003000.png)  


Recursos

- Navegador\.

Observação

- Não há observação\.

Tarefas

- Não há tarefas\. 

