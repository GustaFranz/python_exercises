# -*- coding: utf-8 -*-
"""Componentes visuais reutilizaveis (blocos de baixo acoplamento).

Cada funcao recebe os estilos e o tema ja prontos e devolve um flowable do
ReportLab. Assim o conteudo descreve "o que" mostrar e o componente cuida do
"como" mostrar, separando dados de apresentacao.
"""

from reportlab.graphics.shapes import Drawing, PolyLine
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

from .tema import (
    BRANCO,
    CODE_BG,
    CODE_COMENTARIO,
    CODE_DESTAQUE,
    LINHA,
    Tema,
    ZEBRA,
)


def _escapar(texto: str) -> str:
    """Escapa caracteres especiais de XML para uso seguro em Paragraph."""
    return (
        texto.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _check(tema: Tema, tamanho: float = 9.0) -> Drawing:
    """Cria um marcador de check vetorial (nitido em qualquer leitor)."""
    s = tamanho
    d = Drawing(s, s)
    traco = PolyLine(
        [0.12 * s, 0.52 * s, 0.40 * s, 0.24 * s, 0.86 * s, 0.82 * s],
        strokeColor=tema.check, strokeWidth=max(1.2, 0.18 * s),
        strokeLineJoin=1, strokeLineCap=1,
    )
    d.add(traco)
    return d


def _itens_com_check(estilos, tema: Tema, itens, largura, estilo):
    """Tabela de 2 colunas: check vetorial + texto, para listas amigaveis."""
    larg_check = 0.5 * cm
    linhas = []
    for item in itens:
        linhas.append([_check(tema), Paragraph(item, estilo)])
    tab = Table(linhas, colWidths=[larg_check, largura - larg_check])
    tab.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (0, -1), 2),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("LEFTPADDING", (1, 0), (1, -1), 0),
        ("TOPPADDING", (0, 0), (0, -1), 3.5),
    ]))
    return tab


def faixa_secao(estilos, tema: Tema, titulo: str, largura: float):
    """Barra de titulo de secao com marcador colorido a esquerda."""
    p = Paragraph(titulo, estilos["secao"])
    tab = Table([[p]], colWidths=[largura])
    tab.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tema.suave),
        ("LINEBEFORE", (0, 0), (0, -1), 5, tema.acento),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return tab


def lista_checks(estilos, tema: Tema, itens, largura: float):
    """Lista de itens com marcador de check verde."""
    return _itens_com_check(estilos, tema, itens, largura, estilos["bullet"])


def bloco_codigo(estilos, tema: Tema, titulo, linhas, largura: float):
    """Bloco de codigo estilo editor escuro.

    Parametros:
        titulo: rotulo do bloco; None ou vazio omite o cabecalho.
        linhas: lista de tuplas (codigo, comentario|None).
    """
    corpo = []
    for codigo, comentario in linhas:
        cod = _escapar(codigo).replace(" ", "&nbsp;") if codigo else "&nbsp;"
        if comentario:
            com = _escapar(comentario)
            texto = (f'<font color="#{CODE_DESTAQUE.hexval()[2:]}">{cod}</font>'
                     f'&nbsp;&nbsp;<font color="#{CODE_COMENTARIO.hexval()[2:]}">{com}</font>')
        else:
            texto = cod
        corpo.append([Paragraph(texto, estilos["code"])])

    tab_corpo = Table(corpo, colWidths=[largura])
    tab_corpo.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))

    if not titulo:
        return KeepTogether([tab_corpo])

    cabecalho = [[Paragraph(titulo, estilos["code_titulo"])]]
    tab_cabecalho = Table(cabecalho, colWidths=[largura])
    tab_cabecalho.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tema.acento),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return KeepTogether([tab_cabecalho, tab_corpo])


