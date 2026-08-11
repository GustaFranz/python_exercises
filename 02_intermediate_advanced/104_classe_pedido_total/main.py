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

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, nome: str, quantidade: int, preco: float):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ter um valor positivo")
        if preco <= 0:
            raise ValueError("O preço deve ser positivo")
        self.itens.append({"nome": nome, "quantidade": quantidade, "preco": preco})

    def remover_item(self, nome):
        for item in self.itens:
            if item["nome"] == nome:
                self.itens.remove(item)
                return True
        return False

    def listar_itens():
        return list(self.itens)

    def total(self):
        return sum(item["preco"] * item["quantidade"] for item in self.itens)

    def aplicar_desconto(self, percentual):
        if percentual < 0 or percentual > 100:
            raise ValueError("Desconto deve ser um valor entre 0 e 100")
        return self.total() * (1 - percentual / 100)

    def __str__(self):
        return f'Pedido de {self.cliente}  |  Quant. de itens: {len(self.itens)}  |  Total: R$ {self.total():.2f}'

pedido = Pedido("Escola 7B")

pedido.adicionar_item("caderno", 12, 20.0)
pedido.adicionar_item("borracha", 15, 2.50)
pedido.adicionar_item("estojo", 20, 18.50)
print(f'{pedido}\n')
print(f"Remover Estojo: {pedido.remover_item('estojo')}")
print(pedido)
print(f"Remover Grampeador: {pedido.remover_item('grampeador')}")
print(f'{pedido}\n')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# class Pedido encapsula cliente e lista interna de itens (self.itens)
# Cada item e um dict {nome, quantidade, preco} — estrutura simples e legivel
# adicionar_item valida na entrada: qtd e preco devem ser positivos (ValueError)
# remover_item percorre a lista e retorna True/False conforme encontrou ou nao
# total() soma preco * quantidade com sum() e generator expression
# aplicar_desconto usa total() como base e nao altera os itens do pedido
# Desconto invalido (fora de 0 a 100) gera ValueError antes do calculo
# __str__ resume cliente, quantidade de itens e total formatado (.2f)
# Encapsular estado e expor metodos pequenos e padrao comum em entrevistas
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
