# __ PLANO DE AULA__

Aula 14 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Node fetch

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje vamos consumir o novo endpoint do banco de dados relacional\. Repare que agora nosso backend conversa com outra api de outro backend, nós chamamos isto de micro serviços, a ideia de existir micro serviços é que a nossa api backend possa conversar com múltiplas apis diferentes, isto é muito usado em casos de pagamento, ou validação:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971000004200.png)
2. Para isto iremos instalar o axios no backend também:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971002005600.png)
3. Vamos criar um controller para consumir a api do pokeapi [https://pokeapi\.co/](https://pokeapi.co/) :  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971004006000.png)
4. Próximo passo é  o router:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971006005100.png)
5. Agora adicionaremos ele no projeto:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971007003900.png)
6. Mas porque isto é importante? Principalmente porque vamos utilizar os dados da api externa do pokemon para aprimorar as informações e gerar diferentes itens sem gastar espaço com banco de dados\.
7. E agora nosso GET já está funcionando:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971009006300.png)
8. Vamos agora chamar esta rota no react:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971010859700.png)
9. Agora vamos criar a página:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971012859700.png)
10. Agora vamos adicionar nas rotas e na navbar:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971013860500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971014859600.png)
11. Vamos agora criar a listagem:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971016858500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971018858500.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971019858000.png)
12. E não podemos esquecer de adicionar o modal:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971021858200.png)
13. Agora vamos enviar ao github:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767634971022858300.png)  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa  


