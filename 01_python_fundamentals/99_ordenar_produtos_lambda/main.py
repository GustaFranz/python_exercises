# EXERCICIO 99 - Ordenar produtos com lambda (contexto de comercio)
#
# ENUNCIADO
# Considere a lista de produtos em tuplas (nome, preco):
# produtos = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90), ("lapis", 1.50)]
# Ordene os produtos do mais barato para o mais caro e exiba a lista ordenada.
# Depois exiba tambem do mais caro para o mais barato.
#
# ORIENTACOES
## Use sorted(lista, key=lambda item: item[1]) para ordenar pelo preco.
## O indice 1 da tupla e o preco.
## Para inverter a ordem, use o parametro reverse=True.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

produtos = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90), ("lapis", 1.50)]

produtos_crescente = sorted(produtos, key=lambda item: item[1])

produtos_decrescente = sorted(produtos, key=lambda item: item[1], reverse=True)

print("=== PRODUTOS DO MAIS BARATO AO MAIS CARO ===")
for nome, preco in produtos_crescente:
    print(f"//green/Produto:/green //yellow/{nome:<10}/yellow | //green/Preço: R$/green //cyan/{preco:.2f}/cyan")

print("\n=== PRODUTOS DO MAIS CARO AO MAIS BARATO ===")
for nome, preco in produtos_decrescente:
    print(f"//green/Produto:/green //yellow/{nome:<10}/yellow | //green/Preço: R$/green //cyan/{preco:.2f}/cyan")



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# sorted() com key=lambda item: item[1] ordena pelo preco
# reverse=True inverte sem alterar a lista original
# Tupla (nome, preco): indice 1 define o criterio
# Animado em ordenar produtos com lambda no key
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
