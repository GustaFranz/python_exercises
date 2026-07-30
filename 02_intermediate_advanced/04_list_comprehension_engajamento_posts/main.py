# DEMANDA
# Empresa: Rede Social EduConnect
# Setor: Midia / comunicacao escolar
# Solicitacao: Priorizar posts do backlog editorial pelo engajamento relativo ao total.

# EXERCICIO 04 - List comprehension: ranking de engajamento (contexto corporativo)
#
# posts = [
#     {"titulo": "Feira de Ciencias", "curtidas": 120, "compartilhamentos": 15},
#     {"titulo": "Aviso Prova", "curtidas": 45, "compartilhamentos": 2},
#     {"titulo": "Projeto Leitura", "curtidas": 200, "compartilhamentos": 40},
#     {"titulo": "Recesso", "curtidas": 30, "compartilhamentos": 1},
#     {"titulo": "Hackathon", "curtidas": 90, "compartilhamentos": 12},
# ]
# Score: curtidas + (compartilhamentos * 3)
# 1) scores = [{titulo, score}, ...] via list comprehension
# 2) taxa % de cada post em relacao ao total de scores (outra comprehension)
# 3) top 3 por score para o feed de destaque
# 4) Relatorio: total posts, score medio, top 3 (titulo, score, taxa %)
#
# ORIENTACOES
## score = p["curtidas"] + p["compartilhamentos"] * 3
## total = sum(item["score"] for item in scores)
## taxa = round(item["score"] / total * 100, 1) se total > 0
## top3 = sorted(scores, key=lambda x: x["score"], reverse=True)[:3]

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
