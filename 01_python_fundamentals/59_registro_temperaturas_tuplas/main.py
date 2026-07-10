# EXERCICIO 59 - Registro de temperaturas com tuplas (contexto cientifico)
#
# ENUNCIADO
# Considere as temperaturas registradas por dia em tuplas (dia, temperatura):
# registros = [("segunda", 28), ("terca", 31), ("quarta", 26), ("quinta", 33), ("sexta", 29)]
# O programa deve exibir o dia mais quente e o dia mais frio.
#
# ORIENTACOES
## Percorra a lista de tuplas com for.
## Compare as temperaturas para guardar a maior e a menor.
## Guarde tambem o dia correspondente a cada uma.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

# Considere as temperaturas registradas por dia em tuplas (dia, temperatura):
registros = [("segunda", 28), ("terca", 31), ("quarta", 26), ("quinta", 33), ("sexta", 29)]
# O programa deve exibir o dia mais quente e o dia mais frio.

for i, (dia, temperatura) in enumerate(registros):
    if i == 0:
        dia_mais_quente = dia
        temperatura_mais_quente = temperatura
        dia_mais_frio = dia
        temperatura_mais_frio = temperatura
    else:
        if temperatura > temperatura_mais_quente:
            dia_mais_quente = dia
            temperatura_mais_quente = temperatura
        if temperatura < temperatura_mais_frio:
            dia_mais_frio = dia
            temperatura_mais_frio = temperatura

print(f"Dia mais quente: {dia_mais_quente} com temperatura de {temperatura_mais_quente}°C")
print(f"Dia mais frio: {dia_mais_frio} com temperatura de {temperatura_mais_frio}°C")



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Busca de valor maximo e minimo percorrendo lista de tuplas
# Inicializacao de variaveis de controle no primeiro elemento
# Comparacao sequencial para identificar extremos em registros
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
