# EXERCICIO 100 - Filtrar aprovados com lambda (contexto educacional)
#
# ENUNCIADO
# Considere a lista de notas de uma turma:
# notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]
# Gere uma nova lista apenas com as notas dos aprovados (nota >= 6).
# Exiba a lista de aprovados e a quantidade de aprovados.
#
# ORIENTACOES
## Use filter() com uma lambda que retorna True para nota >= 6.
## Converta o resultado de filter() para list().
## Use len() para contar quantos aprovados existem.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]

lista_aprovados = list(filter(lambda nota: nota >= 6, notas))
quantidade_aprovados = len(lista_aprovados)

print(f'A lista de aprivados é {lista_aprovados}')
print(f'A quantidade de aprovados é: {quantidade_aprovados}')




# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com filter() junto de lambda
# Lambda retorna True quando nota >= 6
# list() converte o filtro em lista utilizavel
# len() conta aprovados sem loop manual
# Animado em filtrar a turma em poucas linhas
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
