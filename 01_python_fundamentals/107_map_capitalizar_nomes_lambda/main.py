# EXERCICIO 107 - Capitalizar nomes com map e lambda (contexto educacional)
#
# ENUNCIADO
# Dada a lista de nomes em minusculo:
# nomes = ["ana", "bruno", "carla", "diego"]
# Gere uma nova lista com cada nome capitalizado (primeira letra maiuscula).
# Exiba a lista original e a lista transformada.
#
# ORIENTACOES
## Use map(lambda nome: nome.capitalize(), nomes).
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

nomes = ["ana", "bruno", "carla", "diego"]
nomes_capitalizados = list(map(lambda x: x.capitalize(), nomes))

print(f'//green/Nomes capitalizados/green //yellow/{nomes_capitalizados}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# map(lambda x: x.capitalize(), nomes) em strings
# Metodo de string chamado dentro da lambda
# Primeira vez padronizando nomes com map
# Animado em transformar lista inteira de uma vez
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
