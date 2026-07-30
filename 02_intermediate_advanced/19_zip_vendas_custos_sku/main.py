# DEMANDA
# Empresa: Mercado Bom Preco
# Setor: Varejo / comercial
# Solicitacao: Relatorio de margem por SKU com alerta de produtos abaixo da meta.

# EXERCICIO 19 - Zip: margem e alerta comercial por SKU
#
# skus = ["SKU01", "SKU02", "SKU03", "SKU04"]
# vendas = [1200.0, 800.0, 450.0, 1500.0]
# custos = [700.0, 500.0, 300.0, 1200.0]
# meta_margem_pct = [35.0, 40.0, 30.0, 25.0]
# Para cada SKU via zip: margem, margem_pct, status ok/abaixo_da_meta
# Relatorio: tabela, maior margem_pct, backlog abaixo da meta, media do portfolio
#
# ORIENTACOES
## for sku, venda, custo, meta in zip(...):
## margem_pct = (margem / venda) * 100
## status = "ok" if margem_pct >= meta else "abaixo_da_meta"
## max(linhas, key=lambda x: x["margem_pct"])

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
