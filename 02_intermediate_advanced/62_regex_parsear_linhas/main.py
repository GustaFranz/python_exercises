# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / importacao
# Solicitacao: Validar lote de exportacao nome;nota;turma antes de carregar no sistema, com relatorio de rejeicoes.

# EXERCICIO 62 - Regex: parsear linhas de exportacao escolar (contexto corporativo)
#
# linhas = [
#   "Ana;7.5;7A", "Bruno;8.0;7B", ";6.0;7A", "Carla;nota;7A",
#   "Pedro;5.5;7A", "7A;12.0;7A", "Lucas;9.2;7B",
# ]
#
# Para cada linha:
#   match = re.search(r"^(.+);([\d.]+);(\w+)$", linha)
#   se match: dict {nome, nota: float, turma}
#   senao: append linha em rejeitadas
#
# Extra: rejeitar nome vazio apos strip ou nota fora de 0..10 (regra de negocio)
# Filtrar turma == "7A" e exibir
# Relatorio: recebidas, validos, rejeitados, rejeitadas
#
# ORIENTACOES
## import re no inicio.
## group(1), group(2), group(3) para extrair campos.
## Valide nota 0..10 apos converter para float.
## Padrao classico de entrevista junior: parse + validate + report.

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
