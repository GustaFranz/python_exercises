# EXERCICIO 95 - Gerador de relatorios de turma (contexto educacional)
#
# ENUNCIADO
# Crie um sistema baseado em funcoes para gerar relatorios de uma turma.
# alunos = {"Ana": 7.5, "Bruno": 3.2, "Carlos": 8.0, "Daniela": 5.5, "Eduardo": 9.1}
# O programa deve retornar:
## media da turma;
## lista de aprovados;
## lista de reprovados;
## melhor aluno.
#
# ORIENTACOES
## Crie funcoes separadas para cada analise.
## Use dicionarios e listas.
## Crie uma funcao principal que organiza o fluxo do programa.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()

alunos = {"Ana": 7.5, "Bruno": 3.2, "Carlos": 8.0, "Daniela": 5.5, "Eduardo": 9.1}


def obter_media(dicionario_alunos):
    total_alunos = len(dicionario_alunos)
    if total_alunos == 0:
        return 0  # O codigo entrega o 0 e finaliza a função.
    soma_notas = 0.0

    for nota in dicionario_alunos.values():
        soma_notas = soma_notas + nota

    return soma_notas / total_alunos


def obter_aprovados(dicionario_alunos):
    lista_aprovados = []

    for nome, nota in dicionario_alunos.items():
        if nota >= 7:
            lista_aprovados.append(nome)
    return lista_aprovados


def obter_alunos_recuperacao(dicionario_alunos):
    lista_alunos_recuperacao = []

    for nome, nota in dicionario_alunos.items():
        if 5 < nota < 7:
            lista_alunos_recuperacao.append(nome)
    return lista_alunos_recuperacao


def obter_reprovados(dicionario_alunos):
    lista_reprovados = []

    for nome, nota in dicionario_alunos.items():
        if nota <= 5:
            lista_reprovados.append(nome)
    return lista_reprovados


def main():
    print(f"//magenta/=============/magenta RELATÓRIO DA TURMA //magenta/=============/magenta")
    print(f'Média da turma: //magenta/{obter_media(alunos):.2f}/magenta')
    print(f'Lista de //yellow/aprovados:/yellow //green/{obter_aprovados(alunos)}/green')
    print(f'Lista de //yellow/reprovados:/yellow //green/{obter_reprovados(alunos)}/green')
    print(f'Lista de alunos em //yellow/recuperação:/yellow //green/{obter_alunos_recuperacao(alunos)}/green')


if __name__ == "__main__":
    main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Funcoes separadas filtram aprovados, recuperacao e reprovados
# Loop em .items() monta listas a partir do dict de notas
# Faixa 5 < nota < 7 separa alunos em recuperacao
# Animado em gerar relatorio completo da turma com funcoes
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
