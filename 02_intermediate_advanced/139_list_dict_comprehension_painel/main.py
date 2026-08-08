# DEMANDA
# Empresa: Consultoria MetaEdu
# Setor: Consultoria educacional
# Solicitacao: Consolidar desempenho por turma e listar turmas em atencao.

# EXERCICIO 139 - List e dict comprehension: painel de desempenho (contexto corporativo)
#
# turmas = [
#     {"codigo": "7A", "alunos": 30, "aprovados": 24},
#     {"codigo": "7B", "alunos": 28, "aprovados": 20},
#     {"codigo": "8A", "alunos": 32, "aprovados": 30},
#     {"codigo": "8B", "alunos": 27, "aprovados": 15},
# ]
# META_APROVACAO = 75.0
# 1) dict comprehension taxas {codigo: taxa %}
# 2) list comprehension em_atencao
# 3) list comprehension destaques (>= 90%)
# 4) dict comprehension resumo ok/atencao
# 5) exibir painel ordenado
#
# ORIENTACOES
## taxas = {t["codigo"]: round(t["aprovados"] / t["alunos"] * 100, 1) for t in turmas}
## em_atencao = [c for c, taxa in taxas.items() if taxa < META_APROVACAO]
## resumo = {c: "ok" if taxa >= META else "atencao" for c, taxa in taxas.items()}

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
