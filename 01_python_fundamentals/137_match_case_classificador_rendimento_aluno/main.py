# EXERCICIO 137 - Classificador de rendimento do aluno com match/case (contexto educacional)
#
# PASSO A PASSO
## Passo 1: Crie a excecao RendimentoInvalidoError para siglas nao permitidas.
## Passo 2: Crie a funcao classificar_rendimento(sigla) com match/case dentro da funcao.
##         Padronize a entrada com strip().upper() antes do match.
##         Aceite apenas: MB (muito bom), B (bom), R (regular), I (insuficiente).
##         Use case _ para lancar excecao quando a sigla for invalida.
## Passo 3: Fora da funcao, leia a sigla do usuario em um loop.
## Passo 4: Use try/except para capturar RendimentoInvalidoError e pedir nova entrada.
## Passo 5: Exiba a classificacao quando a sigla for valida e encerre o loop.
#
# ENUNCIADO
# Crie um classificador de rendimento escolar baseado em siglas.
# O sistema deve:
## solicitar a sigla de rendimento (MB, B, R ou I);
## exibir a descricao correspondente ao rendimento;
## impedir siglas invalidas sem encerrar o programa.
#
# ORIENTACOES
## match/case dentro da funcao; try/except fora da funcao.
## Respeite o principio SRP.
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
