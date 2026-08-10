# DEMANDA
# Empresa: Loja Virtual Escolar
# Setor: Varejo / estoque
# Solicitacao: Controlar estoque de material escolar na loja virtual.

# EXERCICIO 103 - Classe Produto: estoque (contexto corporativo)
#
# Classe Produto:
## __init__(self, nome, preco, estoque)
## vender(self, qtd): reduz estoque se houver; retorna True/False
## repor(self, qtd): aumenta estoque
## __str__: nome, preco e estoque atual
# Teste: produto com estoque 5, vender 3 (ok), vender 5 (falha), repor 10.
#
# ORIENTACOES
## vender retorna False se qtd > estoque sem alterar estoque.
## Metodos usam self.estoque para manter estado.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade > self.estoque:
            return False
        else:
            self.estoque -= quantidade
            return True

    def repor(self, quantidade):
        self.estoque += quantidade
        return True

    def __str__(self):
        return f'Produto: {self.nome} | Preço: {self.preco}  | Estoque atual: {self.estoque}'

caderno = Produto("Caderno", 10.0, 5)
print()
print(caderno)
caderno.vender(3)
print('Vender 3')
caderno.vender(5)
print('Vender 5')
caderno.repor(10)
print('Repor 10')
print()
print(caderno)
print()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
