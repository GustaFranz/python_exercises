# EXERCICIO 94 - Analise de texto (contexto de linguagem)
#
# ENUNCIADO
# Crie funcoes para analisar uma frase.
# frase = "Python e uma linguagem poderosa para analise de dados"
# O programa deve retornar:
## quantidade de palavras;
## palavra mais longa;
## numero de vogais;
## frase em maiusculo.
#
# ORIENTACOES
## Crie funcoes separadas para cada analise.
## Utilize len(), split(), loops e funcoes de string.
## Cada funcao deve retornar um valor especifico.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


frase = "Python e uma linguagem poderosa para analise de dados"


def separar_palavras(frase_analisada):
    return frase_analisada.split()


def colocar_palavras_maiusculas(frase_analisada):
    return frase_analisada.upper()


def contar_palavras(lista_palavras):
    return len(lista_palavras)


def obter_mais_longa(lista_palavras):
    return max(lista_palavras, key=len)


def contar_vogais(frase_analisada):
    somente_letras = frase_analisada.replace(" ", "")
    contador_vogais = 0
    for letra in somente_letras:
        if letra in "aeiou":
            contador_vogais += 1
    return contador_vogais


def main():
    lista_palavras = separar_palavras(frase)
    frase_maiuscula = colocar_palavras_maiusculas(frase)
    quantidade_palavras = contar_palavras(lista_palavras)
    longa = obter_mais_longa(lista_palavras)
    quantidade_vogais = contar_vogais(frase)

    print(f'A lista de palavras é: {lista_palavras}')
    print(f'A frase completa maiúscula é: {frase_maiuscula}')
    print(f'A quantidade de palavras é: {quantidade_palavras}')
    print(f'A palavra mais longa é: {longa}')
    print(f'A quantidade de vogais é: {quantidade_vogais}')


if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# split() divide a frase em lista de palavras
# max(lista, key=len) acha a palavra mais longa
# Loop com in para contar vogais em "aeiou"
# main() orquestra funcoes e junta os resultados
# Animado em analisar texto com funcoes pequenas e claras
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
