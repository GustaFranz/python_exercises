# EXERCICIO 52 - Registro de sessoes de estudo (contexto educacional)
#
# ENUNCIADO
# Um estudante deseja registrar suas sessoes de estudo ao longo da semana.
# Cada sessao possui disciplina e duracao em minutos.
# O sistema deve registrar varias sessoes como tuplas (disciplina, minutos) e 
# calcular o total de tempo estudado por disciplina.
#
# ORIENTACOES
## Use tuplas para cada sessao.
## Utilize dicionario para acumular tempo por disciplina.
## Percorra a lista com for.
## Nao altere as tuplas apos criacao.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

# Criamos uma lista vazia para armazenar as tuplas das sessões
historico_sessoes = []

# 1. FUNÇÃO PARA CRIAR A TUPLA DA SESSÃO
def registrar_sessao():
    disciplina = input("Qual disciplina você quer registrar? ")
    tempo = float(input(f"Qual foi o tempo de estudo (em minutos) para {disciplina}? "))
    return (disciplina, tempo)

def calcular_tempo_por_disciplina(lista_de_sessoes):
    dicionario_acumulado = {}
    for sessao in lista_de_sessoes:
        disciplina = sessao[0]
        tempo = sessao[1]
        
        # Se a disciplina já estiver no dicionário, soma o tempo. Se não, começa com o tempo dela.
        if disciplina in dicionario_acumulado:
            dicionario_acumulado[disciplina] += tempo
        else:
            dicionario_acumulado[disciplina] = tempo
            
    return dicionario_acumulado


historico_sessoes = []

while True:
    print("\n--- Registro de Nova Sessão ---")
    
    nova_sessao = registrar_sessao()
    historico_sessoes.append(nova_sessao)
    resposta = input("Deseja registrar outra sessão? (S/N): ").strip().upper()
    if resposta == "N" or resposta == "NAO":
        print("\nRegistro finalizado!")
        break

resultado_final = calcular_tempo_por_disciplina(historico_sessoes)

print("\n=== TOTAL DE TEMPO POR DISCIPLINA ===")
for disciplina, tempo in resultado_final.items():
    print(f'//green/"{disciplina}"/green: //yellow/{tempo} min/yellow')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Lista de tuplas (disciplina, minutos) para cada sessao
# Primeira vez acumulando tempo no dict com in e +=
# Funcao registrar_sessao() devolve tupla imutavel
# while True com break encerra o registro interativo
# Animado em juntar tuplas, lista e dicionario no mesmo fluxo
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
