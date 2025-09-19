# __PLANO DE AULA__

Aula 13 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- CRUD e assincronismo\.

Objetivos

- Ensinar sobre o que é CRUD e como sincronizar os dados\.

Estratégias e atividades

- Continuar o site da semana passada, criando agora uma tabela para ver as pessoas\.
- O que é um banco de dados\.
- Aprender sobre requisições\.
- Entender o famoso CRUD\.

1. Hoje vamos entender sobre as ações que é possível ter em um site\. Existe o CRUD, onde são as 4 interações básicas do banco de dados:

	![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911700699800.png)

1. Vamos criar os arquivos de *update delete* e *post* importando eles no index\.html:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911702707800.png)
2. Arquivo de *post*: nele vamos criar um objeto com os valores do *input *e enviar para o banco de dados\. Depois disso, vamos formatar a resposta com o *\.then\(\)*  e caso dê errado, ele irá para o *\.catch\(\)*\. Formatando a resposta caso dê certo, vamos chamar a função *pegarDados* e atualizar a tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911707210300.png)
3. O *delete* tem uma URL um pouco diferente, pois o *\.json* dela fica depois do ID do dado no banco que vamos criar\. Caso dê certo, reiniciamos o “pegar dados”, caso dê errado, vamos colocar no console:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911709218600.png)  

4. Agora o editar funciona de dois modos\. Existe duas “situações no editar”:
	1. A primeira é quando clicamos no botão de editar de algo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911711113000.png)
	2. A segunda é quando de fato enviamos para o banco clicando no botão de editar lá do formulário:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911713895000.png)
5. Vamos entender o que acontece quando clicamos no botão editar de uma linha da tabela:
	1. Dentro do *get\.js* se você reparar existe um novo formato de arquivos nos botões onde chamamos as funções do nosso código:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911713895000.png)
	2. A função *EnviandoDadosAtuais* é responsável lá no* update\.js *por colocar o ID do banco dentro da tag do botão\. E colocar os dados no *input* que quer editar:   
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911715901700.png)  
Fazendo com que o formulário se altere, e dentro do botão exista uma meta\-tag que salva o ID do banco:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911717908700.png)
	3. Agora, quando editarmos, após clicar no botão “Edit Aqui\!”, ele irá chamar a função *post* que verificará se está no *editMode*, caso esteja, ele irá chamar a função de* editar*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911719917500.png)
	4. E a função de editar irá trocar os dados no banco substituindo o objeto pelo novo e se der certo recarregará a tabela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911719917500.png)  

6. Para finalizar vamos subir o código no Github\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911721927000.png)	

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758290911723935200.png)

Tarefas

- Tentar clonar o projeto em casa e editar, seja o CSS, ou adicionar mais campos no formulário\.

