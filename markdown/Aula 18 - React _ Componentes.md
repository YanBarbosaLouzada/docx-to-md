# __PLANO DE AULA__

Aula 18 | Tempo estimado: 1 hora e 30 minutos | Web Starter

Tipo da atividade: Offline

Ferramenta\(s\): Computador, Git, nodeJS e VS Code

Conteúdos

- React Componentes\.

Objetivos

- Ensinar sobre React;
- Aprender o que é um componente;
- Configurar um projeto\.

Estratégias e atividades

- Criar um App simples usando React\.

1. Hoje vamos conhecer uma das maravilhas do React que são os componentes\. Resumindo, nós podemos criar templates 100% customizados e independentes\. Esta será a arquitetura das pastas de hoje:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601928002600.png)
2. Vamos começar entendendo o que é um componente simples:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601929003700.png)
3. E como faço para poder usar essa função HTML que retorna um HTML?
	1. Primeiro devemos ir até o App\.js, onde queremos usar a função, e importamos ela:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601931004300.png)
	2. Agora é só utilizar dentro do Return:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601932003400.png)
4. __O que é a função dupla?__ O React só permite passar uma tag por componente, então para poder colocar duas, nós utilizamos o fragmento que nada mais é que o *<> </>* vazio:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601934005200.png)
5. Chegamos ao ponto alto da aula\. Nós vamos primeiro de tudo entender uma coisa, quando nós queremos passar itens, tarefas, variáveis entre outras coisas para um componente, nós passamos por meio de props:   
*function MeuComponente\(props\)\{ return\(<div></div>\)\}*
6. O *Botão\.js* vai usar duas coisas como *props*, uma tarefa que ele vai fazer e qual a classe CSS dele vamos usar, o *props\.children* é tudo que fica entre o componente:  
*<Component> children aqui </Componente>:  
*![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601936005700.png)
7. O Botão\.css:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601938014600.png)
8. Agora, quando chamarmos o botão podemos enviar a classe e a tarefa que queremos:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601940004700.png)
9. E o resultado é que temos um botão reutilizável e customizável:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601941003700.png)

1. Para finalizar, vamos subir o código no Github\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601944177300.png)	

Recursos

- Git Chrome e VS Code\.

Observação

- Sempre que você quiser testar algum exemplo em JavaScript, você pode digitar um código direto no navegador como por exemplo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1758130601947507200.png)

Tarefas

- Clonar o projeto em casa e tentar customizar um novo componente para títulos\.

