# __PLANO DE AULA__

Aula 27 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: No computador

Ferramenta\(s\): Python e VS Code

Conteúdos 

- Laços de repetição For e While\.

Objetivos

- Hoje, vamos explorar os __laços de repetição__ \(loops\) e descobrir como utilizá\-los para automatizar a execução de comandos repetitivos em nossos programas\. Com os loops, podemos escrever códigos mais eficientes e reduzir a quantidade de trabalho manual, permitindo que nossos programas executem tarefas repetitivas de forma automática e precisa\.

Estratégias e atividades

- Vamos ver como o “for” funciona com alguns exemplos\!
- Interação em uma Lista:

\# Mostrando cada brinquedo de dentro de uma caixa

brinquedos = \['boneca', 'carrinho', 'bola'\]

for brinquedo in brinquedos:

    print\(brinquedo\)

- Explicação:
	- O “for” é como um explorador que olha para cada brinquedo na caixa e diz o nome de cada um, um de cada vez\!
- Interação em um Intervalo Numérico:

\# Contando de 1 a 5

for numero in range\(1, 6\):

    print\(numero\)

- Explicação:
	- O “for” é como um contador que começa em 1 e vai até 5, contando de um em um\.
- Uso do “for” com Strings:

\# Mostrando cada letra de uma palavra

palavra = "Python"

for letra in palavra:

    print\(letra\)

- Explicação:
	- O “for” é como um mágico que separa cada letra da palavra e a mostra, uma de cada vez\!

Explorando o “for” em Python:

- Interação com Contagem Personalizada:

\# Contagem personalizada com o for

inicio = 5

fim = 15

for contador in range\(inicio, fim \+ 1\):

    print\(f"Contador: \{contador\}"\)

- Explicação:
	- Aqui, usamos o “for” para criar uma contagem personalizada, começando do número 5 e indo até o 15, incluindo o próprio 15\. O “range\(\)” permite definir o intervalo desejado\.
- Interação com Passos Diferentes:

\# Contagem com passos diferentes

for i in range\(0, 10, 2\):

    print\(i\)

- Explicação:
	- Neste exemplo, o “for” percorre um intervalo de 0 a 9, mas avança de 2 em 2\. Isso é controlado pelo último argumento em “range\(\)”, que especifica o passo\.
- Uso do “for” com Listas Aninhadas \(opcional\):
	- Iteração em uma lista aninhada:

matriz = \[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

for linha in matriz:

    for elemento in linha:

        print\(elemento, end=" "\)

    print\(\)

- Explicação:
	- Este exemplo mostra como usar o “for” com listas aninhadas \(listas dentro de listas\)\. O primeiro “for” percorre cada lista dentro da “matriz” e o segundo \`for\` percorre cada elemento dentro dessas listas, imprimindo\-os\.
- Uso do “for” com Strings e Acumulador:

\# Contando vogais em uma palavra

palavra = "paralelepípedo"

contador\_vogais = 0

for letra in palavra:

    if letra in 'aeiou':

        contador\_vogais \+= 1

print\(f"A palavra '\{palavra\}' tem \{contador\_vogais\} vogais\."\)

- Explicação:
	- Aqui, o “for” percorre cada letra na “palavra”\. O “if” verifica se a letra é uma vogal e, se for, aumenta o contador de vogais\. Ao final, imprime o total de vogais na palavra\.
- Laço de Repetição \`while\` em Python
	- Sintaxe Básica:

\# Sintaxe do while

while condição:

    \# Bloco de código a ser executado

    \# Enquanto a condição for verdadeira

- Exemplo de Uso:

\# Contagem regressiva usando while

contador = 5

while contador > 0:

    print\(contador\)

    contador \-= 1

print\("Fogo\!"\)

- Explicação:
	- __while contador > 0:__ Define a condição para o laço continuar enquanto o contador for maior que zero;
	- __print\(contador\):__ Exibe o valor atual do contador;
	- __contador \-= 1:__ Decrementa o contador a cada iteração;
	- Quando a condição não é mais verdadeira \(contador <= 0\), o laço “while” termina e imprime "Fogo\!"\.
- Importância do “while”:
	- O “while” é útil quando o número de interações não é conhecido antecipadamente ou quando se quer continuar repetindo até que uma condição específica seja alcançada\. No entanto, é essencial garantir que a condição de parada seja alcançada para evitar loops infinitos\.
	- O “while” é uma ferramenta poderosa para criar lógicas de repetição em programas, permitindo executar operações enquanto uma condição é verdadeira\. É fundamental compreender a lógica por trás da condição para evitar loops infinitos e garantir que o código funcione corretamente\.
- Desafios:
	- 1\. Crie uma lista com seus animais favoritos e use o “for” para mostrar cada animal\.
	- 2\. Faça um “for” para contar de 10 até 1, de um em um, e dizer "Foguete decolando\!" quando chegar a 1\.
	- 3\. Pense em uma palavra bem legal e use o \`for\` para mostrar cada letra, mas pule a segunda letra a cada vez\.

Recursos

- Computador, internet, Python e VS Code\.

Observação

Tarefas

- Faça um sistema de loop simples que percorra uma lista\. Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

