# EXERCICIO 109 - Arredondar precos com lambda (contexto de comercio)
#
# ENUNCIADO
# Dada a lista de precos:
# precos = [12.345, 5.678, 99.991, 3.333, 48.876]
# Gere uma nova lista arredondando cada preco para 2 casas decimais.
# Exiba a lista original e a lista arredondada.
#
# ORIENTACOES
## Use map(lambda p: round(p, 2), precos).
## Converta o resultado para list().
## Nao altere a lista original.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

precos = [12.345, 5.678, 99.991, 3.333, 48.876]

precos_arredondados = list(map(lambda p: round(p, 2), precos))

print(f'//green/Precos arredondados/green //yellow/{precos_arredondados}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# round(p, 2) formata precos para duas casas
# map arredonda toda a lista sem loop manual
# Animado em preparar valores para exibicao comercial
# Lista original intacta apos o map
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
