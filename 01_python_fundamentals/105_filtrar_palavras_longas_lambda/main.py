# EXERCICIO 105 - Filtrar palavras longas com lambda (contexto de linguagem)
#
# ENUNCIADO
# Dada a lista de palavras:
# palavras = ["Python", "ia", "dados", "rede", "sol", "educacao"]
# Gere uma nova lista apenas com palavras de 5 ou mais letras.
# Exiba a lista filtrada.
#
# ORIENTACOES
## Use filter(lambda p: len(p) >= 5, palavras).
## Converta o resultado para list().
## Exiba a lista com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

palavras = ["Python", "ia", "dados", "rede", "sol", "educacao"]
maiores_cinco = list(filter(lambda x: len(x) >= 5, palavras))

print(f'//green/Palavras de 5 ou mais letras/green //yellow/{maiores_cinco}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# filter com len(x) >= 5 dentro da lambda
# Criterio de tamanho aplicado em palavras
# Nova lista sem alterar palavras original
# Animado em filtrar texto com a mesma ideia do 104
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
