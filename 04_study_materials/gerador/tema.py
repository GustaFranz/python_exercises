# -*- coding: utf-8 -*-
"""Tema visual: paleta de cores, fontes e estilos de paragrafo.

Centraliza toda a identidade visual para manter consistencia entre os
materiais. Trocar de tema (ex.: Python -> Git) e apenas escolher outra
instancia de `Tema`, sem alterar componentes ou conteudo.
"""

from dataclasses import dataclass

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle


TEXTO = colors.HexColor("#1F2A37")
TEXTO_SUAVE = colors.HexColor("#55606E")
LINHA = colors.HexColor("#D7DEE6")
ZEBRA = colors.HexColor("#F4F7FA")
BRANCO = colors.white

CODE_BG = colors.HexColor("#0F2233")
CODE_FG = colors.HexColor("#E6EDF3")
CODE_COMENTARIO = colors.HexColor("#7FA7C2")
CODE_DESTAQUE = colors.HexColor("#FFD43B")


@dataclass(frozen=True)
class Tema:
    """Conjunto de cores que define a identidade de um material."""

    nome: str
    primaria: colors.Color
    secundaria: colors.Color
    acento: colors.Color
    suave: colors.Color
    cabecalho_tabela: colors.Color
    check: colors.Color


TEMA_PYTHON = Tema(
    nome="python",
    primaria=colors.HexColor("#11283F"),
    secundaria=colors.HexColor("#FFD43B"),
    acento=colors.HexColor("#3776AB"),
    suave=colors.HexColor("#EEF4FA"),
    cabecalho_tabela=colors.HexColor("#3776AB"),
    check=colors.HexColor("#2E9E5B"),
)

TEMA_GIT = Tema(
    nome="git",
    primaria=colors.HexColor("#16222E"),
    secundaria=colors.HexColor("#F05133"),
    acento=colors.HexColor("#F05133"),
    suave=colors.HexColor("#FBEEEA"),
    cabecalho_tabela=colors.HexColor("#C2402A"),
    check=colors.HexColor("#2E9E5B"),
)


def construir_estilos(tema: Tema) -> dict:
    """Cria os estilos de paragrafo usados pelos componentes.

    Parametros:
        tema: tema visual ativo (cores).
    Retorno:
        dict de ParagraphStyle indexado por nome logico.
    """
    e = {}

    e["titulo"] = ParagraphStyle(
        "titulo", fontName="Helvetica-Bold", fontSize=26,
        textColor=BRANCO, alignment=TA_CENTER, leading=30,
    )
    e["subtitulo"] = ParagraphStyle(
        "subtitulo", fontName="Helvetica", fontSize=11.5,
        textColor=colors.HexColor("#C7D3DF"), alignment=TA_CENTER, leading=15,
    )
    e["secao"] = ParagraphStyle(
        "secao", fontName="Helvetica-Bold", fontSize=14,
        textColor=tema.primaria, leading=17,
    )
    e["corpo"] = ParagraphStyle(
        "corpo", fontName="Helvetica", fontSize=10,
        textColor=TEXTO, leading=14.5,
    )
    e["bullet"] = ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=10,
        textColor=TEXTO, leading=15, leftIndent=2,
    )
    e["th"] = ParagraphStyle(
        "th", fontName="Helvetica-Bold", fontSize=9.5,
        textColor=BRANCO, alignment=TA_LEFT, leading=12,
    )
    e["td"] = ParagraphStyle(
        "td", fontName="Helvetica", fontSize=9,
        textColor=TEXTO, leading=12,
    )
    e["td_mono"] = ParagraphStyle(
        "td_mono", fontName="Courier-Bold", fontSize=9,
        textColor=tema.acento, leading=12,
    )
    e["td_res"] = ParagraphStyle(
        "td_res", fontName="Courier", fontSize=9,
        textColor=colors.HexColor("#1B5E20"), leading=12,
    )
    e["code"] = ParagraphStyle(
        "code", fontName="Courier", fontSize=8.8,
        textColor=CODE_FG, leading=12.5,
    )
    e["code_titulo"] = ParagraphStyle(
        "code_titulo", fontName="Helvetica-Bold", fontSize=10,
        textColor=BRANCO, leading=13,
    )
    e["callout_titulo"] = ParagraphStyle(
        "callout_titulo", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=tema.primaria, leading=14,
    )
    e["callout"] = ParagraphStyle(
        "callout", fontName="Helvetica", fontSize=9.5,
        textColor=TEXTO, leading=13.5,
    )
    e["autor"] = ParagraphStyle(
        "autor", fontName="Helvetica", fontSize=9.5,
        textColor=TEXTO, leading=14,
    )
    e["autor_nome"] = ParagraphStyle(
        "autor_nome", fontName="Helvetica-Bold", fontSize=11,
        textColor=tema.primaria, leading=15,
    )
    e["autor_identidade"] = ParagraphStyle(
        "autor_identidade", fontName="Helvetica", fontSize=10,
        textColor=TEXTO, leading=11, spaceBefore=0, spaceAfter=0,
    )
    e["autor_sub"] = ParagraphStyle(
        "autor_sub", fontName="Helvetica-Oblique", fontSize=10,
        textColor=tema.acento, leading=14,
    )
    e["autor_link"] = ParagraphStyle(
        "autor_link", fontName="Helvetica", fontSize=9.5,
        textColor=TEXTO, leading=14,
    )
    e["fluxo_etapa"] = ParagraphStyle(
        "fluxo_etapa", fontName="Helvetica", fontSize=8.5,
        textColor=TEXTO, alignment=TA_CENTER, leading=11,
    )
    e["fluxo_seta"] = ParagraphStyle(
        "fluxo_seta", fontName="Helvetica-Bold", fontSize=9,
        textColor=tema.acento, alignment=TA_CENTER, leading=11,
    )
    return e
