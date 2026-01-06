# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602305082000.png)

# __PLANO DE AULA__

Aula 21 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- HUD \- Vida e Mapa

Objetivos

- Criar barra de vida e um mini mapa\.

Estratégias e atividades

Nosso projeto já está bem avançado, com personagens, inimigos, NPCs, e sistemas de armas e veículos implementados\. Agora, vamos focar nos últimos detalhes que irão complementar e refinar tudo o que construímos até aqui\.

__START__

Hoje, vamos criar elementos essenciais para a __HUD__, incluindo uma barra de vida e um mini mapa, que ajudarão na experiência do jogador\. HUD, que significa __Heads\-Up Display__, é a interface gráfica que exibe informações importantes para o jogador durante o jogo sem interromper a ação\. Ela geralmente inclui elementos como barras de vida, munição, mapas, pontuações, e outros indicadores de status que ajudam o jogador a tomar decisões enquanto joga\.

Primeiro, vamos incluir um mapa\. Para isso, crie nova câmera responsável por seguir o personagem de cima:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602305082000.png)

Renomeie a câmera para MapCamera e posicione\-a de modo a ficar acima do personagem, apontada para baixo \(Rotacione o eixo X em 90 graus\)\. Abaixo um exemplo de como a câmera pode ser configurada:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602310836300.png)

Para que a câmera apareça na HUD como uma miniatura, precisamos fazer algumas configurações:

- Crie uma __nova pasta__ chamada __Minimap__ e dentro dela, um novo objeto do tipo __Render Texture__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602315350900.png)

- Vamos renomeá\-lo para __Minimap Render:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602315350900.png)__

Uma __Render Texture__ é um tipo especial de textura que pode ser usada como alvo de renderização\. Assim, podemos exibir o conteúdo de uma outra câmera na HUD \(ou em qualquer parte do jogo, como um monitor\):

- Vá até a HUD no painel Hierarchy e crie um novo elemento de UI, do tipo __Raw Image__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602315350900.png)

- Renomeie para __Minimap__ e no campo __Texture__ de Raw Image, selecione a __Render Texture__ criada anteriormente:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602326848100.png)

Agora volte à__ MapCamera__ e iremos configurá\-la da seguinte forma:

- __Culling Mask \-> Surface: __Indicamos quais camadas de objetos serão visualizados na câmera\. Neste caso queremos que apenas a superfície \(Surface\) e terreno da cidade apareçam;
- __Projection \-> Orthographic: __Para que a câmera tenha a aparência de um mapa, não utilizaremos uma visão com distorções de perspectiva \(como as demais câmeras do jogo\)\. A perspectiva ortográfica irá manter os elementos achatados\.
- __Size \-> 44: __Ajuste da abertura da lente da câmera\. Precisamos de uma visão bem ampla para o mapa da cidade\. Ajuste conforme desejado\.
- __Clipping Planes > Far \-> 1000: __Estabelecemos uma distância máxima de objetos que a câmera pode renderizar;
- __Target Texture: __Indicamos que a Render Texture da nossa HUD será o alvo da câmera\. Assim, nosso minimapa está completo\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602333849200.png)

Posicione o mapa no canto inferior esquerdo ou direito da HUD\. Para finalizar, vamos adicionar um script ao MapCamera, para que o mapa siga a posição do player constantemente:

 ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602333849200.png)

Script do Minimapa:

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using UnityEngine;__

__public class MiniMap : MonoBehaviour__

__\{__

__    public GameObject player;__

__    void Update\(\)__

__    \{__

__        Vector3 mapPosition = new\(player\.transform\.position\.x, transform\.position\.y, player\.transform\.position\.z\);__

__        Quaternion mapRotation = Quaternion\.Euler\(90, player\.transform\.eulerAngles\.y, transform\.rotation\.z\);__

__        transform\.SetPositionAndRotation\(mapPosition, mapRotation\);__

__    \}__

__\}__

Nosso minimapa já está pronto e funcional, mas para __sinalizar__ o jogador, vamos incluir um__ ícone __no centro do mapa:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602333849200.png)

