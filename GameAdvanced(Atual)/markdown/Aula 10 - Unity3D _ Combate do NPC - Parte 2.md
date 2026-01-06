# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600411369500.png)

# __PLANO DE AULA__

Aula 10 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Combate do NPC \- Parte 2

Objetivos

- Configurar sistema de combate do NPC\.

Estratégias e atividades

Para dar continuidade ao sistema de combate do NPC que iniciamos na aula anterior, vamos fazer alterações importantes no script para integrar a lógica de ataque com o sistema de navegação e comportamento já implementado\. Vamos adicionar o controle de cooldown de ataques, detecção de distância e a execução dos diferentes tipos de ataque\.

__START__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600414982100.png)

Vamos atualizar o script do __NPC__ com o sistema de ataque:

using System\.Collections;

using System\.Collections\.Generic;

using System\.Linq;

using Unity\.VisualScripting;

using UnityEngine;

using UnityEngine\.AI;

using static Player;

public class NPC : MonoBehaviour

\{

   __ public enum NPCState__

__    \{__

__        Passive,__

__        Agressive,__

__        Equipped,__

__        Dead__

__    \}__

    \[Header\("NPC Status"\)\]

    __public NPCState state;__

__    \[SerializeField\] __

__    public float health = 100f;__

__    public bool isDead;__

__    public bool isAttacking;__

__    public bool isHit;__

    \[Header\("Animation"\)\]

    public Animator anim;

    public RuntimeAnimatorController passiveController;

    __public RuntimeAnimatorController enemyController;__

    \[Header\("Combat"\)\]

    __public GameObject player;    __

__    public float lastAttackTime;__

__    public float attackCooldown = 3f;__

__    public float attackDistance = 1f;__

__    \[SerializeField\]__

__    public bool isAgressive;__

    \[Header\("IA"\)\]

    public NavMeshAgent agent;

    public Transform patrolGroup;

    public Transform\[\] patrolPoints;

    private int currentPatrolPointIndex;

    void Start\(\)

    \{

        __isDead = false;__

__        isAttacking = false;__

__        isHit = false;__

        patrolPoints = new Transform\[patrolGroup\.childCount\];

        for \(int i = 0; i < patrolGroup\.childCount; i\+\+\)

        \{

            patrolPoints\[i\] = patrolGroup\.GetChild\(i\);

        \}

        currentPatrolPointIndex = Random\.Range\(0, patrolGroup\.childCount\);

        __state = NPCState\.Passive;__

        agent\.SetDestination\(patrolPoints\[currentPatrolPointIndex\]\.position\);

    \}

    void Update\(\)

    \{

        __if \(\!isDead\)__

__        \{__

__            anim\.SetFloat\("Velocity", agent\.velocity\.magnitude\);__

__             __

__            switch \(state\)__

__            \{__

__                case NPCState\.Passive:__

__                    anim\.runtimeAnimatorController = passiveController;__

__                    Passive\(\);__

__                    break;__

__                case NPCState\.Agressive:__

__                    anim\.runtimeAnimatorController = enemyController;__

__                    Agressive\(\);__

__                    break;__

__                case NPCState\.Dead:__

__                    Die\(\);__

__                    break;__

__            \}__

__            if \(isAgressive && player\.GetComponent<Player>\(\)\.state == PlayerState\.Agressive\)__

__            \{__

__                state = NPCState\.Agressive;__

__            \}__

__        \}__

__        else__

__        \{__

__            anim\.SetBool\("isDead", true\);__

__        \}__

    \}

    public void Passive\(\)

    \{

        if \(\!agent\.pathPending && agent\.remainingDistance < 0\.1f\)

        \{

            currentPatrolPointIndex\+\+;

            if \(currentPatrolPointIndex < patrolPoints\.Count\(\)\)

            \{                

                agent\.SetDestination\(patrolPoints\[currentPatrolPointIndex\]\.position\);

            \}

            else

            \{

                currentPatrolPointIndex = 0;

            \}

        \}

        __if\(player\.GetComponent<Player>\(\)\.state == PlayerState\.Agressive\)__

__        \{__

__            Fear\(\);__

__        \}__

    \}

    __public void Fear\(\)__

__    \{__

__        agent\.speed = 5f;__

__    \}__

    __public void Agressive\(\)__

__    \{__

__        float distanceToPlayer = Vector3\.Distance\(transform\.position, player\.transform\.position\);__

__        Quaternion targetRotation = Quaternion\.LookRotation\(player\.transform\.position \- transform\.position\);__

__        transform\.rotation = Quaternion\.Slerp\(transform\.rotation, targetRotation, 0\.1f\);__

__        if \(player\.GetComponent<Player>\(\)\.isDead || distanceToPlayer > 30\.0f\)__

__        \{__

__            currentPatrolPointIndex = Random\.Range\(0, patrolGroup\.childCount\);__

__            state = NPCState\.Passive;__

__            agent\.SetDestination\(patrolPoints\[currentPatrolPointIndex\]\.position\);__

__            agent\.isStopped = false;__

__            agent\.speed = 2f;__

__        \}__

__        else__

__        \{__

__            if \(isAttacking || isHit\)__

__            \{__

__                agent\.isStopped = true;__

__            \}__

__            else__

__            \{__

__                agent\.isStopped = false;__

__                agent\.speed = 2f;__

__                agent\.SetDestination\(player\.transform\.position\);__

__                if \(distanceToPlayer <= attackDistance\)__

__                \{__

__                    agent\.isStopped = true;__

__                    if \(\!isAttacking && \!isHit && Time\.time >= lastAttackTime \+ attackCooldown\)__

__                    \{__

__                        lastAttackTime = Time\.time;__

__                        int enemyAction = Random\.Range\(1, 10\);__

__                        if \(enemyAction == 1\)__

__                        \{__

__                            anim\.SetTrigger\("Attack1"\);__

__                        \}__

__                        else if \(enemyAction == 2\)__

__                        \{__

__                            anim\.SetTrigger\("Attack2"\);__

__                        \}__

__                        else__

__                        \{__

__                            lastAttackTime \+= 2f;__

__                        \}__

__                    \}__

__                \}__

__            \}__

__        \}        __

__    \}__

    __public void Die\(\)__

__    \{        __

__        isDead = true;__

__        anim\.SetTrigger\("Death"\);__

__        agent\.isStopped = true;__

__    \}__

    __public void HitDamage\(float damage\)__

__    \{        __

__        health \-= damage;__

__        if \(health <= 0f\)__

__        \{__

__            state = NPCState\.Dead;__

__            player\.GetComponent<Player>\(\)\.enemyGroup\.Remove\(gameObject\);__

__            player\.GetComponent<Player>\(\)\.SetEnemyFocus\(\);__

__            return;__

__        \}__

__        else__

__        \{__

__            isHit = true;__

__            anim\.SetTrigger\("Hit"\);__

__        \}__

__    \}__

    __public void BeginAttack\(\)__

__    \{__

__        isAttacking = true;__

__    \}__

__    public void EndAttack\(\)__

__    \{__

__        isAttacking = false;__

__    \}__

__    public void EndHit\(\)__

__    \{__

__        isHit = false;__

__    \}__

__    public void EndDeath\(\)__

__    \{__

__        Destroy\(gameObject, 5f\);__

__    \}__

\}

Assim como fizemos para o Player, vamos adicionar eventos em pontos específicos das animações: __BeginAttack,__ __EndAttack, EndHit__ e __EndDeath:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600435023900.png)__

Ao final, lembre\-se de atualizar as referências de objeto nos scripts__ NPC __e __EnemyBody\.__

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Sem tarefa\.

