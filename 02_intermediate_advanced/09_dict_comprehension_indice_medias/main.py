# DEMANDA
# Empresa: RH Escolar Mais
# Setor: Recursos humanos / gestao escolar
# Solicitacao: Indice de media por matricula e lista de elegiveis ao bonus de desempenho.

# EXERCICIO 09 - Dict comprehension: indice de desempenho e elegibilidade
#
# registros = [
#     {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5], "faltas": 2},
#     {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0], "faltas": 8},
#     {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
#     {"id": 104, "nome": "Diego", "notas": [7.5, 7.0, 6.0], "faltas": 5},
# ]
# 1) medias_por_id = {id: media} via dict comprehension
# 2) elegiveis: media >= 7 e faltas <= 4
# 3) Relatorio: indice, elegiveis, ids fora da meta (media < 7)
#
# ORIENTACOES
## media = sum(r["notas"]) / len(r["notas"])
## elegiveis = {r["id"]: ... for r in registros if ...}
## fora_meta = {i: m for i, m in medias_por_id.items() if m < 7}

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
