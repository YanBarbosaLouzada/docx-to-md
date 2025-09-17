import mammoth
import time
import os

# Configurações do GitHub
USUARIO = "YanBarbosaLouzada"
REPO = "YanBarbosaLouzada/docx-to-md"  # sem .git
BRANCH = "master"  # ou "main"

# Pastas
IMG_FOLDER = "imagens"
os.makedirs(IMG_FOLDER, exist_ok=True)

# Arquivo que vai guardar as URLs
URL_FILE = "imagens_urls.txt"

# Limpa arquivo de URLs antes de cada conversão
open(URL_FILE, "w", encoding="utf-8").close()

def image_handler(image):
    file_name = f"img_{time.time_ns()}.png"
    file_path = os.path.join(IMG_FOLDER, file_name)

    # Salva a imagem
    with image.open() as img_file:
        with open(file_path, "wb") as f:
            f.write(img_file.read())

    # Gera URL do GitHub RAW
    url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{IMG_FOLDER}/{file_name}"

    # Salva URL no arquivo
    with open(URL_FILE, "a", encoding="utf-8") as f:
        f.write(url + "\n")

    return {"src": url}

def docx_to_markdown(input_path, output_path):
    # Garante que a pasta do Markdown existe
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    # Converte DOCX para Markdown
    with open(input_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(
            docx_file,
            convert_image=mammoth.images.inline(image_handler)
        )

    # Salva Markdown
    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(result.value)

    print(f"✅ Markdown gerado: {output_path}")
    print(f"🖼️ Imagens salvas em: {IMG_FOLDER}/")
    print(f"🔗 URLs das imagens salvas em: {URL_FILE}")
    print("🚀 Agora é só copiar as URLs de lá ou fazer git add/commit/push para usar no GitHub")

if __name__ == "__main__":
    docx_to_markdown(
        "Aula 02 - Tabelas, links, imagens & organização de pastas.docx",
        "Aula 02 - Tabelas, links, imagens & organização de pastas.md"
    )
