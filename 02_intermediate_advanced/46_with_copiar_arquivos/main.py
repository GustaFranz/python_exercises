# DEMANDA
# Empresa: Clinica BemViver
# Setor: Saude / prontuario digital
# Solicitacao: Copiar prontuario resumido para pasta backup antes de atualizacao do sistema, com auditoria de sucesso ou falha.

# EXERCICIO 46 - With open: copiar arquivos com verificacao de integridade (contexto corporativo)
#
# Pipeline de backup local:
# 1) Criar pasta backup/ (os.makedirs com exist_ok=True e permitido)
# 2) Criar prontuario_maria.txt com 4+ linhas de resumo de consulta
# 3) Copiar para backup/prontuario_maria.txt com with open (leitura + escrita)
# 4) Verificar integridade: conteudo igual OU mesma quantidade de linhas
# 5) Relatorio: status SUCESSO/FALHA, origem, destino, linhas original vs backup
#
# ORIENTACOES
## Use with open para ler origem e gravar destino.
## Contagem de linhas: len(conteudo.splitlines()) ou loop de readlines.
## status = "SUCESSO" se integridade ok; senao "FALHA" com mensagem curta.
## Nao use shutil.copy — pratique leitura/escrita manual com with.

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
