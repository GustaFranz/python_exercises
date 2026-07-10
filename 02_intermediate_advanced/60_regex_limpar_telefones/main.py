# DEMANDA
# Empresa: Secretaria Digital
# Setor: Educacao / cadastro
# Solicitacao: Padronizar telefones de responsaveis para formato unico.

# EXERCICIO 60 - Regex: limpar telefones (contexto corporativo)
#
# Lista suja:
## "(11) 98765-4321"
## "11 987654321"
## "+55 11 98765-4321"
## "11987654321"
# Para cada item:
## 1) Extraia apenas digitos com re.sub(r"\D", "", texto)
## 2) Se tiver 11 digitos, formate: (XX) XXXXX-XXXX
## 3) Ignore entradas com menos de 10 digitos
# Exiba lista de telefones formatados.
#
# ORIENTACOES
## \D remove tudo que nao e digito.
## Fatie string: ddd = nums[0:2], etc.
## Desafio leve: integra limpeza + formatacao em funcao padronizar_telefone.

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
