# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601638004200.png)

# __PLANO DE AULA__

Aula 17 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Veículos \- Parte 1

Objetivos

- Sistema de Veículos com Wheel Colliders\. 

Estratégias e atividades

Na aula de hoje, vamos criar nosso primeiro __veículo__ e configurá\-lo com __Wheel Colliders__ para que ele possa se movimentar e interagir com o terreno de forma realista:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601654158800.png)

Inicialmente, procure por um veículo na Unity Asset Store\. Escolha um veículo que tenha partes separadas, em especial suas rodas:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601659346300.png)

No script, iremos tratar as partes do carro de forma diferente\. As rodas devem girar de forma independente do resto do veículo\. Então, vamos unir todas as partes que consideramos fazer parte das rodas\. Neste exemplo, o __aro \(rim\)__ ficará dentro do __pneu \(tire\)__, assim quando o pneu girar, ele também gira:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601659346300.png)

Faça isso para todas as rodas, frontais e traseiras:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601671337300.png)

No exemplo deste veículo, temos também o __disco \(disk\)__ e __pinça \(caliper\)__ de freio\. Estes irão __girar no eixo Y__, quando o jogador vira o volante, mas não giram junto com a roda ao acelerar\. Então, deixaremos separados da roda:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601671337300.png)

Agora vamos criar quatro objetos vazios para os colisores\. Toda a física de movimento do veículo será aplicada nestes colisores e em outro maior que incluiremos mais tarde no corpo do veículo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601671337300.png)

Com os quatro objetos selecionados, adicione o componente __Wheel Collider__ e configure da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601671337300.png)

Agora posicione cada colisor de acordo com a posição da roda:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601671337300.png)

Lembre\-se de posicionar cada colisor em sua respectiva posição:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601685045100.png)

Selecione o objeto do carro e adicione o componente__ Rigidbody__ com a seguinte configuração:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601687972200.png)

Vamos adicionar também um__ Sphere Collider__ com a opção __isTrigger__ ativa, que será responsável por detectar quando o player está próximo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601687972200.png)

Com o carro configurado, ainda precisamos adicionar um objeto vazio dentro dele, que será responsável pela __posição do personagem__ dentro dele\. Quando fizermos o teste com o personagem sentado no banco, ajuste a posição até que ele se encaixe corretamente:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601695278400.png)

Por último, vamos adicionar um __Mesh Collider__ ao objeto body, que representa o __chassi__ ou __corpo__ do carro\. Este será responsável pelo peso e centro de massa do carro e, portanto, será muito importante para a física do veículo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601695278400.png)

Observe que a opção __convex__ foi ativada no colisor\. Isso garante que o colisor tenha uma forma mais geométrica, facilitando a detecção de colisões de maneira eficiente\.

Nosso carro agora está pronto para ser programado, mas ainda precisamos criar os controles de direção\. Portanto, vamos para o Input Actions__ Controls__ para atualizá\-lo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601704684300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601704684300.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601704684300.png)

Vamos fazer alterações nos scripts __Player__ e __PlayerBody__ para que o Player detecte carros ao redor e o carro que está mais próximo:

Script do Player:

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

using UnityEngine\.InputSystem\.XR;

using UnityEngine\.TextCore\.Text;

using UnityEngine\.UI;

using static Cinemachine\.CinemachineFreeLook;

using static NPC;

using static Player;

public class Player : MonoBehaviour

