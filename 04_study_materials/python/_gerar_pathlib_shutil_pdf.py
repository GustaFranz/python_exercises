# -*- coding: utf-8 -*-
"""Gera o guia PDF Pathlib_e_Shutil_em_Python.pdf.

Execute na raiz do repositorio:
    python 04_study_materials/python/_gerar_pathlib_shutil_pdf.py

Conteudo baseado na documentacao oficial Python 3.14.6 (pathlib e shutil).
"""

from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
MATERIAIS = BASE.parent
sys.path.insert(0, str(MATERIAIS))

import _layout as layout  # noqa: E402

PDF = BASE / "Pathlib_e_Shutil_em_Python.pdf"
TITULO_GUIA = "PATHLIB E SHUTIL"
NOTA_OFICIAL = "Baseado na documentacao oficial Python 3.14.6"
COR_FAIXA = layout.VERDE


def _conteudo(c: layout.Compositor) -> None:
    """Define todo o conteudo do guia em fluxo continuo."""
    c.titulo_secao("Importar Path e operador /")
    c.paragrafo(
        "Path e a classe principal para caminhos concretos. Ela representa um caminho "
        "real no disco da plataforma em que o codigo roda.",
    )
    c.codigo(
        [
            "from pathlib import Path",
            "",
            "pasta = Path('dados')",
            "arquivo = pasta / 'simulado_7ano.csv'",
            "print(arquivo)  # dados/simulado_7ano.csv",
        ],
    )
    c.titulo_secao("__file__ e .parent")
    c.paragrafo(
        "__file__ guarda o caminho do script em execucao. Com .parent voce sobe um nivel "
        "na arvore de pastas — essencial para achar dados/ sem caminho fixo.",
    )
    c.codigo(
        [
            "pasta_projeto = Path(__file__).resolve().parent",
            "pasta_dados = pasta_projeto / 'dados'",
            "print(pasta_projeto)",
            "print(pasta_dados.exists())",
        ],
    )
    c.caixa(
        "Regra de ouro",
        [
            "Nunca use C:/Users/... fixo no codigo.",
            "Use Path(__file__).parent para achar a pasta do exercicio.",
        ],
    )

    c.titulo_secao("Arvore de pastas do projeto boletim")
    c.paragrafo(
        "No projeto automacao-dashboard-boletim-escolar, os modulos ficam em src/ e "
        "acessam dados/ e saidas/ na raiz com .parent.parent.",
    )
    c.arvore_pastas(
        "automacao-dashboard-boletim-escolar",
        [
            "src/",
            "  leitor_simulados.py",
            "  automacao_portal.py",
            "  consolidacao.py",
            "dados/",
            "  simulados/",
            "  provas/",
            "saidas/",
            "  boletins/",
        ],
    )
    c.codigo(
        [
            "# Script em src/main.py",
            "raiz = Path(__file__).resolve().parent.parent",
            "pasta_simulados = raiz / 'dados' / 'simulados'",
            "pasta_saidas = raiz / 'saidas' / 'boletins'",
        ],
    )
    c.fluxo(["src/main.py", ".parent", ".parent", "raiz do projeto"])

    c.titulo_secao("Propriedades do caminho")
    c.codigo(
        [
            "caminho = Path('dados/simulado_7ano.csv')",
            "",
            "caminho.name      # simulado_7ano.csv",
            "caminho.stem      # simulado_7ano",
            "caminho.suffix    # .csv",
            "caminho.parent    # dados",
            "caminho.parts     # ('dados', 'simulado_7ano.csv')",
        ],
    )
    c.tabela(
        ["Propriedade", "Retorna", "Exemplo"],
        [
            (".name", "Nome com extensao", "notas.csv"),
            (".stem", "Nome sem extensao", "notas"),
            (".suffix", "Extensao", ".csv"),
            (".parent", "Pasta pai", "dados/"),
            (".parts", "Tupla de partes", "('/', 'etc', 'hosts')"),
        ],
        [90, 150, 235],
        titulo_tabela="Referencia rapida",
    )

    c.titulo_secao("exists(), is_file(), is_dir()")
    c.fluxo(["Caminho", "exists()?", "is_file()?", "Agir com seguranca"])
    c.codigo(
        [
            "arquivo = pasta_dados / 'simulado_7ano.csv'",
            "",
            "if arquivo.exists():",
            "    print('Arquivo encontrado')",
            "if arquivo.is_file():",
            "    print('E um arquivo')",
            "if pasta_dados.is_dir():",
            "    print('E uma pasta')",
        ],
    )
    c.caixa(
        "Padrao do projeto real",
        [
            "Sempre verificar .exists() antes de ler ou mover.",
            "Evita FileNotFoundError e mensagens confusas.",
            "Usado em automacao_portal.py antes do shutil.move.",
        ],
    )

    c.titulo_secao("glob() e rglob() — buscar arquivos")
    c.paragrafo(
        "glob busca na pasta atual; rglob busca recursivamente em subpastas. "
        "Retornam um iterador de objetos Path.",
    )
    c.tabela(
        ["Padrao", "O que encontra"],
        [
            ("'*.csv'", "CSV na pasta atual"),
            ("'**/*.csv'", "CSV em qualquer subpasta"),
            ("'simulado_*.csv'", "CSV com prefixo simulado_"),
            ("'*.xlsx'", "Planilhas Excel"),
        ],
        [120, 355],
        titulo_tabela="Padroes comuns",
    )
    c.codigo(
        [
            "pasta = Path('dados')",
            "for csv in pasta.glob('*.csv'):",
            "    print(csv)",
            "",
            "for csv in pasta.rglob('**/*.csv'):",
            "    print(csv.resolve())",
        ],
    )

    c.titulo_secao("mkdir(), touch(), unlink()")
    c.codigo(
        [
            "pasta_saida = raiz / 'saidas' / 'boletins'",
            "pasta_saida.mkdir(parents=True, exist_ok=True)",
            "",
            "arquivo = pasta_saida / 'aluno_01.html'",
            "arquivo.touch()       # cria vazio se nao existir",
            "arquivo.unlink()      # apaga o arquivo",
        ],
    )
    c.tabela(
        ["Metodo", "Funcao", "Parametro importante"],
        [
            ("mkdir()", "Cria pasta", "parents=True, exist_ok=True"),
            ("touch()", "Cria arquivo vazio", "—"),
            ("unlink()", "Remove arquivo", "Verificar exists() antes"),
            ("rename()", "Renomeia/move", "Destino nao pode existir*"),
        ],
        [80, 180, 215],
    )
    c.paragrafo(
        "parents=True cria pastas intermediarias. exist_ok=True evita erro se a pasta ja existir.",
    )

    c.titulo_secao("read_text() e write_text()")
    c.paragrafo(
        "Metodos convenientes para ler e gravar texto. Sempre use encoding='utf-8' "
        "para acentos e caracteres especiais.",
    )
    c.codigo(
        [
            "conteudo = arquivo.read_text(encoding='utf-8')",
            "",
            "html = '<html><body><h1>Boletim</h1></body></html>'",
            "destino = pasta_saida / 'boletim_aluno.html'",
            "destino.write_text(html, encoding='utf-8')",
        ],
    )
    c.caixa(
        "Exemplo do projeto boletim",
        [
            "consolidacao.py grava CSV em saidas/",
            "boletins.py gera HTML por aluno com write_text.",
            "Sempre criar pasta de saida com mkdir antes.",
        ],
    )

    c.titulo_secao("resolve(), absolute(), relative_to()")
    c.codigo(
        [
            "p = Path('dados/../dados/simulado.csv')",
            "p.resolve()      # caminho absoluto, sem ..",
            "p.absolute()     # absoluto a partir do cwd",
            "",
            "base = Path('/projeto')",
            "arquivo = base / 'dados/notas.csv'",
            "arquivo.relative_to(base)  # dados/notas.csv",
        ],
    )
    c.fluxo(["Path(__file__)", ".resolve()", ".parent", ".parent", "raiz"])
    c.paragrafo(
        "resolve() elimina .. e links simbolicos quando possivel. "
        "Use para exibir caminhos completos ou comparar localizacoes.",
    )

    c.titulo_secao("Shutil — operacoes de alto nivel")
    c.paragrafo(
        "O modulo shutil complementa o pathlib: pathlib localiza caminhos; "
        "shutil copia, move e remove arquivos e pastas inteiras.",
    )
    c.comparacao(
        "Qual funcao de copia usar?",
        ["Funcao", "Copia conteudo", "Copia metadados"],
        [
            ("copyfile()", "Sim", "Nao"),
            ("copy()", "Sim", "Permissoes"),
            ("copy2()", "Sim", "Permissoes + datas"),
            ("copystat()", "Nao", "So metadados"),
        ],
        [100, 190, 185],
    )
    c.codigo(
        [
            "import shutil",
            "",
            "shutil.copy('origem.csv', 'destino.csv')",
            "shutil.copy2('origem.csv', 'backup.csv')",
        ],
    )

    c.titulo_secao("move(), copytree(), rmtree()")
    c.fluxo(["Downloads/", "exists()?", "unlink destino", "shutil.move", "dados/simulados/"])
    c.codigo(
        [
            "def mover_csv_baixado(nome: str) -> None:",
            "    origem = pasta_downloads / nome",
            "    destino = pasta_simulados / nome",
            "    if not origem.exists():",
            "        print('Origem nao encontrada')",
            "        return",
            "    if destino.exists():",
            "        destino.unlink()",
            "    shutil.move(origem, destino)",
            "    print(f'Arquivo movido para: {destino}')",
        ],
    )
    c.paragrafo("Funcoes extras uteis:")
    c.codigo(
        [
            "shutil.copytree('src_pasta', 'dst_pasta')",
            "shutil.rmtree('pasta_temp')",
            "shutil.disk_usage('/')  # total, usado, livre",
            "shutil.which('python')  # caminho do executavel",
        ],
    )

    c.titulo_secao("Exercicio integrado")
    c.paragrafo(
        "Combine pathlib + shutil: (1) glob para achar CSV em downloads/, "
        "(2) mkdir em dados/simulados/, (3) move com shutil, (4) confirme com exists().",
    )


