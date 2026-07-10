# EXERCICIO 50 - Ranking imutável de alunos (contexto educacional)
#
# ENUNCIADO
# Um professor deseja registrar um ranking final de desempenho dos alunos após duas provas (1º e 2º avaliação de um bimestre). 
#Esse ranking não pode ser alterado. O programa deve receber nome e nota dos alunos, 
#armazenar como tuplas (nome, nota) e exibir o ranking ordenado por nota do maior para o menor.

# ORIENTACOES
## use lista de tuplas
## utilize sorted com key para ordenação
## não altere as tuplas após criação
## exiba o ranking numerado
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # ESOLUÇÃO DO EXERCÍCIO
# =============================================================================

import easyansi
easyansi.activate()

def nome_aluno():
    while True:
        entrada_nome = input("Nome do aluno ou E para encerrar: ").strip().title()

        if entrada_nome == "":
            print("Você precisa digitar o nome de um aluno ou E para encerrar.")
            continue

        if entrada_nome == "E":
            return None

        return entrada_nome


def notas_aluno(tipo):
    while True:
        entrada_nota = input(f"Digite a nota {tipo} do aluno ou '-' para sem nota: ").strip().upper().replace(",", ".")

        if entrada_nota == "-":
            valor = None

        else:
            try:
                valor = float(entrada_nota)
            except ValueError:
                print("Erro! Digite uma resposta válida ou '-'")
                continue

            if valor < 0 or valor > 10:
                print("Erro! A nota deve estar entre 0 e 10.")
                continue

        while True:
            if valor is None:
                resposta = input("Aluno sem nota. Confirmar? [S]/[N] ").strip().upper()
            else:
                resposta = input(f"A nota digitada foi {valor}. Confirmar? [S]/[N] ").strip().upper()

            if resposta in ["S", "SIM"]:
                return valor

            elif resposta in ["N", "NAO", "NÃO"]:
                print("Digite novamente a nota.")
                break

            else:
                print("Resposta inválida.")

def calcular_media(n1, n2):
    notas = []

    if n1 is not None:
        notas.append(n1)

    if n2 is not None:
        notas.append(n2)

    if len(notas) == 0:
        return None

    return sum(notas) / len(notas)

def chave_ordenacao(aluno):
    media = aluno[3]

    if media is None:
        return 999

    return -media

# ========================= PROGRAMA =========================

lista_alunos = []

print("=" * 105)
print("CADASTRO DE NOTAS")
print("=" * 105)

while True:
    nome = nome_aluno()

    if nome is None:
        break

    n1 = notas_aluno("nota 1")
    n2 = notas_aluno("nota 2")

    # 👉 cada aluno é uma TUPLA
    aluno = (nome, n1, n2)

    lista_alunos.append(aluno)

    print("-" * 105)


# 👉 transformar em TUPLA DE TUPLAS (opcional, mas didático)
dados_alunos = tuple(lista_alunos)


# montar ranking (ainda com tuplas)
ranking = []

for nome, n1, n2 in dados_alunos:
    media = calcular_media(n1, n2)

    aluno_completo = (nome, n1, n2, media)  # nova tupla
    ranking.append(aluno_completo)


ranking.sort(key=chave_ordenacao)


print("-" * 105)
print("RELATÓRIO DE NOTAS (TUPLAS)")
print("-" * 105)

for posicao, (nome, n1, n2, media) in enumerate(ranking, start=1):

    if n1 is None:
        n1_fmt = "S/N"
    else:
        n1_fmt = n1

    if n2 is None:
        n2_fmt = "S/N"
    else:
        n2_fmt = n2

    if media is None:
        media_fmt = "S/N"
    else:
        media_fmt = f"{media:.1f}"

    print(f"//bold-yellow/{posicao}º lugar/bold-yellow | "
          f"//green/{nome:.<55}/green | "
          f"//bold-blue/Nota 1:/bold-blue //yellow/{n1_fmt}/yellow | "
          f"//bold-blue/Nota 2:/bold-blue //yellow/{n2_fmt}/yellow | "
          f"//bold-magenta/Média:/bold-magenta //yellow/{media_fmt}/yellow")



# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================
# #
# Oportunidade de consolidar o uso de funções em um contexto mais complexo
# Trabalho com múltiplas variáveis e controle de métricas no sistema
# Aplicação prática de tuplas conforme proposta do exercício
# Desenvolvimento de lógica mais estruturada e organizada
# Evolução na leitura e manipulação de dados estruturados
# Exercício importante para ganho de autonomia na construção de soluções
# Utilização da biblioteca EasyAnsi para melhoria visual do sistema

# Link do repositório da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
