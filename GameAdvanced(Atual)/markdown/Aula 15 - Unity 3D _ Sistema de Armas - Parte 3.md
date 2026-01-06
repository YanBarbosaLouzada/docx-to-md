# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601271429300.png)

# __PLANO DE AULA__

Aula 15 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Armas \- Parte 3

Objetivos

- Implementar o sistema de armas\.\.

Estratégias e atividades

Para dar continuidade ao sistema de armas que iniciamos nas aulas anteriores, vamos agora implementar a integração completa no script do Player\. Nesta terceira parte, vamos adicionar a mecânica de troca de armas, o sistema de mira \(aim\) e a lógica de disparo, fazendo com que todas as funcionalidades de armamento desenvolvidas até aqui funcionem de forma integrada com o movimento e combate do personagem\.

__START__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601289821300.png)

Vamos alterar o script do player:

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

    public enum PlayerState

    \{

        Passive,

        Agressive,

__        Equipped,__

        Dead

    \}

__    public enum CurrentWeapon__

__    \{__

__        Hand,__

__        Assault,__

__    \}__

    \[Header\("Player Status"\)\]

    public PlayerState state;

    public float health;

    public bool isHit;

    public bool isDead;

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

    public RuntimeAnimatorController combatController;

__    public RuntimeAnimatorController equippedController;__

    public Animator anim;

    \[Header\("Combat"\)\]

    public List<GameObject> enemyGroup;

    public GameObject enemyFocus;

    public bool isAttacking;

    public float timeAttack;

    public int attackCount;    

    public float damage;

__    \[Header\("Equipped"\)\]__

__    public bool playerAim;__

__    public Rig aimRig;__

__    public float rigWeight;__

__    \[Header\("Weapon"\)\]__

__    public GameObject changeWeaponPanel;__

__    public bool changeWeapon;__

__    public Weapons weapons;__

__    public CurrentWeapon currentWeapon;__

__    public Transform weaponSlot;__

    \[Header\("Camera"\)\]

    public Transform camTransform;

    public Transform headTransform;

__    public Transform targetTransform;__

__    public LayerMask targetMask;__

    public CinemachineFreeLook freeLookCam;

    public CinemachineFreeLook combatCam;

__    public Cinemachine3rdPersonAim aimCam; __   

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

        isAttacking = false;

        isDead = false;

        timeAttack = 1f;

        attackCount = 0;

        damage = 20f;

        jumpRange = 0\.5f;

__        playerAim = false;__

__        rigWeight = 0f;__

        turnSmoothTime = 0\.1f;

        surfaceDistance = 0\.4f;

        enemyFocus = null;

        gravity = \-9\.8f;

__        weapons = GetComponent<Weapons>\(\);__

    \}

    void FixedUpdate\(\)

    \{

        if \(\!isDead\)

        \{

            Gravity\(\);

            

            if\(controls\.Player\.ChangeState\.triggered\)

            \{

                AlternateState\(\);

            \}

__            if \(controls\.Equipped\.ChangeWeapon\.IsPressed\(\)\)__

__            \{__

__                changeWeapon = true;__

__                changeWeaponPanel\.SetActive\(true\);__

__                Time\.timeScale = 0\.1f;__

__                float inputX = controls\.Player\.Camera\.ReadValue<Vector2>\(\)\.x;__

__                float inputY = controls\.Player\.Camera\.ReadValue<Vector2>\(\)\.y;__

__                weapons\.SetActiveSlot\(inputX, inputY\);__

__                if\(weapons\.currentWeapon \!= Weapon\.weaponName\.Hand\)__

__                \{__

__                    state = PlayerState\.Equipped;__

__                \}__

__                else__

__                \{__

__                    state = PlayerState\.Passive;__

__                \}__

__                freeLookCam\.m\_XAxis\.m\_MaxSpeed = 0f;__

__                freeLookCam\.m\_YAxis\.m\_MaxSpeed = 0f;__

__            \}__

__            else__

__            \{__

__                changeWeapon = false;__

__                changeWeaponPanel\.SetActive\(false\);__

__                Time\.timeScale = 1f;__

__                freeLookCam\.m\_XAxis\.m\_MaxSpeed = 300f;__

__                freeLookCam\.m\_YAxis\.m\_MaxSpeed = 2f;__

__            \}__

            switch \(state\)

            \{

                case PlayerState\.Passive:

                    isAttacking = false;

                    isHit = false;

                    anim\.runtimeAnimatorController = animController;

                    combatCam\.Priority = 8;                    

                    Move\(\);

                    Jump\(\);

                    break;

                case PlayerState\.Agressive:

                    anim\.runtimeAnimatorController = combatController;

                    combatCam\.Priority = 11;                    

                    Move\(\);

                    Combat\(\);

                    break;

__                case PlayerState\.Equipped:__

__                    anim\.runtimeAnimatorController = equippedController;__

__                    Move\(\);__

__                    Equipped\(\);__

__                    break;__

                case PlayerState\.Dead:

                    Die\(\);

                    break;

            \}

        \}

        else

        \{

            anim\.SetBool\("isDead", true\);

            combatCam\.gameObject\.SetActive\(false\);

            freeLookCam\.gameObject\.SetActive\(true\);

        \}

    \}

