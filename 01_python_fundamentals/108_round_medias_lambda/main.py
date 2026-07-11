# EXERCICIO 108 - Arredondar medias com lambda (contexto educacional)
#
# ENUNCIADO
# Dada a lista de medias com varias casas decimais:
# medias = [7.456, 8.923, 6.111, 9.876, 5.549]
# Gere uma nova lista arredondando cada media para 1 casa decimal.
# Exiba a lista original e a lista arredondada.
#
# ORIENTACOES
## Use map(lambda m: round(m, 1), medias).
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

medias = [7.456, 8.923, 6.111, 9.876, 5.549]
medias_arredondadas = list(map(lambda m: round(m, 1), medias))

print(f'//green/Medias arredondadas/green //yellow/{medias_arredondadas}/yellow')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# map com round(m, 1) limpa medias com muitas casas
# Lambda + round dentro do map evita for item a item
# Lista original separada da transformada
# Animado em deixar notas legiveis rapidamente
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
