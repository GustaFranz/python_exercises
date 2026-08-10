# EXERCICIO 156 - Funcao com **kwargs: registro de presenca (contexto educacional)
#
# ENUNCIADO
# Crie uma funcao chamada registrar_presenca que recebe **kwargs.
# Cada argumento nomeado representa um aluno:
## True = presente
## False = ausente
# A funcao deve exibir:
## lista de presentes;
## lista de ausentes;
## total de presentes e total de ausentes.
# Teste com:
## registrar_presenca(Ana=True, Bruno=False, Carla=True, Daniel=False, Eduardo=True)
#
# ORIENTACOES
## Percorra kwargs.items() e separe em duas listas.
## Use condicionais para classificar cada aluno.
## Exiba o resumo final com totais.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

def registrar_presenca(aula, **aluno):
    print(f'\n:::::::::::::::::::::: DATA DA AULA: {aula} ::::::::::::::::::::::')
    for chave, valor in aluno.items():
        status = "Presente" if valor else "Ausente"
        print(f'{chave}: {status}')


# Estruturas para guardar o histórico e contadores totais
historico_aulas = []
total_presencas = 0
total_faltas = 0

while True:
    aula = input("\nDigite a data da aula (ex: 07/08): ").strip()
    alunos_dict = {}

    # Coleta os alunos e seus status para esta aula
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        presenca_input = input(f"{nome} estava presente? (s/n): ").strip().lower()
        
        presente = presenca_input == 's'
        alunos_dict[nome] = presente

        if presente:
            total_presencas += 1
        else:
            total_faltas += 1

        continuar_aluno = input("Tem mais algum aluno para cadastrar nesta aula? (s/n): ").strip().lower()
        if continuar_aluno != 's':
            break

    # Guarda a aula e o dicionário de alunos para o relatório final
    historico_aulas.append((aula, alunos_dict))

    continuar_aula = input("\nDeseja cadastrar outra aula? (s/n): ").strip().lower()
    if continuar_aula != 's':
        break

# --- RELATÓRIO FINAL ---
print("\n" + "=" * 55)
print("             RELATÓRIO FINAL DE PRESENÇAS             ")
print("=" * 55)

# Chama a função obrigatória usando desempacotamento de dicionário (**alunos)
for data_aula, alunos in historico_aulas:
    registrar_presenca(data_aula, **alunos)

print("\n" + "-" * 55)
print(f"TOTAL DE PRESENÇAS: {total_presencas}")
print(f"TOTAL DE FALTAS:    {total_faltas}")
print("-" * 55)


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# **kwargs agrupa argumentos nomeados; cada chave vira um aluno, o valor True/False indica presenca
# Parametro fixo (aula) vem antes de **kwargs (aluno)
# for chave, valor in aluno.items() classifica cada registro com condicional
# Expressao ternaria: "Presente" if valor else "Ausente"
# **alunos na chamada desempacota o dicionario para **kwargs
# Lista historico_aulas guarda tuplas (data, dict) para o relatorio final
# Contadores total_presencas e total_faltas acumulam dados de varias aulas
# while True com break controla cadastro de alunos e de aulas
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
