# EXERCICIO 55 - Fatiar tupla (contexto introdutorio)
#
# ENUNCIADO
# Dada a tupla abaixo:
# numeros = (10, 20, 30, 40, 50, 60)
# Exiba os 3 primeiros elementos e depois os 2 ultimos elementos.
#
# ORIENTACOES
## Use fatiamento no formato tupla[inicio:fim].
## Lembre que o indice final nao entra no fatiamento.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

numeros = (10, 20, 30, 40, 50, 60)

print(numeros[0:3] + numeros[-2:])

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Fatiamento de tuplas com indices de inicio e fim
# Combinacao de fatias para reunir partes distintas da tupla
# Reforco de que o indice final do slice nao entra no resultado
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
