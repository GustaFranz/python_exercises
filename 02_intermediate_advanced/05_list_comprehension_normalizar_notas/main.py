# DEMANDA
# Empresa: Secretaria Municipal de Educacao
# Setor: Gestao publica escolar
# Solicitacao: Limpar notas invalidas antes de calcular estatisticas da rede.

# EXERCICIO 05 - List comprehension: normalizar notas (contexto corporativo)
#
# notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0]
# Regras de validacao: nota numerica entre 0 e 10 (ignore None e valores fora do intervalo).
# 1) Gere notas_validas com list comprehension (apenas valores validos).
# 2) Gere notas_arredondadas com uma casa decimal.
# 3) Exiba: quantidade descartada, media das validas e lista final.
#
# ORIENTACOES
## Primeiro filtre: [n for n in notas_brutas if isinstance(n, (int, float)) and 0 <= n <= 10]
## Arredonde na segunda comprehension ou com round(n, 1).
## Use sum() e len() para media.

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
