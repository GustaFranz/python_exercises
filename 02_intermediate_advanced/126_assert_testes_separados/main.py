# DEMANDA
# Empresa: DevEscola Labs
# Setor: Educacao / qualidade
# Solicitacao: Validar modulo de desconto e pedido minimo antes de liberar checkout do bazar escolar.

# EXERCICIO 126 - Assert: testes separados com regras de negocio (nivel entrevista junior)
#
# calculos.py — implemente:
## calcular_desconto(valor: float, percentual: float) -> float
##   aplica percentual (0 a 100) sobre valor; valor >= 0
##   percentual invalido (< 0 ou > 100): raise ValueError
## validar_pedido(qtd: int) -> bool
##   True se qtd >= 1; False se qtd <= 0
#
# testes.py — importe calculos e escreva asserts para:
## calcular_desconto(100, 0) == 100
## calcular_desconto(100, 10) == 90
## calcular_desconto(100, 100) == 0
## calcular_desconto(0, 50) == 0
## percentual negativo e acima de 100 devem falhar (try/except ou pytest-style assert raises)
## validar_pedido(0) == False
## validar_pedido(-3) == False
## validar_pedido(5) == True
#
# main.py — apenas oriente: "Execute: python testes.py"
#
# ORIENTACOES
## Separe implementacao (calculos.py) de testes (testes.py).
## Em testes.py: if __name__ == "__main__": rodar asserts e print "Todos os testes passaram."
## Padrao comum em entrevista: modulo puro + suite minima de asserts.

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
