# DEMANDA
# Empresa: Secretaria Municipal de Educacao
# Setor: Gestao publica escolar / dados
# Solicitacao: Limpar lote de notas do staging antes de publicar no dashboard da rede.

# EXERCICIO 05 - List comprehension: pipeline de limpeza de notas (contexto corporativo)
#
# notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]
# Regras: so int/float; 0..10; arredondar 1 casa; status aprovado (>=6) / recuperacao
# 1) notas_validas (filtro)
# 2) notas_arredondadas (round)
# 3) status_lote = [{nota, status}, ...]
# 4) Auditoria: recebidas, descartadas, % descartado, media, qtd por status, lista final
#
# ORIENTACOES
## isinstance(n, (int, float)) and not isinstance(n, bool)
## descartadas = len(notas_brutas) - len(notas_validas)
## status = "aprovado" if nota >= 6 else "recuperacao"

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
