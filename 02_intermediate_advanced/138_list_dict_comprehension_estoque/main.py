# DEMANDA
# Empresa: Papelaria Central
# Setor: Varejo / operacoes
# Solicitacao: Identificar itens criticos e montar mapa de reposicao.

# EXERCICIO 138 - List e dict comprehension: estoque critico (contexto corporativo)
#
# produtos = [
#     {"sku": "P01", "nome": "Caderno", "estoque": 12, "minimo": 10},
#     {"sku": "P02", "nome": "Caneta", "estoque": 3, "minimo": 15},
#     {"sku": "P03", "nome": "Borracha", "estoque": 25, "minimo": 8},
#     {"sku": "P04", "nome": "Estojo", "estoque": 5, "minimo": 5},
#     {"sku": "P05", "nome": "Lapis", "estoque": 2, "minimo": 20},
# ]
# 1) list comprehension criticos (estoque <= minimo)
# 2) dict comprehension mapa_estoque {sku: estoque}
# 3) dict comprehension reposicao para criticos
# 4) exibir relatorio
#
# ORIENTACOES
## criticos = [p["nome"] for p in produtos if p["estoque"] <= p["minimo"]]
## mapa_estoque = {p["sku"]: p["estoque"] for p in produtos}
## reposicao = {p["sku"]: max(0, p["minimo"] - p["estoque"]) for p in produtos if p["estoque"] <= p["minimo"]}

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
