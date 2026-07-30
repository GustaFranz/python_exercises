# DEMANDA
# Empresa: LogiRapida
# Setor: Logistica / pedidos
# Solicitacao: Calcular pedidos de material escolar com regras de desconto e controle de itens.

# EXERCICIO 104 - Classe Pedido: CRUD de itens e desconto (nivel entrevista junior)
#
# Classe Pedido:
## __init__(self, cliente: str) -> self.itens = []  # cada item: {nome, qtd, preco}
## adicionar_item(self, nome, qtd, preco) -> None  # validar qtd > 0 e preco > 0
## remover_item(self, nome) -> bool  # True se removeu, False se nao encontrou
## listar_itens(self) -> list  # retorna itens do pedido
## total(self) -> float  # soma preco * qtd
## aplicar_desconto(self, pct) -> float  # retorna total com desconto; pct entre 0 e 100
## __str__(self) -> str  # cliente, qtd itens e total formatado
#
# Cenario sugerido no main:
## pedido = Pedido("Escola 7B")
## adicionar 3 itens, remover 1, aplicar desconto de 10%, exibir pedido e total final
#
# ORIENTACOES
## Validacao: raise ValueError ou retorne mensagem clara (escolha um padrao consistente).
## total() nao deve aplicar desconto; aplicar_desconto() usa total() como base.
## Pergunta comum em entrevista: encapsular estado e expor metodos pequenos.

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
