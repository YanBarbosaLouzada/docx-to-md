# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951798780600.png)

# __PLANO DE AULA__

Aula 02 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Starter 

Tipo da atividade: No computador

Ferramenta\(s\): Godot

Conteúdos

- Programação com GDScript\.
- Fundamentos da linguagem\.

Objetivos

- Entender a sintaxe e principais conceitos da programação na Godot\.
- Movimentação simples do personagem\.

Estratégias e atividades

Agora que conhecemos a Godot Engine e sua interface, vamos aprender como dar vida aos nós \(objetos\) e às cenas por meio da programação, tornando possível o funcionamento das mecânicas do jogo\.

START

O que é GDScript?

O __GDScript__ é a linguagem de programação usada dentro da Godot Engine, que é parecida com o __Python__, uma linguagem muito usada por iniciantes\. Isso significa que:

- A indentação \(espaço/tabulação\) é importante;
- A sintaxe é simples, sem ponto e vírgula no final das linhas;
- Fácil de ler e entender\.

Exemplo de código em __GDScript__:

__func \_ready\(\):__

__    print\("Olá, mundo\!"\)__

__A primeira linha: extends__

No começo de quase todo script, você vai ver algo assim:

__extends Node2D__

Esse \`extends\` quer dizer que esse código está __ligado a um tipo de nó__ da Godot\. No exemplo acima, estamos dizendo que o script "herda" de um __Node 2D__, que é usado para coisas 2D\.

Outros exemplos:

__extends Node → nó básico\.__

__extends Sprite2D → imagem 2D\.__

__extends CharacterBody2D → personagem com física\.__

__Variáveis e Tipos Básicos__

Variáveis __guardam informações__ \(valores\) que podem ser alteradas durante a execução do jogo, como por exemplo a vida do jogador\. Em GDScript criamos uma variável usando a palavra __var__\.

Exemplo:

__var nome = "Maria"__

__var idade = 14__

__Tipos mais usados:__

__TIPO__

__EXEMPLO__

__USO__

int

vida = 3

Números inteiros

float

var tempo = 2\.5

Números com vírgula

bool

var vivo = true

Verdadeiro ou Falso

String

var nome = “João”

Texto entre aspas

Vector2

var pos = Vector2\(10,20\)

Coordenadas 2D \(x,y\)

Funções principais: \_ready\(\) e \_process\(delta\)

__Função \_ready\(\):__

É chamada __uma vez__ quando o nó aparece na cena\. Ideal para iniciar coisas\.

__func \_ready\(\):__

__    print\("Começou\!"\)__

__Função \_process\(delta\):__

É chamada __todo frame__, ou seja, várias vezes por segundo\. Usada para movimento e lógica contínua\.

__func \_process\(delta\):__

__    position\.x \+= 100 \* delta__

__delta__ é o tempo entre frames\. Usamos ele para o movimento ficar suave em qualquer computador\.

__Estruturas de Decisão: \(if/elif/else\)__

__if vida <= 0:__

__    print\("Game Over"\)__

__elif vida < 3:__

__    print\("Cuidado\!"\)__

__else:__

__    print\("Tudo certo"\)__

- if \(se\) → se for verdade, faz algo\.
- elif \(se não se\) → se não, tenta outra condição\.
- else \(se não\) → se nenhuma for verdadeira, faz isso\.

__Repetições: for e while__

__for__

Usamos para repetir algo __um número de vezes__\.

__for i in range\(5\):__

__    print\(i\)  \# Vai imprimir de 0 a 4__

__while__

Repete __enquanto uma condição for verdadeira__\.

__var contador = 0__

__while contador < 5:__

__    print\(contador\)__

__    contador \+= 1__

Resumo rápido

- __extends __→ diz qual nó seu script está usando\.
- __var__ → cria variáveis\.
- __Tipos importantes:__ \`int\`, \`float\`, \`bool\`, \`String\`, \`Vector2\`\.
- __\_ready\(\)__ → executa no início\.
- __\_process\(delta\)__ → executa todo frame\.
- __if, elif, else__ → decisões\.
- __for, while__ → repetições\.

__Dica__

Sempre que esquecer alguma dessas partes, volte aqui\! Essa apostila é o __guia rápido __para sua jornada com GDScript\.

Já aprendemos sobre as principais ferramentas e como incluir um personagem, mas para que ele ganhe vida, precisamos __programar__ seu funcionamento\. Vamos criar um novo script para o nosso personagem:

- Selecione o Node __CharacterBody2D__ e vamos criar um __script__ para ele:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951842163200.png)

- Crie uma pasta específica para __Scripts__: 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951844169200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951847926200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951847926200.png)

- Ao abrir o script, já temos o comando __extends CharacterBody2D__, que nos permite utilizar os comandos e bibliotecas específicas daquele Node:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951849933400.png)

- Como nosso objetivo é movimentar o personagem, vamos criar uma __variável__ para guardar o valor da velocidade:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951851940800.png)

Na __GDScript__, temos duas funções principais:

- __\_ready\(\):__ Inicializar variáveis e objetos\. Executa comandos no __primeiro frame__ do jogo;
- __\_process\(delta\):__ Comandos em__ looping __durante a execução do jogo, como por exemplo a movimentação do jogador\.

Vamos usar a propriedade __velocity__ dentro da função __\_ready\(\)__\. Quando falamos de objetos 2D, temos dois eixos de movimento:

- Eixo __X__: movimento horizontal \(esquerda e direita\);
- Eixo__ Y__:  movimento vertical \(cima e baixo\)\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951853948300.png)

Primeiro vamos alterar o valor da velocidade horizontal do personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951855955200.png)

Apenas alteramos o valor da __velocidade__, mas precisamos utilizar um __comando__ chamado __move\_and\_slide\(\)__ para __movimentar__ o personagem:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951855955200.png)

Perceba que ao testarmos o jogo, o personagem se movimenta para a direita\. Mas se aplicarmos uma força __negativa__ ao valor de speed, o personagem vai para a __esquerda__\.  

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951857960300.png)

Podemos utilizar __condições__ para acionar comandos, como por exemplo o __pressionamento de teclas__\. Vamos alterar o script para controlar o personagem pelas setas do teclado:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1762261951859966800.png)

Teste e veja que agora o personagem se movimenta apenas quando pressionamos as __setas esquerda__ e __direita\.__

__Desafio: Tente movimentar o personagem para cima e para baixo com as setas repetindo o processo anterior\.__

Finalizamos a segunda aula do módulo __Game Starter__\. Utilize os conhecimentos adquiridos até agora e adicione alguma nova funcionalidade ao personagem\.

Recursos

- Computador, internet, Godot instalado\.

