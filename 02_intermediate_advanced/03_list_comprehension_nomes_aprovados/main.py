# DEMANDA
# Empresa: Colegio Horizonte
# Setor: Educacao basica
# Solicitacao: Lista rapida de alunos aprovados para mural digital.

# EXERCICIO 03 - List comprehension: nomes aprovados (contexto corporativo)
#
# Dados da turma:
# alunos = [
#     {"nome": "Ana", "nota": 7.5},
#     {"nome": "Bruno", "nota": 4.0},
#     {"nome": "Carla", "nota": 8.0},
#     {"nome": "Daniel", "nota": 5.5},
# ]
# Gere lista apenas com nomes dos aprovados (nota >= 6) usando list comprehension.
# Exiba total de aprovados e a lista de nomes.
#
# ORIENTACOES
## Use: [aluno["nome"] for aluno in alunos if aluno["nota"] >= 6]
## Combine filtro (if) com selecao de campo na expressao.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

alunos = [
    {"nome": "Ana", "nota": 7.5},
    {"nome": "Bruno", "nota": 4.0},
    {"nome": "Carla", "nota": 8.0},
    {"nome": "Daniel", "nota": 5.5},
]

NOTA_CORTE = 6.0

aprovados = [aluno for aluno in alunos if aluno["nota"] >= NOTA_CORTE]
nao_aprovados = [aluno for aluno in alunos if aluno["nota"] < NOTA_CORTE]

print("\n========================================================================================")
print("=========================== SITUAÇÃO DOS ALUNOS -- RELATÓRIO ===========================")
print("========================================================================================\n")

print('................................... ALUNOS APROVADOS ...................................\n')

for aluno in aprovados:
    print(f"{aluno["nome"]:<30}  | Nota: {aluno["nota"]} ")

print('\n................................... ALUNOS REPROVADOS ...................................\n')
for aluno in nao_aprovados:
    print(f"{aluno["nome"]:<30}  | Nota: {aluno["nota"]} ")
print()



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# if depois do for filtra: so entram itens que passam na condicao
# [aluno for aluno in alunos if aluno["nota"] >= NOTA_CORTE] mantem o dicionario inteiro
# Se eu quisesse so os nomes: [aluno["nome"] for aluno in alunos if aluno["nota"] >= 6]
# Constante NOTA_CORTE evita numero magico e deixa a regra de aprovacao explicita
# Duas comprehensions (aprovados / nao_aprovados) separam os grupos sem loops longos
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
