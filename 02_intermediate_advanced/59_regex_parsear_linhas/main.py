# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / importacao
# Solicitacao: Interpretar linhas de exportacao no formato nome;nota;turma.

# EXERCICIO 59 - Regex: parsear linhas (contexto corporativo)
#
# Linhas:
## Ana Silva;8.5;7B
## Bruno Costa;6.0;8A
## Carla;9.2;7B
# Para cada linha, extraia nome, nota e turma com re.search:
# Padrao sugerido: r"^(.+);([\d.]+);(\w+)$"
# Monte lista de dicts e exiba alunos da turma 7B.
#
# ORIENTACOES
## group(1), group(2), group(3) para os campos.
## Converta nota para float.
## Filtre turma == "7B" ao exibir.

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
