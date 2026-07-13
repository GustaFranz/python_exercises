# -*- coding: utf-8 -*-
"""Conteudo: Tratamento de Strings em Python."""

from ..tema import TEMA_PYTHON

SPEC = {
    "tema": TEMA_PYTHON,
    "topico": "TRATAMENTO DE STRINGS",
    "destaque": "EM PYTHON",
    "subtitulo": "Guia completo com exemplos, resultados e explicacoes",
    "simbolo": '" "',
    "blocos": [
        {"tipo": "secao", "titulo": "O que sao strings?"},
        {"tipo": "checks", "itens": [
            "Strings sao sequencias de caracteres (textos).",
            "Podem usar aspas simples ' ', duplas \" \" ou triplas ''' '''.",
            "Strings sao <b>imutaveis</b> (nao mudam diretamente; geram novas).",
            "Possuem diversos metodos uteis para manipulacao.",
            "Muito usadas em validacoes, formatacoes e processamento de dados.",
        ]},

        {"tipo": "secao", "titulo": "Criando strings"},
        {"tipo": "tabela",
         "cabecalho": ["Codigo", "Resultado", "Explicacao"],
         "larguras": [0.34, 0.22, 0.44], "mono": [0], "resultado": 1,
         "linhas": [
            ["'Python'", "Python", "String com aspas simples."],
            ['"Python"', "Python", "String com aspas duplas."],
            ["'''Python'''", "Python", "Aspas triplas (permite multilinha)."],
            ['"""L1\\nL2"""', "L1 / L2", "Strings em varias linhas."],
            ["str(123)", "123", "Converte um numero para string."],
         ]},

        {"tipo": "secao", "titulo": "Metodos e operacoes com strings"},
        {"tipo": "paragrafo",
         "texto": "Em todos os exemplos abaixo usamos "
                  "<b>texto = \"  Python é Incrível!  \"</b> "
                  "(repare nos espacos no inicio e no fim)."},

        {"tipo": "paragrafo", "texto": "<b>Maiusculas e minusculas</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicacao"],
         "larguras": [0.30, 0.30, 0.40], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.upper()", "PYTHON É INCRÍVEL!", "Converte tudo para maiusculas."],
            ["texto.lower()", "python é incrível!", "Converte tudo para minusculas."],
            ["texto.capitalize()", "Python é incrível!", "Deixa so o primeiro caractere maiusculo."],
            ["texto.title()", "Python É Incrível!", "Primeira letra de cada palavra maiuscula."],
            ["texto.swapcase()", "pYTHON É iNCRÍVEL!", "Inverte maiusculas e minusculas."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Remocao de espacos</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicacao"],
         "larguras": [0.30, 0.30, 0.40], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.strip()", "'Python é Incrível!'", "Remove espacos do inicio e do fim."],
            ["texto.lstrip()", "'Python é Incrível!  '", "Remove espacos apenas a esquerda."],
            ["texto.rstrip()", "'  Python é Incrível!'", "Remove espacos apenas a direita."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Busca e contagem</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicacao"],
         "larguras": [0.30, 0.18, 0.52], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.find('Python')", "2", "Indice da primeira ocorrencia (ha 2 espacos antes)."],
            ["texto.rfind('!')", "19", "Indice da ultima ocorrencia do caractere."],
            ["texto.count('o')", "1", "Quantas vezes o caractere/substring aparece."],
            ["'é' in texto", "True", "Verifica se a substring esta presente."],
            ["'xyz' not in texto", "True", "Verifica se a substring NAO esta presente."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Substituicao</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicacao"],
         "larguras": [0.36, 0.30, 0.34], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.replace('Python','Top')", "Top é Incrível!", "Substitui todas as ocorrencias."],
            ["texto.replace('o','0')", "Pyth0n é Incrível!", "Substitui caractere por caractere."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Divisao e juncao</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicacao"],
         "larguras": [0.34, 0.34, 0.32], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.split()", "['Python','é','Incrível!']", "Divide por espacos em uma lista."],
            ["texto.split('é')", "['Python ',' Incrível!']", "Divide usando o separador informado."],
            ["'-'.join(lista)", "Python-é-Incrível", "Junta itens de uma lista com o separador."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Verificacoes</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicacao"],
         "larguras": [0.30, 0.18, 0.52], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.isalpha()", "False", "Ha espacos e '!', entao nem tudo sao letras."],
            ["texto.isalnum()", "False", "Nem tudo sao letras ou numeros."],
            ["texto.isdigit()", "False", "Nao sao todos digitos."],
            ["texto.isspace()", "False", "Nao sao apenas espacos."],
            ["texto.startswith('Py')", "False", "Comeca com espacos, nao com 'Py'."],
            ["texto.endswith('!')", "False", "Termina com espacos, nao com '!'."],
         ]},

        {"tipo": "callout", "titulo": "Atencao",
         "texto": "startswith/endswith deram False por causa dos espacos nas "
                  "pontas. Aplique .strip() antes para comparar so o conteudo: "
                  "texto.strip().startswith('Py') -> True."},

        {"tipo": "secao", "titulo": "Exercicio: analisador de frases"},
        {"tipo": "paragrafo",
         "texto": "O usuario digita frases ate escrever 'fim'. Para cada frase, "
                  "removemos espacos extras, contamos palavras e vogais e "
                  "verificamos se comeca com maiuscula. No fim, exibimos um "
                  "relatorio com totais e medias."},
        {"tipo": "codigo", "titulo": "analisador.py", "linhas": [
            ("frases = []", None),
            ("while True:", None),
            ("    entrada = input('Digite uma frase (ou \"fim\"): ')", None),
            ("    if entrada.lower() == 'fim':", None),
            ("        break", None),
            ("    frases.append(entrada.strip())", None),
            ("", None),
            ("total = len(frases)", None),
            ("total_palavras = sum(len(f.split()) for f in frases)", None),
            ("media = total_palavras / total if total else 0", None),
            ("vogais = sum(c.lower() in 'aeiou' for f in frases for c in f)", None),
            ("maiusculas = sum(1 for f in frases if f[:1].isupper())", None),
            ("mais = max(frases, key=lambda f: len(f.split()))", None),
            ("menos = min(frases, key=lambda f: len(f.split()))", None),
            ("", None),
            ("print('Total de frases:', total)", None),
            ("print('Media de palavras:', round(media, 2))", None),
            ("print('Frase com mais palavras:', mais)", None),
            ("print('Frase com menos palavras:', menos)", None),
            ("print('Total de vogais:', vogais)", None),
            ("print('Comecam com maiuscula:', maiusculas)", None),
        ]},

        {"tipo": "callout", "titulo": "Dica final + boas praticas",
         "cor": "#FFD43B",
         "texto": [
            "Sempre remova espacos desnecessarios com .strip().",
            "Use .lower() para comparacoes seguras (sem diferenciar caixa).",
            "Evite repetir codigo: aproveite os metodos prontos.",
            "Lembre: strings sao imutaveis — os metodos geram novas strings.",
         ]},
    ],
}
