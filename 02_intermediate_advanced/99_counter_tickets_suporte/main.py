# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / suporte
# Solicitacao: Resumir backlog da plataforma por categoria e sinalizar risco de SLA em tickets criticos.

# EXERCICIO 99 - Counter: tickets de suporte e SLA (nivel entrevista junior)
#
# Tickets de exemplo:
## [
##   {"id": 101, "categoria": "login", "prioridade": "alta", "titulo": "Senha bloqueada"},
##   {"id": 102, "categoria": "notas", "prioridade": "media", "titulo": "Nota errada"},
##   {"id": 103, "categoria": "login", "prioridade": "alta", "titulo": "Acesso negado"},
##   {"id": 104, "categoria": "video", "prioridade": "baixa", "titulo": "Aula travando"},
##   {"id": 105, "categoria": "notas", "prioridade": "alta", "titulo": "Media incorreta"},
##   {"id": 106, "categoria": "pagamento", "prioridade": "alta", "titulo": "Boleto duplicado"},
##   {"id": 107, "categoria": "video", "prioridade": "media", "titulo": "Sem audio"},
##   {"id": 108, "categoria": "login", "prioridade": "alta", "titulo": "2FA falhou"},
## ]
#
# Implemente:
## contar_por_categoria(tickets) -> Counter
## contar_criticos(tickets) -> int  # prioridade == "alta"
## backlog_ordenado(contador) -> list[tuple]  # most_common
## verificar_sla(qtd_criticos, limite=3) -> str  # "OK" ou mensagem de alerta
## gerar_relatorio(tickets) -> imprime visao completa para o time de suporte
#
# ORIENTACOES
## Counter([t["categoria"] for t in tickets]) e .most_common().
## SLA: if qtd_criticos > 3: alerta de risco operacional.
## Nivel entrevista: combinar collections, filtros e relatorio textual.

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
