# DEMANDA
# Empresa: MonitoraTI
# Setor: Infraestrutura / integracoes
# Solicitacao: Repetir consulta ao servico de monitoramento quando falhar na primeira tentativa.

# EXERCICIO 87 - HTTP: retry simples (contexto corporativo)
#
# simular_servico(tentativa):
## tentativa 1 -> {"status": 0, "erro": "Timeout"}
## tentativa >= 2 -> {"status": 200, "dados": "Servidor OK"}
# Implemente consultar_com_retry(max_tentativas=3):
## Tenta de 1 ate max_tentativas
## Retorna dados quando status 200
## Se esgotar tentativas: retorna None e mensagem de falha
#
# ORIENTACOES
## Loop for com range(1, max_tentativas + 1).
## Retry e padrao comum em integracoes reais.

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
