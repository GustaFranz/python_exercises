# DEMANDA
# Empresa: BigData Escolar
# Setor: Educacao / analytics
# Solicitacao: Evitar consultas repetidas a API de indicadores escolares.

# EXERCICIO 90 - HTTP: cache e log de falhas (contexto corporativo)
#
# Cache global: cache_api = {}
# simular_indicador(id, falhar=False):
## falhar True -> {"status": 500, "erro": "Erro interno"}
## falhar False -> {"status": 200, "dados": {"id": id, "valor": id * 10}}
# Implemente buscar_indicador(id, falhar=False):
## Se id no cache: retorna cache[id] com mensagem "Cache hit"
## Senao consulta API; se 200 grava cache e retorna
## Se falha: logging.error e retorna None
# Teste: 2 chamadas mesmo id (2a deve usar cache), 1 chamada com falha.
#
# ORIENTACOES
## Desafio leve: integra dict cache + logging + tratamento HTTP simulado.
## import logging no inicio.

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
