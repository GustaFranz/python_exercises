# DEMANDA
# Empresa: Loja Virtual Escolar
# Setor: Varejo / precificacao
# Solicitacao: Calcular preco final no bazar conforme perfil: cliente comum, escola ou parceiro.

# EXERCICIO 110 - Heranca: descontos polimorficos por cliente (nivel entrevista junior)
#
# Hierarquia:
## class Cliente: __init__(self, nome); desconto(self) -> 0.0
## class ClienteEscola(Cliente): desconto(self) -> 0.10
## class ClienteParceiro(Cliente): desconto(self) -> 0.15
#
# Funcao:
## calcular_preco_final(cliente: Cliente, valor: float) -> float
##   return valor * (1 - cliente.desconto())
#
# Lista polimorfica de teste:
## [
##   Cliente("Maria"),
##   ClienteEscola("Escola 12"),
##   ClienteParceiro("Papelaria Centro"),
## ]
#
# Para valor_base = 100.0, exiba tabela:
## Nome | Tipo | Desconto | Preco final
#
# ORIENTACOES
## Polimorfismo: loop unico sobre list[Cliente] sem if/elif por tipo.
## isinstance() so se necessario para exibir "Tipo" no relatorio.
## Pergunta classica: por que desconto() na base retorna 0.0?

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
