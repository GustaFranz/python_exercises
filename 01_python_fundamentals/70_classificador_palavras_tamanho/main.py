# EXERCICIO 70 - Classificador de palavras por tamanho (contexto de analise de texto)
#
# ENUNCIADO
# Considere a lista de palavras abaixo:
# palavras = ["python", "ai", "educacao", "dados", "ia", "programacao", "sol", "modelo", "rede"]
# O programa deve separar as palavras em:
## curtas (ate 4 letras);
## medias (5 a 8 letras);
## longas (9 ou mais letras).
#
# ORIENTACOES
## Utilize len() para medir cada palavra.
## Percorra a lista com for.
## Distribua os itens em novas listas conforme as condicoes.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

palavras = ["python", "ai", "educacao", "dados", "ia", "programacao", "sol", "modelo", "rede"]
curtas = []
medias = []
longas = []

for p in palavras:
    if len(p) <= 4:
        curtas.append(p)

    elif len(p) <= 8:
        medias.append(p)
    
    else:
        longas.append(p)

quantidade_curtas = len(curtas)
quantidade_medias = len(medias)
quantidade_longas = len(longas)

print(f'//green/Palavras curtas (até 4 letras): {curtas}/green')
print(f'//green/Quantidade de palavras curtas: {quantidade_curtas}/green')

print(f'//yellow/Palavras médias (5 a 8 letras): {medias}/yellow')
print(f'//yellow/Quantidade de palavras médias: {quantidade_medias}/yellow')

print(f'//red/Palavras longas (9 ou mais letras): {longas}/red')    
print(f'//red/Quantidade de palavras longas: {quantidade_longas}/red')



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Classificacao de palavras por tamanho com len()
# Distribuicao em listas curtas, medias e longas com elif
# Contagem de itens por categoria com len()
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
