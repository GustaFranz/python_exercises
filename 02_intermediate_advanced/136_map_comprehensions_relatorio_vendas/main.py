# DEMANDA
# Empresa: Loja Tech Escolar
# Setor: Varejo / analytics
# Solicitacao: Calcular margem por SKU, destacar top vendas e indexar alertas.

# EXERCICIO 136 - map e comprehensions: relatorio de vendas (contexto corporativo)
#
# vendas = [
#     {"sku": "A1", "produto": "Tablet", "qtd": 3, "preco": 800.0},
#     {"sku": "B2", "produto": "Fone", "qtd": 10, "preco": 45.0},
#     {"sku": "C3", "produto": "Mouse", "qtd": 25, "preco": 35.0},
#     {"sku": "D4", "produto": "Teclado", "qtd": 8, "preco": 120.0},
# ]
# CUSTO_PERCENTUAL = 0.65
# META_FATURAMENTO = 500.0
# 1) map para faturamento (qtd * preco)
# 2) list comprehension enriquecida com margem
# 3) filtrar destaques >= META
# 4) dict comprehension alertas por sku
# 5) ranking, destaques e alertas
#
# ORIENTACOES
## faturamentos = list(map(lambda v: v["qtd"] * v["preco"], vendas))
## enriquecidos = [{...} for v, fat in zip(vendas, faturamentos)]
## alertas = {r["sku"]: "meta_ok" if r["faturamento"] >= META else "abaixo" for r in enriquecidos}

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