def gerar_pdf() -> None:
    """Monta documento com capa, indice e conteudo em fluxo."""
    doc = layout.novo_documento()

    page_capa = layout.nova_pagina(doc)
    layout.capa(
        page_capa,
        "Pathlib e Shutil",
        "Caminhos e arquivos no Python",
        [
            "Quem quer parar de usar strings frageis como C:\\Users\\...\\arquivo.csv.",
            "Estudantes do projeto de boletim escolar e automacao de dados.",
            "Quem precisa mover, copiar, criar pastas e ler arquivos com seguranca.",
        ],
        titulo_guia=TITULO_GUIA,
        cor_faixa=COR_FAIXA,
    )
    y = 280
    y = layout.titulo(page_capa, y, "Por que Path em vez de string?")
    layout.comparacao(
        page_capa,
        y,
        "String x Path",
        ["Aspecto", "String", "Path"],
        [
            ("Juntar pastas", "'pasta' + '/' + 'arquivo'", "pasta / 'arquivo'"),
            ("Portabilidade", "Barras \\ ou / manual", "Ajusta ao sistema"),
            ("Metodos uteis", "os.path separado", ".exists(), .glob(), etc."),
            ("Legibilidade", "Caminho longo confuso", "Objeto com propriedades"),
        ],
        [110, 185, 180],
    )

    page_indice = layout.nova_pagina(doc)
    layout.cabecalho(page_indice, TITULO_GUIA, cor_faixa=COR_FAIXA)
    layout.rodape(page_indice, 2, nota=NOTA_OFICIAL)
    y = 52
    y = layout.titulo(page_indice, y, "Indice do guia")
    y = layout.paragrafo(
        page_indice,
        y,
        "Este guia traduz a documentacao oficial para linguagem simples, com exemplos "
        "do projeto de boletim escolar.",
    )
    itens = [
        ("Importar Path e operador /", "3"),
        ("Arvore de pastas do projeto", "3"),
        ("Propriedades: name, stem, suffix", "4"),
        ("exists(), is_file(), is_dir()", "4"),
        ("glob() e rglob()", "5"),
        ("mkdir, touch, unlink", "5"),
        ("read_text e write_text", "6"),
        ("resolve, parent, relative_to", "6"),
        ("shutil: copy, copy2, move", "6"),
        ("copytree, rmtree, integracao", "6"),
    ]
    y += 6
    for secao, pag in itens:
        page_indice.insert_text((layout.MARGEM_X, y), secao, fontsize=10, fontname="helv", color=layout.PRETO)
        page_indice.insert_text((480, y), pag, fontsize=10, fontname="hebo", color=layout.AZUL)
        y += 18

    compositor = layout.Compositor(doc, TITULO_GUIA, cor_faixa=COR_FAIXA, nota_rodape=NOTA_OFICIAL)
    _conteudo(compositor)

    layout.salvar_pdf(doc, PDF)
    print(f"OK  {PDF.relative_to(BASE.parent.parent)}  ({compositor.numero + 2} paginas)")


def main() -> None:
    """Ponto de entrada do gerador."""
    gerar_pdf()


if __name__ == "__main__":
    main()
