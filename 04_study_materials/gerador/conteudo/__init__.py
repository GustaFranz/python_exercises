"""Conteudo didatico de cada material (dados puros, sem renderizacao).

Cada modulo expoe a variavel `SPEC`, um dicionario que descreve o material:
tema, titulo, subtitulo e a lista de blocos. Isso mantem o conteudo desacoplado
do motor de geracao, facilitando adicionar novos materiais no futuro.
"""

from . import dicionarios, easyansi, git, listas, pathlib_shutil, strings, tuplas

# Registro central: nome do arquivo de saida -> especificacao do material.
MATERIAIS = {
    "Dicionarios em Python": dicionarios.SPEC,
    "EasyAnsi em Python": easyansi.SPEC,
    "Git para iniciantes": git.SPEC,
    "Listas em Python": listas.SPEC,
    "Pathlib e Shutil em Python": pathlib_shutil.SPEC,
    "Tratamento de Strings em Python": strings.SPEC,
    "Tuplas em Python": tuplas.SPEC,
}

__all__ = ["MATERIAIS"]
