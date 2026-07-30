# DEMANDA
# Empresa: Consultoria MetaEdu
# Setor: Consultoria educacional
# Solicitacao: Classificar turmas do portfolio e montar backlog de intervencao.

# EXERCICIO 10 - Dict comprehension: plano de acao por turma
#
# turmas = {
#     "9A": {"aprovacao": 72, "media": 7.1, "evasao": 3},
#     "9B": {"aprovacao": 58, "media": 5.8, "evasao": 8},
#     "9C": {"aprovacao": 81, "media": 8.0, "evasao": 2},
#     "9D": {"aprovacao": 45, "media": 4.9, "evasao": 12},
# }
# critica: aprovacao < 50 ou evasao >= 10
# atencao: 50 <= aprovacao < 70
# estavel: demais
# 1) prioridades via dict comprehension
# 2) backlog = so critica e atencao
# 3) Relatorio: qtd por prioridade + backlog (critica primeiro)
#
# ORIENTACOES
## Use if/elif em funcao auxiliar ou expressao ternaria aninhada
## backlog = {t: p for t, p in prioridades.items() if p != "estavel"}
## sorted(backlog.items(), key=lambda x: 0 if x[1] == "critica" else 1)

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
