# -*- coding: utf-8 -*-
"""Gera o guia PDF EasyAnsi_em_Python.pdf.

Execute na raiz do repositorio:
    python materiais/easyansi/_gerar_easyansi_pdf.py
"""

from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
MATERIAIS = BASE.parent
sys.path.insert(0, str(MATERIAIS))

import _layout as layout  # noqa: E402

PDF = BASE / "EasyAnsi_em_Python.pdf"
TITULO_GUIA = "EASYANSI EM PYTHON"


def _conteudo(c: layout.Compositor) -> None:
    """Define todo o conteudo do guia em fluxo continuo."""
    c.titulo_secao("Por que usar EasyAnsi?")
    c.paragrafo(
        "A EasyAnsi foi criada para quem quer cor no terminal sem aprender uma biblioteca "
        "pesada. Voce escreve a cor dentro da string, como numa f-string.",
    )
    c.comparacao(
        "EasyAnsi x bibliotecas mais complexas",
        ["Necessidade", "EasyAnsi", "Alternativas pesadas"],
        [
            ("Comecar rapido", "from easyansi import eprint", "Configurar Console, markup"),
            ("Colorir uma palavra", "//red/{valor}/red", "Montar objetos Text"),
            ("Mensagem de sucesso", "success('Pronto')", "Criar renderizavel"),
            ("Log colorido", "setup_logging()", "Handlers, temas, plugins"),
            ("Tag escrita errada", "Vira texto normal", "Pode quebrar o programa"),
        ],
        [130, 170, 175],
    )
    c.caixa(
        "Filosofia da biblioteca",
        [
            "Menos conceitos, menos imports.",
            "Comandos faceis de lembrar no dia a dia.",
            "Fail-safe: URLs e tags desconhecidas nao quebram a saida.",
        ],
    )

    c.titulo_secao("Sintaxe //cor/texto/cor")
    c.tabela(
        ["Padrao", "Significado", "Exemplo"],
        [
            ("//nome/", "Abre tag de estilo", "//red/"),
            ("/nome", "Fecha tag explicitamente", "/red"),
            ("//", "Fecha ultima tag aberta", "//green/texto//"),
        ],
        [90, 170, 195],
        titulo_tabela="Abertura e fechamento",
    )
    c.codigo(
        [
            "from easyansi import eprint",
            "",
            "eprint('//green/Ola, mundo!/green')",
            "eprint('Sobrou //red/1/red item no estoque')",
            "eprint('Acesse https://exemplo.com')  # URL intacta",
        ],
    )
    c.caixa(
        "Fail-safe",
        [
            "Somente nomes conhecidos viram cor.",
            "//erro/texto/erro vira texto puro (nao quebra).",
            "URLs com // permanecem literais.",
        ],
    )

    c.titulo_secao("activate() vs eprint/einput")
    c.fluxo(["Script novo?", "Sim: activate()", "Nao: eprint/einput"])
    c.paragrafo("Com activate(), print e input normais passam a interpretar as tags EasyAnsi:")
    c.codigo(
        [
            "import easyansi",
            "easyansi.activate()",
            "",
            "print('//green/Tudo certo!/green')",
            "nome = input('Digite //cyan/seu nome/cyan: ')",
            "easyansi.deactivate()  # restaura originais",
        ],
    )
    c.paragrafo("Alternativa explicita (sem alterar print global):")
    c.codigo(
        [
            "from easyansi import eprint, einput, fmt",
            "",
            "eprint('//green/Tudo certo!/green')",
            "nome = einput('Digite //cyan/seu nome/cyan: ')",
            "mensagem = fmt('//yellow/aviso/yellow')",
        ],
    )

    c.titulo_secao("Atalhos e mensagens de status")
    c.paragrafo("Atalhos de cor — ideais para autocomplete no editor:")
    c.codigo(
        [
            "from easyansi import red, green, yellow, blue, bold",
            "",
            "print(red('erro'), green('ok'), yellow('aviso'))",
            "print(bold(red('critico')))  # encadeamento",
        ],
    )
    c.paragrafo("Mensagens prontas para o dia a dia:")
    c.codigo(
        [
            "from easyansi import success, error, warning, info",
            "",
            "success('Salvo com sucesso')",
            "error('Falha ao conectar')",
            "warning('Conexao lenta')",
            "info('Rodando na porta 8080')",
        ],
    )
    c.tabela(
        ["Funcao", "Uso tipico"],
        [
            ("red(), green(), ...", "Destacar palavras isoladas"),
            ("bold(), italic(), ...", "Enfatizar titulos e notas"),
            ("success(), error()", "Feedback de operacao"),
            ("style('bold-blue', txt)", "Combo personalizado"),
        ],
        [160, 315],
        titulo_tabela="Referencia rapida de atalhos",
    )

    c.titulo_secao("Titulos, paint e f-strings")
    c.codigo(
        [
            "from easyansi import title, t, paint, ask, activate",
            "",
            "activate()",
            "print(title('CADASTRO DE ALUNOS', '='))",
            "print(t('MENU', '~', style='bold-blue'))",
            "print(paint('Texto inteiro azul', 'bold-blue'))",
            "nome = ask('Qual seu nome?', prompt_style='bold-blue')",
        ],
    )
    c.paragrafo("Funciona dentro de f-strings com variaveis:")
    c.codigo(
        [
            "pontos = 42",
            "print(f'Resultado: //green/{pontos}/green pontos')",
            "print(f'Nota //bold-blue/{7.5}/bold-blue em Matematica')",
        ],
    )
    c.caixa(
        "Dica sobre input colorido",
        [
            "O terminal nao colore em tempo real o que voce digita.",
            "ask() colore o prompt; a resposta aparece colorida ao imprimir depois.",
        ],
    )

    c.titulo_secao("Estilos combinados, fundos e hex")
    c.paragrafo("Combine estilos com hifen: bold-blue, italic-underline-red.")
    c.codigo(
        [
            "print('//bold-blue/cabecalho/bold-blue')",
            "print('//italic-underline-magenta/destaque/')",
            "print('//bg-yellow/texto em fundo amarelo/bg-yellow')",
            "print('//#ff8800/laranja exato/#ff8800')",
            "print('//negrito-vermelho/erro em portugues/negrito-vermelho')",
        ],
    )
    c.tabela(
        ["Tipo", "Tag", "Exemplo"],
        [
            ("Estilo + cor", "bold-blue", "//bold-blue/texto/bold-blue"),
            ("Fundo", "bg-yellow", "//bg-yellow/aviso/bg-yellow"),
            ("Hex", "#ff8800", "//#ff8800/laranja/#ff8800"),
            ("PT", "negrito-vermelho", "//negrito-vermelho/erro/"),
        ],
        [90, 130, 255],
        titulo_tabela="Variacoes de cor e estilo",
    )

    c.titulo_secao("Logging colorido e preview()")
    c.codigo(
        [
            "import logging",
            "from easyansi.logging import setup_logging",
            "",
            "setup_logging(level=logging.INFO)",
            "logging.info('Servidor iniciado')",
            "logging.warning('Cache desatualizado')",
            "logging.error('Falha ao conectar')",
        ],
    )
    c.tabela(
        ["Nivel", "Cor padrao"],
        [
            ("DEBUG", "dim"),
            ("INFO", "cyan"),
            ("WARNING", "yellow"),
            ("ERROR", "red"),
            ("CRITICAL", "bold-red"),
        ],
        [120, 355],
        titulo_tabela="Cores por nivel de log",
    )
    c.paragrafo("Para ver todas as cores disponiveis no terminal:")
    c.codigo(["import easyansi", "easyansi.preview()"])

    c.titulo_secao("Comportamento inteligente da saida")
    c.fluxo(["Terminal?", "Pipe/redir?", "NO_COLOR?", "Aplicar cor"])
    c.tabela(
        ["Condicao", "Comportamento"],
        [
            ("Terminal interativo (TTY)", "Cores ANSI aplicadas"),
            ("Saida em pipe / arquivo", "Texto limpo (sem escape)"),
            ("Variavel NO_COLOR", "Texto limpo"),
            ("FORCE_COLOR definido", "Cores forcadas"),
        ],
        [200, 275],
    )

    c.titulo_secao("Exercicio pratico — menu de notas")
    c.codigo(
        [
            "import easyansi",
            "easyansi.activate()",
            "",
            "print(easyansi.title('NOTAS DO ALUNO', '='))",
            "print('//cyan/1/cyan Listar  //cyan/2/cyan Cadastrar  //cyan/0/cyan Sair')",
            "opcao = input('Escolha: ')",
            "if opcao == '1': print('//green/Notas carregadas/green')",
            "elif opcao == '2': print('//yellow/Cadastro em breve/yellow')",
            "else: print('//dim/Encerrando/dim')",
        ],
    )
    c.subtitulo("Cola rapida da API")
    c.paragrafo(
        "fmt · eprint · einput · activate · title · t · paint · ask · preview · "
        "red/green/bold · success/error/warning/info · setup_logging",
    )


