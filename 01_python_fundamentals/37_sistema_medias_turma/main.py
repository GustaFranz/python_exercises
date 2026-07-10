# EXERCICIO 37 - Sistema de médias de turma (contexto educacional)
#
# ENUNCIADO
# Uma turma possui 8 alunos. O professor deseja digitar a nota de cada aluno e ao final obter:
## média da turma;
## maior nota;
## menor nota;
## quantidade de alunos acima da média 6.
#
# ORIENTACOES
# Use um for para iterar pelos 8 alunos.
## Armazene as notas em uma lista.
## Após o loop, percorra a lista novamente para cálculos.
## Utilize sum(), max(), min() quando possível.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================


notas = []
for a in range(1, 9):
    aluno = float(input(f'Nota do aluno {a}: ').replace(',', '.'))
    notas.append(aluno)

media = sum(notas) / len(notas)

print("-"*70)
print(f'as notas da turma são: {notas}')
print("-"*70)
print(f'A média da turma é {media:.1f}')
print("-"*70)
print(f'A menor nota da turma foi {min(notas):.1f}')
print("-"*70)
print(f'A maior nota da turma foi {max(notas):.1f}')

notas_acima_6 = 0

for n in notas:
    if n > 6:
        notas_acima_6 += 1
print("-"*70)
print(f'Quantidade de alunos com nota acima de 6,0: {notas_acima_6}')


# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# Nesse exercício pesquisei uma forma do programa aceitar a vírgula para o caso do usuário não usar ponto na resposta
# Aprendi a função replace(',', '.') para adaptar a entrada do usuário.
# Após pesquisa, também aprendi a armazenar dados em uma lista
# e analisar esses dados usando funções como:
# max(), min(), sum() e len()


# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO