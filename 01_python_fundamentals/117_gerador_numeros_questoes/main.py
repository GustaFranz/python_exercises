# EXERCICIO 117 - Gerador de numeros para questoes (contexto educacional)
#
# ENUNCIADO
# Um professor deseja gerar numeros aleatorios para montar questoes de matematica automaticamente.
# O sistema deve:
## gerar 10 pares de numeros aleatorios entre 1 e 20;
## calcular soma, subtracao e multiplicacao de cada par;
## armazenar os resultados em uma estrutura organizada.
#
# ORIENTACOES
## Utilize a biblioteca random.
## Use randint().
## Armazene resultados em listas ou dicionarios.
## Evite repeticao de pares iguais.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
from random import randint

import easyansi

easyansi.activate()


def gerar_pares_aleatorios(qtd_pares, min_valor, max_valor):
    """Gera pares de numeros aleatorios unicos"""
    pares = set()
    while len(pares) < qtd_pares:
        par = (randint(min_valor, max_valor), randint(min_valor, max_valor))
        pares.add(par)
    return list(pares)


def calcular_operacoes(pares):
    """Calcula soma, subtracao e multiplicacao de cada par"""
    resultados = []
    for a, b in pares:
        resultado = {
            'par': (a, b),
            'soma': a + b,
            'subtracao': a - b,
            'multiplicacao': a * b
        }
        resultados.append(resultado)
    return resultados


def main():
    qtd_pares = 10
    min_valor = 1
    max_valor = 20

    pares_aleatorios = gerar_pares_aleatorios(qtd_pares, min_valor, max_valor)
    resultados = calcular_operacoes(pares_aleatorios)
    print(f"//bold-magenta/============= //bold-blue/GERADOR DE NÚMEROS PARA QUESTÕES //bold-magenta/=============\n")

    for resultado in resultados:
        par = resultado['par']
        print(f"//green/Par: //yellow/{par}, "
              f"//green/Soma: //yellow/{resultado['soma']}, "
              f"//green/Subtracao: //yellow/{resultado['subtracao']}, "
              f"//green/Multiplicacao: //yellow/{resultado['multiplicacao']}")
    print(f"//bold-magenta/==============================================================\n")


if __name__ == "__main__":
    main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Uso de random e randint()
# set() evita pares repetidos na geracao
# Dict organiza par e operacoes na mesma estrutura
# # Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
