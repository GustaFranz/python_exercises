# DEMANDA
# Empresa: LimpezaDados Servicos
# Setor: Tratamento de dados
# Solicitacao: Limpar base de clientes importada antes de subir ao CRM.

# EXERCICIO 40 - CSV: pipeline limpar e exportar (contexto corporativo)
#
# clientes_sujos.csv com problemas:
# nome,email,idade
# Ana,ana@mail.com,25
# ,bruno@mail.com,30        <- nome vazio
# Carla,email-invalido,abc  <- idade invalida
# Daniel,daniel@mail.com,28
# Pipeline:
## 1) Ler CSV
## 2) Filtrar: nome nao vazio, idade numerica, "@" no email
## 3) Exportar clientes_limpos.csv
# Exiba: lidos, descartados, exportados.
#
# ORIENTACOES
## Validar cada linha antes de incluir na lista limpa.
## isinstance ou try/int(idade) para idade.
## DictWriter para exportar resultado.
## Crie clientes_sujos.csv no inicio do script se necessario.

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
