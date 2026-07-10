# DEMANDA
# Empresa: AgroEscola
# Setor: Educacao / campo
# Solicitacao: Exibir previsao do tempo para visita tecnica mesmo se API falhar.

# EXERCICIO 89 - HTTP: consulta com fallback (contexto corporativo)
#
# simular_clima_api(sucesso=True):
## sucesso True -> {"status": 200, "cidade": "Campinas", "temp": 28}
## sucesso False -> {"status": 0, "erro": "Timeout"}
# DADOS_PADRAO = {"cidade": "Campinas", "temp": 25, "fonte": "cache local"}
# Implemente obter_previsao(usar_api=True):
## Tenta API; se status 200 retorna dados com fonte "api"
## Senao retorna DADOS_PADRAO com aviso "Usando dados em cache"
#
# ORIENTACOES
## Fallback = plano B quando servico principal falha.
## Teste com usar_api=True (falha) e simule sucesso alterando simular_clima_api.

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
