# DEMANDA
# Empresa: FinTech Escolar
# Setor: Financeiro / analytics
# Solicitacao: Processar transacoes do dia em pipeline lazy para relatorio executivo.

# EXERCICIO 143 - Funcao geradora: pipeline de relatorio (contexto corporativo)
#
# transacoes_brutas = [
#     "101;Ana;150.0;ok",
#     "102;Bruno;-20.0;ok",
#     "103;Carla;300.0;ok",
#     "104;Diego;abc;ok",
#     "105;Elena;80.0;cancelado",
#     "106;Fabio;45.5;ok",
# ]
# VALOR_MINIMO = 50.0
# 1) parse_transacoes(linhas) -> yield dict
# 2) filtrar_validas(transacoes) -> yield elegiveis
# 3) gerar_resumo(transacoes) -> yield strings formatadas
# Encadear geradores no main + total + contagem
#
# ORIENTACOES
## partes = linha.split(";")
## try: valor = float(partes[2]) except: continue (nao yield)
## Pipeline: for linha in gerar_resumo(filtrar_validas(parse_transacoes(brutas))):
## Total: acumule valor das transacoes apos filtrar_validas

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
