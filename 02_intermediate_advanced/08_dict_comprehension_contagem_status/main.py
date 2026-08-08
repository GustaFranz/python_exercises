# DEMANDA
# Empresa: LogiRapida Entregas
# Setor: Logistica
# Solicitacao: Resumo de pedidos por status para reuniao operacional.

# EXERCICIO 08 - Dict comprehension: contagem de status (contexto corporativo)
#
# pedidos = ["entregue", "pendente", "entregue", "cancelado", "pendente", "entregue", "pendente"]
# Status unicos conhecidos: entregue, pendente, cancelado
# Monte contagem com dict comprehension:
# {status: pedidos.count(status) for status in set(pedidos)}
# Exiba cada status e sua quantidade.
#
# ORIENTACOES
## Use set(pedidos) para obter status unicos.
## .count() funciona, mas e O(n^2); aceitavel neste exercicio introdutorio.
## Formate saida legivel para reuniao.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
'''Lembrar que .count() funciona, mas e O(n^2); aceitavel aqui para aprendizado de dect comprehensions. '''

pedidos = ["entregue", "pendente", "entregue", "cancelado", "pendente", "entregue", "pendente"]

status_pedidos = {status: pedidos.count(status) for status in set(pedidos)}
print()
print(f'Pendente: {status_pedidos["pendente"]}, Cancelados: {status_pedidos["cancelado"]}, Entregues: {status_pedidos["entregue"]}')
print()





# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Dict comprehension monta status -> quantidade em uma linha
# set(pedidos) devolve so os status unicos (sem repetir chave)
# pedidos.count(status) conta quantas vezes aquele status aparece na lista
# .count() dentro da comprehension e O(n^2): cada status varre a lista de novo
# Em listas grandes, prefira um for unico ou Counter (uma passagem = O(n))
# Aqui o foco e praticar dict comprehension; o custo extra e aceitavel
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
