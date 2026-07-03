# EXERCICIO 64 - Fatiar lista (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista abaixo:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# Exiba os 4 primeiros elementos e depois os 3 ultimos elementos.
#
# ORIENTACOES
## Use fatiamento no formato lista[inicio:fim].
## Lembre que o indice final nao entra no fatiamento.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

print(f'Os quatro primeiros números da lista //yellow/numeros/yellow são //green/{numeros[0:4]}/green')
print(f'Os últimos 3 elementos da lista //yellow/numeros/yellow são //green/{numeros[-3:]}/green')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Fatiamento para obter os primeiros elementos da lista
# Fatiamento com indice negativo para os ultimos elementos
# Reforco de que o indice final do slice nao entra no resultado
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
