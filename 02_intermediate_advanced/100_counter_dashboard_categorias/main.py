# DEMANDA
# Empresa: MonitoraTI
# Setor: Infraestrutura / NOC
# Solicitacao: Painel rapido de alertas por tipo para reuniao diaria de status (standup).

# EXERCICIO 100 - Counter: dashboard textual para standup (nivel entrevista junior)
#
# Eventos do turno:
## ["cpu", "disco", "cpu", "rede", "cpu", "disco", "memoria", "cpu", "rede", "cpu"]
#
# Implemente:
## montar_contador(eventos) -> Counter
## calcular_percentual(qtd, total) -> float
## identificar_gargalo(contador) -> tuple[str, int]  # categoria e quantidade top
## gerar_dashboard(eventos) -> str multilinha para standup
#
# Formato esperado (exemplo):
## === Dashboard de alertas — turno manha ===
## cpu: 5 (50.0%)
## disco: 2 (20.0%)
## rede: 2 (20.0%)
## memoria: 1 (10.0%)
## Total: 10 eventos
## Gargalo: cpu (5 eventos)
#
# ORIENTACOES
## Percentual: (qtd / total) * 100 com uma casa decimal.
## Gargalo = categoria com maior contagem (most_common(1)).
## Retorne string formatada; main imprime o dashboard.

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
