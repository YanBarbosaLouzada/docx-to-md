# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599841027100.png)

# __PLANO DE AULA__

Aula 06 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Combate

Objetivos

- Configurar sistema de combate do Player\.

Estratégias e atividades

Vamos configurar o __sistema de combate __entre o Player e os NPCs\. Primeiro, vamos adicionar uma câmera de combate\. Crie uma nova __Cinemachine Virtual Camera__ que inicialmente ficará __desabilitada:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599846238500.png)

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599849987600.png)__

Deixe a câmera mais afastada do personagem para obter uma visão mais ampla do combate\. Configure a distância como desejar\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599858301900.png)

De início, vamos baixar __duas animações de Ataque__ do Player, animação de __Hit \(Dano\)__ e __Death \(Morte\)__\.

Após baixar e configurar corretamente as animações conforme as aulas anteriores, vamos criar um __Animator Controller__ e chamá\-lo de __Combat Controller__\. Configure\-o da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599864630100.png)

Para configurar as __colisões de ataque__ sem alterar a física básica do personagem, utilizaremos um objeto auxiliar que representará o __corpo do personagem__\. Todas as interações de ataque serão feitas com este objeto, que chamaremos de __PlayerBody:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599869972400.png)__

Adicione os componentes __Rigidbody__ e __Capsule Collider__ ao PlayerBody\. Vamos criar um Script para controlar as colisões:

Script PlayerBody:

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using UnityEngine;__

__public class PlayerBody : MonoBehaviour__

__\{__

__    Player player;__

__    void Start\(\)__

__    \{__

__        player = GetComponentInParent<Player>\(\);__

__    \}__

__    private void OnTriggerEnter\(Collider other\)__

__    \{__

__        if \(other\.gameObject\.CompareTag\("EnemyHit"\)\)__

__        \{__

__            if \(other\.gameObject\.GetComponentInParent<NPC>\(\)\.isAttacking && \!player\.isHit\)__

__            \{__

__                player\.HitDamage\(20\);__

__            \}__

__        \}__

__    \}__

__\}__

Para configurar os __hit Points__\(pontos de contato\), vamos criar__ Sphere Colliders__ nos objetos que representam as mãos e pés do Player\. Durante o ataque, estes colisores irão determinar quando o Player acertou o inimigo, através das TAGs:

- __Left\_Hand__ \- Tag na mão esquerda
- __Right\_Hand__ \- Tag na mão direita
- __Left\_Leg__ \- Tag na perna esquerda
- __Right\_Leg__ \- Tag na perna direita

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599877449200.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599877449200.png)

Agora, vamos adicionar novos comandos de ataque, atualizando o __Input Actions__ Controls, incluindo:

- A Action __Attack__ para acionar os golpes do Player;
- A Action __ChangeState__ para alternar entre o modo pacífico e agressivo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599889398000.png)

Na próxima aula iremos alterar o script do personagem para funcionar com o sistema de ataque\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Crie uma apresentação com pelo menos 3 diferentes sistemas de ataque em jogos\. Explique cada um deles e suas principais características\.

