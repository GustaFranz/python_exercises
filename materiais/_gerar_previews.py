# -*- coding: utf-8 -*-
"""Gera miniaturas PNG dos PDFs para cards no README.

Execute na raiz do repositorio:
    python materiais/_gerar_previews.py
"""

from __future__ import annotations

from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
SAIDA = BASE / "assets" / "cards"
CARD_W, CARD_H = 640, 360
ZOOM = 2.0

MATERIAIS = (
    ("git", BASE / "git" / "Git_para_iniciantes.pdf", "Git para iniciantes", "#F05133"),
    ("dicionarios", BASE / "python" / "Dicionarios_em_Python.pdf", "Dicionarios", "#3776AB"),
    ("listas", BASE / "python" / "Listas_em_Python.pdf", "Listas", "#3776AB"),
    ("tuplas", BASE / "python" / "Tuplas_em_Python.pdf", "Tuplas", "#3776AB"),
    ("strings", BASE / "python" / "Tratamento_de_Strings_em_Python.pdf", "Strings", "#3776AB"),
)


def _fonte(tamanho: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Retorna fonte monoespacada ou fallback do sistema."""
    candidatos = (
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    for caminho in candidatos:
        if Path(caminho).exists():
            return ImageFont.truetype(caminho, tamanho)
    return ImageFont.load_default()


def pagina_para_card(pdf: Path, rotulo: str, cor_borda: str, destino: Path) -> None:
    """Converte a primeira pagina do PDF em card PNG padronizado."""
    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    doc.close()

    img.thumbnail((CARD_W, CARD_H - 36), Image.Resampling.LANCZOS)
    fundo = Image.new("RGB", (CARD_W, CARD_H), "#F4F7FA")
    x = (CARD_W - img.width) // 2
    y = 36 + (CARD_H - 36 - img.height) // 2
    fundo.paste(img, (x, y))

    draw = ImageDraw.Draw(fundo)
    draw.rectangle([0, 0, CARD_W, 32], fill=cor_borda)
    draw.text((12, 8), rotulo, fill="#FFFFFF", font=_fonte(14))
    draw.rectangle([0, 0, CARD_W - 1, CARD_H - 1], outline=cor_borda, width=2)

    destino.parent.mkdir(parents=True, exist_ok=True)
    fundo.save(destino, "PNG", optimize=True)
    print(f"OK  {destino.relative_to(BASE.parent)}")


def main() -> None:
    """Gera todos os cards configurados em MATERIAIS."""
    for slug, pdf, rotulo, cor in MATERIAIS:
        if not pdf.exists():
            raise FileNotFoundError(f"PDF nao encontrado: {pdf}")
        pagina_para_card(pdf, rotulo, cor, SAIDA / f"{slug}.png")


if __name__ == "__main__":
    main()
