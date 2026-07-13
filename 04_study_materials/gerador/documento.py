# -*- coding: utf-8 -*-
"""Montagem do documento PDF a partir de uma especificacao de conteudo.

Responsabilidade unica: orquestrar capa, cabecalho/rodape, assinatura do autor
e traduzir a lista de "blocos" (dados) em flowables (apresentacao), usando os
componentes reutilizaveis. Nao contem nenhum conteudo didatico.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from . import componentes as c
from .tema import LINHA, Tema, construir_estilos

AUTOR_NOME = "Prof. Gustavo Franz (Science/Biology)"
AUTOR_SUBTITULO_1 = "Python Developer in Progress"
AUTOR_SUBTITULO_2 = "Building Educational Solutions with Python"
AUTOR_LINHA = (
    "Professor de Ciencias e Biologia desde 2013 — atualmente estudando Programacao."
)
AUTOR_MENSAGEM = (
    "Eu crio estes resumos para organizar os assuntos e estudar de forma clara e "
    "objetiva. Estou compartilhando porque eles tambem podem ajudar outros "
    "desenvolvedores que estao comecando. Bons estudos — vamos aprender juntos!"
)

GITHUB_URL = "https://github.com/GustaFranz"
GITHUB_LABEL = "github.com/GustaFranz"
REPO_EXERCICIOS_URL = "https://github.com/GustaFranz/python_exercises"
REPO_EXERCICIOS_LABEL = "github.com/GustaFranz/python_exercises"
REPO_EXERCICIOS_DESC = (
    "Para quem quiser ver a resolucao dos meus exercicios em Python."
)
REPO_EASYANSI_URL = "https://github.com/GustaFranz/easyansi"
REPO_EASYANSI_LABEL = "github.com/GustaFranz/easyansi"
REPO_EASYANSI_DESC = (
    "Para quem quiser codificar personalizando com cores e estilos de forma "
    "mais facil, pratica e intuitiva."
)


def _link(url: str, rotulo: str, tema: Tema) -> str:
    """Retorna HTML de link clicavel com cor do tema."""
    cor = tema.acento.hexval()[2:]
    return f'<a href="{url}"><font color="#{cor}"><u>{rotulo}</u></font></a>'


MARGEM = 1.4 * cm
TOPO = 2.2 * cm
RODAPE = 1.6 * cm


def _largura_util():
    largura, _ = A4
    return largura - 2 * MARGEM


def _capa(estilos, tema: Tema, topico, destaque, subtitulo, simbolo):
    """Faixa-titulo no topo da primeira pagina."""
    largura = _largura_util()
    cor_dest = tema.secundaria.hexval()[2:]
    titulo_html = f'{topico} <font color="#{cor_dest}">{destaque}</font>'
    if simbolo:
        titulo_html += f'   <font color="#{cor_dest}">{simbolo}</font>'

    conteudo = [
        [Paragraph(titulo_html, estilos["titulo"])],
        [Paragraph(subtitulo, estilos["subtitulo"])],
    ]
    tab = Table(conteudo, colWidths=[largura])
    tab.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tema.primaria),
        ("TOPPADDING", (0, 0), (-1, 0), 16),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 16),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
    ]))
    return tab


def _cartao(estilos, tema: Tema, linhas_paragrafo, estilos_linha=None):
    """Cartao com borda lateral colorida (reutilizado no inicio e no fim)."""
    largura = _largura_util()
    estilos_linha = estilos_linha or [estilos["autor"]] * len(linhas_paragrafo)
    conteudo = [[Paragraph(html, est)] for html, est in zip(linhas_paragrafo, estilos_linha)]
    tab = Table(conteudo, colWidths=[largura])
    tab.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tema.suave),
        ("BOX", (0, 0), (-1, -1), 0.6, LINHA),
        ("LINEBEFORE", (0, 0), (0, -1), 5, tema.acento),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return tab


def _html_identidade(tema: Tema) -> str:
    """Tres linhas de apresentacao em bloco unico, com espacamento compacto."""
    cor_nome = tema.primaria.hexval()[2:]
    cor_sub = tema.acento.hexval()[2:]
    return (
        f'<font name="Helvetica-Bold" size="11" color="#{cor_nome}">{AUTOR_NOME}</font><br/>'
        f'<font name="Helvetica-Oblique" size="10" color="#{cor_sub}">{AUTOR_SUBTITULO_1}</font><br/>'
        f'<font name="Helvetica-Oblique" size="10" color="#{cor_sub}">{AUTOR_SUBTITULO_2}</font>'
    )


def _intro_github(estilos, tema: Tema):
    """Cartao inicial com apresentacao e link do GitHub."""
    linhas_html = [
        _html_identidade(tema),
        f'<b>GitHub:</b> {_link(GITHUB_URL, GITHUB_LABEL, tema)}',
    ]
    estilos_linha = [estilos["autor_identidade"], estilos["autor_link"]]
    return KeepTogether([_cartao(estilos, tema, linhas_html, estilos_linha)])


def _assinatura(estilos, tema: Tema):
    """Cartao final com apresentacao, mensagem e links dos repositorios."""
    linhas_html = [
        _html_identidade(tema),
        AUTOR_LINHA,
        AUTOR_MENSAGEM,
        f'<b>GitHub:</b> {_link(GITHUB_URL, GITHUB_LABEL, tema)}',
        (f'<b>Exercicios Python:</b> {_link(REPO_EXERCICIOS_URL, REPO_EXERCICIOS_LABEL, tema)}'
         f'<br/>{REPO_EXERCICIOS_DESC}'),
        (f'<b>EasyAnsi:</b> {_link(REPO_EASYANSI_URL, REPO_EASYANSI_LABEL, tema)}'
         f'<br/>{REPO_EASYANSI_DESC}'),
    ]
    estilos_linha = [
        estilos["autor_identidade"],
        estilos["autor"],
        estilos["autor"],
        estilos["autor_link"],
        estilos["autor_link"],
        estilos["autor_link"],
    ]

    return KeepTogether([Spacer(1, 0.3 * cm), _cartao(estilos, tema, linhas_html, estilos_linha)])


def _moldura(tema: Tema, topico_limpo, nota_rodape: str = ""):
    """Retorna a funcao onPage que desenha cabecalho e rodape correntes."""

    def desenhar(canvas, doc):
        largura, altura = A4
        canvas.saveState()

        canvas.setFillColor(tema.primaria)
        canvas.rect(0, altura - 0.95 * cm, largura, 0.95 * cm, fill=1, stroke=0)
        canvas.setFillColor(colors.white)
        canvas.setFont("Helvetica-Bold", 8.5)
        canvas.drawString(MARGEM, altura - 0.62 * cm, topico_limpo.upper())
        canvas.setFont("Helvetica", 8.5)
        canvas.drawRightString(largura - MARGEM, altura - 0.62 * cm,
                               f"Material do {AUTOR_NOME}")

        canvas.setStrokeColor(LINHA)
        canvas.setLineWidth(0.5)
        canvas.line(MARGEM, 1.15 * cm, largura - MARGEM, 1.15 * cm)
        canvas.setFillColor(colors.HexColor("#55606E"))
        canvas.setFont("Helvetica", 8)
        if nota_rodape:
            canvas.setFont("Helvetica", 7.5)
            canvas.drawString(MARGEM, 0.82 * cm, nota_rodape)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(MARGEM, 0.7 * cm,
                          f"{AUTOR_SUBTITULO_1} — {GITHUB_LABEL}")
        canvas.drawRightString(largura - MARGEM, 0.7 * cm,
                               f"Pagina {canvas.getPageNumber()}")
        canvas.restoreState()

    return desenhar


def _renderizar_bloco(bloco, estilos, tema: Tema):
    """Traduz um bloco de dados em um flowable usando os componentes."""
    largura = _largura_util()
    tipo = bloco["tipo"]

    if tipo == "secao":
        return c.faixa_secao(estilos, tema, bloco["titulo"], largura)
    if tipo == "checks":
        return c.lista_checks(estilos, tema, bloco["itens"], largura)
    if tipo == "codigo":
        return c.bloco_codigo(estilos, tema, bloco.get("titulo"), bloco["linhas"], largura)
    if tipo == "paragrafo":
        return c.paragrafo(estilos, bloco["texto"])
    if tipo == "espaco":
        return c.espaco(bloco.get("altura", 0.35))
    if tipo == "callout":
        cor = bloco.get("cor")
        cor_barra = colors.HexColor(cor) if cor else None
        return c.callout(estilos, tema, bloco.get("titulo"),
                         bloco["texto"], largura, cor_barra)
    if tipo == "tabela":
        fracoes = bloco["larguras"]
        larguras = [largura * f for f in fracoes]
        return c.tabela(
            estilos, tema, bloco["cabecalho"], bloco["linhas"], larguras,
            colunas_mono=set(bloco.get("mono", [])),
            coluna_resultado=bloco.get("resultado"),
            titulo_tabela=bloco.get("titulo_tabela"),
        )
    if tipo == "fluxo":
        return c.fluxo(estilos, tema, bloco["etapas"], largura)
    if tipo == "arvore":
        return c.arvore_pastas(estilos, tema, bloco["raiz"], bloco["itens"], largura)
    raise ValueError(f"Tipo de bloco desconhecido: {tipo}")


def gerar_pdf(spec: dict, destino: Path):
    """Gera um PDF a partir da especificacao de conteudo.

    Parametros:
        spec: dict com chaves tema, topico, destaque, subtitulo, simbolo, blocos.
        destino: caminho do arquivo PDF a ser criado.
    Retorno:
        Path do arquivo gerado.
    """
    tema: Tema = spec["tema"]
    estilos = construir_estilos(tema)
    destino = Path(destino)

    doc = BaseDocTemplate(
        str(destino), pagesize=A4,
        leftMargin=MARGEM, rightMargin=MARGEM,
        topMargin=TOPO, bottomMargin=RODAPE,
        title=f"{spec['topico']} {spec['destaque']}".strip(),
        author=AUTOR_NOME, subject="Material de estudo de programacao",
    )
    largura, altura = A4
    frame = Frame(
        MARGEM, RODAPE, largura - 2 * MARGEM, altura - TOPO - RODAPE,
        id="principal", leftPadding=0, rightPadding=0,
        topPadding=0, bottomPadding=0,
    )
    topico_limpo = f"{spec['topico']} {spec['destaque']}".strip()
    nota_rodape = spec.get("nota_rodape", "")
    doc.addPageTemplates([
        PageTemplate(
            id="pad",
            frames=[frame],
            onPage=_moldura(tema, topico_limpo, nota_rodape),
        )
    ])

    elementos = [
        _capa(estilos, tema, spec["topico"], spec["destaque"],
              spec["subtitulo"], spec.get("simbolo", "")),
        Spacer(1, 0.35 * cm),
        _intro_github(estilos, tema),
        Spacer(1, 0.35 * cm),
    ]
    for bloco in spec["blocos"]:
        elementos.append(_renderizar_bloco(bloco, estilos, tema))
        if bloco["tipo"] in {"secao"}:
            elementos.append(Spacer(1, 0.15 * cm))
        else:
            elementos.append(Spacer(1, 0.28 * cm))

    elementos.append(_assinatura(estilos, tema))
    doc.build(elementos)
    return destino
