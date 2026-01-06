# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600049537600.png)

# __PLANO DE AULA__

Aula 07 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Combate

Objetivos

- Configurar sistema de combate do Player\.

Estratégias e atividades

Para dar continuidade ao sistema de ataque que iniciamos na aula anterior, precisamos fazer alterações no script do Player para integrar as mecânicas de combate com o sistema de movimento já implementado\. Vamos adicionar a lógica de detecção de inimigos, controle de foco de alvo e a execução dos ataques\.

__START__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600049537600.png)

Altere o script do __Player__:

using System;

using System\.Collections;

using System\.Collections\.Generic;

using System\.ComponentModel\.Design;

using System\.Threading;

using Cinemachine;

using JetBrains\.Annotations;

using TMPro;

using Unity\.VisualScripting;

using UnityEngine;

using UnityEngine\.Animations\.Rigging;

using UnityEngine\.EventSystems;

using UnityEngine\.InputSystem;

using UnityEngine\.TextCore\.Text;

using UnityEngine\.UI;

using static Cinemachine\.CinemachineFreeLook;

using static NPC;

public class Player : MonoBehaviour

\{

__    public enum PlayerState__

__    \{__

__        Passive,__

__        Agressive,__

__        Dead__

__    \}__

   __ \[Header\("Player Status"\)\]__

__    public PlayerState state;__

__    public float health;__

__    public bool isHit;__

__    public bool isDead;__

    \[Header\("Movement"\)\]

    public float playerSpeed;

    public float playerSprint;

    public float currentSpeed;

    public float smoothSpeed;

    public float jumpRange;

    Vector3 velocity;

    \[Header\("Animation"\)\]

    public CharacterController playerController;

    public RuntimeAnimatorController animController;

__    public RuntimeAnimatorController combatController;__

    public Animator anim;

__    \[Header\("Combat"\)\]__

__    public List<GameObject> enemyGroup;__

__    public GameObject enemyFocus;__

__    public bool isAttacking;__

__    public float timeAttack;__

__    public int attackCount;    __

__    public float damage;__

    \[Header\("Camera"\)\]

    public Transform camTransform;

    public Transform headTransform;

    public Transform targetTransform;

    public LayerMask targetMask;

    public CinemachineFreeLook freeLookCam;

    __public CinemachineFreeLook combatCam; __   

    public float turnSmoothTime;

    float turnSmoothVelocity;

    \[Header\("Gravity"\)\]

    public Transform surfaceCheck;

    public LayerMask surfaceMask;

    public float surfaceDistance;

    public float gravity;

    public bool onSurface;

    \[Header\("Input"\)\]

    public Controls controls;

    private void Awake\(\)

    \{

        UnityEngine\.Cursor\.visible = false;

        UnityEngine\.Cursor\.lockState = CursorLockMode\.Locked;

        controls = new Controls\(\);

        controls\.Enable\(\);        

    \}

    void Start\(\)

    \{

        playerSpeed = 2f;

        playerSprint = 5f;

        smoothSpeed = 10f;

        currentSpeed = 0f;

        __isAttacking = false;__

        isDead = false;

       __ timeAttack = 1f;__

        __attackCount = 0;__

        __damage = 20f;__

        jumpRange = 0\.5f;

        turnSmoothTime = 0\.1f;

        surfaceDistance = 0\.4f;

        __enemyFocus = null;__

        gravity = \-9\.8f;

    \}

__    void FixedUpdate\(\)__

__    \{__

__        if \(\!isDead\)__

__        \{__

            Gravity\(\);

            

__            if\(controls\.Player\.ChangeState\.triggered\)__

__            \{__

__                AlternateState\(\);__

__            \}__

__            switch \(state\)__

__            \{__

__                case PlayerState\.Passive:__

__                    isAttacking = false;__

__                    isHit = false;__

__                    anim\.runtimeAnimatorController = animController;__

__                    combatCam\.Priority = 8;   __                 

                    Move\(\);

__                    break;__

__                case PlayerState\.Agressive:__

__                    anim\.runtimeAnimatorController = combatController;__

__                    combatCam\.Priority = 11;    __                

                    Move\(\);

                    __Combat\(\);__

                   __ break;__

__                case PlayerState\.Dead:__

__                    Die\(\);__

__                    break;__

__            \}__

__        \}__

__        else__

__        \{__

__            anim\.SetBool\("isDead", true\);__

__            combatCam\.gameObject\.SetActive\(false\);__

__            freeLookCam\.gameObject\.SetActive\(true\);__

__        \}__

__    \}__

    private void Gravity\(\)

    \{

        onSurface = Physics\.CheckSphere\(surfaceCheck\.position, surfaceDistance, surfaceMask\);

        if \(onSurface && velocity\.y < 0\)

        \{

            velocity\.y = \-2f;

        \}

        velocity\.y \+= gravity \* Time\.deltaTime;

        playerController\.Move\(playerSpeed \* Time\.deltaTime \* velocity\.normalized\);

        anim\.SetBool\("OnSurface", onSurface\);

    \}

    __public void AlternateState\(\)__

__\{__

__        if \(\!isAttacking && \!isHit\)__

__        \{__

__            if \(state == PlayerState\.Passive && enemyGroup\.Count > 0\)__

__            \{__

__                state = PlayerState\.Agressive;__

__                SetEnemyFocus\(\);__

__            \}__

__            else if \(state == PlayerState\.Agressive\)__

__            \{__

__                state = PlayerState\.Passive;__

__            \}__

__        \}__

__    \}__

    private void Move\(\)

    \{

        float inputX = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.x;

        float inputZ = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.y;

        float moveSpeed;

        Vector3 direction = new Vector3\(inputX, 0, inputZ\)\.normalized;

        float targetAngle = Mathf\.Atan2\(direction\.x, direction\.z\) \* Mathf\.Rad2Deg \+ camTransform\.eulerAngles\.y;

        float angle = Mathf\.SmoothDampAngle\(transform\.eulerAngles\.y, targetAngle, ref turnSmoothVelocity, turnSmoothTime\);

        moveSpeed = \(controls\.Player\.Sprint\.IsPressed\(\) ? playerSprint : playerSpeed\);

        transform\.rotation = Quaternion\.Euler\(0, angle, 0\);

        Vector3 moveDirection = Quaternion\.Euler\(0, targetAngle, 0\) \* Vector3\.forward;

        if \(direction\.magnitude >= 0\.1f\)

        \{

            playerController\.Move\(moveSpeed \* Time\.deltaTime \* moveDirection\.normalized\);

            currentSpeed = Mathf\.Lerp\(currentSpeed, moveSpeed, smoothSpeed \* Time\.deltaTime\);

        \}

        else

        \{

            currentSpeed = Mathf\.Lerp\(currentSpeed, 0, smoothSpeed \* Time\.deltaTime\);

        \}

        anim\.SetFloat\("Speed", currentSpeed\);

    \}

__    public void Combat\(\)__

__\{__

__        if \(enemyFocus \!= null\)__

__        \{__

__            Vector3 target = new Vector3\(enemyFocus\.transform\.position\.x, transform\.position\.y, enemyFocus\.transform\.position\.z\);__

__            if \(enemyGroup\.Count > 0\)__

__            \{__

__                if \(enemyFocus\.GetComponent<NPC>\(\)\.isAgressive\)__

__                \{__

__                    transform\.LookAt\(target\);__

__                \}__

__            \}__

__            else__

__            \{__

__                Invoke\("AlternateState", 2f\);__

__            \}__

__        \}__

__        if \(controls\.Player\.Attack\.triggered && \!isHit\)__

__        \{__

__            isAttacking = true;__

__            anim\.SetTrigger\("Attack"\);__

__        \}__

__    \}__

   __ public void SetEnemyFocus\(\)__

__    \{__

__        foreach \(GameObject enemy in enemyGroup\)__

__        \{__

__            if \(enemy\.GetComponent<NPC>\(\)\.isDead\)__

__            \{__

__                enemyGroup\.Remove\(enemy\);__

__            \}__

__            else if \(enemyFocus == null\)__

__            \{__

__                enemyFocus = enemy;__

__            \}__

__            if \(enemyGroup\.Count > 0\)__

__            \{__

__                if \(Vector3\.Distance\(transform\.position, enemy\.transform\.position\) < Vector3\.Distance\(transform\.position, enemyFocus\.transform\.position\)\)__

__                \{__

__                    enemyFocus = enemy;__

__                \}__

__            \}__

__        \}__

__    \}__

__    public void HitDamage\(float damage\)__

__    \{__

__        health \-= damage;__

__        if \(health <= 0f\)__

__        \{__

__            state = PlayerState\.Dead;__

__            return;__

__        \}__

__        else__

__        \{__

__            isHit = true;__

__            anim\.SetTrigger\("Hit"\);__

__        \}__

__    \}__

__    private void OnTriggerEnter\(Collider other\)__

__    \{__

__        if \(other\.CompareTag\("Enemy"\)\)__

__        \{__

__            NPC enemyNPC = other\.gameObject\.GetComponentInParent<NPC>\(\);__

__            if \(enemyNPC && \!enemyNPC\.isDead\)__

__            \{__

__                if \(\!enemyGroup\.contains\(enemyNPC\.gameObject\)\)__

__                \{__

__                    enemyGroup\.add\(enemyNPC\.gameObject\);__

__                \}__

__            \}__

__        \}__

__    \}__

__    public void BeginAttack1\(\) // Método para iniciar ataque 1__

__    \{__

__        isAttacking = true;__

__        audioSource\.loop = false;__

__        audioSource\.clip = audioAttack1;__

__        audioSource\.Play\(\);__

__    \}__

    __public void BeginAttack2\(\)__

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

__    public void Die\(\)__

__    \{__

__        isDead = true;__

__        anim\.SetTrigger\("Death"\);__

__        Time\.timeScale = Mathf\.Lerp\(Time\.timeScale, 0\.5f, 3f\);__

__    \}__

\}

Para finalizar, adicionaremos __eventos em pontos específicos das animações__ que irão disparar as funções __BeginAttack1__ e __BeginAttack2__ \(Início dos ataques\), __EndAttack __\(Fim dos ataques\) e __EndHit__ \(Fim do Dano\)__ __no Script do Player\. 

Para criá\-los,__ selecione__ a animação e no Inspector, vá até __Animation\. __Altere o ponto específico de acordo com a animação de ataque ou hit escolhida:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600084678000.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708600084678000.png)

Lembre\-se de fazer o mesmo processo para todos os eventos:__ BeginAttack1__, __BeginAttack2__, __EndAttack, EndHit__\.

Por fim, atualize as referências de objetos e componentes nos scripts __Player__ e __PlayerBody__, no Inspector\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

