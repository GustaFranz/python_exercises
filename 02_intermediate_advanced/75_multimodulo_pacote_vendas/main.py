# DEMANDA
# Empresa: Loja Virtual Escolar
# Setor: Varejo / analytics
# Solicitacao: Empacotar analise de vendas escolares para reutilizar em outros scripts.

# EXERCICIO 75 - Multi-modulo: pacote analise_vendas (contexto corporativo)
#
# analise_vendas/vendas.py: total_vendas(vendas) soma campo "valor" de cada dict
# analise_vendas/relatorio.py: gerar_resumo(total, qtd) -> string
# analise_vendas/__init__.py: from .vendas import total_vendas; from .relatorio import gerar_resumo
# main.py: from analise_vendas import total_vendas, gerar_resumo
# Dados: [{"produto": "caderno", "valor": 12}, {"produto": "caneta", "valor": 3}]
#
# ORIENTACOES
## __init__.py torna a pasta um pacote importavel.
## Use imports relativos dentro do pacote (from .vendas import ...).
## Desafio leve: estrutura reutilizavel em projetos maiores.

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
