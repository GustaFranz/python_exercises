# EXERCICIO 79 - Remover chave do dicionario (contexto de comercio)
#
# ENUNCIADO
# Dado o dicionario abaixo:
# estoque = {"caderno": 50, "caneta": 200, "borracha": 80, "regua": 30}
# Exiba o dicionario completo.
# Remova o item "borracha" do estoque.
# Exiba o dicionario novamente apos a remocao.
#
# ORIENTACOES
## Use pop("chave") para remover um item e obter o valor removido.
## Exiba o dicionario com print() antes e depois da remocao.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
estoque = {"caderno": 50, "caneta": 200, "borracha": 80, "regua": 30}

print("Estoque inicial:")
print(estoque)

valor_removido = estoque.pop("borracha", None)

print("Estoque após remoção:")
print(estoque)



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
