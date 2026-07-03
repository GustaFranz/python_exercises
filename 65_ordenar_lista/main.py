# EXERCICIO 65 - Ordenar lista (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista abaixo:
# numeros = [5, 2, 9, 1, 7, 3]
# Exiba a lista ordenada em ordem crescente e depois em ordem decrescente.
#
# ORIENTACOES
## Use sorted() para gerar uma nova lista ordenada sem alterar a original.
## Para decrescente, use sorted(lista, reverse=True).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

numeros = [5, 2, 9, 1, 7, 3]
print(f' Lista //yellow/numeros/yellow em ordem crescente: //green/{sorted(numeros)}/green')
print(f' Lista //yellow/numeros/yellow em ordem decrescente: //green/{sorted(numeros, reverse=True)}/green')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Funcao sorted para ordenar sem alterar a lista original
# Parametro reverse=True para ordem decrescente
# Exibicao comparativa entre crescente e decrescente
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
