# __ PLANO DE AULA__

Aula 23 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Validações

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

Agora vamos entender nesta aula a diferença de imagem\(container\) e máquina virtual\(machine virtualization\)\.A fim de resumir, vamos entender o que é um sistema operacional, que nada mais é do que um software que executa em cima da placa\. Vamos imaginar que você tem uma casa e quer brincar de fazer várias pequenas casinhas para seus brinquedos\.

- __Máquina Virtual \(VM\)__

Pense na máquina virtual como se você estivesse construindo uma casa completa, com tudo o que uma casa precisa: paredes, telhado, cozinha, banheiro, etc\. Cada casa tem seu próprio espaço, suas próprias instalações e seus próprios móveis\. Mesmo que você tenha várias casinhas no seu quintal, cada uma delas é independente e tem tudo o que precisa para funcionar sozinha\.

- __Vantagem:__ Cada casa é completamente independente, então se uma tiver problemas, não afeta as outras\.
- __Desvantagem:__ Construir cada casa completa leva tempo e ocupa bastante espaço no quintal\.

__Container__

Agora, pense no container como se você estivesse criando várias casinhas, mas todas compartilham algumas coisas\. Por exemplo, todas usam a mesma cozinha e o mesmo banheiro, mas têm seus próprios quartos e áreas de brincar\. Então, cada casinha precisa de menos espaço e é mais rápida de construir, porque muitas coisas são compartilhadas entre elas\.

- __Vantagem:__ Como várias casinhas compartilham algumas partes, é mais rápido e ocupa menos espaço\.
- __Desvantagem:__ Se a cozinha ou o banheiro compartilhado tiverem um problema, todas as casinhas podem ser afetadas\.

### <a id="_2md7kbyg0au"></a>__Resumo__

- __Máquina Virtual:__ Cada casa \(VM\) é completa e independente, mas leva mais tempo e espaço\.
- __Container:__ Cada casinha \(container\) é mais leve e rápida de fazer, porque compartilha partes com outras casinhas\.

Então, quando você quer ter várias "casinhas" para seus brinquedos, os containers são como casinhas que compartilham recursos, e as máquinas virtuais são como casinhas completas e separadas\.

Agora que tivemos essa pequena explicação vamos começar a entender como funcionam os sistemas operacionais, vamos entender como o nosso código está funcionando e porque isto é importante, nós utilizamos um sistema operacional chamado WINDOWS que é onde nosso código está sendo usado, mas agora porque isso importa? Porque iremos usar o git que nada mais é que um servidor linux rodando em cima do windows, ou seja estamos usando 2 sistemas operacionais distintos\. e é usando este sistema operacional que vamos pedir pro github testar nosso código\.Mas antes devemos entender nosso fluxo atual:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344114131600.png)

1. Vamos entender que o nosso sistema operacional é o windows, e dentro deles usamos um outro sistema chamado unix que contém o git dentro\. Vamos agora criar um sistema de validação usando o github actions\. Vamos agora começar a utilizar o projeto\. Vamos agora criar o código em \.github/workflows/ci\.yml![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344116221000.png)
2. Vamos agora no  \.github/workflows/ci\.yml:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344117445000.png)
3. Vamos agora dar um git push no nosso repositório  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344119451600.png)
4. Agora se formos ao github,veremos que ao lado do nome tem um símbolo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344119451600.png)
5. Ao clicarmos no laranja veremos que está rodando nosso CI de testes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344119451600.png)
6. Agora em detalhes podemos ver o processo:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344119451600.png)
7. E o que isto pode ajudar? Vemos agora que os testes passaram:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344126799500.png)  

8. Mas e quando os testes falharem?Para isto vamos editar um teste para retornar o erro, vou editar qualquer teste para falhar::  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344127799500.png)
9. E subir ao github:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344129802600.png)
10. Repare que agora o github nos avisa que algo deu errado e no próprio repositório nos avisa que o código está errado:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635344131813500.png)
11. Agora os alunos devem tentar criar  uma nova página contando sobre qualquer tem e criar seus próprios testes esperando que o github actions passe\.  
  
   
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


