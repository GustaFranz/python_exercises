# -*- coding: utf-8 -*-
"""Gera banner PNG para o README principal.

Execute:
    python 04_study_materials/_gerar_banner.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
SAIDA = BASE / "assets" / "banner.png"
LARGURA, ALTURA = 1200, 320


def _fonte(tamanho: int, negrito: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    nome = "C:/Windows/Fonts/segoeuib.ttf" if negrito else "C:/Windows/Fonts/segoeui.ttf"
    if Path(nome).exists():
        return ImageFont.truetype(nome, tamanho)
    return ImageFont.load_default()


def main() -> None:
    """Desenha banner com identidade visual do repositorio."""
    img = Image.new("RGB", (LARGURA, ALTURA), "#11283F")
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, ALTURA - 8, LARGURA, ALTURA], fill="#FFD43B")
    draw.rectangle([0, 0, 6, ALTURA], fill="#3776AB")

    draw.text((48, 52), "python_exercises", fill="#FFD43B", font=_fonte(42, True))
    draw.text(
        (48, 110),
        "Prof. Gustavo Franz  ·  Science/Biology  ·  Python Developer in Progress",
        fill="#E6EDF3",
        font=_fonte(22),
    )
    draw.text(
        (48, 155),
        "290 exercicios  ·  71 resolvidos  |  7 guias PDF  |  4 trilhas",
        fill="#7FA7C2",
        font=_fonte(18),
    )

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    img.save(SAIDA, "PNG", optimize=True)
    print(f"OK  {SAIDA.relative_to(BASE.parent)}")


if __name__ == "__main__":
    main()
