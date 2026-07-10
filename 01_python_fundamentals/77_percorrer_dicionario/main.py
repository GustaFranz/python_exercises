# EXERCICIO 77 - Percorrer dicionario (contexto educacional)
#
# ENUNCIADO
# Dado o dicionario abaixo:
# notas = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
# Exiba cada aluno com a sua nota, um por linha.
#
# ORIENTACOES
## Percorra o dicionario com for usando .items().
## Exiba a chave (aluno) e o valor (nota) de cada par.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
notas = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
for aluno, nota in notas.items():
    print(f'Aluno: {aluno:<20} | Nota: {nota}')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
