# EXERCICIO 145 - Validador de tipo de passagem com match/case (contexto urbano)
#
# OBJETIVO
# Usar match/case com guardas (if) para validar tipos de passagem de transporte.
#
# CONCEITO - MATCH/CASE COM GUARDAS (if)
## Quando a validacao depende de intervalo ou condicao extra, use guardas:
##   match valor:
##       case n:
##           if isinstance(n, int) and 0 <= n <= 100:
##               return "Valido"
## Guardas permitem combinar match/case com logica condicional sem if/elif longos.
## Para entradas de texto que representam categorias fixas, literais sao suficientes:
##   case "I": return "Integral"
## Para valores numericos de desconto ou codigo, converta antes:
##   preco = float(entrada.replace(",", "."))
##   match preco:
##       case p if p == 0:
##           return "Gratuidade"
## SRP:
## - validar_passagem() usa match/case e raise
## - main() usa try/except para ValueError (conversao) e excecao customizada
#
# PASSO A PASSO DETALHADO
## Passo 1: Crie PassagemInvalidaError(Exception).
## Passo 2: Crie validar_passagem(tipo) com match/case:
##     def validar_passagem(tipo):
##         tipo_limpo = tipo.strip().upper()
##         match tipo_limpo:
##             case "I":
##                 return "Passagem integral — tarifa completa"
##             case "E":
##                 return "Passagem estudante — 50% de desconto"
##             case "G":
##                 return "Gratuidade — idoso ou deficiente"
##             case "S":
##                 return "Social — tarifa reduzida"
##             case _:
##                 raise PassagemInvalidaError(
##                     "Tipo invalido. Use I, E, G ou S."
##                 )
## Explicacao:
## - case "I" | "E" poderia unir tipos, mas aqui cada um tem mensagem distinta
## - upper() padroniza entrada independente de maiusculas/minusculas
## - case _ garante que tipos desconhecidos nunca passam silenciosamente
## Passo 3: Fluxo principal com try/except fora da funcao:
##     while True:
##         tipo = input("Tipo de passagem (I/E/G/S): ")
##         try:
##             info = validar_passagem(tipo)
##             print(info)
##             break
##         except PassagemInvalidaError as e:
##             print(f"Erro: {e}")
#
# ENUNCIADO
# Crie um validador de tipo de passagem para transporte publico escolar.
# Codigos aceitos: I (integral), E (estudante), G (gratuidade), S (social).
# O sistema deve:
## solicitar o tipo de passagem;
## exibir a descricao e beneficio da tarifa;
## recusar tipos invalidos sem quebrar o programa.
#
# ORIENTACOES
## match/case dentro da funcao; try/except fora da funcao.
## Use case _ para tipos nao reconhecidos.
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
