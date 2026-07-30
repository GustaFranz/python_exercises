# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / plataforma
# Solicitacao: Localizar matricula em export legado e contar quantas vezes ela aparece no backlog de registros.

# EXERCICIO 67 - Recursao: busca linear e contagem de ocorrencias (contexto corporativo)
#
# matriculas = [101, 205, 308, 308, 412, 308, 519]
#
# buscar_indice(lista, alvo, indice=0):
#   caso base: indice >= len(lista) -> -1
#   se lista[indice] == alvo: return indice
#   senao: return buscar_indice(lista, alvo, indice + 1)
#
# contar_ocorrencias(lista, alvo, indice=0):
#   caso base: indice >= len(lista) -> 0
#   achou = 1 if lista[indice] == alvo else 0
#   return achou + contar_ocorrencias(lista, alvo, indice + 1)
#
# Testes:
#   buscar_indice(matriculas, 308) -> 2
#   contar_ocorrencias(matriculas, 308) -> 3
#   buscar_indice(matriculas, 999) -> -1
#   contar_ocorrencias(matriculas, 999) -> 0
#
# ORIENTACOES
## Parametro indice com default 0 na assinatura.
## Duas funcoes recursivas independentes — reutilize a ideia de caso base.
## Exiba resultados formatados para facilitar correcao manual.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
