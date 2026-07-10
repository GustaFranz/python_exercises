# DEMANDA
# Empresa: MonitoraTI
# Setor: Infraestrutura / backup
# Solicitacao: Listar todos os arquivos em estrutura de pastas para auditoria.

# EXERCICIO 65 - Recursao: estrutura aninhada (contexto corporativo)
#
# Estrutura simulada:
# arvore = {
#   "documentos": {"relatorio.txt": None, "notas": {"prova1.pdf": None}},
#   "imagens": {"logo.png": None},
# }
# Implemente listar_arquivos(no, caminho=""):
## Se valor e dict: para cada chave, chame listar_arquivos recursivamente
## Se valor e None: e arquivo — imprima caminho completo (ex: documentos/relatorio.txt)
# Exiba todos os arquivos encontrados.
#
# ORIENTACOES
## None representa arquivo; dict representa pasta.
## Monte caminho com f"{caminho}/{chave}" ou similar, tratando raiz vazia.
## Desafio leve: integra recursao com estruturas aninhadas.

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
