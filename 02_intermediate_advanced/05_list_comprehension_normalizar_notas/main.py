# ==============================================================================
# DEMANDA DE TRABALHO (TICKET)
# Empresa: Secretaria Municipal de Educação
# Setor: Gestão Pública Escolar / Dados
#
# CONTEXTO:
# As escolas enviaram um lote de notas para a base temporária (staging).
# Antes de publicar esses dados no dashboard da rede, você precisa sanitizar
# a lista e gerar um relatório de auditoria sobre a qualidade dos dados.
# ==============================================================================
# 1. DADOS DE ENTRADA (BASE STAGING)
# A lista abaixo contém erros propositais (strings, nulos e valores fora da escala).
# ------------------------------------------------------------------------------
# notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]
# ------------------------------------------------------------------------------
# 2. REGRAS DE NEGÓCIO E VALIDAÇÃO
# Uma nota só é considerada VÁLIDA se atender a TODAS as condições:
#   a) Tipo: Numérico (int ou float). 
#      *Atenção: Booleans (True/False) devem ser desconsiderados!
#   b) Intervalo: Estritamente entre 0.0 e 10.0 (inclusive).
# ------------------------------------------------------------------------------
# 3. O QUE VOCÊ DEVE DESENVOLVER (REQUISITOS)
# Utilize LIST COMPREHENSION para resolver as Etapas 1, 2 e 3:
# [ ] Etapa 1: notas_validas
#     Filtre a lista 'notas_brutas' mantendo apenas os elementos válidos.
# [ ] Etapa 2: notas_arredondadas
#     A partir de 'notas_validas', garanta que todas as notas estejam
#     arredondadas para 1 casa decimal (dica: use round(nota, 1)).
# [ ] Etapa 3: status_lote
#     Crie uma lista de dicionários mapeando a nota e a situação do aluno.
#     - Regra: nota >= 6.0 -> "aprovado" | nota < 6.0 -> "recuperacao"
#     - Formato do item: {"nota": 7.5, "status": "aprovado"}
# [ ] Etapa 4: Relatório de Auditoria
#     Calcule e exiba no terminal os seguintes indicadores:
#       1) Qtd total de notas recebidas
#       2) Qtd total de notas descartadas
#       3) Percentual de descarte (%)
#       4) Média geral das notas válidas
#       5) Qtd total de aprovados e de recuperações
#       6) A lista final formatada (status_lote)
# ------------------------------------------------------------------------------
# 4. DICAS TÉCNICAS E FÓRMULAS
# - Checagem de tipo exato (evita booleans):
#   isinstance(n, (int, float)) and not isinstance(n, bool)
# - Qtd de notas descartadas:
#   len(notas_brutas) - len(notas_validas)
# - If ternário no List Comprehension (Etapa 3):
#   "aprovado" if nota >= 6.0 else "recuperacao"
# ------------------------------------------------------------------------------
# 5. EXEMPLO DE SAÍDA ESPERADA NO TERMINAL:
# === RELATÓRIO DE AUDITORIA DO LOTE ===
# Total recebidas:  12
# Total descartadas: 5
# % Descartadas:     41.67%
# Média das válidas: 6.36
# Aprovados:         5
# Recuperação:       2
#
# --- DADOS FINAIS PARA O DASHBOARD ---
# [
#   {'nota': 7.5, 'status': 'aprovado'},
#   {'nota': 8.0, 'status': 'aprovado'},
#   {'nota': 6.5, 'status': 'aprovado'},
#   {'nota': 4.0, 'status': 'recuperacao'},
#   {'nota': 9.0, 'status': 'aprovado'},
#   {'nota': 0.0, 'status': 'recuperacao'},
#   {'nota': 10.0, 'status': 'aprovado'}
# ]
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]







# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