__    public void Equipped\(\)__

__    \{__

__        float maxDistance = 100f;__

__        RaycastHit hit;__

__        aimRig\.weight = Mathf\.Lerp\(aimRig\.weight, rigWeight, turnSmoothTime\);__

__        if \(Physics\.Raycast\(camTransform\.position,camTransform\.forward, out hit, maxDistance, targetMask\)\)__

__        \{__

__            targetTransform\.position = hit\.point;__

__        \}__

__        else__

__        \{__

__            targetTransform\.position = camTransform\.position \+ camTransform\.forward \* maxDistance;__

__        \}__

__        if \(controls\.Equipped\.Aim\.ReadValue<float>\(\) > 0\)__

__        \{__

__            freeLookCam\.Priority = 8;__

__            freeLookCam\.transform\.rotation = Quaternion\.LookRotation\(transform\.forward\);__

__            playerAim = true;__

__            rigWeight = 1f;__

__            anim\.SetBool\("Aim", true\);           __

__        \}__

__        else__

__        \{__

__            freeLookCam\.Priority = 10;            __

__            if \(playerAim\)__

__            \{__

__                freeLookCam\.transform\.rotation = Quaternion\.LookRotation\(transform\.forward\);__

__            \}__

__            playerAim = false;         __

__        __

__            rigWeight = 0f;__

__            anim\.SetBool\("Aim", false\);__

__        \}__

__        if\(playerAim && controls\.Equipped\.Shoot\.ReadValue<float>\(\) > 0\)__

__        \{__

__            weapons\.Shoot\(hit\);          __

__        \}__

__    \}__

    private void Gravity\(\)

    \{

        //Checagem do Player em uma Superfície

        onSurface = Physics\.CheckSphere\(surfaceCheck\.position, surfaceDistance, surfaceMask\);

        if \(onSurface && velocity\.y < 0\)

        \{

            velocity\.y = \-2f;

        \}

        //Gravidade

        velocity\.y \+= gravity \* Time\.deltaTime;

        playerController\.Move\(playerSpeed \* Time\.deltaTime \* velocity\.normalized\);

        anim\.SetBool\("OnSurface", onSurface\);

    \}

    public void AlternateState\(\)

    \{

        if \(\!isAttacking && \!isHit\)

        \{

            if \(state == PlayerState\.Passive && enemyGroup\.Count > 0\)

            \{

                state = PlayerState\.Agressive;

                SetEnemyFocus\(\);

            \}

            else if \(state == PlayerState\.Agressive\)

            \{

                state = PlayerState\.Passive;

            \}

        \}

    \}

    private void Move\(\)

    \{

        float inputX = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.x;

        float inputZ = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.y;

        float moveSpeed;

        Vector3 direction = new Vector3\(inputX, 0, inputZ\)\.normalized;

        float targetAngle = Mathf\.Atan2\(direction\.x, direction\.z\) \* Mathf\.Rad2Deg \+ camTransform\.eulerAngles\.y;

        float angle = Mathf\.SmoothDampAngle\(transform\.eulerAngles\.y, targetAngle, ref turnSmoothVelocity, turnSmoothTime\);

__       if \(state == PlayerState\.Equipped && playerAim\)__

__\{__

__    Vector2 inputY = controls\.Player\.Camera\.ReadValue<Vector2>\(\);__

__    float newRotationX = headTransform\.localEulerAngles\.x \- inputY\.y;__

__    if \(newRotationX > 180\)__

__        newRotationX \-= 360;__

__    newRotationX = Mathf\.Clamp\(newRotationX, \-80f, 80f\);__

__    transform\.eulerAngles \+= new Vector3\(0f, inputY\.x, 0f\);__

__    headTransform\.localEulerAngles = new Vector3\(newRotationX, headTransform\.localEulerAngles\.y, headTransform\.localEulerAngles\.z\);__

__\}__

__else__

__\{__

__    headTransform\.localEulerAngles = new Vector3\(Mathf\.Lerp\(headTransform\.localEulerAngles\.x, 0f, smoothSpeed\), headTransform\.localEulerAngles\.y, headTransform\.localEulerAngles\.z\);__

__    transform\.rotation = direction\.magnitude >= 0\.1f ? Quaternion\.Euler\(0f, angle, 0f\) : transform\.rotation;__

__\}__

__        if \(direction\.magnitude >= 0\.1f && onSurface && \!isAttacking && \!isHit\)__

__        \{__

__            Vector3 moveDirection = Quaternion\.Euler\(0f, targetAngle, 0f\) \* Vector3\.forward;__

__            float targetSpeed = controls\.Player\.Run\.IsPressed\(\) && \!playerAim ? playerSprint : playerSpeed;__

__            currentSpeed = Mathf\.Lerp\(currentSpeed, targetSpeed, Time\.deltaTime \* smoothSpeed\);__

__            playerController\.Move\(currentSpeed \* Time\.deltaTime \* moveDirection\.normalized\);__

__            jumpRange = 0f;__

__        \}__

__        else if\(direction\.magnitude < 0\.1f\)__

__        \{__

__            currentSpeed = Mathf\.Lerp\(currentSpeed, 0f, Time\.deltaTime \* smoothSpeed\);__

__            jumpRange = 0\.5f;__

__        \}__

__        if \(state == PlayerState\.Agressive || playerAim\)__

__        \{__

__            anim\.SetFloat\("inputX", direction\.x\);__

__            anim\.SetFloat\("inputZ", direction\.z\);__

__        \}__

__        moveSpeed = new Vector3\(playerController\.velocity\.x, 0f, playerController\.velocity\.z\)\.magnitude;__

__        anim\.SetFloat\("Velocity", moveSpeed\);__

__    \}__

    public void SetEnemyFocus\(\)

    \{

        foreach \(GameObject enemy in enemyGroup\)

        \{

            if \(enemy\.GetComponent<NPC>\(\)\.isDead\)

            \{

                enemyGroup\.Remove\(enemy\);

            \}

            else if \(enemyFocus == null\)

            \{

                enemyFocus = enemy;

            \}

            if \(enemyGroup\.Count > 0\)

            \{

                if \(Vector3\.Distance\(transform\.position, enemy\.transform\.position\) < Vector3\.Distance\(transform\.position, enemyFocus\.transform\.position\)\)

                \{

                    enemyFocus = enemy;

                \}

            \}

        \}

    \}

    public void Combat\(\)

    \{

        if \(enemyFocus \!= null\)

        \{

            Vector3 target = new\(enemyFocus\.transform\.position\.x, transform\.position\.y, enemyFocus\.transform\.position\.z\);

            if \(enemyGroup\.Count > 0\)

            \{                

                if \(enemyFocus\.GetComponent<NPC>\(\)\.isAgressive\)

                \{

                    transform\.LookAt\(target\);

                \}               

            \}

            else

            \{

                Invoke\("AlternateState", 2f\); 

            \}

        \}

        if \(controls\.Player\.Attack\.triggered && \!isHit\)

        \{

            isAttacking = true;

            anim\.SetTrigger\("Attack"\);

        \}

    \}

    public void HitDamage\(float damage\)

    \{

        health \-= damage;

        if \(health <= 0f\)

        \{

            state = PlayerState\.Dead;

            return;

        \}

        else

        \{

            isHit = true;

            anim\.SetTrigger\("Hit"\);

        \}

    \}

    private void OnTriggerEnter\(Collider other\)

    \{

        if \(other\.CompareTag\("Enemy"\)\)

        \{

            NPC enemyNPC = other\.gameObject\.GetComponentInParent<NPC>\(\);

            if \(enemyNPC && \!enemyNPC\.isDead\)

            \{

                if \(\!enemyGroup\.Contains\(enemyNPC\.gameObject\)\)

                \{

                    enemyGroup\.Add\(enemyNPC\.gameObject\);

                \}

            \}

        \}

    \}

    public void BeginAttack1\(\)

    \{

        isAttacking = true;

    \}

    public void BeginAttack2\(\)

    \{

        isAttacking = true;

    \}

    public void EndAttack\(\)

    \{

        isAttacking = false;

    \}

    public void EndHit\(\)

    \{

        isHit = false;

    \}

    public void Die\(\)

    \{

        isDead = true;

        anim\.SetTrigger\("Death"\);

        Time\.timeScale = Mathf\.Lerp\(Time\.timeScale, 0\.5f, 3f\);

    \}

\}

Finalizamos o sistema básico de armas\. A partir de agora, uma nova arma pode ser criada na classe Weapons e basta adicionar seu modelo 3D e icones correspondentes\.

Lembre\-se de atualizar as referências nos scripts __Player__ e __Weapons__\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Escolha três jogos 3D populares que possuem sistemas de armas bem implementados \(por exemplo, "Call of Duty", "Fortnite", "Overwatch"\)\.
- Analisar e documentar as características das armas nesses jogos, incluindo tipos de armas, mecânicas de disparo, sistema de recarga, personalização e efeitos visuais/sonoros\.

