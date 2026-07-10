# -*- coding: utf-8 -*-
"""Gera um cartaz JPEG da rotina do dia da EBF com as logos e visual moderno."""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ----------------------------------------------------------------------------
# Configurações de cores (extraídas das marcas EBF / Igreja Batista Plenitude)
# ----------------------------------------------------------------------------
YELLOW = (242, 168, 29)
MAGENTA = (179, 25, 130)
BLUE = (20, 80, 126)
LIGHT_BLUE = (41, 171, 226)
BG = (244, 246, 250)
CARD = (255, 255, 255)
TEXT_DARK = (38, 43, 52)
TEXT_GRAY = (118, 124, 133)

BRAND_CYCLE = [YELLOW, MAGENTA, BLUE, LIGHT_BLUE]

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}\\{name}", size)


F_TITLE = font("segoeuib.ttf", 92)
F_SUB = font("seguisb.ttf", 40)
F_STEP = font("segoeuib.ttf", 40)
F_NOTE = font("segoeui.ttf", 31)
F_NUM = font("segoeuib.ttf", 40)
F_FOOT = font("seguisb.ttf", 30)
F_KICKER = font("seguisb.ttf", 34)

# ----------------------------------------------------------------------------
# Conteúdo da rotina (renumerado de forma sequencial para leitura limpa)
# ----------------------------------------------------------------------------
STEPS = [
    ("Chegada das crianças", None),
    ("Chamada enquanto organizamos as crianças",
     "Gustavo está levando etiquetas para colocar o nome das crianças nas mochilas."),
    ("Lição Bíblica - Gustavo", None),
    ("Convite (Apelo)",
     "Ficar atento a esse momento e registrar com fotos. Após o apelo, as crianças "
     "que levantaram a mão devem procurar a Ellen, que anotará o nome delas."),
    ("Atividades de revisão",
     "a) Memorizar o versículo   b) Tiro ao alvo (arco e flecha)"),
    ("Descida para o lanche — 16:20",
     "Orientar as crianças a levar todos os materiais antes de sair. "
     "Garantir que nenhuma mochila ficou na sala."),
    ("Lanche",
     "Tirar fotos do momento do lanche para o grupo dos pais."),
    ("Brincadeiras: Terreno",
     "- Tirar fotos para os pais\n- Levar sacolas para guardar as bolsas e sapatos"),
    ("Entrega das crianças aos pais", None),
    ("Organização da sala de aula para o dia seguinte.", None),
]

# ----------------------------------------------------------------------------
# Dimensões base
# ----------------------------------------------------------------------------
W = 1080
MARGIN = 55                      # margem externa do cartaz
CARD_X0 = MARGIN
CARD_X1 = W - MARGIN
PAD = 60                         # padding interno do card
CONTENT_X0 = CARD_X0 + PAD
CONTENT_X1 = CARD_X1 - PAD
CONTENT_W = CONTENT_X1 - CONTENT_X0


