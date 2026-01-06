# ![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601005909000.png)

# __PLANO DE AULA__

Aula 14 | Tempo estimado: 1 hora e 30 minutos | Faixa\-Etária: Game Advanced

Tipo da atividade: No computador

Ferramenta\(s\): Unity 3D

Conteúdos

- Sistema de Armas \- Parte 2

Objetivos

- Implementar o sistema de armas\.\.

Estratégias e atividades

Na aula de hoje, iremos implementar o sistema de armas montado na aula anterior\. Mas, antes, vamos criar __elementos de interface__ para visualizar a troca e ativação de armas:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601021199300.png)

__START__

Primeiro vamos baixar imagens de ícones que representam as armas, como por exemplo o __FPS Icons Pack__:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601021199300.png)

Também precisamos de uma imagem para a __WeaponWheel \(Roda de Armas\)__, como o__ Pi UI:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601021199300.png)__

Na Unity, para trabalharmos com interface, utilizamos o objeto __Canvas\.__ Vamos criar um novo Canvas e chamá\-lo de __HUD__ \(heads\-up display \- tela de alerta\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601021199300.png)

Dentro da HUD, criaremos um __Panel__ chamado __ChangeWeaponPanel__ e dentro dele, uma __Image__ chamada __WeaponWheel:__

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601037923900.png)![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601037923900.png)

Selecione a WeaponWheel e, no componente Image, adicione o sprite da roda de armas baixado anteriormente\. Ajuste o tamanho e cores como desejar:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601037923900.png)

Agora iremos adicionar os itens da roda de armas\. Se dividirmos a Weapon Wheel em __oito partes iguais__, temos o espaço para cada novo__ ícone __de arma:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601046253500.png)

Vamos começar com o ícone __Hand __\(Mão\) para o Player desarmado\. Adicione uma nova image dentro da __Weapon Wheel__ com o sprite da __mão__ e outro com o ícone do Rifle, que chamaremos de __Assault:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601046253500.png)__

Ajuste a posição dos __ícones__ de modo que pareçam estar fixados na __Weapon Wheel:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601054752700.png)__

Por fim, adicionamos mais um objeto vazio dentro da Weapon Wheel chamado__ targetWheel__, que será responsável por apontar para o item escolhido de acordo com o ponteiro do mouse \(ou joystick, com gamepad\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601054752700.png)

Além do ícone na Weapon Wheel, queremos que, ao equipar uma arma, o ícone seja mostrado o tempo todo no canto superior esquerdo da interface\. Para isso, adicionaremos uma nova image dentro da HUD, chamada__ Icon\_Slot __e dentro dela outra image chamada __Weapon\_Icon:__

__![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601063172900.png)__

Em __Weapon\_Icon__, adicione o sprite __Hand __\(mão\):

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601063172900.png)

Por fim, vamos adicionar uma image centralizada na HUD, para servir de mira para o personagem\. Insira uma imagem de sua escolha, podendo ser uma cruz, ou simplesmente um ponto:

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601063172900.png)