def tabela(estilos, tema: Tema, cabecalho, linhas, larguras,
           colunas_mono=None, coluna_resultado=None, titulo_tabela=None):
    """Tabela com cabecalho colorido, zebra e colunas opcionais monoespacadas."""
    colunas_mono = colunas_mono or set()
    partes = []

    if titulo_tabela:
        partes.append(Paragraph(
            f'<b>{_escapar(titulo_tabela)}</b>', estilos["corpo"]
        ))
        partes.append(Spacer(1, 0.15 * cm))

    dados = [[Paragraph(_escapar(c), estilos["th"]) for c in cabecalho]]
    for linha in linhas:
        celulas = []
        for i, valor in enumerate(linha):
            if i in colunas_mono:
                estilo = estilos["td_mono"]
            elif coluna_resultado is not None and i == coluna_resultado:
                estilo = estilos["td_res"]
            else:
                estilo = estilos["td"]
            celulas.append(Paragraph(_escapar(str(valor)), estilo))
        dados.append(celulas)

    tab = Table(dados, colWidths=larguras, repeatRows=1)
    estilo = [
        ("BACKGROUND", (0, 0), (-1, 0), tema.cabecalho_tabela),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("BOX", (0, 0), (-1, -1), 0.6, LINHA),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINHA),
    ]
    for i in range(1, len(dados)):
        if i % 2 == 0:
            estilo.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    tab.setStyle(TableStyle(estilo))
    partes.append(tab)
    return KeepTogether(partes) if len(partes) > 1 else tab


def callout(estilos, tema: Tema, titulo, texto, largura, cor_barra=None):
    """Caixa de destaque (dica, observacao, boas praticas)."""
    cor = cor_barra or tema.secundaria
    conteudo = []
    if titulo:
        conteudo.append([Paragraph(titulo, estilos["callout_titulo"])])
    if isinstance(texto, (list, tuple)):
        inner = largura - 0.95 * cm
        conteudo.append([_itens_com_check(estilos, tema, texto, inner,
                                          estilos["callout"])])
    else:
        conteudo.append([Paragraph(texto, estilos["callout"])])

    tab = Table(conteudo, colWidths=[largura])
    tab.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tema.suave),
        ("BOX", (0, 0), (-1, -1), 0.6, LINHA),
        ("LINEBEFORE", (0, 0), (0, -1), 5, cor),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return tab


def fluxo(estilos, tema: Tema, etapas, largura: float):
    """Diagrama horizontal com setas entre etapas."""
    if not etapas:
        return Spacer(1, 0)

    n = len(etapas)
    seta_larg = 0.45 * cm
    etapa_larg = (largura - seta_larg * max(0, n - 1)) / n
    linha = []
    larguras = []
    for indice, etapa in enumerate(etapas):
        linha.append(Paragraph(_escapar(etapa), estilos["fluxo_etapa"]))
        larguras.append(etapa_larg)
        if indice < n - 1:
            linha.append(Paragraph("→", estilos["fluxo_seta"]))
            larguras.append(seta_larg)

    tab = Table([linha], colWidths=larguras)
    tab.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, LINHA),
        ("BACKGROUND", (0, 0), (-1, -1), BRANCO),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return KeepTogether([
        Paragraph("<b>Fluxo:</b>", estilos["corpo"]),
        Spacer(1, 0.1 * cm),
        tab,
    ])


def arvore_pastas(estilos, tema: Tema, raiz: str, itens, largura: float):
    """Diagrama textual de arvore de diretorios em bloco monoespacado."""
    linhas = [(f"{raiz}/", None)]
    for indice, item in enumerate(itens):
        prefixo = "└── " if indice == len(itens) - 1 else "├── "
        linhas.append((f"    {prefixo}{item}", None))
    return bloco_codigo(estilos, tema, "Estrutura de pastas", linhas, largura)


def paragrafo(estilos, texto):
    """Paragrafo de corpo simples."""
    return Paragraph(texto, estilos["corpo"])


def espaco(altura=0.35):
    """Espacador vertical em centimetros."""
    return Spacer(1, altura * cm)
