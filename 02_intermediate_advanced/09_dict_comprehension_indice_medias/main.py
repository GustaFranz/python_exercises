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
#     {"id": 105, "nome": "Rodrigo", "notas": [8.5, 7.0, 9.0], "faltas": 5},
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

registros = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5], "faltas": 2},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0], "faltas": 8},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
    {"id": 104, "nome": "Diego", "notas": [7.5, 7.0, 6.0], "faltas": 5},
    {"id": 105, "nome": "Rodrigo", "notas": [8.5, 7.0, 9.0], "faltas": 5},

]

medias_por_id = [{"id": item["id"], "media": round(sum(item["notas"])/len(item["notas"]), 1), "faltas": item["faltas"]} for item in registros]
print()
print("==================== RELATÓRIO POR ID ================")
print()

cont_elegiveis = 0
for item in medias_por_id:
    if item["media"] >= 7 and item["faltas"] <= 4:
        status = "elegível"
        cont_elegiveis += 1
    else:
        status = "inelegível"
    print(f'id: {item["id"]} | media: {item["media"]} |  status: {status} ')
print()
print(f'Quantidade de elegíveis ao bônus: {cont_elegiveis}')
print()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Dict comprehension monta indice id -> media a partir da lista de registros
# media = sum(notas) / len(notas); round(..., 1) deixa o valor legivel no relatorio
# Filtro na comprehension: so entram elegiveis (media >= 7 e faltas <= 4)
# Outro filtro em .items(): fora_meta pega quem tem media < 7
# Indice por id facilita consulta e relatorio sem revarrear a lista toda vez
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
