# EXERCICIO 60 - Catalogo de precos com tuplas (contexto de comercio)
#
# ENUNCIADO
# Considere um catalogo de produtos em tuplas (produto, preco):
# catalogo = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90), ("lapis", 1.50)]
# O programa deve exibir a soma total dos precos e o nome do produto mais caro.
#
# ORIENTACOES
## Percorra a lista de tuplas com for.
## Some os precos em uma variavel de total.
## Guarde o produto que tiver o maior preco.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

catalogo = [("caderno", 24.90), ("caneta", 2.50), ("mochila", 89.90), ("lapis", 1.50)]

for i, (produto, preco) in enumerate(catalogo):
    if i == 0:
        produto_mais_caro = produto
        preco_mais_caro = preco
        total_precos = preco
    else:
        total_precos += preco
        if preco > preco_mais_caro:
            produto_mais_caro = produto
            preco_mais_caro = preco

print(f"//green/Total dos precos:/green //red/R${total_precos:.2f}/red")
print(f"//green/Produto mais caro:/green //yellow/{produto_mais_caro}/yellow //green/com preco de/green //red/R${preco_mais_caro:.2f}/red")

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Percorrer lista de tuplas com enumerate e desempacotamento
# Acumulador para soma total dos precos do catalogo
# Comparacao sequencial para identificar o produto mais caro
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