\{

    public enum PlayerState

    \{

        Passive,

        Agressive,

        Equipped,

        Driving,

        Dead

    \}

    public enum CurrentWeapon

    \{

        Hand,

        Pistol,

        Assault,

        Sub,

        Grenade,

        Explosive,

        Sniper,

        Knife

    \}

    \[Header\("Player Status"\)\]

    public PlayerState state;

    public Collider playerCollider;

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

    public RuntimeAnimatorController equippedController;

    public RuntimeAnimatorController drivingController;

    public Animator anim;

__    \[Header\("Drive"\)\]__

__    public bool isDriving;__

__    public float enterDistance = 3\.0f;__

__    public Transform playerSeat;__

__    private GameObject currentCar;__

__    public GameObject nearestCar;__

    \[Header\("Combat"\)\]

    public List<GameObject> enemyGroup;

    public GameObject enemyFocus;

    public bool isAttacking;

    public float timeAttack;

    public int attackCount;    

    public float damage;

    \[Header\("Equipped"\)\]

    public bool playerAim;

    public Rig aimRig;

    public float rigWeight;

    \[Header\("Weapon"\)\]

    public GameObject changeWeaponPanel;

    public bool changeWeapon;

    public Weapons weapons;

    public CurrentWeapon currentWeapon;

    public Transform weaponSlot;

    \[Header\("Camera"\)\]

    public Transform camTransform;

    public Transform headTransform;

    public Transform targetTransform;

    public LayerMask targetMask;

    public CinemachineFreeLook freeLookCam;

    public CinemachineFreeLook combatCam;

    public Cinemachine3rdPersonAim aimCam;    

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

__        isDriving = false;__

        isAttacking = false;

        isDead = false;

        timeAttack = 1f;

        attackCount = 0;

        damage = 20f;

        jumpRange = 0\.5f;

        playerAim = false;

        rigWeight = 0f;

        turnSmoothTime = 0\.1f;

        surfaceDistance = 0\.4f;

        enemyFocus = null;

        gravity = \-9\.8f;

        weapons = GetComponent<Weapons>\(\);

    \}

    void FixedUpdate\(\)

    \{

        if \(\!isDead\)

        \{

__            if \(controls\.Player\.Drive\.triggered\)__

__            \{__

__                if \(\!isDriving\)__

__                \{__

__                    EnterCar\(\);__

__                \}__

__                else__

__                \{__

__                    ExitCar\(\);__

__                \}                __

__            \}__

            if \(controls\.Player\.ChangeState\.triggered__ && \!isDriving__\)

            \{

                AlternateState\(\);

            \}

            if \(controls\.Equipped\.ChangeWeapon\.IsPressed\(\)__ && \!isDriving__\)

            \{

                changeWeapon = true;

                changeWeaponPanel\.SetActive\(true\);

                Time\.timeScale = 0\.1f;

                float inputX = controls\.Player\.Camera\.ReadValue<Vector2>\(\)\.x;

                float inputY = controls\.Player\.Camera\.ReadValue<Vector2>\(\)\.y;

                weapons\.SetActiveSlot\(inputX, inputY\);

                if\(weapons\.currentWeapon \!= Weapon\.weaponName\.Hand\)

                \{

                    state = PlayerState\.Equipped;

                \}

                else

                \{

                    state = PlayerState\.Passive;

                \}

                freeLookCam\.m\_XAxis\.m\_MaxSpeed = 0f;

                freeLookCam\.m\_YAxis\.m\_MaxSpeed = 0f;

            \}

            else

            \{

                changeWeapon = false;

                changeWeaponPanel\.SetActive\(false\);

                Time\.timeScale = 1f;

                freeLookCam\.m\_XAxis\.m\_MaxSpeed = 300f;

                freeLookCam\.m\_YAxis\.m\_MaxSpeed = 2f;

            \}

            switch \(state\)

            \{

                case PlayerState\.Passive:

                    isAttacking = false;

                    isHit = false;

                    anim\.runtimeAnimatorController = animController;

                    combatCam\.Priority = 8;

                    Gravity\(\);

                    Move\(\);

                    Jump\(\);

                    break;

                case PlayerState\.Agressive:

                    anim\.runtimeAnimatorController = combatController;

                    combatCam\.Priority = 11;

                    Gravity\(\);

                    Move\(\);

                    Combat\(\);

                    break;

                case PlayerState\.Equipped:

                    anim\.runtimeAnimatorController = equippedController;

                    Gravity\(\);

                    Move\(\);

                    Equipped\(\);

                    break;

__                case PlayerState\.Driving:__

__                    anim\.runtimeAnimatorController = drivingController;__

__                    break;__

                case PlayerState\.Dead:

                    Gravity\(\);

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

__    void EnterCar\(\)__

__    \{__

__        if \(nearestCar \!= null\)__

__        \{__

__            float distance = Vector3\.Distance\(transform\.position, nearestCar\.transform\.position\);__

__            if \(distance <= enterDistance\)__

__            \{__

__                StartCoroutine\(EnterCarCoroutine\(\)\);__

__            \}__

__        \}__

__    \}__

__    IEnumerator EnterCarCoroutine\(\)__

__    \{__

__        yield return new WaitForSeconds\(0\.5f\);__

__        currentCar = nearestCar;__

__        isDriving = true;__

__        state = PlayerState\.Driving;__

__        playerController\.enabled = false;__

__        playerCollider\.enabled = false;__

__        transform\.SetParent\(playerSeat\);__

__        transform\.localPosition = Vector3\.zero;__

__        transform\.localRotation = Quaternion\.identity;__

__        currentCar\.GetComponent<CarController>\(\)\.enabled = true;__

__    \}__

__    void ExitCar\(\)__

__    \{__

__        if \(currentCar \!= null\)__

__        \{__

__            StartCoroutine\(ExitCarCoroutine\(\)\);__

__        \}__

__    \}__

__    IEnumerator ExitCarCoroutine\(\)__

__    \{__

__        yield return new WaitForSeconds\(0\.5f\);__

__        state = PlayerState\.Passive;__

__        currentCar\.GetComponent<CarController>\(\)\.enabled = false;__

__        transform\.SetParent\(null\);__

__        transform\.position = currentCar\.transform\.position \+ currentCar\.transform\.right \* \-2;__

__        playerController\.enabled = true;__

__        playerCollider\.enabled = true;        __

__        currentCar = null;__

__        isDriving = false;__

__        nearestCar = null;__

__    \}__

    public void Equipped\(\)

    \{

        float maxDistance = 100f;

        RaycastHit hit;

        aimRig\.weight = Mathf\.Lerp\(aimRig\.weight, rigWeight, turnSmoothTime\);

        if \(Physics\.Raycast\(camTransform\.position,camTransform\.forward, out hit, maxDistance, targetMask\)\)

        \{

            targetTransform\.position = hit\.point;

        \}

        else

        \{

            targetTransform\.position = camTransform\.position \+ camTransform\.forward \* maxDistance;

        \}

        if \(controls\.Equipped\.Aim\.ReadValue<float>\(\) > 0\)

        \{

            freeLookCam\.Priority = 8;

            freeLookCam\.transform\.rotation = Quaternion\.LookRotation\(transform\.forward\);

            playerAim = true;

            rigWeight = 1f;

            anim\.SetBool\("Aim", true\);           

        \}

        else

        \{

            freeLookCam\.Priority = 10;            

            if \(playerAim\)

            \{

                freeLookCam\.transform\.rotation = Quaternion\.LookRotation\(transform\.forward\);

            \}

            playerAim = false;         

        

            rigWeight = 0f;

            anim\.SetBool\("Aim", false\);

        \}

        if\(playerAim && controls\.Equipped\.Shoot\.ReadValue<float>\(\) > 0\)

        \{

            weapons\.Shoot\(hit\);          

        \}

    \}

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

        if \(state == PlayerState\.Equipped && playerAim\)

        \{

            Vector2 inputY = controls\.Player\.Camera\.ReadValue<Vector2>\(\);

            float newRotationX = headTransform\.localEulerAngles\.x \- inputY\.y;

            if \(newRotationX > 180\)

                newRotationX \-= 360;

            newRotationX = Mathf\.Clamp\(newRotationX, \-80f, 80f\);

            transform\.eulerAngles \+= new Vector3\(0f, inputY\.x, 0f\);

            headTransform\.localEulerAngles = new Vector3\(newRotationX, headTransform\.localEulerAngles\.y, headTransform\.localEulerAngles\.z\);

        \}

        else

        \{

            headTransform\.localEulerAngles = new Vector3\(Mathf\.Lerp\(headTransform\.localEulerAngles\.x, 0f, smoothSpeed\), headTransform\.localEulerAngles\.y, headTransform\.localEulerAngles\.z\);

            transform\.rotation = direction\.magnitude >= 0\.1f ? Quaternion\.Euler\(0f, angle, 0f\) : transform\.rotation;

        \}

        if \(direction\.magnitude >= 0\.1f && onSurface && \!isAttacking && \!isHit\)

        \{

            Vector3 moveDirection = Quaternion\.Euler\(0f, targetAngle, 0f\) \* Vector3\.forward;

            float targetSpeed = controls\.Player\.Run\.IsPressed\(\) && \!playerAim ? playerSprint : playerSpeed;

            currentSpeed = Mathf\.Lerp\(currentSpeed, targetSpeed, Time\.deltaTime \* smoothSpeed\);

            playerController\.Move\(currentSpeed \* Time\.deltaTime \* moveDirection\.normalized\);

            jumpRange = 0f;

        \}

        else if\(direction\.magnitude < 0\.1f\)

        \{

            currentSpeed = Mathf\.Lerp\(currentSpeed, 0f, Time\.deltaTime \* smoothSpeed\);

            jumpRange = 0\.5f;

        \}

        if \(state == PlayerState\.Agressive || playerAim\)

        \{

            anim\.SetFloat\("inputX", direction\.x\);

            anim\.SetFloat\("inputZ", direction\.z\);

        \}

        moveSpeed = new Vector3\(playerController\.velocity\.x, 0f, playerController\.velocity\.z\)\.magnitude;

        anim\.SetFloat\("Velocity", moveSpeed\);

    \}

    public void Jump\(\)

    \{

        if \(onSurface\)

        \{

            if \(controls\.Player\.Jump\.triggered\)

            \{

                anim\.SetTrigger\("Jump"\);

                velocity\.y = Mathf\.Sqrt\(\(jumpRange\) \* \-2 \* gravity\);

            \}

            else

            \{

                anim\.ResetTrigger\("Jump"\);

            \}

        \}

    \}

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

        audioSource\.loop = false;

        audioSource\.clip = audioAttack1;

        audioSource\.Play\(\);

    \}

    public void BeginAttack2\(\)

    \{

        isAttacking = true;

        audioSource\.loop = false;

        audioSource\.clip = audioAttack2;

        audioSource\.Play\(\);

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

Finalizamos a implementação da mecânica de entrada no veículo\. Na próxima aula, avançaremos para a programação do funcionamento do veículo, onde exploraremos a aceleração, direção e a física\. Além disso, aprenderemos a utilizar uma ferramenta de criação de estradas sobre terrenos\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Dentre os diversos tipos de jogos que utilizam veículos, três exemplos se destacam: *Rocket League*, *Forza Motorsport* e *Mario Kart*\. Escolha um desses jogos e desenvolva uma análise sobre como você acredita que a mecânica dos veículos funciona nesse jogo\.

