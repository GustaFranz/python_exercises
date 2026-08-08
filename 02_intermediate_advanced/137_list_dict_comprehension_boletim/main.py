# DEMANDA
# Empresa: Colegio Horizonte
# Setor: Educacao / secretaria
# Solicitacao: Gerar lista de aprovados e indice de medias por matricula.

# EXERCICIO 137 - List e dict comprehension: boletim da turma (contexto corporativo)
#
# VISAO DO BLOCO — list + dict comprehension (exercicios 137 a 139)
# Este bloco treina:
## 137 — Boletim: aprovados + indice de medias
## 138 — Estoque critico: alertas + mapa de quantidades
## 139 — Painel de desempenho por turma
#
# alunos = [
#     {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5]},
#     {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0]},
#     {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5]},
#     {"id": 104, "nome": "Diego", "notas": [6.0, 7.0, 5.5]},
# ]
# NOTA_APROVACAO = 6.0
# 1) dict comprehension medias por id
# 2) list comprehension nomes aprovados
# 3) dict comprehension recuperacao (media < meta)
# 4) exibir tudo + taxa de aprovacao
#
# ORIENTACOES
## medias = {a["id"]: sum(a["notas"]) / len(a["notas"]) for a in alunos}
## aprovados = [a["nome"] for a in alunos if medias[a["id"]] >= NOTA_APROVACAO]
## recuperacao = {i: m for i, m in medias.items() if m < NOTA_APROVACAO}

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