- Escolha um ícone de sua preferência para identificar a posição do jogador no mapa\. Os pacotes baixados anteriormente incluem vários ícones, mas fique a vontade para baixar novos:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602342488100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602345002200.png)

Com nosso mapa finalizado, agora podemos incluir uma __barra de vida__ para o personagem\. O player já tem um sistema de vida funcional, então o que precisamos fazer é criar e atualizar a barra de vida conforme o valor do HP do personagem:

- Dentro do minimapa, crie uma nova __image__ chamada __HP\_Bar__, vamos posicioná\-la na parte de cima e com a mesma largura do mapa:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602350517000.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602350517000.png)

- Altere a cor da barra de acordo com o tema do seu jogo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602358171500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602358171500.png)

Esta primeira será o fundo da barra\. Duplique\-a para criar a verdadeira barra de vida, que chamaremos de __HP__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602358171500.png)

- Para o funcionamento da barra, altere o tipo de imagem para __Filled__, com método __Horizontal__ e origem __Esquerda__, com a quantidade inicial __1:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602364916300.png)

Agora vamos fazer as alterações no script do Player para que a barra de vida seja atualizada constantemente\.

Script do Player:

__using System;__

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using System\.ComponentModel\.Design;__

__using System\.Threading;__

__using Cinemachine;__

__using JetBrains\.Annotations;__

__using TMPro;__

__using Unity\.VisualScripting;__

__using UnityEngine;__

__using UnityEngine\.Animations\.Rigging;__

__using UnityEngine\.EventSystems;__

__using UnityEngine\.InputSystem;__

__using UnityEngine\.InputSystem\.XR;__

__using UnityEngine\.TextCore\.Text;__

__using UnityEngine\.UI;__

__using static Cinemachine\.CinemachineFreeLook;__

__using static NPC;__

__using static Player;__

__public class Player : MonoBehaviour__

