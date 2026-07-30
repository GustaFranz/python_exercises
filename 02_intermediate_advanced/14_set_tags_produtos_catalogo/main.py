# DEMANDA
# Empresa: Livraria Saber
# Setor: Varejo / catalogo digital
# Solicitacao: Garantir filtros do e-commerce com tags obrigatorias e limpar tags orfas.

# EXERCICIO 14 - Set: auditoria de tags do catalogo
#
# produtos = [
#     {"nome": "Python Basico", "tags": ["programacao", "iniciante", "python"]},
#     {"nome": "Git Pratico", "tags": ["ferramentas", "git", "iniciante"]},
#     {"nome": "Logica", "tags": ["logica", "iniciante"]},
#     {"nome": "SQL Pro", "tags": ["banco", "avancado", "sql"]},
# ]
# tags_obrigatorias = {"programacao", "iniciante", "ferramentas"}
# tags_proibidas = {"spam", "promocao_falsa"}
# tags_permitidas_extra = {"python", "git", "logica", "banco", "avancado", "sql"}
# 1) tags_catalogo = uniao de todas as tags
# 2) cobertura_ok, faltando, orfas, bloqueadas
# 3) Relatorio com totais e conjuntos ordenados
#
# ORIENTACOES
## tags_catalogo = set(); for p in produtos: tags_catalogo |= set(p["tags"])
## faltando = tags_obrigatorias - tags_catalogo
## orfas = tags_catalogo - tags_obrigatorias - tags_permitidas_extra
## sorted(conjunto) para exibir

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
