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

# Limpa arquivo de URLs antes de começar
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
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    with open(input_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(
            docx_file,
            convert_image=mammoth.images.inline(image_handler)
        )

    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(result.value)

    print(f"✅ Markdown gerado: {output_path}")

# --- PROCESSA TODOS OS DOCX DE UMA PASTA ---
DOCX_FOLDER = "docx"  # pasta onde estão os arquivos
OUTPUT_FOLDER = "markdown"  # pasta pra salvar os MD
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file_name in os.listdir(DOCX_FOLDER):
    if file_name.endswith(".docx"):
        input_path = os.path.join(DOCX_FOLDER, file_name)
        output_file = file_name.replace(".docx", ".md")
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        docx_to_markdown(input_path, output_path)

print(f"🖼️ Todas as imagens estão em: {IMG_FOLDER}/")
print(f"🔗 Todas as URLs em: {URL_FILE}")
