# -*- coding: utf-8 -*-
"""Conteudo: Tuplas em Python."""

from ..tema import TEMA_PYTHON

SPEC = {
    "tema": TEMA_PYTHON,
    "topico": "TUPLAS",
    "destaque": "EM PYTHON",
    "subtitulo": "Guia completo com exemplos, resultados e explicacoes",
    "simbolo": "( , , )",
    "blocos": [
        {"tipo": "secao", "titulo": "Regras principais"},
        {"tipo": "checks", "itens": [
            "Tuplas sao <b>IMUTAVEIS</b>: nao da para alterar, adicionar ou "
            "remover elementos depois de criadas.",
            "Ordenadas: os elementos possuem posicao (indice).",
            "Permitem elementos duplicados.",
            "Podem armazenar diferentes tipos de dados.",
            "Usamos parenteses ( ) para criar tuplas.",
        ]},

        {"tipo": "secao", "titulo": "Criando tuplas"},
        {"tipo": "codigo", "titulo": "Formas de criar uma tupla", "linhas": [
            ("t1 = (10, 20, 30)", "# tupla com numeros"),
            ("t2 = ('Python', 3.14, True)", "# tipos diferentes"),
            ("t3 = (1,)", "# 1 elemento (virgula obrigatoria)"),
            ("t4 = tuple([1, 2, 3, 4])", "# convertendo lista em tupla"),
        ]},
        {"tipo": "callout", "titulo": "Observacao importante",
         "texto": "(1) NAO e uma tupla — e apenas um valor entre parenteses. "
                  "A tupla de um elemento exige a virgula: (1,)."},

        {"tipo": "secao", "titulo": "Operacoes e analise de tuplas"},
        {"tipo": "paragrafo",
         "texto": "Exemplos considerando <b>numeros = (10, 20, 30, 40, 50)</b>."},
        {"tipo": "tabela",
         "cabecalho": ["Comando", "Resultado", "Por que esse e o resultado?"],
         "larguras": [0.26, 0.28, 0.46],
         "mono": [0], "resultado": 1,
         "linhas": [
            ["numeros[0]", "10", "O indice 0 e o primeiro elemento da tupla."],
            ["numeros[2]", "30", "O indice 2 aponta para o terceiro elemento."],
            ["numeros[-1]", "50", "Indices negativos comecam pelo final: -1 e o ultimo."],
            ["numeros[-2]", "40", "O -2 e o penultimo elemento."],
            ["numeros[1:4]", "(20, 30, 40)", "Do indice 1 (incluido) ate antes do 4."],
            ["numeros[0:3]", "(10, 20, 30)", "Os indices 0, 1 e 2, parando antes do 3."],
            ["numeros[2:]", "(30, 40, 50)", "Do indice 2 ate o ultimo elemento."],
            ["numeros[:3]", "(10, 20, 30)", "Do primeiro ate antes do indice 3."],
            ["numeros[:]", "(10,...,50)", "Todos os elementos (copia da tupla)."],
            ["numeros[-3:]", "(30, 40, 50)", "O indice -3 e o valor 30; vai ate o final."],
            ["len(numeros)", "5", "len() conta quantos elementos existem na tupla."],
            ["30 in numeros", "True", "in verifica se o valor 30 esta na tupla."],
            ["100 in numeros", "False", "O valor 100 nao existe na tupla."],
            ["numeros.count(20)", "1", "count() informa quantas vezes o valor aparece."],
            ["numeros.index(40)", "3", "index() retorna o indice da primeira ocorrencia."],
            ["numeros + (60, 70)", "(...,60,70)", "Cria uma nova tupla unindo as duas; a original nao muda."],
            ["numeros * 2", "(...repetida)", "Repete a sequencia inteira da tupla duas vezes."],
         ]},

        {"tipo": "secao", "titulo": "Fatiamento (slice) visual"},
        {"tipo": "paragrafo",
         "texto": "Considere <b>numeros = (10, 20, 30, 40, 50)</b> e seus indices:"},
        {"tipo": "tabela",
         "cabecalho": ["Indice", "0", "1", "2", "3", "4"],
         "larguras": [0.20, 0.16, 0.16, 0.16, 0.16, 0.16],
         "mono": [0],
         "linhas": [["Valor", "10", "20", "30", "40", "50"]]},
        {"tipo": "tabela",
         "cabecalho": ["Expressao", "Resultado", "Leitura"],
         "larguras": [0.22, 0.26, 0.52], "mono": [0], "resultado": 1,
         "linhas": [
            ["numeros[1:4]", "(20, 30, 40)", "Do indice 1 (incluido) ate antes do 4."],
            ["numeros[2:]", "(30, 40, 50)", "Do indice 2 ate o final."],
            ["numeros[:3]", "(10, 20, 30)", "Do inicio ate antes do indice 3."],
            ["numeros[-3:]", "(30, 40, 50)", "Os tres ultimos elementos."],
         ]},
        {"tipo": "callout", "titulo": "Regra de ouro do fatiamento",
         "texto": "O indice inicial e INCLUIDO; o indice final NAO e incluido."},

        {"tipo": "secao", "titulo": "Exercicio: medias e situacao dos alunos"},
        {"tipo": "paragrafo",
         "texto": "Voce recebeu os dados de alunos e suas notas. Calcule a media "
                  "de cada um e exiba nome, notas, media e situacao "
                  "(Aprovado se media >= 7; senao Reprovado)."},
        {"tipo": "codigo", "titulo": "medias.py", "linhas": [
            ("alunos = (", None),
            ("    ('Ana',    (8.5, 7.0, 9.0)),", None),
            ("    ('Bruno',  (6.0, 5.5, 7.0)),", None),
            ("    ('Carla',  (9.5, 9.0, 8.5)),", None),
            ("    ('Daniel', (7.0, 7.5, 6.5)),", None),
            (")", None),
            ("", None),
            ("resultado = []", None),
            ("for nome, notas in alunos:", None),
            ("    media = sum(notas) / len(notas)", None),
            ("    situacao = 'Aprovado' if media >= 7 else 'Reprovado'", None),
            ("    resultado.append((nome, round(media, 2), situacao))", None),
            ("", None),
            ("for nome, media, situacao in resultado:", None),
            ("    print(nome, media, situacao)", None),
        ]},
        {"tipo": "tabela",
         "cabecalho": ["Aluno", "Notas", "Media", "Situacao"],
         "larguras": [0.20, 0.34, 0.18, 0.28], "mono": [1], "resultado": 2,
         "linhas": [
            ["Ana", "(8.5, 7.0, 9.0)", "8.17", "Aprovado"],
            ["Bruno", "(6.0, 5.5, 7.0)", "6.17", "Reprovado"],
            ["Carla", "(9.5, 9.0, 8.5)", "9.00", "Aprovado"],
            ["Daniel", "(7.0, 7.5, 6.5)", "7.00", "Aprovado"],
         ]},

        {"tipo": "callout", "titulo": "Dica final",
         "cor": "#FFD43B",
         "texto": "Tuplas sao ideais para dados que NAO devem mudar — como "
                  "coordenadas, configuracoes e registros fixos."},
    ],
}
