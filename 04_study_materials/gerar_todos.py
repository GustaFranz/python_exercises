# -*- coding: utf-8 -*-
"""Gera todos os PDFs de estudo com layout unificado (ReportLab).

Execute na raiz do repositorio:
    python 04_study_materials/gerar_todos.py

Depois, atualize os cards do README:
    python 04_study_materials/_gerar_previews.py
"""

from pathlib import Path

from gerador import gerar_pdf
from gerador.conteudo import MATERIAIS

BASE = Path(__file__).resolve().parent

DESTINOS = {
    "Dicionarios em Python": BASE / "python" / "Dicionarios_em_Python.pdf",
    "Listas em Python": BASE / "python" / "Listas_em_Python.pdf",
    "Tuplas em Python": BASE / "python" / "Tuplas_em_Python.pdf",
    "Tratamento de Strings em Python": BASE / "python" / "Tratamento_de_Strings_em_Python.pdf",
    "Git para iniciantes": BASE / "git" / "Git_para_iniciantes.pdf",
    "Pathlib e Shutil em Python": BASE / "python" / "Pathlib_e_Shutil_em_Python.pdf",
    "EasyAnsi em Python": BASE / "easyansi" / "EasyAnsi_em_Python.pdf",
}


def main() -> None:
    """Gera cada material registrado em MATERIAIS no destino correspondente."""
    for nome, spec in MATERIAIS.items():
        destino = DESTINOS.get(nome)
        if destino is None:
            raise KeyError(f"Destino nao configurado para: {nome}")
        destino.parent.mkdir(parents=True, exist_ok=True)
        gerar_pdf(spec, destino)
        print(f"OK  ->  {destino.relative_to(BASE.parent)}")
    print(f"\n{len(MATERIAIS)} PDFs gerados.")


if __name__ == "__main__":
    main()
