"""Motor modular para gerar PDFs didaticos de programacao.

Separa responsabilidades em modulos independentes:
- tema:        cores, fontes e estilos de paragrafo.
- componentes: blocos visuais reutilizaveis (cards, tabelas, codigo, callouts).
- documento:   monta o PDF final a partir de uma especificacao de conteudo.

O conteudo de cada material vive em `gerador.conteudo` e e totalmente
desacoplado da renderizacao, permitindo reaproveitar o motor para novos temas.
"""

from .documento import gerar_pdf
from .tema import Tema, TEMA_GIT, TEMA_PYTHON

__all__ = ["gerar_pdf", "Tema", "TEMA_PYTHON", "TEMA_GIT"]
