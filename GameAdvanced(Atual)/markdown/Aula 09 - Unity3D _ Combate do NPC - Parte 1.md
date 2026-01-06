# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600250820300.png)

# __PLANO DE AULA__

Aula 09 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Combate do NPC \- Parte 1

Objetivos

- Configurar sistema de combate do NPC\.

Estratégias e atividades

Continuando a configuração do sistema de combate, chegou a hora de ajustar o NPC\. Vamos repetir o mesmo processo do Player, baixando as animações de ataque \(__Attack1__ e __Attack2__\),__ Hit__ \(Dano\) e __Death__ \(Morte\)\. 

Atualize primeiro o Animator__ NPC\_Passive:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600255611900.png)__

Depois, crie um novo Animator Controller, chamado__ NPC\_Combat__ e configure desta forma:

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600255611900.png)__

Também criaremos um objeto para o NPC para representar seu corpo, chamado __Enemy\.__ Crie e adicione a__ TAG Enemy__ ao objeto, assim como os componentes __Rigidbody__ e __Capsule Collider__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600255611900.png)

Vamos criar o script do objeto Enemy e chamá\-lo de __EnemyBody__:

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using UnityEngine;__

__public class EnemyBody : MonoBehaviour__

__\{__

__    NPC npc;__

__    void Start\(\)__

__    \{__

__        npc = GetComponentInParent<NPC>\(\);__

__    \}__

__    void Update\(\)__

__    \{__

__        __

__    \}__

__    private void OnTriggerEnter\(Collider other\)__

__    \{__

__        if \(other\.gameObject\.CompareTag\("Right\_Hand"\)\)__

__        \{__

__            if \(other\.gameObject\.GetComponentInParent<Player>\(\)\.isAttacking && \!npc\.isHit\)__

__            \{__

__                npc\.HitDamage\(20\);__

__            \}__

__        \}__

__        else if \(other\.gameObject\.CompareTag\("Left\_Hand"\)\)__

__        \{__

__            if \(other\.gameObject\.GetComponentInParent<Player>\(\)\.isAttacking && \!npc\.isHit\)__

__            \{__

__                npc\.HitDamage\(20\);__

__            \}__

__        \}__

__        else if \(other\.gameObject\.CompareTag\("Right\_Leg"\)\)__

__        \{__

__            if \(other\.gameObject\.GetComponentInParent<Player>\(\)\.isAttacking && \!npc\.isHit\)__

__            \{__

__                npc\.HitDamage\(30\);__

__            \}__

__        \}__

__        else if \(other\.gameObject\.CompareTag\("Left\_Leg"\)\)__

__        \{__

__            if \(other\.gameObject\.GetComponentInParent<Player>\(\)\.isAttacking && \!npc\.isHit\)__

__            \{__

__                npc\.HitDamage\(30\);__

__            \}__

__        \}__

__    \}__

__\}__

No __NPC__, crie e adicione a TAG __EnemyHit__ no objeto que representa a mão do personagem, normalmente chamado de __mixamorig:RightHand__ em animações do Mixamo \(se sua animação utiliza as duas mãos, então adicione a TAG EnemyHit na mão esquerda também\)\. Também criaremos um __Sphere Collider__ com __isTrigger__ selecionado:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600255611900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600276663700.png)

Na próxima aula vamos fazer as alterações no script do NPC para torná\-lo um inimigo dentro do jogo\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Sem tarefa\.

