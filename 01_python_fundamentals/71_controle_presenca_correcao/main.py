# EXERCICIO 71 - Controle de presenca com correcao (contexto educacional)
#
# ENUNCIADO
# Considere a lista abaixo que representa registros de presenca, porem contem dados invalidos:
# presencas = ["P", "F", "P", "X", "F", "P", "Z", "F", "P", "P", "Y", "F"]
# O programa deve:
## criar uma nova lista apenas com valores validos ('P' e 'F');
## contar total de presencas e faltas;
## calcular percentual de frequencia.
#
# ORIENTACOES
## Filtre os dados validos com for.
## Ignore valores invalidos.
## Use contadores.
## Calcule percentual ao final.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

presencas = ["P", "F", "P", "X", "F", "P", "Z", "F", "P", "P", "Y", "F"]

presencas_validas = []
for presenca in presencas:
    if presenca in ['P', 'F']:
        presencas_validas.append(presenca)

print(f'//green/Presencas validas: {presencas_validas}/green')

presencas_count = presencas_validas.count('P')
faltas_count = presencas_validas.count("F")
porcentagem_frequencia = (presencas_count / len(presencas_validas)) * 100

print(f'//green/Total de presencas:/green //yellow/{presencas_count}/yellow')
print(f'//green/Total de faltas:/green //yellow/{faltas_count}/yellow')
print(f'//green/Percentual de frequencia:/green //yellow/{porcentagem_frequencia:.2f}%/yellow')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Limpeza de lista: manter so P e F com in e append
# Metodo count() para total de presencas e faltas
# Percentual de frequencia com len() no denominador
# Primeira correcao de dados invalidos em lista de chamada
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
