# DEMANDA
# Empresa: Loja Virtual Escolar
# Setor: Varejo / PDV
# Solicitacao: Simular ponto de venda do bazar escolar com registro de vendas.

# EXERCICIO 105 - Classe: simulador de caixa (contexto corporativo)
#
# Classe ItemVenda: nome, preco, quantidade; subtotal() -> preco * quantidade
# Classe Caixa:
## __init__(self, operador): self.vendas = []
## registrar_venda(self, item: ItemVenda): append item
## total_dia(self): soma subtotais
## __str__: operador, qtd vendas e total do dia
# Simule caixa "Maria" com 3 itens vendidos e exiba resumo.
#
# ORIENTACOES
## Desafio leve: duas classes — ItemVenda (dados) e Caixa (agregador).
## Caixa recebe instancias de ItemVenda em registrar_venda.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class ItemVenda:

    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.preco * self.quantidade 

class Caixa:

    def __init__(self, operador: str):
        self.operador = operador
        self.vendas = []

    def registrar_venda(self, item: ItemVenda):
        self.vendas.append(item)

    def total_dia(self) -> float:
        return sum(item.subtotal() for item in self.vendas)

    def __str__(self):
        titulo = "================================ RELATÓRIO DO CAIXA  ================================"
        largura = len(titulo)
        relatorio = (f'{titulo}\n'
                     f'{self.operador:^{largura}}\n'
                     f'\n')

        for item in self.vendas:
            relatorio += (
                f'Produto: {item.nome:<12}  |  Vendas: {item.quantidade:<8}  |  Subtotal: R${item.subtotal():<15}\n')

        relatorio += (
            f'Total de vendas: {len(self.vendas)}\n'
            f'Total do dia: R$ {self.total_dia():.2f}\n'
        )

        return relatorio
        
if __name__ == "__main__":

    caixa_maria = Caixa("Maria")

    caixa_maria.registrar_venda(ItemVenda("Livro", 25.5, 1))
    caixa_maria.registrar_venda(ItemVenda("Caderno", 12.00, 6))
    caixa_maria.registrar_venda(ItemVenda("Agenda", 28.45, 8))

    print(caixa_maria)


    
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Duas classes com papeis distintos: ItemVenda (dados) e Caixa (agregador)
# ItemVenda guarda nome, preco e quantidade; subtotal() calcula preco * quantidade
# Caixa mantem self.vendas (lista) e o operador responsavel pelo PDV
# registrar_venda recebe instancias de ItemVenda e faz append na lista
# Composicao: um Caixa "tem" varios ItemVenda — objetos colaborando juntos
# total_dia() soma os subtotais com sum() e generator expression
# __str__ monta o relatorio: operador, itens, qtd de vendas e total do dia
# Separar item e caixa deixa cada classe pequena e com responsabilidade clara
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
