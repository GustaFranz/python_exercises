# EXERCICIO 73 - Otimizacao de lista de tarefas (contexto de produtividade)
#
# ENUNCIADO
# Considere a lista de tarefas abaixo:
# tarefas = ["estudar", "exercicios", "ler", "estudar", "revisar", "ler", "projeto", "exercicios"]
# O programa deve:
## remover duplicatas;
## gerar uma nova lista organizada em ordem alfabetica.
#
# ORIENTACOES
## Utilize set() para remover duplicatas.
## Converta novamente para lista.
## Aplique sorted() para ordenacao final.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

tarefas = ["estudar", "exercicios", "ler", "estudar", "revisar", "ler", "projeto", "exercicios"]
## remover duplicatas
list_tarefas_sem_duplicatas = list(set(tarefas))
## gerar uma nova lista organizada em ordem alfabetica.
list_tarefas_ordenadas = sorted(list_tarefas_sem_duplicatas)

print(f'//green/Tarefas sem duplicatas:/green //yellow/{list_tarefas_sem_duplicatas}/yellow')
print(f'//green/Tarefas ordenadas:/green //yellow/{list_tarefas_ordenadas}/yellow')
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com set() para remover duplicatas
# sorted() para ordenar a lista sem duplicar tarefas
# Animado em ver tarefas unicas e ordenadas com poucas linhas
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
