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
turmas = {
    "9A": {"aprovacao": 72, "media": 7.1, "evasao": 3},
    "9B": {"aprovacao": 58, "media": 5.8, "evasao": 8},
    "9C": {"aprovacao": 81, "media": 8.0, "evasao": 2},
    "9D": {"aprovacao": 45, "media": 4.9, "evasao": 12},
}

def classificar(dados):
    if dados["aprovacao"] < 50 or dados["evasao"] >= 10:
        return "critica"
    elif 50 <= dados["aprovacao"] < 70:
        return "atencao"
    else:
        return "estavel"

prioridades = {turma: classificar(dados) for turma, dados in turmas.items()}
backlog = {turma: prioridade for turma, prioridade in prioridades.items() if prioridade != "estavel"}

qtd_critica = sum(1 for p in prioridades.values() if p == "critica")
qtd_atencao = sum(1 for p in prioridades.values() if p == "atencao")
qtd_estavel = sum(1 for p in prioridades.values() if p == "estavel")

backlog_ordenado = sorted(backlog.items(), key=lambda item: 0 if item[1] == "critica" else 1)

print("=== PLANO DE ACAO POR TURMA ===")
print()
print(f"Criticas: {qtd_critica} | Atencao: {qtd_atencao} | Estaveis: {qtd_estavel}")
print("\n----------- BACKLOG DE INTERVENCAO  -----------\n")
for turma, prioridade in backlog_ordenado:
    print(f"  {turma}: {prioridade}")
print()



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Dict comprehension aplica classificar() em todas as turmas: {turma: prioridade for ...}
# Funcao auxiliar separa a regra de negocio da montagem do dicionario
# Ordem do if/elif importa: critica (aprovacao < 50 ou evasao >= 10) vem antes de atencao
# Segunda comprehension filtra o backlog: so entram prioridades diferentes de "estavel"
# sum(1 for p in prioridades.values() if p == ...) conta por categoria sem Counter
# sorted(..., key=lambda) ordena o backlog: critica (0) antes de atencao (1)
# Regras compostas com or exigem testar o caso mais grave primeiro (ex.: 9D)
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
