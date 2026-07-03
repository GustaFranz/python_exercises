# EXERCICIO 72 - Analisador de desempenho de posts (contexto digital)
#
# ENUNCIADO
# Considere a lista de curtidas de posts abaixo:
# curtidas = [120, 45, 300, 90, 15, 600, 250, 80, 10, 400]
# O programa deve classificar os posts em:
## baixo desempenho (0 a 100);
## medio desempenho (101 a 300);
## alto desempenho (acima de 300).
# Alem disso, deve contar quantos posts existem em cada categoria.
#
# ORIENTACOES
## Percorra a lista com for.
## Use condicoes numericas para separacao.
## Mantenha contadores para cada categoria.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

curtidas = [120, 45, 300, 90, 15, 600, 250, 80, 10, 400]
baixo = []
medio = []
alto = []

for c in curtidas:
    if c >= 0 and c <= 100:
        baixo.append(c)
    elif c >= 101 and c <= 300:
        medio.append(c)
    else:
        alto.append(c)

print(f'//green/{len(baixo)}/green posts na categoria de //yellow/baixo desempenho/yellow')
print(f'//green/{len(medio)}/green posts na categoria de //yellow/medio desempenho/yellow')
print(f'//green/{len(alto)}/green posts na categoria de //yellow/alto desempenho/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Classificacao de posts por faixas numericas de curtidas
# Separacao em listas com if/elif/else
# Contagem por categoria com len() nas listas geradas
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