__\{__

__    public enum PlayerState__

__    \{__

__        Passive,__

__        Agressive,__

__        Equipped,__

__        Driving,__

__        Dead__

__    \}__

__    public enum CurrentWeapon__

__    \{__

__        Hand,__

__        Pistol,__

__        Assault,__

__        Sub,__

__        Grenade,__

__        Explosive,__

__        Sniper,__

__        Knife__

__    \}__

__    \[Header\("Player Status"\)\]__

__    public PlayerState state;__

__    public Collider playerCollider;__

__    public float health;__

__    public float maxHealth;__

__    public Image HPBar;__

__    public bool isHit;__

__    public bool isDead;__

__    \[Header\("Movement"\)\]__

__    public float playerSpeed;__

__    public float playerSprint;__

__    public float currentSpeed;__

__    public float smoothSpeed;__

__    public float jumpRange;__

__    Vector3 velocity;__

__    \[Header\("Animation"\)\]__

__    public CharacterController playerController;__

__    public RuntimeAnimatorController animController;__

__    public RuntimeAnimatorController combatController;__

__    public RuntimeAnimatorController equippedController;__

__    public RuntimeAnimatorController drivingController;__

__    public Animator anim;__

__    \[Header\("Audio"\)\]__

__    public AudioSource audioSource;__

__    public AudioClip audioAttack1;__

__    public AudioClip audioAttack2;__

__    \[Header\("Drive"\)\]__

__    public bool isDriving;__

__    public float enterDistance = 3\.0f;__

__    public Transform playerSeat;__

__    private GameObject currentCar;__

__    public GameObject nearestCar;__

__    \[Header\("Combat"\)\]__

__    public List<GameObject> enemyGroup;__

__    public GameObject enemyFocus;__

__    public bool isAttacking;__

__    public float timeAttack;__

__    public int attackCount;    __

__    public float damage;__

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

__    \[Header\("Camera"\)\]__

__    public Transform camTransform;__

__    public Transform headTransform;__

__    public Transform targetTransform;__

__    public LayerMask targetMask;__

__    public CinemachineFreeLook freeLookCam;__

__    public CinemachineFreeLook combatCam;__

__    public Cinemachine3rdPersonAim aimCam;    __

__    public float turnSmoothTime;__

__    float turnSmoothVelocity;__

__    \[Header\("Gravity"\)\]__

__    public Transform surfaceCheck;__

__    public LayerMask surfaceMask;__

__    public float surfaceDistance;__

__    public float gravity;__

__    public bool onSurface;__

__    \[Header\("Input"\)\]__

__    public Controls controls;__

__    private void Awake\(\)__

__    \{__

__        UnityEngine\.Cursor\.visible = false;__

__        UnityEngine\.Cursor\.lockState = CursorLockMode\.Locked;__

__        controls = new Controls\(\);__

__        controls\.Enable\(\);        __

__    \}__

__    void Start\(\)__

__    \{__

__        playerSpeed = 2f;__

__        playerSprint = 5f;__

__        smoothSpeed = 10f;__

__        currentSpeed = 0f;__

__        isDriving = false;__

__        isAttacking = false;__

__        isDead = false;__

__        timeAttack = 1f;__

__        attackCount = 0;__

__        damage = 20f;__

__        jumpRange = 0\.5f;__

__        playerAim = false;__

__        rigWeight = 0f;__

__        turnSmoothTime = 0\.1f;__

__        surfaceDistance = 0\.4f;__

__        enemyFocus = null;__

__        gravity = \-9\.8f;__

__        weapons = GetComponent<Weapons>\(\);__

__    \}__

__    void FixedUpdate\(\)__

__    \{__

__        if \(\!isDead\)__

__        \{__

__            UpdateHealth\(\);__

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

__            if \(controls\.Player\.ChangeState\.triggered && \!isDriving\)__

__            \{__

__                AlternateState\(\);__

__            \}__

__            if \(controls\.Equipped\.ChangeWeapon\.IsPressed\(\) && \!isDriving\)__

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

__            switch \(state\)__

__            \{__

__                case PlayerState\.Passive:__

__                    isAttacking = false;__

__                    isHit = false;__

__                    anim\.runtimeAnimatorController = animController;__

__                    combatCam\.Priority = 8;__

__                    Gravity\(\);__

__                    Move\(\);__

__                    Jump\(\);__

__                    break;__

__                case PlayerState\.Agressive:__

__                    anim\.runtimeAnimatorController = combatController;__

__                    combatCam\.Priority = 11;__

__                    Gravity\(\);__

__                    Move\(\);__

__                    Combat\(\);__

__                    break;__

__                case PlayerState\.Equipped:__

__                    anim\.runtimeAnimatorController = equippedController;__

__                    Gravity\(\);__

__                    Move\(\);__

__                    Equipped\(\);__

__                    break;__

__                case PlayerState\.Driving:__

__                    anim\.runtimeAnimatorController = drivingController;__

__                    break;__

__                case PlayerState\.Dead:__

__                    Gravity\(\);__

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

__    void UpdateHealth\(\)__

__    \{__

__        health = Mathf\.Clamp\(health, 0, maxHealth\);__

__        HPBar\.fillAmount = health / maxHealth;__

__    \}__

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

__    private void Gravity\(\)__

__    \{__

__        onSurface = Physics\.CheckSphere\(surfaceCheck\.position, surfaceDistance, surfaceMask\);__

__        if \(onSurface && velocity\.y < 0\)__

__        \{__

__            velocity\.y = \-2f;__

__        \}__

__        velocity\.y \+= gravity \* Time\.deltaTime;__

__        playerController\.Move\(playerSpeed \* Time\.deltaTime \* velocity\.normalized\);__

__        anim\.SetBool\("OnSurface", onSurface\);__

__    \}__

__    public void AlternateState\(\)__

__    \{__

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

__    private void Move\(\)__

__    \{__

__        float inputX = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.x;__

__        float inputZ = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.y;__

__        float moveSpeed;__

__        Vector3 direction = new Vector3\(inputX, 0, inputZ\)\.normalized;__

__        float targetAngle = Mathf\.Atan2\(direction\.x, direction\.z\) \* Mathf\.Rad2Deg \+ camTransform\.eulerAngles\.y;__

__        float angle = Mathf\.SmoothDampAngle\(transform\.eulerAngles\.y, targetAngle, ref turnSmoothVelocity, turnSmoothTime\);__

__        if \(state == PlayerState\.Equipped && playerAim\)__

__        \{__

__            Vector2 inputY = controls\.Player\.Camera\.ReadValue<Vector2>\(\);__

__            float newRotationX = headTransform\.localEulerAngles\.x \- inputY\.y;__

__            if \(newRotationX > 180\)__

__                newRotationX \-= 360;__

__            newRotationX = Mathf\.Clamp\(newRotationX, \-80f, 80f\);__

__            transform\.eulerAngles \+= new Vector3\(0f, inputY\.x, 0f\);__

__            headTransform\.localEulerAngles = new Vector3\(newRotationX, headTransform\.localEulerAngles\.y, headTransform\.localEulerAngles\.z\);__

__        \}__

__        else__

__        \{__

__            headTransform\.localEulerAngles = new Vector3\(Mathf\.Lerp\(headTransform\.localEulerAngles\.x, 0f, smoothSpeed\), headTransform\.localEulerAngles\.y, headTransform\.localEulerAngles\.z\);__

__            transform\.rotation = direction\.magnitude >= 0\.1f ? Quaternion\.Euler\(0f, angle, 0f\) : transform\.rotation;__

__        \}__

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

__    public void Jump\(\)__

__    \{__

__        if \(onSurface\)__

__        \{__

__            if \(controls\.Player\.Jump\.triggered\)__

__            \{__

__                anim\.SetTrigger\("Jump"\);__

__                velocity\.y = Mathf\.Sqrt\(\(jumpRange\) \* \-2 \* gravity\);__

__            \}__

__            else__

__            \{__

__                anim\.ResetTrigger\("Jump"\);__

__            \}__

__        \}__

__    \}__

__    public void SetEnemyFocus\(\)__

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

__    public void Combat\(\)__

__    \{__

__        if \(enemyFocus \!= null\)__

__        \{__

__            Vector3 target = new\(enemyFocus\.transform\.position\.x, transform\.position\.y, enemyFocus\.transform\.position\.z\);__

__            if \(enemyGroup\.Count > 0\)__

__            \{                __

__                if \(enemyFocus\.GetComponent<NPC>\(\)\.isAgressive\)__

__                \{__

__                    transform\.LookAt\(target\);__

__                \}               __

__            \}__

__            else__

__            \{__

__                Invoke\("AlternateState", 2f\); __

__            \}__

__        \}__

__        if \(controls\.Player\.Attack\.triggered && \!isHit\)__

__        \{__

__            isAttacking = true;__

__            anim\.SetTrigger\("Attack"\);__

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

__                if \(\!enemyGroup\.Contains\(enemyNPC\.gameObject\)\)__

__                \{__

__                    enemyGroup\.Add\(enemyNPC\.gameObject\);__

__                \}__

__            \}__

__        \}__

__    \}__

__    public void BeginAttack1\(\)__

__    \{__

__        isAttacking = true;__

__        audioSource\.loop = false;__

__        audioSource\.clip = audioAttack1;__

__        audioSource\.Play\(\);__

__    \}__

__    public void BeginAttack2\(\)__

__    \{__

__        isAttacking = true;__

__        audioSource\.loop = false;__

__        audioSource\.clip = audioAttack2;__

__        audioSource\.Play\(\);__

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

__\}__

No Inspector, altere o valor de __Max Health__ \(vida máxima\) e inclua a __image__ da barra de vida: 

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708602389505200.png)

Teste o jogo no combate com os NPC’s inimigos e veja que a barra de vida agora funciona\.

Finalizamos mais uma aula e agora que nosso personagem tem uma HUD com várias informações, tente inserir mais elementos de gameplay utilizando recursos de interface, como por exemplo uma barra de stamina ou contagem de munições\. Continue explorando e experimentando, e nos vemos na próxima aula\!

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download) 
- Para as tarefas:

Tarefa

- Tente criar outro elemento de HUD que ajude nosso personagem em sua jornada\. Implemente em um novo projeto da Unity ou desenhe / rascunhe em uma folha de papel e traga na próxima aula \(print ou papel\)\.

