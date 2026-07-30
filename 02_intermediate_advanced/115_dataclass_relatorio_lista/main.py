# DEMANDA
# Empresa: BigData Escolar
# Setor: Educacao / analytics
# Solicitacao: Consolidar vendas do bazar em relatorio analitico para reuniao comercial.

# EXERCICIO 115 - Dataclass: relatorio analitico de vendas (nivel entrevista junior)
#
# @dataclass Venda:
## produto: str
## quantidade: int
## valor_unit: float
## subtotal(self) -> float  # quantidade * valor_unit (metodo ou property)
#
# Vendas de exemplo:
## [
##   Venda("Caderno", 10, 8.50),
##   Venda("Caneta", 50, 2.00),
##   Venda("Mochila", 3, 120.00),
##   Venda("Lapis", 30, 1.50),
## ]
#
# Funcoes:
## gerar_relatorio(vendas: list[Venda]) -> dict
##   retorna {"total": ..., "ticket_medio": ..., "top_produto": ...}
## filtrar_vendas_acima(vendas: list[Venda], limite: float) -> list[Venda]
## exibir_relatorio(relatorio: dict) -> None  # impressao formatada
#
# Teste com limite = 50.0 e mostre vendas acima desse subtotal.
#
# ORIENTACOES
## ticket_medio = total / len(vendas) se lista nao vazia.
## top_produto: produto com maior subtotal (desempate: primeiro encontrado).
## Retornar dict facilita testes e integracao — padrao comum em APIs internas.

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
