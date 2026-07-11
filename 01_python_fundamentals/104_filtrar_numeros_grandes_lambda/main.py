# EXERCICIO 104 - Filtrar numeros grandes com lambda (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista de numeros:
# numeros = [3, 8, 15, 22, 7, 30, 4, 18]
# Gere uma nova lista apenas com valores maiores que 10.
# Exiba a lista filtrada e a quantidade de itens.
#
# ORIENTACOES
## Use filter(lambda n: n > 10, numeros).
## Converta o resultado para list().
## Use len() para contar os itens filtrados.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

numeros = [3, 8, 15, 22, 7, 30, 4, 18]
numeros_maiores_dez = list(filter(lambda x: x > 10, numeros))

print(f'//green/Números maiores que 10/green //yellow/{numeros_maiores_dez}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# filter(lambda x: x > 10, numeros) mantem so os grandes
# Lambda como criterio booleano no filter
# list() materializa o resultado filtrado
# Animado em separar valores sem escrever for
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
