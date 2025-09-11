import pypandoc
import base64
import os
import re
import glob
from pathlib import Path

# 📂 Ajuste os caminhos conforme necessário
input_dir = r"C:\Users\JGFel\Documents\python\teste"
output_dir = r"C:\Users\JGFel\Documents\python\teste\markdowns"

os.makedirs(output_dir, exist_ok=True)

def convert_docx_to_md(input_file, output_file, media_dir_for_file):
    os.makedirs(media_dir_for_file, exist_ok=True)

    # 1) Converter DOCX -> MD
    pypandoc.convert_file(
        input_file,
        "gfm",
        outputfile=output_file,
        extra_args=[f"--extract-media={media_dir_for_file}"]
    )

    # 2) Ler markdown gerado
    with open(output_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Regex ainda mais flexível: captura qualquer <img ... src="..."> até fechar
    pattern = re.compile(
        r'<img[^>]*?src=["\']([^"\']+)["\'][^>]*?>',
        re.IGNORECASE | re.DOTALL
    )

    def img_to_base64(match):
        img_path_raw = match.group(1).strip()
        img_name = Path(img_path_raw).name  # pega só o nome (ex: image14.png)

        # procurar recursivamente dentro da pasta de mídia do arquivo
        real_img = None
        for root, _, files in os.walk(media_dir_for_file):
            for f in files:
                if f.lower() == img_name.lower():
                    real_img = os.path.join(root, f)
                    break
            if real_img:
                break

        if not real_img or not os.path.exists(real_img):
            print(f"⚠️ Imagem não encontrada: {img_name}")
            return ""  # remove a tag quebrada

        ext = Path(real_img).suffix.lower().lstrip('.')
        with open(real_img, "rb") as img_file:
            img_bytes = img_file.read()
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")

        return f"![image](data:image/{ext};base64,{img_b64})"

    # 3) Substituir imagens
    md_content = pattern.sub(img_to_base64, md_content)

    # 4) Salvar markdown final
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md_content)

def process_all_docx(input_dir, output_dir):
    for docx_file in glob.glob(os.path.join(input_dir, "*.docx")):
        file_name = Path(docx_file).stem
        md_file = os.path.join(output_dir, f"{file_name}.md")
        media_dir_for_file = os.path.join(output_dir, f"{file_name}_media")
        convert_docx_to_md(docx_file, md_file, media_dir_for_file)
        print(f"✅ {file_name} convertido -> {md_file}")

if __name__ == "__main__":
    process_all_docx(input_dir, output_dir)
    print("🎉 Conversão concluída!")
