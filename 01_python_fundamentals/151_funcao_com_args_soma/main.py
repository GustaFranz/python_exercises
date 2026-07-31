# EXERCICIO 151 - Funcao com *args: soma variavel (contexto introdutorio)
#
# ENUNCIADO
# Crie uma funcao chamada somar_todos que recebe *args e retorna a soma de todos os numeros.
# Teste a funcao com:
## somar_todos(4, 6)
## somar_todos(10, 20, 30)
## somar_todos(1, 2, 3, 4, 5)
# Exiba cada resultado com uma mensagem clara.
#
# ORIENTACOES
## Use def somar_todos(*args): para aceitar varios argumentos.
## Percorra args com um loop ou use sum(args).
## *args chega como tupla; voce pode receber qualquer quantidade de valores.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

def somar_todos(*args):
    soma = sum(args)
    return soma

soma1 = somar_todos(4, 6)
soma2 = somar_todos(10, 20, 30)
soma3 = somar_todos(1, 2, 3, 4, 5)
soma = soma1, soma2, soma3
soma_total = sum(soma)

print(f'Soma 1 = {soma1},\n'
      f'Soma 2 = {soma2},\n'
      f'soma 3 = {soma3},\n'
      f'As tupla das somas é {soma},\n'
      f'A soma total é {soma_total}.')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
