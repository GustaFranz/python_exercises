# DEMANDA
# Empresa: MonitoraTI
# Setor: Infraestrutura / suporte
# Solicitacao: Padronizar mensagens do script de verificacao de servidores.

# EXERCICIO 81 - Introducao ao logging (contexto corporativo)
#
# VISAO DO BLOCO — logging (exercicios 81 a 85)
# Este bloco treina:
## 81 — Introducao: substituir print por logging.info
## 82 — Niveis INFO e ERROR
## 83 — Gravar log em arquivo
## 84 — Pipeline com log em cada etapa
## 85 — Auditoria CSV com log estruturado
#
# Conceitos basicos:
## import logging
## logging.basicConfig(level=logging.INFO)
## logging.info("mensagem") / logging.error("falha")
## Melhor que print para scripts profissionais e depuracao
#
# Implemente verificar_servidor(nome, online):
## Se online: logging.info(f"Servidor {nome}: OK")
## Se nao: logging.error(f"Servidor {nome}: OFFLINE")
# Configure basicConfig(level=logging.INFO) no inicio.
# Teste com ("web-01", True) e ("db-01", False).
# Nao use print — apenas logging.
#
# ORIENTACOES
## logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
## Substitua prints por logging.info e logging.error.

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
