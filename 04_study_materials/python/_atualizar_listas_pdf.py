# -*- coding: utf-8 -*-
"""Insere a pagina sobre sorted() e set() no guia de listas.

Execute na raiz do repositorio:
    python 04_study_materials/python/_atualizar_listas_pdf.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import fitz

BASE = Path(__file__).resolve().parent
MATERIAIS = BASE.parent
sys.path.insert(0, str(MATERIAIS))

import _layout as layout  # noqa: E402

PDF = BASE / "Listas_em_Python.pdf"
TITULO_GUIA = "LISTAS EM PYTHON"


def _tabela_sort(page: fitz.Page, y: float) -> float:
    """Desenha tabela comparativa entre sort() e sorted()."""
    return layout.tabela(
        page,
        y,
        ["Aspecto", "sort()", "sorted()"],
        [
            ("Altera a lista original?", "Sim", "Nao"),
            ("Retorno", "None", "Nova lista"),
            ("Onde usar", "Metodo: lista.sort()", "Funcao: sorted(lista)"),
            ("Lista original depois", "Fica ordenada", "Permanece igual"),
        ],
        [170, 130, 130],
        titulo_tabela="Comparacao rapida",
    )


def pagina_sorted_set(page: fitz.Page, numero: int) -> None:
    """Preenche a pagina inserida com conteudo sobre sorted() e set()."""
    layout.cabecalho(page, TITULO_GUIA)
    y = 52

    y = layout.titulo(page, y, "Ordenacao: sort() x sorted()")
    y = layout.paragrafo(
        page,
        y,
        "As duas formas ordenam valores, mas se comportam de maneira diferente. "
        "Escolha sort() quando quiser alterar a propria lista; use sorted() quando "
        "precisar manter a original intacta.",
    )
    y = _tabela_sort(page, y)

    y = layout.paragrafo(page, y, "Exemplo com sort() — altera a lista original:")
    y = layout.codigo(
        page,
        y,
        [
            "numeros = [3, 1, 4, 1, 5]",
            "numeros.sort()",
            "print(numeros)  # [1, 1, 3, 4, 5]",
        ],
    )

    y = layout.paragrafo(page, y, "Exemplo com sorted() — cria uma nova lista ordenada:")
    y = layout.codigo(
        page,
        y,
        [
            "original = [3, 1, 4, 1, 5]",
            "ordenada = sorted(original)",
            "print(ordenada)   # [1, 1, 3, 4, 5]",
            "print(original)   # [3, 1, 4, 1, 5]  (nao mudou)",
        ],
    )

    y = layout.titulo(page, y, "Funcao set() — remover duplicatas")
    y = layout.paragrafo(
        page,
        y,
        "A funcao set() converte uma lista em conjunto e remove valores repetidos. "
        "Conjuntos nao garantem ordem; quando precisar de lista novamente, use list(set(lista)).",
    )
    y = layout.codigo(
        page,
        y,
        [
            "presencas = ['P', 'F', 'P', 'X', 'F', 'P']",
            "unicos = set(presencas)",
            "print(unicos)              # {'P', 'F', 'X'} (sem repeticao)",
            "lista_unica = list(set(presencas))",
            "print(lista_unica)         # ordem pode variar",
        ],
    )
    y = layout.paragrafo(
        page,
        y,
        "Dica: use set() para contar itens distintos ou limpar repeticoes antes de analisar dados.",
    )

    layout.rodape(page, numero)


def atualizar_numeros(doc: fitz.Document) -> None:
    """Atualiza o texto 'Pagina N' em todas as paginas do PDF."""
    for indice in range(doc.page_count):
        page = doc[indice]
        for bloco in page.get_text("dict")["blocks"]:
            if bloco.get("type") != 0:
                continue
            for linha in bloco["lines"]:
                for span in linha["spans"]:
                    if span["text"].startswith("Pagina "):
                        rect = fitz.Rect(span["bbox"])
                        page.draw_rect(rect + (-2, -2, 2, 2), color=layout.BRANCO, fill=layout.BRANCO)
        layout.rodape(page, indice + 1)


def main() -> None:
    """Insere a pagina nova e renumera o PDF de listas."""
    if not PDF.exists():
        raise FileNotFoundError(f"PDF nao encontrado: {PDF}")

    doc = fitz.open(PDF)
    if doc.page_count >= 6:
        print("PDF ja parece conter a pagina extra. Nada a fazer.")
        doc.close()
        return

    doc.new_page(2, width=layout.LARGURA_PAGINA, height=layout.ALTURA_PAGINA)
    pagina_sorted_set(doc[2], 3)
    atualizar_numeros(doc)

    temp = PDF.with_suffix(".tmp.pdf")
    doc.save(temp, garbage=4, deflate=True)
    doc.close()
    temp.replace(PDF)
    print(f"OK  {PDF.relative_to(BASE.parent.parent)}")


if __name__ == "__main__":
    main()
