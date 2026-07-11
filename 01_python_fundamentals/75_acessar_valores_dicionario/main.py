# EXERCICIO 75 - Acessar valores do dicionario (contexto introdutorio)
#
# ENUNCIADO
# Dado o dicionario abaixo:
# aluno = {"nome": "Ana", "idade": 15, "cidade": "Recife"}
# Exiba o nome e a cidade do aluno.
#
# ORIENTACOES
## Acesse cada valor pela sua chave: dicionario["chave"].
## Exiba os valores com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
aluno = {"nome": "Ana", "idade": 15, "cidade": "Recife"}
print(f'Nome: {aluno["nome"]} | '
      f'Cidade: {aluno["cidade"]}')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Acesso a valores por chave com colchetes
# f-string juntando mais de um campo do dict
# Reforco: chave errada gera KeyError
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
