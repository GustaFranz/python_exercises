# EXERCICIO 142 - Validador de forma de pagamento com match/case (contexto comercial)
#
# OBJETIVO
# Aplicar match/case para validar formas de pagamento em contexto de cantina ou loja.
#
# CONCEITO - MATCH/CASE COM ALTERNATIVAS (|)
## O operador | no case permite aceitar varios valores no mesmo bloco:
##   case "D" | "C":
##       return "Pagamento em cartao"
## Isso reduz repeticao quando diferentes codigos tem o mesmo tratamento.
## Padronizacao antes do match:
##   codigo = entrada.strip().upper()
## garante que "d", " D " e "D" sejam tratados igualmente.
## case _ e o padrao de seguranca: qualquer codigo nao listado e invalido.
## SRP:
## - validar_pagamento() concentra match/case e regras de negocio
## - try/except no main trata falhas de entrada sem misturar logica de validacao
#
# PASSO A PASSO DETALHADO
## Passo 1: Crie PagamentoInvalidoError(Exception).
## Passo 2: Crie validar_pagamento(codigo) com match/case:
##     def validar_pagamento(codigo):
##         codigo_limpo = codigo.strip().upper()
##         match codigo_limpo:
##             case "D":
##                 return "Dinheiro — pagamento na entrega"
##             case "C":
##                 return "Cartao — debito ou credito"
##             case "P":
##                 return "PIX — transferencia instantanea"
##             case "V":
##                 return "Vale — credito escolar"
##             case _:
##                 raise PagamentoInvalidoError(
##                     "Forma invalida. Use D, C, P ou V."
##                 )
## Explicacao:
## - cada case representa uma forma de pagamento permitida
## - strip().upper() evita erro por espacos ou minusculas
## - case _ lanca excecao para qualquer outro caractere
## Passo 3: Loop principal com try/except fora da funcao:
##     while True:
##         forma = input("Forma de pagamento (D/C/P/V): ")
##         try:
##             mensagem = validar_pagamento(forma)
##             print(mensagem)
##             break
##         except PagamentoInvalidoError as e:
##             print(f"Erro: {e}")
#
# ENUNCIADO
# Crie um validador de forma de pagamento para a cantina escolar.
# Codigos aceitos: D (dinheiro), C (cartao), P (PIX), V (vale escolar).
# O sistema deve:
## solicitar a forma de pagamento;
## confirmar o metodo com mensagem descritiva;
## recusar codigos invalidos sem encerrar o programa.
#
# ORIENTACOES
## match/case dentro da funcao; try/except fora da funcao.
## Use case _ para formas nao reconhecidas.
#
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
