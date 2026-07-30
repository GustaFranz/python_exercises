# DEMANDA
# Empresa: LimpezaDados Servicos
# Setor: Tratamento de dados
# Solicitacao: Rastrear importacao de vendas escolares com alertas quando a base chega vazia ou invalida.

# EXERCICIO 88 - Logging: pipeline ETL por etapas (nivel entrevista junior)
#
# Mini ETL em 3 funcoes:
## carregar_vendas(fonte) -> logging.info("Etapa 1: carregar") -> retorna lista bruta
## limpar_vendas(vendas) -> logging.info("Etapa 2: limpar") -> remove vazios/invalidos
##   cada registro descartado: logging.warning com motivo
## agregar_vendas(vendas) -> logging.info("Etapa 3: agregar") -> retorna dict {qtd, total}
##   se qtd == 0: logging.error("Nenhum registro valido para agregar")
#
# Dados brutos (simulando CSV importado):
## [
##   {"produto": "Caderno", "valor": 12.50},
##   {"produto": "", "valor": 0},
##   {"produto": "Caneta", "valor": 3.00},
##   {"produto": "   ", "valor": 5.00},
##   {"produto": "Lapis", "valor": -1},
##   {"produto": "Borracha", "valor": 2.00},
## ]
#
# Funcao executar_pipeline(fonte) orquestra as 3 etapas e retorna resultado da agregacao.
# Exiba resumo: quantidade valida e valor total agregado.
#
# ORIENTACOES
## Registro invalido: produto vazio/whitespace ou valor <= 0.
## Use logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s").
## Nivel entrevista: pipeline legivel, logs uteis para operacao, sem solucao pronta abaixo.

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
