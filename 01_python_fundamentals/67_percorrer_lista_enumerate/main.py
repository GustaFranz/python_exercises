# EXERCICIO 67 - Percorrer lista com enumerate (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista abaixo:
# disciplinas = ["Matematica", "Portugues", "Ciencias", "Historia", "Geografia"]
# Exiba cada disciplina com o seu numero de posicao, comeando por 1.
#
# ORIENTACOES
## Use for com enumerate() para obter indice e valor ao mesmo tempo.
## Para comecar a contagem em 1, use enumerate(lista, start=1).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

disciplinas = ["Matematica", "Portugues", "Ciencias", "Historia", "Geografia"]

for i, (d) in enumerate(disciplinas, start=1):
    print(f"{i:<5}| {d}")

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Percorrer lista com enumerate e start=1 para numeracao
# Exibicao de indice e valor em colunas alinhadas
# Primeiro contato com enumerate em contexto escolar
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