![](https://raw.githubusercontent.com/YanBarbosaLouzada/docx-to-md/master/imagens/img_1767708601071420200.png)

Agora que temos o __sistema de arma__ e__ interface__ configurados, vamos criar um script da classe __Weapons__, que será base para qualquer arma implementada futuramente\.

Script __Weapons:__

__using System;__

__using System\.Collections;__

__using System\.Collections\.Generic;__

__using System\.Linq;__

__using System\.Reflection;__

__using UnityEditor\.ShaderGraph;__

__using UnityEngine;__

__using UnityEngine\.UI;__

__using static Player;__

__using static Weapon;__

__public class Weapon__

__\{__

__    public enum weaponName__

__    \{__

__        Hand,__

__        Assault,__

__    \}__

__    public weaponName name;__

__    public GameObject weaponObject;__

__    public Vector3 muzzlePosition;__

__    public bool hasWeapon;__

__    public int damage;__

__    public float fireRate;__

__    public float range;__

__    public int maxAmmo;__

__    public int currentAmmo;__

__    public Weapon\(weaponName name, Vector3 muzzlePosition, bool hasWeapon, int damage, float fireRate, float range, int maxAmmo\)__

__    \{__

__        this\.name = name;__

__        this\.muzzlePosition = muzzlePosition;__

__        this\.hasWeapon = hasWeapon;__

__        this\.damage = damage;__

__        this\.fireRate = fireRate;__

__        this\.range = range;__

__        this\.maxAmmo = maxAmmo;__

__        this\.currentAmmo = maxAmmo;__

__    \}__

__\}__

__public class Weapons : MonoBehaviour__

__\{__

__    public GameObject weaponIcon;__

__    public GameObject weaponSlot;__

__    public GameObject targetWheel;        __

__    public LayerMask slotMask;__

__    public Weapon assault = new Weapon\(weaponName\.Assault, new\(0, 0, 0\), false, 30, 0\.1f, 70f, 30\);__

__    public ParticleSystem impactParticle;__

__    public ParticleSystem impactBullet;__

__    public ParticleSystem muzzleSpark;__

__    public weaponName currentWeapon = weaponName\.Hand;__

__    public Weapon currentWeaponInstance;__

__    public float nextFireTime = 0f;__

__    public Sprite handIcon;__

__    private void Awake\(\)__

__    \{__

__        handIcon = weaponIcon\.GetComponent<Image>\(\)\.sprite;__

__    \}__

__    public void AddWeapon\(weaponName name\)__

__    \{__

__        PropertyInfo\[\] properties = typeof\(Weapons\)\.GetProperties\(BindingFlags\.Instance\);__

__        foreach \(PropertyInfo property in properties\)__

__        \{__

__            if \(property\.PropertyType == typeof\(Weapon\)\)__

__            \{__

__                Weapon weapon = \(Weapon\)property\.GetValue\(this\);__

__                if \(weapon\.name == name\)__

__                \{__

__                    if \(weapon\.hasWeapon\)__

__                    \{__

__                        weapon\.currentAmmo = weapon\.maxAmmo;__

__                    \}__

__                    else__

__                    \{__

__                        weapon\.hasWeapon = true;__

__                    \}__

__                \}__

__            \}__

__        \}        __

__    \}__

__    public void SetActiveSlot\(float inputX, float inputY\)__

__    \{        __

__        GameObject\[\] weaponSlots = GameObject\.FindGameObjectsWithTag\("WeaponSlot"\);__

__        Vector2 inputVector = new Vector2\(inputX, inputY\);__

__        float angle = Mathf\.Atan2\(inputVector\.y, inputVector\.x\) \* Mathf\.Rad2Deg;__

__        if \(inputVector\.magnitude > 0\)__

__        \{__

__            targetWheel\.transform\.rotation = Quaternion\.Euler\(0, 0, angle\);__

__        \}__

__        RaycastHit2D hit = Physics2D\.Raycast\(targetWheel\.transform\.position, targetWheel\.transform\.right, 500f, slotMask\);__

__        if \(hit\.collider \!= null\)__

__        \{__

__            hit\.collider\.gameObject\.transform\.localScale = new\(1\.5f, 1\.5f, 1f\);__

__            foreach \(GameObject slot in weaponSlots\)__

__            \{__

__                if \(hit\.collider\.gameObject \!= slot\)__

__                \{__

__                    slot\.transform\.localScale = new\(1f, 1f, 1f\);__

__                    __

__                    SetWeapon\(hit\.collider\.gameObject\);__

__                \}__

__            \}__

__        \}__

__    \}__

__    public void SetWeapon\(GameObject slot\)__

__    \{__

__        foreach \(Transform child in weaponSlot\.transform\)__

__        \{__

__            child\.gameObject\.SetActive\(false\);__

__        \}__

__        if \(slot\.name \!= "Hand"\)__

__        \{__

__            currentWeapon = \(weaponName\)Enum\.Parse\(typeof\(weaponName\), slot\.name\);__

__            currentWeaponInstance = GetCurrentWeaponInstance\(\);__

__            weaponIcon\.GetComponent<Image>\(\)\.sprite = slot\.GetComponent<Image>\(\)\.sprite;__

__            weaponSlot\.transform\.Find\(slot\.name\)\.gameObject\.SetActive\(true\);__

__        \}__

__        else__

__        \{__

__            currentWeapon = weaponName\.Hand;__

__            weaponIcon\.GetComponent<Image>\(\)\.sprite = handIcon;__

__        \}__

__    \}__

__    private Weapon GetCurrentWeaponInstance\(\)__

__    \{__

__        switch \(currentWeapon\)__

__        \{__

__            case weaponName\.Assault:__

__                return assault;__

__            default:__

__                return null;__

__        \}__

__    \}__

__    public void Shoot\(RaycastHit hit\)__

__    \{__

__        if \(currentWeaponInstance \!= null && Time\.time >= nextFireTime && currentWeaponInstance\.currentAmmo > 0\)__

__        \{__

__            currentWeaponInstance\.currentAmmo\-\-;__

__            nextFireTime = Time\.time \+ 0\.01f / currentWeaponInstance\.fireRate;__

__            __

__            Instantiate\(muzzleSpark, weaponSlot\.transform\);__

__            if \(hit\.collider \!= null\)__

__            \{__

__                if \(hit\.collider\.gameObject\.CompareTag\("Enemy"\)\)__

__                \{__

__                    hit\.collider\.GetComponentInParent<NPC>\(\)\.HitDamage\(10\);__

__                \}__

__                else__

__                \{__

__                    Instantiate\(impactParticle, hit\.point, Quaternion\.LookRotation\(hit\.normal\)\);__

__                    if \(UnityEngine\.Random\.Range\(1, 3\) == 1\)__

__                    \{__

__                        Instantiate\(impactBullet, hit\.point, Quaternion\.LookRotation\(hit\.normal\)\);__

__                    \}__

__                \}__

__            \}__

__        \}        __

__    \}__

__\}__

Na próxima aula iremos modificar o script do Player para finalizar o sistema de armas do personagem\.

Recursos

- Computador, internet e Unity\.

Observação

- Os assets e scripts estão disponíveis no Google Drive;
- Link para o download da Unity:
	- [https://unity\.com/pt/download](https://unity.com/pt/download)

