# EXERCICIO 85 - Avaliacao de produtos (contexto de comercio)
#
# ENUNCIADO
# Considere o seguinte dicionario de produtos e avaliacoes medias:
# produtos = {"notebook": 4.5, "mouse": 3.8, "teclado": 4.2, "monitor": 4.7, "fone": 3.5}
# O programa deve:
## separar produtos em bons (>= 4.0) e regulares (< 4.0);
## criar dois dicionarios separados;
## identificar o produto melhor avaliado.
#
# ORIENTACOES
## Use .items().
## Crie novos dicionarios.
## Utilize max() com key.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

bons_produtos = {}
regulares_produtos = {}

produtos = {"notebook": 4.5, "mouse": 3.8, "teclado": 4.2, "monitor": 4.7, "fone": 3.5}

for produto, avaliacao in produtos.items():
    if avaliacao >= 4.0:
        bons_produtos[produto] = avaliacao
    else:
        regulares_produtos[produto] = avaliacao

print(f'//green/O dicionário de produtos bons é:/green //yellow/{bons_produtos}/yellow')
print(f'//green/O dicionário de produtos regulares é:/green //yellow/{regulares_produtos}/yellow')
print(f'//green/O produto melhor avaliado é:/green //yellow/{max(produtos, key=produtos.get)}/yellow')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
