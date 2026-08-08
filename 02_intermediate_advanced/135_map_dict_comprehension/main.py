# DEMANDA
# Empresa: Cantina Escolar Plus
# Setor: Alimentacao / operacoes
# Solicitacao: Aplicar taxa de servico e indexar precos finais por codigo.

# EXERCICIO 135 - map e dict comprehension (contexto corporativo)
#
# codigos = ["S1", "S2", "S3", "S4"]
# precos_base = [5.0, 8.5, 12.0, 3.5]
# TAXA = 0.10
# 1) map para preco final com taxa
# 2) round(valor, 2)
# 3) dict comprehension {codigo: preco}
# 4) filtrar promocionais (preco <= 10.0)
# 5) exibir tabela, promocionais e item mais caro
#
# ORIENTACOES
## precos_finais = list(map(lambda p: round(p * (1 + TAXA), 2), precos_base))
## tabela = {c: p for c, p in zip(codigos, precos_finais)}
## promocionais = {c: p for c, p in tabela.items() if p <= 10.0}

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
