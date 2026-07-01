# EXERCICIO 54 - Acessar elementos da tupla (contexto introdutorio)
#
# ENUNCIADO
# Dada a tupla abaixo:
# cores = ("vermelho", "verde", "azul", "amarelo")
# Exiba o primeiro e o ultimo elemento da tupla.
#
# ORIENTACOES
## Use o indice 0 para acessar o primeiro elemento.
## Use o indice -1 para acessar o ultimo elemento.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

cores = ("vermelho", "verde", "azul", "amarelo")
print(f'O primeiro elemento da tupla é //bold-red/{cores[0]}/bold-red '
      f'e o último elemento da tupla é //bold-yellow/{cores[3]}/bold-yellow ')



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Acesso a elementos de tupla por indice positivo e negativo
# Uso de f-string para formatar saida com destaque visual
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
