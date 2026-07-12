# EXERCICIO 113 - Cadastro de alunos modular (contexto educacional)
#
# ENUNCIADO
# Crie um sistema de cadastro de alunos utilizando modulos separados.
# O sistema deve permitir:
## cadastrar aluno;
## listar alunos;
## buscar aluno.
#
# ORIENTACOES
## Modulo cadastro.py.
## Modulo consulta.py.
## Modulo lista.py.
## main.py como controlador principal.
## Use listas para armazenar dados.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import cadastro
import consulta
import lista


def exibir_menu():
    print("\n=== CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("0 - Sair")


def main():
    alunos = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip().capitalize()
            idade = input("Idade: ").strip()
            matricula = input("Matrícula: ").strip()
            cadastro.cadastrar_aluno(alunos, nome, idade, matricula)

        elif opcao == "2":
            lista.listar_alunos(alunos)

        elif opcao == "3":
            matricula = input("Digite a matrícula do aluno: ").strip()
            consulta.buscar_aluno(alunos, matricula)

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Modulos cadastro, consulta e lista em CRUD simples
# main com while True e menu de opcoes
# if __name__ == '__main__' protege a execucao
# Animado em juntar modulos com entrada do usuario
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