def gerar_pdf() -> None:
    """Monta documento com capa, indice e conteudo em fluxo."""
    doc = layout.novo_documento()

    page_capa = layout.nova_pagina(doc)
    layout.capa(
        page_capa,
        "EasyAnsi",
        "Cores no terminal de forma simples",
        [
            "Iniciantes em Python que querem saida colorida sem configuracao complexa.",
            "Professores e estudantes que preferem sintaxe parecida com f-string.",
            "Quem precisa de mensagens de status, titulos e logging colorido.",
        ],
        titulo_guia=TITULO_GUIA,
    )
    y = 280
    y = layout.titulo(page_capa, y, "Instalacao")
    y = layout.codigo(
        page_capa,
        y,
        [
            "pip install py-easyansi",
            "",
            "# ou a partir do codigo-fonte:",
            "pip install -e C:/caminho/para/EasyAnsi",
        ],
    )
    layout.paragrafo(
        page_capa,
        y,
        "Requisitos: Python 3.8+ e terminal com suporte ANSI (Windows 10+ ja funciona).",
    )

    page_indice = layout.nova_pagina(doc)
    layout.indice_visual(
        page_indice,
        TITULO_GUIA,
        [
            ("Por que usar EasyAnsi", "3"),
            ("Sintaxe //cor/texto/cor", "3"),
            ("activate() vs eprint/einput", "4"),
            ("Atalhos e mensagens de status", "4"),
            ("Titulos, paint e f-strings", "5"),
            ("Estilos combinados e cores hex", "5"),
            ("Logging colorido e preview()", "6"),
            ("Comportamento inteligente", "6"),
            ("Exercicio pratico + cola rapida", "6"),
        ],
        2,
    )

    compositor = layout.Compositor(doc, TITULO_GUIA)
    _conteudo(compositor)

    layout.salvar_pdf(doc, PDF)
    print(f"OK  {PDF.relative_to(BASE.parent.parent)}  ({compositor.numero + 2} paginas)")


def main() -> None:
    """Ponto de entrada do gerador."""
    gerar_pdf()


if __name__ == "__main__":
    main()
