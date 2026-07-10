# DEMANDA
# Empresa: Clinica BemViver
# Setor: Saude / LGPD
# Solicitacao: Exibir CPF mascarado em telas de recepcao.

# EXERCICIO 58 - Regex: mascarar CPF (contexto corporativo)
#
# CPF de entrada: "123.456.789-00"
# Substitua os 3 primeiros blocos por *** mantendo os 2 ultimos digitos visiveis.
# Resultado esperado: ***.***.***-00
# Use re.sub com padrao que capture os digitos finais.
#
# ORIENTACOES
## Padrao exemplo: r"\d{3}\.\d{3}\.\d{3}-(\d{2})"
## Substituicao: r"***.***.***-\1"
## Teste com um unico CPF formatado.

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
