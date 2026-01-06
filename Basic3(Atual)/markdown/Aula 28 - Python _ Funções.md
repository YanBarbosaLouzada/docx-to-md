# __PLANO DE AULA__

Aula 28 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: No computador

Ferramenta\(s\): Python e VS Code

Conteúdos 

- Funções\.

Objetivos

- Aprender sobre algo muito especial na programação chamado "funções"\.

Estratégias e atividades

- O que são Funções?
	- As funções são como pequenos robôs que fazem tarefas específicas quando as chamamos\. Por exemplo, um robô para contar histórias, outro para fazer cálculos matemáticos e até mesmo um para criar saudações especiais\!
- Definindo uma Função:

\# Definindo uma função para saudar

def saudacao\(\):

    print\("Olá\! Bem\-vindo à aula sobre funções\."\)

\# Chamando a função

saudacao\(\)  \# O robô de saudação entra em ação\!

- Explicação:
	- Aqui, a função “saudacao\(\)” é como um robô que sabe como cumprimentar\. Quando chamamos “saudacao\(\)”, o robô faz sua mágica e imprime a saudação\!
- Funções que fazem cálculos:

\# Uma função que soma dois números

def soma\(a, b\):

    resultado = a \+ b

    return resultado

\# Chamando a função

print\("Resultado da soma:", soma\(5, 3\)\)  \# O robô de soma faz o cálculo\!

- Explicação:
	- Agora temos um robô especializado em somar\! Ele recebe dois números e devolve a soma deles\. Chamamos o robô com “soma\(5, 3\)” e ele nos dá o resultado\!
- Funções podem ser inteligentes:

\# Função que saúda com nome, mas se não dissermos um, ela inventa um para nós\!

def saudacao\(nome="amigo"\):

    print\(f"Olá, \{nome\}\!"\)

\# Chamando a função

saudacao\(\)  \# O robô de saudação nos chama de "amigo"

saudacao\("Alice"\)  \# Mas se dermos um nome, ele usa esse nome\!

- Explicação:
	- O robô de saudação é muito amigável\! Se esquecemos de dizer um nome, ele nos chama de "amigo"\. Mas se dissermos um nome, ele usa esse nome para nos cumprimentar\!
- As Funções podem se autochamar:

\# Função que calcula o fatorial de um número

def fatorial\(n\):

    if n == 1:

        return 1

    else:

        return n \* fatorial\(n \- 1\)

\# Chamando a função

print\("Fatorial de 5:", fatorial\(5\)\)  \# O robô de fatorial usa sua magia\!

- Explicação:
	- O robô de fatorial é muito esperto\! Ele usa a mágica da recursão, ou seja, chama a si mesmo para calcular o fatorial\. Por exemplo, “fatorial\(5\)” significa 5 x 4 x 3 x 2 x 1\.
- Função com lista como parâmetro:

\# Função que encontra o maior número em uma lista

def maior\_numero\(lista\):

    maior = lista\[0\]

    for numero in lista:

        if numero > maior:

            maior = numero

    return maior

\# Chamando a função

numeros = \[10, 25, 7, 42, 15\]

print\("O maior número é:", maior\_numero\(numeros\)\)

- Explicação:
	- A função “maior\_numero\(\)” recebe uma lista de números como parâmetro e encontra o maior entre eles utilizando um loop “for” e uma comparação simples\.
- Função com retorno múltiplo:

\# Função que retorna múltiplos valores

def calcular\(valores\):

    soma = sum\(valores\)

    media = soma / len\(valores\)

    return soma, media

\# Chamando a função

lista = \[5, 10, 15, 20, 25\]

soma\_total, media\_total = calcular\(lista\)

print\("Soma:", soma\_total\)

print\("Média:", media\_total\)

- Explicação:
	- Aqui, a função “calcular\(\)” recebe uma lista de valores e retorna tanto a soma quanto a média desses valores\. Isso é possível porque ela retorna múltiplos valores, que são recebidos separadamente na chamada da função\.
- Função com argumentos variáveis:

\# Função com argumentos variáveis \(\*args\)

def somar\(\*args\):

    soma = sum\(args\)

    return soma

\# Chamando a função

print\("Soma:", somar\(5, 10, 15\)\)

print\("Outra Soma:", somar\(1, 2, 3, 4, 5\)\)

- Explicação:
	- A função “somar\(\)” utiliza “\*args” para aceitar um número variável de argumentos\. Isso permite somar qualquer quantidade de números passados para a função\.
- Desafio das Tabuadas:
	- Crie uma função chamada “tabuada” que recebe um número como parâmetro e exibe a tabuada desse número de 1 a 10\.
	- Por exemplo, ao chamar “tabuada\(7\)”, a função deve imprimir a tabuada do 7:

7 x 1 = 7

7 x 2 = 14

7 x 3 = 21

7 x 10 = 70

Use o loop “for” dentro da função para gerar essa tabuada\!

\# Função para exibir a tabuada de um número de 1 a 10

def tabuada\(numero\):

    for i in range\(1, 11\):

        resultado = numero \* i

        print\(f"\{numero\} x \{i\} = \{resultado\}"\)

\# Chamando a função para exibir a tabuada do 7

tabuada\(7\)

Recursos

- Computador, internet, Python e VS Code\.

Observação

Tarefas

- Faça uma função Alimentação que cada vez que comer um alimento você aumenta 1 quilo\. Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

