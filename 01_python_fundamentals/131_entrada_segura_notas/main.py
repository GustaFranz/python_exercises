# EXERCICIO 131 - Entrada segura de notas (contexto educacional)
#
# ENUNCIADO
# Crie um sistema que receba notas de alunos e calcule a media da turma.
# O programa deve estar protegido contra entradas invalidas.
# O sistema deve:
## solicitar 5 notas do usuario;
## calcular a media final;
## impedir que o programa quebre com entradas invalidas (texto ou valores fora do padrao).
#
# ORIENTACOES
## Use try/except.
## Trate ValueError.
## Valide se a nota esta entre 0 e 10.
## Peca nova entrada em caso de erro.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

def calcular_media(notas):
    return sum(notas) / len(notas)


alunos = []
while True:
    nome = input("Digite o nome do aluno: ")
    if nome.strip() == "":
        print("Nome invalido. Por favor, digite um nome valido.")
        continue

    notas = []
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1} do aluno {nome}: "))
                if nota < 0 or nota > 10:
                    print(f"//red/Nota invalida. Por favor, digite uma nota entre 0 e 10.")
                else:
                    break
            except ValueError:
                print(f"//red/Entrada invalida. Por favor, digite um numero valido.")
        notas.append(nota)

    media = calcular_media(notas)
    alunos.append({"nome": nome, "media": media})
    print(f"A media do aluno //green/{nome} é: //green/{media:.2f}")

    while True:
        continuar = input("Deseja cadastrar outro aluno? [S/N]: ").strip().lower()
        if continuar in ("s", "n"):
            break
        print("Opcao invalida. Digite S para continuar ou N para encerrar.")

    if continuar == "n":
        break

print("\n//magenta/----------------------------- //yellow/RELATORIO FINAL //magenta/-----------------------------")
for numero, aluno in enumerate(alunos, start=1):
    print(f"{numero}. {aluno['nome']}: media {aluno['media']:.2f}")
print(f'//yellow/---------------------------------------------------------------------------')
print(f"Total de alunos cadastrados: {len(alunos)}")



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
