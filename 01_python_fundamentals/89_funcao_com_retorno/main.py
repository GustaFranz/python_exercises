# EXERCICIO 89 - Funcao com retorno (contexto introdutorio)
#
# ENUNCIADO
# Crie uma funcao chamada somar que recebe dois numeros (a, b) e retorna a soma.
# Guarde o resultado da chamada em uma variavel e exiba esse resultado.
#
# ORIENTACOES
## Use a palavra return para devolver o resultado da funcao.
## O valor retornado pode ser guardado em uma variavel.
## Exiba o resultado com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
def somar(a, b):
    return a + b

result_1 = somar(2, 5)

result_2 = somar(-7, 23)

print(f' {result_1}, {result_2}')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro return guardando resultado em variavel
# somar() devolve valor para usar fora da funcao
# Separei calculo (return) de exibicao (print)
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
