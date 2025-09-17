import mammoth
import time
import os
import shutil

# Configurações do seu GitHub
USUARIO = "YanBarbosaLouzada"
REPO = "https://github.com/YanBarbosaLouzada/docx-to-md.git"
BRANCH = "master"  # ou "main"
IMG_FOLDER = "imagens"

# cria a pasta se não existir
os.makedirs(IMG_FOLDER, exist_ok=True)

def image_handler(image):
    # nome único pra imagem
    file_name = f"img_{int(time.time())}.png"
    file_path = os.path.join(IMG_FOLDER, file_name)

    # salva local
    with open(file_path, "wb") as f:
        f.write(image.read())

    # monta a URL crua do GitHub
    url = f"https://raw.githubusercontent.com/{USUARIO}/{REPO}/{BRANCH}/{IMG_FOLDER}/{file_name}"

    return {"src": url}


def docx_to_markdown(input_path, output_path):
    with open(input_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(
            docx_file,
            convert_image=mammoth.images.inline(image_handler)
        )
        markdown = result.value

    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown)

    print(f"✅ Markdown gerado: {output_path}")
    print(f"🖼️ Imagens salvas na pasta: {IMG_FOLDER}/")
    print("🚀 Agora é só dar commit/push no GitHub para as URLs ficarem ativas.")
    

if __name__ == "__main__":
    docx_to_markdown("meuarquivo.docx", "saida.md")
