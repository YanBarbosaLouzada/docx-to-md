 PLANO DE AULA

Aula 19 | Tempo estimado: 1 hora e 30 minutos | Web Intermediary 

Tipo da atividade: Offline

Ferramenta\(s\):  React e Postgresql

Conteúdos

- Testes

Objetivos

- Criar Repositório e subir a aplicação online
- Entender como a Web funciona, o que é a Web e o que um backend faz\.

Estratégias e atividades

1. Hoje vamos testar o sucesso do envio de mensagens nos estados\. Para verificar se as mensagens estão sendo enviadas corretamente, mas primeiro vamos interagir com essas libs:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343755975200.png)
2. __npm i axios\-mock\-adapter mock\-socket socket\.io__
3. Agora vamos instalar libs de desenvolvimento:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343757996800.png)
4. __npm i \-D @babel/preset\-env @babel/preset\-react babel\-jest  babel\-plugin\-transform\-import\-meta identity\-obj\-proxy__
5. Vamos também criar um modelo pro jest dentro do package\.json:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)

Configuração do Jest

O Jest é uma ferramenta para executar testes em JavaScript/Node\.js\. Seu

arquivo de configuração \(jest\.config\.js\) é usado para personalizar o

comportamento padrão do Jest\.

Por que precisamos do jest\.config\.js?

Modularidade: Permite configurar como os testes serão executados\.

Mapeamento de paths: Ajuda a entender importações customizadas\.

Suporte a transpiladores \(ex\.: Babel\): Necessário para suportar recursos modernos do JavaScript\.  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)

Principais funcionalidades:

__testEnvironment__: Define o ambiente de execução dos testes\. Use jsdom para front\-end e node para back\-end\.

__transform__: Diz ao Jest como processar arquivos JS modernos com Babel\.

__moduleNameMapper__: Define aliases para caminhos customizados nos imports\.

__collectCoverage__: Gera relatórios sobre a cobertura dos testes\.

1. Vamos aproveitar e criar um babel também:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)
2. Não podemos esquecer de configurar também o setupTestes:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)
3. Para que o teste funcione vamos precisar apenas alterar um pedaço do chat:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)
4. Agora vamos ao teste do join:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)
5. Agora vamos testar o Chat:  
![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)
6. Não podemos esquecer de subir no github:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343759978200.png)
7. Sempre lembre de verificar os testes pelo terminal:![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767635343771973800.png)  
  
  
  


Recursos

- [Git \- Downloads](https://git-scm.com/downloads)
- [Download Visual Studio Code \- Mac, Linux, Windows](https://code.visualstudio.com/download)

Observação

- Todos os arquivos de configuração já estão disponíveis e o código está no repositório da Mynds, existe um Github chamado GithubTutorial onde o professor pode entender 100% de todos os detalhes e configurações necessárias na ferramenta Git\.

Tarefas

- Sem tarefa

