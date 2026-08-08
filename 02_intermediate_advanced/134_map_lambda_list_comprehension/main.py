# DEMANDA
# Empresa: Moda Escolar Online
# Setor: Varejo / catalogo
# Solicitacao: Padronizar nomes de produtos e listar itens em promocao.

# EXERCICIO 134 - map com lambda e list comprehension (contexto corporativo)
#
# produtos = ["  CAMISETA POLO ", "tenis escolar", " MOCHILA ", "bone oficial", "calcado esportivo"]
# precos = [89.9, 120.0, 150.0, 35.0, 199.9]
# LIMITE_PROMOCAO = 100.0
# 1) map(lambda p: p.strip().title(), produtos)
# 2) list comprehension: [{"nome": n, "preco": p} for n, p in zip(nomes, precos)]
# 3) filtrar promocao com list comprehension
# 4) exibir catalogo, promocao e quantidade
#
# ORIENTACOES
## list(map(...)) materializa os nomes padronizados
## zip alinha nome e preco pelo indice
## promocao = [item for item in catalogo if item["preco"] <= LIMITE_PROMOCAO]

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
