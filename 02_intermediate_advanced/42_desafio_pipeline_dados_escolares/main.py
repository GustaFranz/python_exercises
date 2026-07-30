# DEMANDA
# Empresa: DataEdu Analytics
# Setor: Educacao / engenharia de dados junior
# Solicitacao: Pipeline de staging: cruzar cadastro e notas, persistir JSON e exportar CSV limpo.

# DESAFIO - Pipeline de dados escolares
# Conteudos: merge, JSON, CSV, with open
#
# 1) with open: ler cadastro.json e notas.csv (crie os arquivos se preciso)
# 2) merge left por id; orfas -> inconsistencias
# 3) gravar saida/consolidado.json
# 4) exportar saida/aprovacao.csv (so com nota); status aprovado se nota >= 6
# 5) resumo: lidos, consolidados, inconsistencias, exportados
#
# ORIENTACOES
## import json, csv, os
## os.makedirs("saida", exist_ok=True)
## indice_notas = {int(r["id"]): float(r["nota"]) for r in ...}

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
