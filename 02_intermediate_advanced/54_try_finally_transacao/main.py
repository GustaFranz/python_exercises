# DEMANDA
# Empresa: FinEdu Carteira
# Setor: Financeiro educacional
# Solicitacao: Registrar toda tentativa de transferencia no log, com ou sem erro.

# EXERCICIO 54 - Try finally: transacao simulada (contexto corporativo)
#
# Variavel global simulada: log_operacoes = []
# Funcao transferir(origem, destino, valor, saldo):
## try: se valor > saldo: raise SaldoInsuficienteError (reutilize ou recrie)
##       senao retorna saldo - valor
## except SaldoInsuficienteError as e: registra erro; retorna saldo
## finally: append em log_operacoes com texto "Tentativa origem->destino: valor"
# Execute 2 transferencias e exiba log ao final.
#
# ORIENTACOES
## finally adiciona ao log sempre — sucesso ou falha.
## SaldoInsuficienteError pode ser a mesma do exercicio 46.

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
