# DEMANDA
# Empresa: Seguros Familia Protegida
# Setor: Seguros / cadastro de clientes
# Solicitacao: Backup automatico antes de cada atualizacao do cadastro de clientes.

# EXERCICIO 34 - JSON: backup incremental (contexto corporativo)
#
# clientes.json com lista de clientes (id, nome, plano).
# Ao atualizar cliente (por id), antes salve copia em backup_YYYYMMDD_HHMMSS.json.
# Use datetime.now().strftime("%Y%m%d_%H%M%S") no nome.
# Implemente: fazer_backup(origem), atualizar_cliente(caminho, id, campo, valor).
# Simule uma atualizacao e confirme que backup foi criado.
#
# ORIENTACOES
## import shutil ou leia e grave copia com json.
## from datetime import datetime para nome do backup.
## Ordem: backup -> carregar -> atualizar -> salvar.

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
