# EXERCICIO 153 - Funcao com *args: relatorio do aluno (contexto educacional)
#
# ENUNCIADO
# Crie uma funcao chamada relatorio_aluno que recebe:
## nome (parametro obrigatorio)
## *notas (quantidade variavel de notas)
# A funcao deve exibir um relatorio com:
## nome do aluno;
## quantidade de notas recebidas;
## media das notas;
## maior nota.
# Teste com:
## relatorio_aluno("Ana", 7.5, 8.0, 6.5)
## relatorio_aluno("Bruno", 4.0, 5.5, 3.0, 6.0, 7.0)
#
# ORIENTACOES
## Parametros fixos vem antes de *args: def relatorio_aluno(nome, *notas).
## Use len(notas), sum(notas) e max(notas).
## Formate a saida em linhas separadas para facilitar a leitura.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

def relatorio_alunos(aluno: str, *args: float):
    notas = args
    nome_aluno = aluno.title()
    if not notas:
        return nome_aluno, 0.0, 0.0
    quant_notas = len(notas)
    soma_notas = sum(notas)
    media_notas = soma_notas / quant_notas
    maior_nota = max(notas)
    relatorio = nome_aluno, media_notas, maior_nota
    return relatorio



while True:
    print("\n============================== CADASTRO DE NOTAS ==============================\n")
    entrada_aluno = input("Nome do aluno: ")
    nome_aluno = entrada_aluno.strip().title()

    contador_notas = 0
    entrada_limite = int(input("Quantas notas você quer cadastrar? "))
    if entrada_limite <= 0:
        print("Digite um limite maior que zero")

    notas_aluno = []
    for i in range(1, entrada_limite + 1):
        entrada_nota = float(input(f"Digite a {contador_notas} nota: "))
        notas_aluno.append(entrada_nota)


    relatorio = relatorio_alunos(nome_aluno, *notas_aluno)
    print(f'\n=================================== RELATÓRIO ALUNO ===================================\n')
    print(f'Nome do aluno: {relatorio[0]}\n'
          f'Média: {relatorio[1]:.1f}\n'
          f'Maior nota: {relatorio[2]}\n')
    break

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Parametro fixo (nome) vem antes de *args (notas)
# len, sum e max em *args montam quantidade, media e maior nota
# Ao chamar, *lista_notas desempacota a lista para *args
# Protegi o caso sem notas para nao dividir por zero
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
