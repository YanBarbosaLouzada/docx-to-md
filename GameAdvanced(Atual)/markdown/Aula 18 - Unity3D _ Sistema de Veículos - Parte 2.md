# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601853885300.png)

# __PLANO DE AULA__

Aula 18 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Veículos \- Parte 2

Objetivos

- Sistema de Veículos e Criador de Estradas\.

Estratégias e atividades

Na aula de hoje iremos trabalhar no __script__ de funcionamento do veículo, o sistema de direção, aceleração e freio\.

__START__

Antes de iniciarmos a programação, vamos criar uma nova __Tag__ chamada__ Car__ que servirá para identificarmos quando o personagem está na área de colisão de algum veículo:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601853885300.png)

Adicione agora um novo __script__ ao veículo\. Vamos chamá\-lo de __Car Controller__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601853885300.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601853885300.png)

Script do Veículo:

__using System;__

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using UnityEngine;__

__public class CarController : MonoBehaviour__

__\{__

__    public enum Axel__

__    \{__

__        Front,__

__        Rear__

__    \}__

__    \[Serializable\]__

__    public struct Wheel__

__    \{__

__        public GameObject WheelMesh;__

__        public GameObject WheelDisk;__

__        public WheelCollider WheelCollider;__

__        public Axel axel;__

__    \}__

__    public float maxAcceleration = 30\.0f;__

__    public float brakeAcceleration = 50\.0f;__

__    public float turnSensitivity = 1\.0f;__

__    public float maxSteerAngle = 30\.0f;__

__    public Vector3 centerOfMass;__

__    public List<Wheel> wheels;__

__    private Rigidbody carRb;__

__    float moveInput;__

__    float steerInput;__

__    public Controls controls;__

__    private void OnEnable\(\)__

__    \{__

__        UnityEngine\.Cursor\.visible = false;__

__        UnityEngine\.Cursor\.lockState = CursorLockMode\.Locked;__

__        controls = new Controls\(\);__

__        controls\.Enable\(\);__

__    \}__

__    private void OnDisable\(\)__

__    \{__

__        controls = null;__

__    \}__

__    private void Start\(\)__

__    \{__

__        carRb = GetComponent<Rigidbody>\(\);__

__        carRb\.centerOfMass = centerOfMass;__

__    \}__

__    private void Update\(\)__

__    \{__

__        GetInputs\(\);__

__        Animate\(\);__

__    \}__

__    public void LateUpdate\(\)__

__    \{__

__        Move\(\);__

__        Brake\(\);__

__        Steer\(\);        __

__    \}__

__    void GetInputs\(\)__

__    \{__

__        moveInput = controls\.Driving\.Move\.ReadValue<float>\(\);__

__        steerInput = controls\.Driving\.Direction\.ReadValue<Vector2>\(\)\.x;__

__    \}__

__    void Move\(\)__

__    \{__

__        foreach \(Wheel wheel in wheels\)__

__        \{__

__            wheel\.WheelCollider\.motorTorque = moveInput \* 600 \* maxAcceleration \* Time\.deltaTime;__

__        \}__

__    \}__

__    void Steer\(\)__

__    \{__

__        foreach\(Wheel wheel in wheels\)__

__        \{__

__            if \(wheel\.axel == Axel\.Front\)__

__            \{__

__                var steerAngle = steerInput \* turnSensitivity \* maxSteerAngle;__

__                wheel\.WheelCollider\.steerAngle = Mathf\.Lerp\(wheel\.WheelCollider\.steerAngle, steerAngle, 0\.6f\);__

__            \}__

__        \}__

__    \}__

__    void Brake\(\)__

__    \{__

__        if \(controls\.Driving\.Brake\.IsPressed\(\)\)__

__        \{__

__            foreach \(var wheel in wheels\)__

__            \{__

__                wheel\.WheelCollider\.brakeTorque = 300 \* brakeAcceleration \* Time\.deltaTime;__

__            \}__

__        \}__

__        else__

__        \{__

__            foreach\(var wheel in wheels\)__

__            \{__

__                wheel\.WheelCollider\.brakeTorque = 0\.0f;__

__            \}__

__        \}        __

__    \}__

__    void Animate\(\)__

__    \{__

__        foreach\(var wheel in wheels\)__

__        \{__

__            wheel\.WheelCollider\.GetWorldPose\(out Vector3 pos, out Quaternion rot\);__

__            wheel\.WheelMesh\.transform\.SetPositionAndRotation\(pos, rot\);__

__            if \(wheel\.axel == Axel\.Front\)__

__            \{__

__                Quaternion diskRotation = Quaternion\.Euler\(0f, rot\.eulerAngles\.y, 0f\);__

__                wheel\.WheelDisk\.transform\.rotation = diskRotation;__

__            \}__

__        \}__

__    \}__

__\}__

Configure as referências do script da seguinte forma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601869560500.png)

Teste a cena e veja que já é possível__ entrar__ no veículo e __dirigir__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601869560500.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601869560500.png)

Na terceira parte, iremos aprender a como criar e editar estradas para testar melhor nosso veículo\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download)

