# __PLANO DE AULA__

Aula 10 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- Interagindo com formulários\.

Objetivos

- Ensinar os alunos sobre como o mundo real funciona;
- Usar o  [https://fonts\.google\.com/](https://fonts.google.com/);
- Usar o [https://getbootstrap\.com/docs/5\.3/getting\-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/);
- Usar o [https://color\.adobe\.com/pt/trends](https://color.adobe.com/pt/trends)\.  


Estratégias e atividades

- Estilizar o site da aula passada e aprender sobre JavaScript\.
- Aprender sobre novas tags:
	- <form></form>;
	- <input />;
	- <label></label>\.

1. Hoje vamos fazer um formulário interativo no HTML\. Para isso, precisaremos aprender algumas tags:
	1. __<form onSubmit=”nomeDaFunção\(\)”> </form>    
__Representa o espaço do formulário\.
	2. __<label for=”idDoInput”> texto do label</label  
__Representa o cabeçalho do input, uma coisa muito legal sobre os labels é que se o for estiver com o ID do input na hora que clicar na palavra do texto do label, irá automaticamente permitir digitar o input\.
	3. __<input type=”tipo do input” placeholder=”texto que aparece” />  
__Campo onde o usuário vai digitar\.
	4. __<button type=”submit”> Enviar</button>__

Botão que chama a função presente no onSubmit

- 
	1. Vamos também mover o script para outro arquivo, igual fazemos com o CSS, para ficar mais bonito: *<script src="\./nomeDoArquivo\.js"></script>*
	2. E o resultado do HTML é: \(lembre\-se sempre de ter o script no final do arquivo\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601170356600.png)

1. Vamos entender o código JavaScript\. A ideia deste projeto é salvar as pessoas e colocar em uma lista\. Então, precisaremos de duas coisas: o objeto *pessoa *e a *lista*:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601172542200.png)  

2. Agora, vamos criar a função ValoresForm\(event\)\. O motivo de ela ser um evento é porque se não for o navegador irá reiniciar a página no automático e para prevenir isto, usaremos o *event\.preventDefault\(\)* na função\. Após isso, pegamos os valores que estão escritos nos campos do formulário \(document é o código HTML gerado pelo navegador\) e adicionaremos em variáveis para poder montar o *objetoPessoa*, depois vamos limpar os campos do formulário, e por fim, adicionar a nossa variável *objetoPessoa* na lista\. E avisar o usuário que deu certo:  
  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601174543000.png)
3. Mas e se quisermos ver as pessoas na lista? Vamos criar um botão em HTML e chamar uma nova função:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601176542800.png)
4. Vamos usar a função *map*, onde ela irá para cada item da lista executar uma tarefa:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601177543400.png)
5. Para finalizar, vamos deixar o site bonitinho:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601179544100.png)
6. Agora, ao cadastrar uma pessoa, vemos que o site já salva a pessoa exibindo o alert:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601181542900.png)
7. E se clicarmos no visualizar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601182817400.png)
8. Para finalizar, vamos subir o código no Github \(em um novo repositório do Github sempre\):  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601184816900.png)

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601186816800.png)

Tarefas

- Sem tarefa\.

