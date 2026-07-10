# -*- coding: utf-8 -*-
"""Layout compartilhado para geracao de PDFs educacionais.

Funcoes reutilizaveis de cabecalho, rodape, texto, codigo, tabelas e diagramas.
Usado pelos scripts em 04_study_materials/python/, 04_study_materials/easyansi/ e similares.
"""

from __future__ import annotations

from pathlib import Path

import fitz

# Paleta padrao dos materiais
AZUL = (0.22, 0.46, 0.73)
VERDE = (0.18, 0.49, 0.20)
CINZA = (0.33, 0.33, 0.33)
PRETO = (0, 0, 0)
BRANCO = (1, 1, 1)
FUNDO_CODIGO = (0.95, 0.97, 0.99)
BORDA_CODIGO = (0.9, 0.92, 0.95)
FUNDO_CAIXA = (0.96, 0.98, 1.0)
BORDA_CAIXA = (0.82, 0.86, 0.92)

LARGURA_PAGINA = 595
ALTURA_PAGINA = 842
MARGEM_X = 40
LARGURA_TEXTO = LARGURA_PAGINA - 80
Y_MAX = 788


def novo_documento() -> fitz.Document:
    """Cria documento PDF vazio no tamanho A4."""
    return fitz.open()


def nova_pagina(doc: fitz.Document) -> fitz.Page:
    """Adiciona pagina A4 ao documento e retorna a referencia."""
    return doc.new_page(width=LARGURA_PAGINA, height=ALTURA_PAGINA)


