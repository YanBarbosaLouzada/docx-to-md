# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599293527600.png)

# __PLANO DE AULA__

Aula 02 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Movimentação e Animações Básicas\.

Objetivos

- Movimentação do Player;
- Animações Básicas do Player;
- Primeiro Script\.

Estratégias e atividades

Nesta aula, vamos abordar a configuração da movimentação e animações básicas do personagem\. Inicialmente, iremos incorporar ao objeto __Player__ o componente __Character Controller__, responsável por sua movimentação e colisão:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599297691300.png)

O Character Controller adiciona um__ colisor em forma de cápsula__ automaticamente ao objeto e para um melhor encaixe em nosso personagem, vamos alterar alguns valores:

- __Y \-> 0\.9 __
- __Radius \-> 0\.3__
- __Height \-> 1\.8__

As animações podem ser baixadas no __mixamo__, utilizando o mesmo personagem para melhor compatibilidade e evitar erros\. Selecione as animações __Walk \(andando\), Run \(Correndo\)__ e __Fall \(Caindo\)__ e salve na pasta__ Animations > Player__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599303080500.png)__

A animação será configurada diretamente no modelo 3D, utilizando o componente __Animator__\. Este componente receberá um __Animator Controller__, o qual será criado na pasta de animações do personagem\. Em seguida, adicione o Animator Controller ao animator do personagem\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599308078100.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599310082400.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599313078800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599314080300.png)

Agora que o Player já possui os componentes Character Controller e Animator, vamos criar o primeiro __script__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599317079600.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599319174800.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599320910200.png)

Embora o__ código__ do script possa ser escrito em qualquer editor de código, como o VS Code, é altamente recomendável utilizar o__ Microsoft Visual Studio__ para obter uma experiência de desenvolvimento mais integrada à__ Unity Engine__\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599320910200.png)

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

__using UnityEngine\.EventSystems;__

__using UnityEngine\.InputSystem;__

__using UnityEngine\.TextCore\.Text;__

__using UnityEngine\.UI;__

__using static Cinemachine\.CinemachineFreeLook;__

__public class Player : MonoBehaviour__

__\{__

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

__    public Animator anim;__

__    \[Header\("Camera"\)\]__

__    public Transform camTransform;__

__    public CinemachineFreeLook freeLookCam;  __

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

__        turnSmoothTime = 0\.1f;__

__        surfaceDistance = 0\.4f;__

__        gravity = \-9\.8f;__

__    \}__

__    void FixedUpdate\(\)__

__    \{  __

__        Gravity\(\);            __

__        Move\(\);__

__    \}__

__    private void Gravity\(\)__

__    \{__

__        onSurface = Physics\.CheckSphere\(surfaceCheck\.position, surfaceDistance, surfaceMask\);__

__        if \(onSurface && velocity\.y < 0\)__

__        \{__

__            velocity\.y = \-2f;__

__        \}__

__        //Gravidade__

__        velocity\.y \+= gravity \* Time\.fixedDeltaTime;__

__        playerController\.Move\(playerSpeed \* Time\.fixedDeltaTime \* velocity\.normalized\);__

__        anim\.SetBool\("OnSurface", onSurface\);__

__    \}__

__    private void Move\(\)__

__    \{__

__        float inputX = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.x;__

__        float inputZ = controls\.Player\.Move\.ReadValue<Vector2>\(\)\.y;__

__        float moveSpeed;__

__        Vector3 direction = new Vector3\(inputX, 0, inputZ\)\.normalized;__

__        float targetAngle = Mathf\.Atan2\(direction\.x, direction\.z\) \* Mathf\.Rad2Deg \+ camTransform\.eulerAngles\.y;__

__        float angle = Mathf\.SmoothDampAngle\(transform\.eulerAngles\.y, targetAngle, ref turnSmoothVelocity, turnSmoothTime\);__

__       if \(direction\.magnitude >= 0\.1f && onSurface\)__

__        \{__

__            Vector3 moveDirection = Quaternion\.Euler\(0f, targetAngle, 0f\) \* Vector3\.forward;__

__            float targetSpeed = controls\.Player\.Run\.IsPressed\(\) ? playerSprint : playerSpeed;__

__            currentSpeed = Mathf\.Lerp\(currentSpeed, targetSpeed, Time\.deltaTime \* smoothSpeed\);__

__            playerController\.Move\(currentSpeed \* Time\.deltaTime \* moveDirection\.normalized\);__

__            jumpRange = 0f;__

__        \}__

__        else if\(direction\.magnitude < 0\.1f\)__

__        \{__

__            currentSpeed = Mathf\.Lerp\(currentSpeed, 0f, Time\.deltaTime \* smoothSpeed\);__

__            jumpRange = 0\.5f;__

__        \}__

__        moveSpeed = new Vector3\(playerController\.velocity\.x, 0f, playerController\.velocity\.z\)\.magnitude;__

__        anim\.SetFloat\("Velocity", moveSpeed\);__

__    \}__

Explicação da __conversão da direção__ do movimento em relação ao __ângulo__ da câmera:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599320910200.png)

Para que o código funcione corretamente, precisamos sinalizar os __objetos__ e __componentes__ que fizemos referência:

- __Character Controller;__
- __Animator;__
- __Camera;__
- __SurfaceCheck\.__

Marque também a Layer __Surface__ como a Layer responsável pela superfície\.

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599335918200.png)

Agora, precisamos alterar a __tag__ e a__ layer__ dos objetos considerados superfícies para __Surface__\. Por enquanto, vamos marcar a rua \(__Road__\) e a rodovia \(__HighWay__\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599335918200.png)

Verifique também se os__ objetos__ da layer__ Surface__ estão sendo exibidos na__ câmera__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599339158100.png)

Para finalizar, vamos configurar o __Animator Controller__ com os seguintes __parâmetros__:

Bool >__ Idle__

Bool > __Walking__

Bool >__ OnSurface__

Trigger >__ Jump__

Float > __Velocity__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599341174500.png)

O movimento \(__Walking e Running__\) deve ser configurado como uma__ Blend Tree__, utilizando o parâmetro __Velocity__, para que a transição do movimento seja mais suave e realista:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599345202900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708599347212500.png)

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download)

Tarefa

- Pesquise sobre Animação com Captura de Movimentos nos Games\. 
- Envie em um pendrive, no Google Drive, ou para o e\-mail __myndstechschool@gmail\.com__\.