def wrap(text, fnt, max_w):
    """Quebra o texto em linhas que cabem em max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if fnt.getlength(test) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def load_logo(path, target_h):
    img = Image.open(path).convert("RGBA")
    ratio = target_h / img.height
    return img.resize((int(img.width * ratio), target_h), Image.LANCZOS)


def _pasta_desktop() -> Path:
    """Retorna a pasta Desktop disponivel (OneDrive ou local)."""
    candidatos = [
        Path.home() / "OneDrive" / "Área de Trabalho",
        Path.home() / "Desktop",
        Path.home() / "OneDrive" / "Desktop",
    ]
    for pasta in candidatos:
        if pasta.is_dir():
            return pasta
    return Path.home() / "Desktop"


_DESKTOP = _pasta_desktop()
_DOWNLOADS = Path.home() / "Downloads"
SOURCE_CARTAZ = str(_DESKTOP / "cartaz_rotina_ebf.jpg")
LOGO_FILES = {
    "ebf": str(_DOWNLOADS / "IMG_3292.JPG.jpeg"),
    "igreja": str(_DOWNLOADS / "IMG_3389.PNG"),
}
LOGO_CROPS = {
    "ebf": (115, 115, 380, 245),
    "igreja": (640, 95, 1015, 265),
}


def get_logo(name, target_h):
    """Carrega logo do arquivo original ou recorta do cartaz existente."""
    path = LOGO_FILES[name]
    if os.path.isfile(path):
        return load_logo(path, target_h)
    source = Image.open(SOURCE_CARTAZ)
    cropped = source.crop(LOGO_CROPS[name]).convert("RGBA")
    ratio = target_h / cropped.height
    return cropped.resize((int(cropped.width * ratio), target_h), Image.LANCZOS)


def note_lines(nota, max_w):
    """Quebra notas em linhas, respeitando quebras explícitas."""
    lines = []
    for paragraph in nota.split("\n"):
        lines.extend(wrap(paragraph, F_NOTE, max_w))
    return lines


# ----------------------------------------------------------------------------
# Canvas alto; recortamos ao final conforme a altura real usada
# ----------------------------------------------------------------------------
H = 2400
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)


def rounded(xy, r, fill):
    draw.rounded_rectangle(xy, radius=r, fill=fill)


# ---- Card branco de fundo (a altura final é ajustada depois) ---------------
# Desenhado por último não dá; então desenhamos agora com altura provisória e
# redesenhamos elementos por cima. Melhor: calcular tudo, depois desenhar.

# ---------------------------------------------------------------------------
# 1ª passada: calcular a altura total necessária
# ---------------------------------------------------------------------------
LOGO_H = 130
NUM_D = 74            # diâmetro do badge numérico
row_gap = 30
note_line_h = 40
step_line_h = 50


def measure():
    y = 0
    y += PAD                      # topo do card
    y += LOGO_H                   # linha das logos
    y += 45                       # espaço
    y += 6                        # divisória
    y += 45
    y += 100                      # título
    y += 60                       # pílula subtítulo
    y += 55                       # espaço antes da lista
    for titulo, nota in STEPS:
        tlines = wrap(titulo, F_STEP, CONTENT_W - NUM_D - 30)
        block = max(NUM_D, len(tlines) * step_line_h)
        if nota:
            nlines = note_lines(nota, CONTENT_W - NUM_D - 30)
            block += len(nlines) * note_line_h + 8
        y += block + row_gap
    y += 20
    y += 90                       # rodapé
    y += PAD
    return y


card_h = measure()
TOTAL_H = int(card_h + 2 * MARGIN)

# Recria o canvas com a altura certa
img = Image.new("RGB", (W, TOTAL_H), BG)
draw = ImageDraw.Draw(img)

# Card branco com "sombra" simples
shadow_off = 10
draw.rounded_rectangle(
    (CARD_X0 + shadow_off, MARGIN + shadow_off, CARD_X1 + shadow_off, MARGIN + card_h + shadow_off),
    radius=48, fill=(225, 228, 234))
draw.rounded_rectangle(
    (CARD_X0, MARGIN, CARD_X1, MARGIN + card_h), radius=48, fill=CARD)

# Barra colorida decorativa no topo do card
bar_h = 16
bar = Image.new("RGB", (CARD_X1 - CARD_X0, bar_h))
bdraw = ImageDraw.Draw(bar)
seg = (CARD_X1 - CARD_X0) / 4
for i, c in enumerate(BRAND_CYCLE):
    bdraw.rectangle((int(i * seg), 0, int((i + 1) * seg), bar_h), fill=c)
# aplica cantos arredondados no topo
mask = Image.new("L", bar.size, 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, bar.size[0], bar.size[1] + 40), radius=48, fill=255)
img.paste(bar, (CARD_X0, MARGIN), mask)

# ---------------------------------------------------------------------------
# 2ª passada: desenhar o conteúdo
# ---------------------------------------------------------------------------
y = MARGIN + PAD

# ---- Logos ----------------------------------------------------------------
ebf = get_logo("ebf", LOGO_H)
igreja = get_logo("igreja", LOGO_H + 20)

img.paste(ebf, (CONTENT_X0, y + (LOGO_H - ebf.height) // 2), ebf)
img.paste(igreja, (CONTENT_X1 - igreja.width, y + (LOGO_H - igreja.height) // 2 - 10), igreja)
y += LOGO_H + 45

# ---- Divisória ------------------------------------------------------------
draw.line((CONTENT_X0, y, CONTENT_X1, y), fill=(230, 232, 238), width=3)
y += 45

# ---- Kicker + Título ------------------------------------------------------
kicker = "ESCOLA BÍBLICA DE FÉRIAS"
kw = F_KICKER.getlength(kicker)
draw.text(((W - kw) / 2, y), kicker, font=F_KICKER, fill=MAGENTA)
y += 55

titulo = "ROTINA DO DIA"
tw = F_TITLE.getlength(titulo)
draw.text(((W - tw) / 2, y), titulo, font=F_TITLE, fill=BLUE)
y += 105

# ---- Pílula do subtítulo --------------------------------------------------
sub = "SÁBADO   •   EQUIPE PRETA"
sw = F_SUB.getlength(sub)
pill_w = sw + 80
pill_h = 62
px0 = (W - pill_w) / 2
draw.rounded_rectangle((px0, y, px0 + pill_w, y + pill_h), radius=pill_h / 2, fill=YELLOW)
draw.text(((W - sw) / 2, y + (pill_h - F_SUB.size) / 2 - 4), sub, font=F_SUB, fill=(255, 255, 255))
y += pill_h + 55

# ---- Lista de etapas ------------------------------------------------------
text_x = CONTENT_X0 + NUM_D + 30
for i, (titulo, nota) in enumerate(STEPS):
    color = BRAND_CYCLE[i % len(BRAND_CYCLE)]
    tlines = wrap(titulo, F_STEP, CONTENT_W - NUM_D - 30)

    # badge numérico
    draw.ellipse((CONTENT_X0, y, CONTENT_X0 + NUM_D, y + NUM_D), fill=color)
    num = str(i + 1)
    nw = F_NUM.getlength(num)
    draw.text((CONTENT_X0 + (NUM_D - nw) / 2, y + (NUM_D - F_NUM.size) / 2 - 2),
              num, font=F_NUM, fill=(255, 255, 255))

    ty = y + 4
    for line in tlines:
        draw.text((text_x, ty), line, font=F_STEP, fill=TEXT_DARK)
        ty += step_line_h

    block = max(NUM_D, len(tlines) * step_line_h)
    if nota:
        ny = y + len(tlines) * step_line_h + 8
        wrapped = note_lines(nota, CONTENT_W - NUM_D - 30)
        for line in wrapped:
            draw.text((text_x, ny), line, font=F_NOTE, fill=TEXT_GRAY)
            ny += note_line_h
        block += len(wrapped) * note_line_h + 8

    y += block + row_gap

# ---- Rodapé ---------------------------------------------------------------
y += 20
draw.line((CONTENT_X0, y, CONTENT_X1, y), fill=(230, 232, 238), width=3)
y += 28
foot = "Registre os momentos com fotos e compartilhe no grupo dos pais"
fw = F_FOOT.getlength(foot)
# pequeno coração desenhado antes do texto
hx = (W - fw) / 2 - 42
hy = y + 6
r = 8
draw.ellipse((hx, hy, hx + r, hy + r), fill=MAGENTA)
draw.ellipse((hx + r - 2, hy, hx + 2 * r - 2, hy + r), fill=MAGENTA)
draw.polygon([(hx - 1, hy + r / 2 + 1), (hx + 2 * r - 1, hy + r / 2 + 1),
              (hx + r - 1, hy + r * 1.9)], fill=MAGENTA)
draw.text(((W - fw) / 2, y), foot, font=F_FOOT, fill=BLUE)

# ---------------------------------------------------------------------------
# Salvar
# ---------------------------------------------------------------------------
OUT = str(_DESKTOP / "cartaz_rotina_ebf.jpg")
img.save(OUT, "JPEG", quality=95)
print("Cartaz salvo em:", OUT)
print("Dimensões:", img.size)
