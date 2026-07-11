# EXERCICIO 106 - Dobrar numeros com map e lambda (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista de numeros:
# numeros = [1, 2, 3, 4, 5, 6]
# Gere uma nova lista com o dobro de cada valor.
# Exiba a lista original e a lista transformada.
#
# ORIENTACOES
## Use map(lambda x: x * 2, numeros).
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

numeros = [1, 2, 3, 4, 5, 6]
lista_dobro = list(map(lambda x: x * 2, numeros))

print("//magenta/----------------------/magenta LISTAS //magenta/----------------------/magenta")
print(f'//green/Lista original/green //yellow/{numeros}/yellow')
print(f'//green/Lista com o dobro de cada valor/green //yellow/{lista_dobro}/yellow')
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# map aplica transformacao em cada item da lista
# Lambda x * 2 dobra sem for manual
# Lista original preservada na exibicao
# Animado em ver map substituir loop simples
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
