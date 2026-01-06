# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599720878500.png)

# __PLANO DE AULA__

Aula 05 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de NPC\.

Objetivos

- Configurar sistema de NPC;

Estratégias e atividades

Na aula de hoje, criaremos um __NPC \(non\-playable character\)__, que representa os personagens que vivem no mundo do jogo e podem ter ações específicas ou aleatórias, interagindo com o Player\.

Para criar o NPC, vá até o site __Mixamo__ e escolha um personagem__ humanóide__\. Baixe também suas animações básicas: __Idle__ \(Parado\), __Walk__ \(andar\) e __Run__ \(correr\), repetindo o processo realizado anteriormente com o Player\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599720878500.png)

Após adicionar o modelo 3D na cena, vamos chamá\-lo de __NPC__ e adicionar o componente__ Animator__ para controlar suas animações\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599734762000.png)

Crie um __Animator Controller__ e configure da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599734762000.png)

Para movimentar o NPC, utilizaremos o componente __Nav Mesh Agent__\. Desta forma, podemos indicar para qual posição ele irá seguir, assim como controlar sua velocidade e em qual área ele poderá se movimentar:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599734762000.png)

Precisamos também indicar em qual a superfície o NPC pode se movimentar\. Adicionamos o componente __NavMeshSurface__ aos objetos considerados superfície caminhável\. No Inspector, marque a opção Default Área como __Walkable__, clique em__ Bake__ para confirmar e aguarde a Unity criar a malha do Nav Mesh:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599734762000.png)

Nosso NPC andará normalmente pela malh em __pontos pré\-estabelecidos__ e para facilitar esse processo, criaremos um objeto vazio chamado __PatrolGroup__ e dentro dele outros objetos chamados __Point\_1__, __Point\_2, Point\_3__ e etc\. Espalhe estes pontos pela área que o NPC irá circular, como um quarteirão por exemplo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599734762000.png)

Com tudo configurado, vamos criar o __script__ responsável por controlar o NPC\.

Script do NPC:

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using System\.Linq;__

__using Unity\.VisualScripting;__

__using UnityEngine;__

__using UnityEngine\.AI;__

__using static Player;__

__public class NPC : MonoBehaviour__

__\{__

__    \[Header\("Animation"\)\]__

__    public Animator anim;__

__    public RuntimeAnimatorController passiveController;__

__    \[Header\("IA"\)\]__

__    public NavMeshAgent agent;__

__    public Transform patrolGroup;__

__    public Transform\[\] patrolPoints;__

__    private int currentPatrolPointIndex;__

__    void Start\(\)__

__    \{__

__        patrolPoints = new Transform\[patrolGroup\.childCount\];__

__        for \(int i = 0; i < patrolGroup\.childCount; i\+\+\)__

__        \{__

__            patrolPoints\[i\] = patrolGroup\.GetChild\(i\);__

__        \}__

__        currentPatrolPointIndex = Random\.Range\(0, patrolGroup\.childCount\);__

__        agent\.SetDestination\(patrolPoints\[currentPatrolPointIndex\]\.position\);__

__    \}__

__    void Update\(\)__

__    \{__

__            anim\.SetFloat\("Velocity", agent\.velocity\.magnitude\)__

__	Passive\(\);__

__    \}__

__    public void Passive\(\)__

__    \{__

__        if \(\!agent\.pathPending && agent\.remainingDistance < 0\.1f\)__

__        \{__

__            currentPatrolPointIndex\+\+;__

__            if \(currentPatrolPointIndex < patrolPoints\.Count\(\)\)__

__            \{                __

__                agent\.SetDestination\(patrolPoints\[currentPatrolPointIndex\]\.position\);__

__            \}__

__            else__

__            \{__

__                currentPatrolPointIndex = 0;__

__            \}__

__        \}__

__    \}__

__\}__

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download)

Tarefa

- Faça uma pesquisa sobre inteligência artificial no contexto do desenvolvimento de jogos \(NPCs, inimigos\)\.
- Envie em um pendrive, no Google Drive, ou para o e\-mail __myndstechschool@gmail\.com__\.

