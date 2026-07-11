# EXERCICIO 103 - Ordenar ranking com lambda (contexto educacional)
#
# ENUNCIADO
# Considere o ranking em tuplas (nome, nota):
# ranking = [("Ana", 7.5), ("Bruno", 9.0), ("Carla", 6.0), ("Diego", 8.2)]
# Ordene da maior para a menor nota e exiba o ranking ordenado.
#
# ORIENTACOES
## Use sorted(ranking, key=lambda aluno: aluno[1], reverse=True).
## O indice 1 da tupla e a nota.
## Exiba a lista ordenada com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

ranking = [("Ana", 7.5), ("Bruno", 9.0), ("Carla", 6.0), ("Diego", 8.2)]
ranking_ordenado = sorted(ranking, key= lambda aluno: aluno[1], reverse = True)

print(f'//green/Ranking ordenado da maior para a menor nota/green //yellow/{ranking_ordenado}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# key=lambda aluno: aluno[1] ordena pela nota da tupla
# reverse=True coloca maior nota no topo
# Animado em montar ranking sem loop manual
# sorted nao altera a lista ranking original
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
