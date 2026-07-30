# DEMANDA
# Empresa: MonitoraTI
# Setor: Infraestrutura / observabilidade
# Solicitacao: Auditar arquivo de acesso simulado em chunks para contagem de linhas e tokens ERROR/INFO dentro do SLA de processamento.

# EXERCICIO 47 - With open: ler log em chunks e auditar tokens (contexto corporativo)
#
# CHUNK_SIZE = 128
# 1) Gerar acesso.log com 30+ linhas, ex.:
#    "2026-07-30 INFO usuario=ana acao=login"
#    "2026-07-30 ERROR usuario=bruno acao=timeout"
# 2) Ler em loop: while True: bloco = f.read(CHUNK_SIZE); if not bloco: break
# 3) Acumular blocos (ou contar direto no bloco) para metricas do arquivo inteiro
# 4) Contar linhas (splitlines no texto acumulado ou contador de "\n" nos blocos)
# 5) Contar tokens "ERROR" e "INFO" (str.count e aceitavel neste nivel)
# 6) Relatorio: chunks, caracteres, linhas, ERROR, INFO, % ERROR sobre total de linhas
#
# ORIENTACOES
## Nao carregue o arquivo inteiro com f.read() sem argumento.
## Acumule texto parcial ou some metricas bloco a bloco.
## Gere linhas de log com loop for ao criar o arquivo.
## % ERROR = (linhas com ERROR / total linhas) * 100 — arredonde 1 casa.

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
