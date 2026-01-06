# __P__

# __LANO DE AULA__

Aula 26 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Basic 3

Tipo da atividade: No computador

Ferramenta\(s\): Python e VS Code

Conteúdos 

- Condicionais e Operadores Relacionais e Lógicos em Python usando o VS Code\.

Objetivos

- Nesta aula, vamos aprender sobre condicionais, operadores relacionais e lógicos em Python, utilizando o ambiente do VS Code para escrever e executar nossos códigos\.

Estratégias e atividades

- Uso do VSCode:
	- Instale o VSCode conforme as instruções anteriores;
	- Abra o VSCode e crie um novo arquivo Python \(extensão \.py\);
	- Copie e cole os exemplos de código;
	- Explique os códigos\.
- Condicionais e comparação de valores:

\# Exemplo de condicionais if\-elif\-else

\# if \-> SE / elif \-> SENÃO SE / else \-> SENÃO

idade = 18

if idade < 18:

    print\("Você é menor de idade\."\)

elif idade == 18:

    print\("Você tem 18 anos\."\)

else:

    print\("Você é maior de idade\."\)

\`\`\`

- Explicação:
	- Utilizamos “if”, “elif” \(abreviação de "else if"\) e “else” para criar diferentes caminhos de execução com base em condições\.
	- == é usado para comparar se dois valores são iguais\.
- Expressões Condicionais:

\# Expressões condicionais \- Ternary Operator

idade = 20

mensagem = "Menor de idade" if idade < 18 else "Maior de idade"

print\(mensagem\)

- Explicação:
	- Esta é uma expressão condicional ternária, onde a variável “mensagem” recebe um valor baseado na condição fornecida após o “if”\.
- Operadores Relacionais e Lógicos:

\# Exemplo de operadores relacionais e lógicos

idade = 25

tem\_cartao = True

if idade >= 18 and tem\_cartao:

    print\("Você pode comprar bebidas alcóolicas\."\)

elif idade < 18 or not tem\_cartao:

    print\("Desculpe, você não pode comprar bebidas alcóolicas\."\)

\`\`\`

Explicação:

\- \`and\`, \`or\` e \`not\` são operadores lógicos para expressar condições mais complexas\.

\- \`>=\`, \`<\`, etc\., são operadores relacionais para comparar valores\.

- Atividade para os Alunos:
	- Peça aos alunos para escreverem seus próprios blocos de código usando condicionais, operadores relacionais e lógicos para resolver problemas simples, como verificar se um número é par ou ímpar, ou se uma pessoa pode votar dependendo da idade\.
- Exemplos Adicionais de Condicionais e Operadores Relacionais/Lógicos:

\# Verificação se um número é par ou ímpar

numero = 7

if numero % 2 == 0:

    print\(f"\{numero\} é um número par\."\)

else:

    print\(f"\{numero\} é um número ímpar\."\)

\`\`\`

- Explicação:
	- % é o operador módulo, usado para verificar o resto da divisão por 2\. Se o resto for 0, o número é par; caso contrário, é ímpar\.

\# Verificação de faixa etária para acesso a diferentes áreas de um evento

idade = 22

if idade < 12:

    print\("Você pode acessar a área infantil\."\)

elif 12 <= idade < 18:

    print\("Você pode acessar a área juvenil\."\)

else:

    print\("Você pode acessar todas as áreas do evento\."\)

\`\`\`

- Explicação:
	- Usamos múltiplos “if” e “elif” para criar diferentes faixas etárias de acesso com base na idade\.

\# Verificação de login simples

usuario = "user123"

senha = "senha123"

input\_usuario = input\("Digite seu usuário: "\)

input\_senha = input\("Digite sua senha: "\)

if input\_usuario == usuario and input\_senha == senha:

    print\("Login bem\-sucedido\!"\)

else:

    print\("Usuário ou senha incorretos\."\)

\`\`\`

- Explicação:
	- Usamos operadores lógicos “and” para verificar se ambos \(usuário e senha\) estão corretos\.
- Operadores Lógicos com Listas:

\# Verificação se um item está em uma lista usando operador lógico

numeros = \[1, 2, 3, 4, 5\]

if 3 in numeros or 6 in numeros:

    print\("Pelo menos um dos números está presente na lista\."\)

else:

    print\("Nenhum dos números está na lista\."\)

\`\`\`

Explicação:

\- Usamos operadores lógicos \`or\` para verificar se pelo menos um dos números está presente na lista\.

Recursos

- Computador, internet, Python e VS Code\.

Observação

- Não há\.

Tarefas

- Faça um sistema simples que utilize uma condição\. Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail myndstechschool@gmail\.com\.

