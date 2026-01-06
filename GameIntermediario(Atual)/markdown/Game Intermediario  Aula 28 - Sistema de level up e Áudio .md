# __PLANO DE AULA__

Aula 28 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Intermediary 

Tipo da atividade: No computador

Ferramenta\(s\): Unity 2D

Conteúdos

- Sistema de level up e Áudio 

Objetivos

- Montar um Sistema de level up e Áudio

Estratégias e atividades

- Baixe os assets de som de level up e o sprite 
	- Se quiser coloque mais áudios no jogo 
- Ajuste o sprite do level up , sprite mode = multiple, pixel para 32, filter mode point\(no filter\)
	- Clique em sprite editor \->slice\-> automatic\->slice
- Crie um novo controller para o level up 
- Crie uma animação para o sprite e chame de level up 
	- Para criar o animator basta abrir o animation e arrastar os frames do sprite para o animation
	- Para criar o controller basta clicar no \+ que está do lado da aba project e selecionar animator controller mude o nome para FX\_LevelUp\_0\.
- Lembre de tirar o loop da animação levelup 
- ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589893359200.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589894365000.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589896362100.png)  

- Agora vamos criar o canvas que falta para EXP
	- Dentro do canvas coloque o Gameobject “EXPText”, dentro dele adicione o canvas text e o level text
	- Siga as configurações do print abaixo ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589899203300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589901202200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589903218600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589904201900.png)

-  Faça as alterações dos scripts Player\.cs, Entity\.cs e Monster\.cs
-  Dentro do player fizemos as seguintes alterações\.\. 
	- Adicionamos o componente o Audio source

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589906202100.png)

- 
	- Adicionamos as informações do EXP & Sound![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589907202600.png)
	- Adicionamos o Canvas que criamos para exp EXP text e Level Up Sound

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767727589909201400.png)

Recurso

- Computador, internet, unity\.

Observação

- Os assets e scripts estão disponíveis no github;
- Link para o download da unity
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:
	-  Traga em um pendrive, no seu OneDrive/Google Drive, ou envie para o e\-mail [myndstechschool@gmail\.com](mailto:myndstechschool@gmail.com)\.
- Avise as Crianças que o GDD será usado no TCC 

Tarefas

- Continue fazendo o seu GDD em casa\.