def salvar_pdf(doc: fitz.Document, destino: Path) -> None:
    """Salva documento com compactacao e substitui arquivo existente."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporario = destino.with_suffix(".tmp.pdf")
    doc.save(temporario, garbage=4, deflate=True)
    doc.close()
    temporario.replace(destino)


def cabecalho(page: fitz.Page, titulo_guia: str, *, cor_faixa: tuple[float, float, float] = AZUL) -> None:
    """Desenha faixa superior, rodape do autor e titulo do guia.

    Args:
        page: pagina PyMuPDF.
        titulo_guia: texto em caixa alta na faixa azul.
        cor_faixa: cor RGB normalizada da faixa superior.
    """
    page.draw_rect(fitz.Rect(0, 0, page.rect.width, 28), color=cor_faixa, fill=cor_faixa)
    page.insert_text(
        (MARGEM_X, 19),
        titulo_guia.upper(),
        fontsize=8.5,
        fontname="hebo",
        color=BRANCO,
    )
    page.insert_text(
        (MARGEM_X, 805),
        "Material do Prof. Gustavo Franz (Science/Biology)",
        fontsize=8.5,
        fontname="helv",
        color=PRETO,
    )
    page.insert_text(
        (MARGEM_X, 817),
        "Python Developer in Progress · github.com/GustaFranz",
        fontsize=8.0,
        fontname="helv",
        color=CINZA,
    )


def rodape(page: fitz.Page, numero: int, *, nota: str = "") -> None:
    """Desenha numero da pagina e nota opcional no rodape.

    Args:
        page: pagina PyMuPDF.
        numero: numero da pagina (1-based).
        nota: texto extra a esquerda do numero (ex.: fonte oficial).
    """
    if nota:
        page.insert_text((MARGEM_X, 824), nota, fontsize=7.5, fontname="helv", color=CINZA)
    page.insert_text(
        (524, 824),
        f"Pagina {numero}",
        fontsize=8.0,
        fontname="helv",
        color=CINZA,
    )


def iniciar_pagina(
    page: fitz.Page,
    titulo_guia: str,
    numero: int,
    *,
    cor_faixa: tuple[float, float, float] = AZUL,
    nota_rodape: str = "",
) -> float:
    """Prepara pagina interna e retorna posicao Y inicial do conteudo."""
    cabecalho(page, titulo_guia, cor_faixa=cor_faixa)
    rodape(page, numero, nota=nota_rodape)
    return 52.0


def titulo(page: fitz.Page, y: float, texto: str, *, tamanho: float = 14) -> float:
    """Insere titulo de secao e retorna Y seguinte."""
    page.insert_text((MARGEM_X, y), texto, fontsize=tamanho, fontname="hebo", color=AZUL)
    return y + 22


def subtitulo(page: fitz.Page, y: float, texto: str) -> float:
    """Insere subtitulo menor e retorna Y seguinte."""
    page.insert_text((MARGEM_X, y), texto, fontsize=11, fontname="hebo", color=PRETO)
    return y + 18


def paragrafo(page: fitz.Page, y: float, texto: str, *, indent: float = 0) -> float:
    """Insere paragrafo com quebra de linha automatica."""
    x = MARGEM_X + indent
    largura = LARGURA_TEXTO - indent
    if fitz.get_text_length(texto, fontname="helv", fontsize=10) <= largura:
        page.insert_text((x, y), texto, fontsize=10, fontname="helv", color=PRETO)
        return y + 16

    palavras = texto.split()
    linha = ""
    for palavra in palavras:
        teste = f"{linha} {palavra}".strip()
        if fitz.get_text_length(teste, fontname="helv", fontsize=10) <= largura:
            linha = teste
        else:
            page.insert_text((x, y), linha, fontsize=10, fontname="helv", color=PRETO)
            y += 14
            linha = palavra
    if linha:
        page.insert_text((x, y), linha, fontsize=10, fontname="helv", color=PRETO)
        y += 14
    return y + 4


def item_lista(page: fitz.Page, y: float, texto: str, *, marcador: str = "•") -> float:
    """Insere item de lista com marcador e retorna Y seguinte."""
    page.insert_text((MARGEM_X + 8, y), marcador, fontsize=10, fontname="helv", color=AZUL)
    return paragrafo(page, y, texto, indent=20)


def codigo(page: fitz.Page, y: float, linhas: list[str]) -> float:
    """Insere bloco de codigo monoespacado com fundo cinza."""
    altura = 14 * len(linhas) + 12
    page.draw_rect(
        fitz.Rect(36, y - 10, page.rect.width - 36, y + altura - 10),
        color=BORDA_CODIGO,
        fill=FUNDO_CODIGO,
        width=0.5,
    )
    for indice, linha in enumerate(linhas):
        page.insert_text(
            (44, y + indice * 14),
            linha,
            fontsize=9,
            fontname="cour",
            color=PRETO,
        )
    return y + altura + 8


def tabela(
    page: fitz.Page,
    y: float,
    cabecalhos: list[str],
    linhas: list[tuple[str, ...]],
    colunas: list[int],
    *,
    titulo_tabela: str = "",
) -> float:
    """Desenha tabela com cabecalho azul e retorna Y seguinte.

    Args:
        page: pagina PyMuPDF.
        y: posicao vertical inicial.
        cabecalhos: textos do cabecalho.
        linhas: tuplas com valores por coluna.
        colunas: larguras das colunas em pontos.
        titulo_tabela: rotulo opcional acima da tabela.
    """
    x0 = MARGEM_X
    altura_linha = 18
    if titulo_tabela:
        page.insert_text((x0, y), titulo_tabela, fontsize=11, fontname="hebo", color=PRETO)
        y += 16

    xs = [x0]
    for largura in colunas[:-1]:
        xs.append(xs[-1] + largura)

    for indice, texto in enumerate(cabecalhos):
        page.draw_rect(
            fitz.Rect(xs[indice], y, xs[indice] + colunas[indice], y + altura_linha),
            color=AZUL,
            fill=AZUL,
            width=0.5,
        )
        page.insert_text(
            (xs[indice] + 6, y + 12),
            texto,
            fontsize=9,
            fontname="hebo",
            color=BRANCO,
        )

    y += altura_linha
    for linha in linhas:
        for indice, texto in enumerate(linha):
            page.draw_rect(
                fitz.Rect(xs[indice], y, xs[indice] + colunas[indice], y + altura_linha),
                color=BORDA_CAIXA,
                fill=FUNDO_CAIXA if indice == 0 else BRANCO,
                width=0.5,
            )
            page.insert_text(
                (xs[indice] + 6, y + 12),
                texto,
                fontsize=8.5,
                fontname="helv",
                color=PRETO,
            )
        y += altura_linha
    return y + 10


def comparacao(
    page: fitz.Page,
    y: float,
    titulo_tabela: str,
    cabecalhos: list[str],
    linhas: list[tuple[str, ...]],
    colunas: list[int] | None = None,
) -> float:
    """Atalho para tabela comparativa de duas ou mais colunas."""
    if colunas is None:
        restante = LARGURA_TEXTO - 120
        meio = restante // (len(cabecalhos) - 1)
        colunas = [120] + [meio] * (len(cabecalhos) - 1)
    return tabela(page, y, cabecalhos, linhas, colunas, titulo_tabela=titulo_tabela)


def caixa(page: fitz.Page, y: float, titulo: str, linhas: list[str]) -> float:
    """Desenha bloco com borda para destacar um conceito."""
    altura = 18 + 14 * len(linhas) + 10
    page.draw_rect(
        fitz.Rect(36, y - 4, page.rect.width - 36, y + altura - 4),
        color=BORDA_CAIXA,
        fill=FUNDO_CAIXA,
        width=1,
    )
    page.insert_text((44, y + 10), titulo, fontsize=10, fontname="hebo", color=AZUL)
    pos = y + 26
    for linha in linhas:
        page.insert_text((48, pos), linha, fontsize=9.5, fontname="helv", color=PRETO)
        pos += 14
    return y + altura + 8


def fluxo(page: fitz.Page, y: float, etapas: list[str]) -> float:
    """Desenha fluxo horizontal com setas entre etapas."""
    if not etapas:
        return y
    page.insert_text((MARGEM_X, y), "Fluxo:", fontsize=10, fontname="hebo", color=PRETO)
    y += 18
    x = MARGEM_X
    for indice, etapa in enumerate(etapas):
        largura = max(70, int(fitz.get_text_length(etapa, fontname="helv", fontsize=9)) + 16)
        page.draw_rect(
            fitz.Rect(x, y, x + largura, y + 22),
            color=BORDA_CAIXA,
            fill=BRANCO,
            width=0.8,
        )
        page.insert_text((x + 6, y + 14), etapa, fontsize=9, fontname="helv", color=PRETO)
        x += largura + 4
        if indice < len(etapas) - 1:
            page.insert_text((x, y + 14), "->", fontsize=9, fontname="hebo", color=AZUL)
            x += 18
    return y + 34


def arvore_pastas(page: fitz.Page, y: float, raiz: str, itens: list[str]) -> float:
    """Desenha diagrama textual de arvore de diretorios."""
    page.insert_text((MARGEM_X, y), f"{raiz}/", fontsize=10, fontname="hebo", color=AZUL)
    y += 16
    for indice, item in enumerate(itens):
        prefixo = "└── " if indice == len(itens) - 1 else "├── "
        page.insert_text(
            (MARGEM_X + 12, y),
            f"{prefixo}{item}",
            fontsize=9.5,
            fontname="cour",
            color=PRETO,
        )
        y += 14
    return y + 6


def capa(
    page: fitz.Page,
    titulo_principal: str,
    subtitulo: str,
    topicos: list[str],
    *,
    titulo_guia: str = "",
    cor_faixa: tuple[float, float, float] = AZUL,
) -> None:
    """Monta pagina de capa com faixa, titulo e topicos."""
    cabecalho(page, titulo_guia or titulo_principal, cor_faixa=cor_faixa)
    page.draw_rect(fitz.Rect(0, 28, page.rect.width, 120), color=cor_faixa, fill=cor_faixa)
    page.insert_text((MARGEM_X, 78), titulo_principal, fontsize=22, fontname="hebo", color=BRANCO)
    page.insert_text((MARGEM_X, 102), subtitulo, fontsize=12, fontname="helv", color=BRANCO)

    y = 150
    y = titulo(page, y, "Para quem e este guia")
    for topico in topicos:
        y = item_lista(page, y, topico)

    page.insert_text(
        (MARGEM_X, 790),
        "Prof. Gustavo Franz · Science/Biology · Python Developer in Progress",
        fontsize=9,
        fontname="helv",
        color=CINZA,
    )


def indice_visual(page: fitz.Page, titulo_guia: str, itens: list[tuple[str, str]], numero: int) -> None:
    """Monta pagina de indice com secao e pagina de destino."""
    y = iniciar_pagina(page, titulo_guia, numero)
    y = titulo(page, y, "Indice do guia")
    y = paragrafo(
        page,
        y,
        "Use este indice para ir direto ao tema. Cada secao traz exemplos copiaveis "
        "e diagramas para facilitar o estudo.",
    )
    y += 6
    for secao, pagina_destino in itens:
        page.insert_text((MARGEM_X, y), secao, fontsize=10, fontname="helv", color=PRETO)
        page.insert_text((480, y), pagina_destino, fontsize=10, fontname="hebo", color=AZUL)
        y += 18


def _altura_paragrafo(texto: str, *, indent: float = 0) -> float:
    """Estima altura vertical de um paragrafo."""
    largura = LARGURA_TEXTO - indent
    if fitz.get_text_length(texto, fontname="helv", fontsize=10) <= largura:
        return 16
    linhas = 1
    palavras = texto.split()
    linha = ""
    for palavra in palavras:
        teste = f"{linha} {palavra}".strip()
        if fitz.get_text_length(teste, fontname="helv", fontsize=10) <= largura:
            linha = teste
        else:
            linhas += 1
            linha = palavra
    return linhas * 14 + 4


def _altura_codigo(linhas: list[str]) -> float:
    """Estima altura de bloco de codigo."""
    return 14 * len(linhas) + 20


def _altura_tabela(
    cabecalhos: list[str],
    linhas: list[tuple[str, ...]],
    *,
    titulo_tabela: str = "",
) -> float:
    """Estima altura de tabela."""
    altura = 18 * (len(linhas) + 1) + 10
    if titulo_tabela:
        altura += 16
    return altura


def _altura_caixa(linhas: list[str]) -> float:
    """Estima altura de caixa de destaque."""
    return 18 + 14 * len(linhas) + 18


def _altura_fluxo(etapas: list[str]) -> float:
    """Estima altura de diagrama de fluxo."""
    return 52 if etapas else 0


def _altura_arvore(itens: list[str]) -> float:
    """Estima altura de arvore de pastas."""
    return 16 + 14 * len(itens) + 6


class Compositor:
    """Empacota secoes inteiras em paginas sem cortar blocos no meio."""

    def __init__(
        self,
        doc: fitz.Document,
        titulo_guia: str,
        *,
        cor_faixa: tuple[float, float, float] = AZUL,
        nota_rodape: str = "",
    ) -> None:
        self.doc = doc
        self.titulo_guia = titulo_guia
        self.cor_faixa = cor_faixa
        self.nota_rodape = nota_rodape
        self.page: fitz.Page | None = None
        self.y = 52.0
        self.numero = 0

    def _abrir_pagina(self) -> None:
        """Cria nova pagina interna com cabecalho e rodape."""
        self.numero += 1
        self.page = nova_pagina(self.doc)
        self.y = iniciar_pagina(
            self.page,
            self.titulo_guia,
            self.numero,
            cor_faixa=self.cor_faixa,
            nota_rodape=self.nota_rodape,
        )

    def _pagina(self) -> fitz.Page:
        if self.page is None:
            self._abrir_pagina()
        return self.page

    def cabe(self, altura: float) -> bool:
        """Verifica se bloco inteiro cabe na pagina atual."""
        return self.y + altura <= Y_MAX

    def garantir_bloco(self, altura: float) -> None:
        """Abre nova pagina se bloco nao couber inteiro na atual."""
        if self.page is None or not self.cabe(altura):
            self._abrir_pagina()

    def titulo_secao(self, texto: str, *, tamanho: float = 14) -> None:
        """Insere titulo de secao com quebra de pagina previa se necessario."""
        altura = 24 if tamanho >= 14 else 20
        self.garantir_bloco(altura)
        self.y = titulo(self._pagina(), self.y, texto, tamanho=tamanho)

    def paragrafo(self, texto: str, *, indent: float = 0) -> None:
        """Insere paragrafo atomico."""
        altura = _altura_paragrafo(texto, indent=indent)
        self.garantir_bloco(altura)
        self.y = paragrafo(self._pagina(), self.y, texto, indent=indent)

    def codigo(self, linhas: list[str]) -> None:
        """Insere bloco de codigo atomico."""
        altura = _altura_codigo(linhas)
        self.garantir_bloco(altura)
        self.y = codigo(self._pagina(), self.y, linhas)

    def tabela(
        self,
        cabecalhos: list[str],
        linhas: list[tuple[str, ...]],
        colunas: list[int],
        *,
        titulo_tabela: str = "",
    ) -> None:
        """Insere tabela atomica."""
        altura = _altura_tabela(cabecalhos, linhas, titulo_tabela=titulo_tabela)
        self.garantir_bloco(altura)
        self.y = tabela(
            self._pagina(),
            self.y,
            cabecalhos,
            linhas,
            colunas,
            titulo_tabela=titulo_tabela,
        )

    def comparacao(
        self,
        titulo_tabela: str,
        cabecalhos: list[str],
        linhas: list[tuple[str, ...]],
        colunas: list[int] | None = None,
    ) -> None:
        """Insere tabela comparativa atomica."""
        if colunas is None:
            restante = LARGURA_TEXTO - 120
            meio = restante // (len(cabecalhos) - 1)
            colunas = [120] + [meio] * (len(cabecalhos) - 1)
        altura = _altura_tabela(cabecalhos, linhas, titulo_tabela=titulo_tabela)
        self.garantir_bloco(altura)
        self.y = comparacao(self._pagina(), self.y, titulo_tabela, cabecalhos, linhas, colunas)

    def caixa(self, titulo: str, linhas: list[str]) -> None:
        """Insere caixa de destaque atomica."""
        altura = _altura_caixa(linhas)
        self.garantir_bloco(altura)
        self.y = caixa(self._pagina(), self.y, titulo, linhas)

    def fluxo(self, etapas: list[str]) -> None:
        """Insere fluxo atomico."""
        altura = _altura_fluxo(etapas)
        self.garantir_bloco(altura)
        self.y = fluxo(self._pagina(), self.y, etapas)

    def arvore_pastas(self, raiz: str, itens: list[str]) -> None:
        """Insere arvore de pastas atomica."""
        altura = _altura_arvore(itens)
        self.garantir_bloco(altura)
        self.y = arvore_pastas(self._pagina(), self.y, raiz, itens)

    def subtitulo(self, texto: str) -> None:
        """Insere subtitulo atomico."""
        self.garantir_bloco(20)
        self.y = subtitulo(self._pagina(), self.y, texto)

    def espaco(self, pixels: float = 8) -> None:
        """Adiciona espacamento vertical pequeno entre blocos."""
        self.y += pixels
