"""
Gera imagem do relatório exibido no terminal pelo main.py.

Objetivo: reproduzir a saída de pontos cadastrados com as mesmas cores
e formatação do GeoExplorer, pronta para uso no README.
"""

import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from adicionar_moldura import adicionar_moldura

LARGURA = 920
MARGEM = 28
LINHA_ALTURA = 26

COR_TERMINAL = (30, 30, 30)
COR_SEPARADOR = (80, 80, 80)
COR_TITULO = (46, 204, 113)
COR_INDICE = (86, 182, 194)
COR_LAT = (241, 196, 15)
COR_LONG = (155, 89, 182)
COR_TOTAL = (46, 204, 113)
COR_TEXTO = (220, 220, 220)


def carregar_fonte(tamanho: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Carrega fonte monoespaçada do sistema."""
    candidatas = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    ]
    for caminho in candidatas:
        if Path(caminho).exists():
            return ImageFont.truetype(caminho, tamanho)
    return ImageFont.load_default()


def montar_linhas_pontos(dados: list[dict]) -> list[str]:
    """
    Monta linhas do relatório no mesmo formato do main.py.

    Parâmetros:
        dados: lista de dicts com nome, latitude e longitude.

    Retorno:
        Lista de strings prontas para desenho.
    """
    linhas = []
    for indice, item in enumerate(dados, start=1):
        nome = item["nome"].strip()
        latitude = item["latitude"]
        longitude = item["longitude"]
        linhas.append(
            f"{indice:02d}. {nome:.<25} │ Latitude: {latitude} │ Longitude: {longitude}"
        )
    return linhas


def texto_relatorio(dados: list[dict]) -> str:
    """
    Monta relatório completo em texto puro.

    Parâmetros:
        dados: pontos geográficos cadastrados.

    Retorno:
        Texto do relatório sem códigos ANSI.
    """
    separador = "=" * 95
    linhas = [
        separador,
        "GEOEXPLORER EDUCACIONAL | GUSTAVO FRANZ",
        separador,
        "",
        separador,
        "PONTOS GEOGRÁFICOS CADASTRADOS",
        separador,
        *montar_linhas_pontos(dados),
        separador,
        f"Total de pontos cadastrados: {len(dados)}",
        separador,
        "",
        f"Dados salvos em: dados_coordenadas.json",
        f"Mapa salvo em: mapa_pontos.html",
    ]
    return "\n".join(linhas)


def desenhar_relatorio(dados: list[dict]) -> Image.Image:
    """
    Desenha o relatório em estilo terminal.

    Parâmetros:
        dados: pontos geográficos cadastrados.

    Retorno:
        Imagem PIL com o relatório renderizado.
    """
    fonte = carregar_fonte(16)
    fonte_titulo = carregar_fonte(17)

    linhas_pontos = montar_linhas_pontos(dados)
    blocos = [
        ("titulo", "=" * 95),
        ("titulo", "GEOEXPLORER EDUCACIONAL | GUSTAVO FRANZ"),
        ("titulo", "=" * 95),
        ("vazio", ""),
        ("titulo", "=" * 95),
        ("titulo", "PONTOS GEOGRÁFICOS CADASTRADOS"),
        ("titulo", "=" * 95),
    ]

    for linha in linhas_pontos:
        blocos.append(("ponto", linha))

    blocos.extend(
        [
            ("titulo", "=" * 95),
            ("total", f"Total de pontos cadastrados: {len(dados)}"),
            ("titulo", "=" * 95),
            ("vazio", ""),
            ("texto", "Dados salvos em: dados_coordenadas.json"),
            ("texto", "Mapa salvo em: mapa_pontos.html"),
        ]
    )

    altura = MARGEM * 2 + LINHA_ALTURA * len(blocos)
    imagem = Image.new("RGB", (LARGURA, altura), COR_TERMINAL)
    draw = ImageDraw.Draw(imagem)

    y = MARGEM
    for tipo, conteudo in blocos:
        if tipo == "vazio":
            y += LINHA_ALTURA // 2
            continue

        fonte_usada = fonte_titulo if tipo == "titulo" else fonte

        if tipo == "titulo":
            cor = COR_TITULO
        elif tipo == "total":
            cor = COR_TOTAL
        elif tipo == "texto":
            cor = COR_TEXTO
        elif tipo == "ponto":
            cor = COR_INDICE
            draw.text((MARGEM, y), conteudo, fill=cor, font=fonte_usada)

            match = re.match(
                r"(\d{2}\. .+?) │ (Latitude: .+?) │ (Longitude: .+)",
                conteudo,
            )
            if match:
                parte_indice = match.group(1)
                parte_lat = match.group(2)
                parte_long = match.group(3)
                x = MARGEM
                draw.text((x, y), parte_indice, fill=COR_INDICE, font=fonte_usada)
                x += draw.textlength(parte_indice + " │ ", font=fonte_usada)
                draw.text((x, y), parte_lat, fill=COR_LAT, font=fonte_usada)
                x += draw.textlength(parte_lat + " │ ", font=fonte_usada)
                draw.text((x, y), parte_long, fill=COR_LONG, font=fonte_usada)
                y += LINHA_ALTURA
                continue
        else:
            cor = COR_TEXTO

        draw.text((MARGEM, y), conteudo, fill=cor, font=fonte_usada)
        y += LINHA_ALTURA

    return imagem


def main() -> None:
    """Gera TXT e PNG do relatório com moldura."""
    pasta = Path(__file__).resolve().parent
    pasta_exercicio = pasta.parent
    caminho_json = pasta_exercicio / "dados_coordenadas.json"

    with open(caminho_json, encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    relatorio = texto_relatorio(dados)
    caminho_txt = pasta / "relatorio_terminal.txt"
    caminho_png_original = pasta / "originais" / "relatorio_terminal_original.png"
    caminho_png_final = pasta / "relatorio_terminal.png"

    caminho_png_original.parent.mkdir(parents=True, exist_ok=True)

    caminho_txt.write_text(relatorio, encoding="utf-8")
    imagem = desenhar_relatorio(dados)
    imagem.save(caminho_png_original, "PNG", optimize=True)
    adicionar_moldura(caminho_png_original, caminho_png_final)

    print(f"Gerado: {caminho_txt.name}")
    print(f"Gerado: {caminho_png_final.name}")


if __name__ == "__main__":
    main()
