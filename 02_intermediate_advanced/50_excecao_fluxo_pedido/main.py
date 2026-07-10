# DEMANDA
# Empresa: Loja Virtual Escolar
# Setor: Varejo / e-commerce
# Solicitacao: Garantir que pedidos invalidos nao entrem na fila de separacao.

# EXERCICIO 50 - Excecao customizada: fluxo de pedido (contexto corporativo)
#
# Excecoes: EstoqueInsuficienteError, PedidoVazioError.
# Dados: estoque = {"caderno": 5, "caneta": 0}
# Funcao processar_pedido(itens) onde itens e lista de dicts {"produto": str, "qtd": int}
## PedidoVazioError se lista vazia
## EstoqueInsuficienteError se qtd > estoque ou estoque zero
## retorna "Pedido aceito" se ok
# Teste: pedido vazio, caneta qtd 1, caderno qtd 2 (ok).
# Cada teste deve mostrar sucesso ou erro sem derrubar o programa.
#
# ORIENTACOES
## Loop nos itens validando estoque.get(produto, 0).
## Encadeie validacoes: primeiro vazio, depois estoque.
## Integra raise com try/except do bloco anterior.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
