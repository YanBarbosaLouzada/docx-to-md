import mammoth
import time
import os
import shutil

# Configurações do seu GitHub
USUARIO = "YanBarbosaLouzada"
REPO = "https://github.com/YanBarbosaLouzada/docx-to-md.git"
BRANCH = "master"  # ou "main"
IMG_FOLDER = "imagens"
os.makedirs(IMG_FOLDER, exist_ok=True)

def image_handler(image):
    file_name = f"img_{int(time.time())}.png"
    file_path = os.path.join(IMG_FOLDER, file_name)

    # salva imagem em disco
    with image.open() as img_file:
        with open(file_path, "wb") as f:
            f.write(img_file.read())

    # monta URL do GitHub RAW
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
    print(f"🖼️ Imagens salvas em: {IMG_FOLDER}/")
    print("🚀 Agora só dar git add/commit/push para ativar as URLs")


if __name__ == "__main__":
    docx_to_markdown(
        "Aula 02 - Tabelas, links, imagens & organização de pastas.docx",
        "Aula 02 - Tabelas, links, imagens & organização de pastas.md"
    )