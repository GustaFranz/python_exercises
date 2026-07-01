# EXERCICIO 56A - Percorrer tupla (contexto introdutorio)
#
# ENUNCIADO
# Dada a tupla abaixo:
# dias = ("segunda", "terca", "quarta", "quinta", "sexta")
# Exiba cada dia em uma linha e, no final, mostre o total de dias.
#
# ORIENTACOES
## Use for para percorrer a tupla.
## Use len() para contar quantos elementos existem.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

dias = ("segunda", "terca", "quarta", "quinta", "sexta")

print("-" * 10 + "DIAS DA SEMANA" + "-" * 10)
for i, dia in enumerate(dias):
    print(f"{i + 1} | //bold-green/{dia}/bold-green")

quant_dias = len(dias)
print("-" * 30)
print(f"De segunda a sexta ha //bold-green/{quant_dias}/bold-green dias")
print("-" * 30)

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Percorrer tuplas com for e enumerate para exibir indice e valor
# Contagem de elementos com len() em estruturas imutaveis
# Reforco de indices iniciando em 1 na exibicao para o usuario
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
