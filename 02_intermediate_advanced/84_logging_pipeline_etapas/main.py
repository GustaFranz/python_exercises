# DEMANDA
# Empresa: LimpezaDados Servicos
# Setor: Tratamento de dados
# Solicitacao: Rastrear etapas de limpeza de base de clientes importada.

# EXERCICIO 84 - Logging: pipeline por etapas (contexto corporativo)
#
# Pipeline em 3 funcoes:
## etapa_ler(dados) -> logging.info("Etapa 1: leitura") -> retorna dados
## etapa_limpar(dados) -> logging.info("Etapa 2: limpeza") -> remove vazios
## etapa_exportar(dados) -> logging.info("Etapa 3: exportacao") -> retorna qtd
# Dados iniciais: ["Ana", "", "Bruno", "  ", "Carla"]
# Execute pipeline e exiba quantidade exportada.
#
# ORIENTACOES
## Cada etapa registra inicio com logging.info.
## Use logging.error se lista ficar vazia apos limpeza.

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
