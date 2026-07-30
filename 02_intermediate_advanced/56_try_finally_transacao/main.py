# DEMANDA
# Empresa: FinEdu Carteira
# Setor: Financeiro educacional
# Solicitacao: Processar transferencias com fallback seguro e trilha de auditoria mesmo quando a operacao falha.

# EXERCICIO 56 - Try finally: transferencia com auditoria obrigatoria (contexto corporativo)
#
# contas = {"ana": 500.0, "bruno": 120.0}
#
# def transferir(origem, destino, valor):
#   status = "ok"
#   try:
#     if valor > contas[origem]:
#       raise ValueError("Saldo insuficiente")
#     contas[origem] -= valor
#     contas[destino] += valor
#   except ValueError:
#     status = "fail"
#   finally:
#     append em auditoria.log: f"{origem}->{destino};{valor};{status}"
#
# Testes obrigatorios:
# 1) transferir("ana", "bruno", 80.0)  -> sucesso
# 2) transferir("bruno", "ana", 999.0) -> falha (saldo insuficiente)
# Exiba contas finais e leia auditoria.log ao final.
#
# ORIENTACOES
## finally executa sempre — sucesso ou falha.
## Use with open("auditoria.log", "a", encoding="utf-8") no finally.
## ValueError e o contrato de negocio pedido (nao precisa excecao customizada).
## Nao altere saldos quando der ValueError.

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
