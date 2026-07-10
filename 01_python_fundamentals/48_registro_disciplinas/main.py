# EXERCICIO 48 - Sistema de registro de disciplinas (educacional)
#
# ENUNCIADO
# Uma escola deseja armazenar as disciplinas ofertadas em um semestre. Cada disciplina possui nome e carga horária, 
# e esses dados não devem ser alterados após o registro. 
# O programa deve permitir cadastrar várias disciplinas, armazenar nome e carga horária em uma tupla 
# e exibir todas as disciplinas cadastradas ao final.

# ORIENTACOES
## use tuplas para armazenar cada disciplina no formato (nome, carga_horaria)
## utilize uma lista para armazenar múltiplas tuplas
## não altere os dados após inserção
## percorra os dados com for
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

import easyansi
easyansi.activate()

print("=" * 95)
print("//bold-cyan/SISTEMA DE REGISTRO DE DISCIPLINAS/bold-cyan")
print("=" * 95)

disciplinas = []

while True:
    nome = input("\n//magenta/Nome da disciplina [FIM ou F para encerrar]:/magenta ").strip()

    if nome.upper() in ["FIM", "F"]:
        break

    while True:
        try:
            carga_horaria = int(input("//yellow/Carga horária:/yellow "))

            if carga_horaria <= 0:
                print("//red/A carga horária deve ser maior que zero./red")
            else:
                break

        except ValueError:
            print("//red/Digite um número inteiro válido./red")

    disciplinas.append((nome.title(), carga_horaria))
    print("//green/Disciplina cadastrada com sucesso!/green")

disciplinas = tuple(disciplinas)

print("\n" + "=" * 95)
print("//bold-cyan/DISCIPLINAS CADASTRADAS/bold-cyan")
print("=" * 95)

if len(disciplinas) == 0:
    print("//red/Nenhuma disciplina foi cadastrada./red")
else:
    total_carga = 0

    for posicao, (nome, carga) in enumerate(disciplinas, start=1):
        print(f"//bold-white/{posicao}./bold-white //cyan/{nome}/cyan - //yellow/{carga} horas/yellow")
        total_carga += carga

    print("-" * 95)
    print(f"//bold-green/Total de disciplinas:/bold-green {len(disciplinas)}")
    print(f"//bold-green/Carga horária total:/bold-green {total_carga} horas")

print("=" * 95)



# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================


# Estruturação de dados com tuplas imutáveis para representar registros (nome e carga horária)
# Uso de lista como estrutura intermediária antes da conversão para tupla
# Teve a oportunidade de relembrar e aplicar laço while True com condição de parada
# Teve a oportunidade de relembrar e aplicar tratamento de strings (strip, upper, title)
# Aplicação de validação de dados com try/except para evitar erros de conversão
# Uso de desempacotamento de tuplas em estruturas de repetição (for nome, carga in ...)
# Aplicação de biblioteca externa easyansi para estilização de saída no terminal

# Link do repositório da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
