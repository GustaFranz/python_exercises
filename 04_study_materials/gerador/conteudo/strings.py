# -*- coding: utf-8 -*-
"""Conteúdo: Tratamento de Strings em Python."""

from ..tema import TEMA_PYTHON

SPEC = {
    "tema": TEMA_PYTHON,
    "topico": "TRATAMENTO DE STRINGS",
    "destaque": "EM PYTHON",
    "subtitulo": "Guia completo com exemplos, resultados e explicações",
    "simbolo": '" "',
    "blocos": [
        {"tipo": "secao", "titulo": "O que são strings?"},
        {"tipo": "checks", "itens": [
            "Strings são sequências de caracteres (textos).",
            "Podem usar aspas simples ' ', duplas \" \" ou triplas ''' '''.",
            "Strings são <b>imutáveis</b> (não mudam diretamente; geram novas).",
            "Possuem diversos métodos úteis para manipulação.",
            "Muito usadas em validações, formatações e processamento de dados.",
        ]},

        {"tipo": "secao", "titulo": "Criando strings"},
        {"tipo": "tabela",
         "cabecalho": ["Código", "Resultado", "Explicação"],
         "larguras": [0.34, 0.22, 0.44], "mono": [0], "resultado": 1,
         "linhas": [
            ["'Python'", "Python", "String com aspas simples."],
            ['"Python"', "Python", "String com aspas duplas."],
            ["'''Python'''", "Python", "Aspas triplas (permite multilinha)."],
            ['"""L1\\nL2"""', "L1 / L2", "Strings em várias linhas."],
            ["str(123)", "123", "Converte um número para string."],
         ]},

        {"tipo": "secao", "titulo": "Métodos e operações com strings"},
        {"tipo": "paragrafo",
         "texto": "Em todos os exemplos abaixo usamos "
                  "<b>texto = \"  Python é Incrível!  \"</b> "
                  "(repare nos espaços no início e no fim)."},

        {"tipo": "paragrafo", "texto": "<b>Maiúsculas e minúsculas</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicação"],
         "larguras": [0.30, 0.30, 0.40], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.upper()", "PYTHON É INCRÍVEL!", "Converte tudo para maiúsculas."],
            ["texto.lower()", "python é incrível!", "Converte tudo para minúsculas."],
            ["texto.capitalize()", "Python é incrível!", "Deixa só o primeiro caractere maiúsculo."],
            ["texto.title()", "Python É Incrível!", "Primeira letra de cada palavra maiúscula."],
            ["texto.swapcase()", "pYTHON É iNCRÍVEL!", "Inverte maiúsculas e minúsculas."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Remoção de espaços</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicação"],
         "larguras": [0.30, 0.30, 0.40], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.strip()", "'Python é Incrível!'", "Remove espaços do início e do fim."],
            ["texto.lstrip()", "'Python é Incrível!  '", "Remove espaços apenas à esquerda."],
            ["texto.rstrip()", "'  Python é Incrível!'", "Remove espaços apenas à direita."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Busca e contagem</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicação"],
         "larguras": [0.30, 0.18, 0.52], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.find('Python')", "2", "Índice da primeira ocorrência (há 2 espaços antes)."],
            ["texto.rfind('!')", "19", "Índice da última ocorrência do caractere."],
            ["texto.count('o')", "1", "Quantas vezes o caractere/substring aparece."],
            ["'é' in texto", "True", "Verifica se a substring está presente."],
            ["'xyz' not in texto", "True", "Verifica se a substring NÃO está presente."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Substituição</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicação"],
         "larguras": [0.36, 0.30, 0.34], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.replace('Python','Top')", "Top é Incrível!", "Substitui todas as ocorrências."],
            ["texto.replace('o','0')", "Pyth0n é Incrível!", "Substitui caractere por caractere."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Divisão e junção</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicação"],
         "larguras": [0.34, 0.34, 0.32], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.split()", "['Python','é','Incrível!']", "Divide por espaços em uma lista."],
            ["texto.split('é')", "['Python ',' Incrível!']", "Divide usando o separador informado."],
            ["'-'.join(lista)", "Python-é-Incrível", "Junta itens de uma lista com o separador."],
         ]},

        {"tipo": "paragrafo", "texto": "<b>Verificações</b>"},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Explicação"],
         "larguras": [0.30, 0.18, 0.52], "mono": [0], "resultado": 1,
         "linhas": [
            ["texto.isalpha()", "False", "Há espaços e '!', então nem tudo são letras."],
            ["texto.isalnum()", "False", "Nem tudo são letras ou números."],
            ["texto.isdigit()", "False", "Não são todos dígitos."],
            ["texto.isspace()", "False", "Não são apenas espaços."],
            ["texto.startswith('Py')", "False", "Começa com espaços, não com 'Py'."],
            ["texto.endswith('!')", "False", "Termina com espaços, não com '!'."],
         ]},

        {"tipo": "callout", "titulo": "Atenção",
         "texto": "startswith/endswith deram False por causa dos espaços nas "
                  "pontas. Aplique .strip() antes para comparar só o conteúdo: "
                  "texto.strip().startswith('Py') -> True."},

        {"tipo": "secao", "titulo": "Exercício: analisador de frases"},
        {"tipo": "paragrafo",
         "texto": "O usuário digita frases até escrever 'fim'. Para cada frase, "
                  "removemos espaços extras, contamos palavras e vogais e "
                  "verificamos se começa com maiúscula. No fim, exibimos um "
                  "relatório com totais e médias."},
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
            ("print('Média de palavras:', round(media, 2))", None),
            ("print('Frase com mais palavras:', mais)", None),
            ("print('Frase com menos palavras:', menos)", None),
            ("print('Total de vogais:', vogais)", None),
            ("print('Começam com maiúscula:', maiusculas)", None),
        ]},

        {"tipo": "callout", "titulo": "Dica final + boas práticas",
         "cor": "#FFD43B",
         "texto": [
            "Sempre remova espaços desnecessários com .strip().",
            "Use .lower() para comparações seguras (sem diferenciar caixa).",
            "Evite repetir código: aproveite os métodos prontos.",
            "Lembre: strings são imutáveis — os métodos geram novas strings.",
         ]},
    ],
}
