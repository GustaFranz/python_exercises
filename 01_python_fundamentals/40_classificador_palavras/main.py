# EXERCICIO 40 - Classificador de palavras (contexto de análise de texto)
#
# ENUNCIADO
# O usuário vai digitar 10 palavras. O programa deve classificar:
## palavras curtas (até 4 letras);
## palavras médias (5 a 8 letras);
## palavras longas (9+ letras).
# Ao final, exibir quantas palavras existem em cada categoria.
#
# ORIENTACOES
## Use for com 10 repetições.
## Use len() para medir palavras.
## Utilize contadores.
## Pode armazenar em listas separadas (opcional).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

## Use for com 10 repetições.

def vermelho(texto):
    return f"\033[31m{texto}\033[0m"

todas_as_palavras = []
palavras_curtas = []
palavras_medias = []
palavras_longas = []
todas = 0
curtas = 0
medias = 0
longas = 0

for p in range (1, 11):
    palavra = input("Digite uma palavra: " ).capitalize()
    cont = (len(palavra))
    todas_as_palavras.append(palavra)

    if cont <= 4:
        palavras_curtas.append(palavra)
        curtas += 1
        todas += 1

    elif cont <= 8:
        palavras_medias.append(palavra)
        medias += 1
        todas += 1


    else:
        palavras_longas.append(palavra)
        longas += 1
        todas += 1

print('~' * 130)
print(f'Você digitou ao todo {vermelho(todas)} palavras.')
print(f'A sua lista completa de palavras é {vermelho(todas_as_palavras)}.')
print('~' * 130)

if palavras_curtas:
    print(f'Lista de palavras curtas = {vermelho(palavras_curtas)}')
    if curtas == 1:
        print(f'Você digitou {vermelho(curtas)} palavra curta.')
    else:
        print(f'Você digitou {vermelho(curtas)} palavras curtas.')
print('~' * 130)

if palavras_medias:
    print(f'Lista de palavras medias = {vermelho(palavras_medias)}')
    if medias == 1:
        print(f'Você digitou {vermelho(medias)} palavra média.')
    else:
        print(f'Você digitou {vermelho(medias)} palavras médias.')
print('~' * 130)

if palavras_longas:
    print(f'Lista de palavras longas = {vermelho(palavras_longas)}')
    if longas ==1:
        print(f'Você digitou {vermelho(longas)} palavra longa.')
    else:
        print(f'Você digitou {vermelho(longas)} palavras longas.')
print('~' * 130)


# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# - Aplicação de estruturas de repetição (for) para coleta e processamento de dados
# - Uso de condicionais para classificação de informações
# - Manipulação e organização de dados em listas
# - Utilização de len() para análise de strings
# - Melhoria na saída de dados (formatação, singular/plural e customização com cores)
#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
