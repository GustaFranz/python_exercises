# EXERCICIO 84 - Cadastro de alunos com multiplas informacoes (contexto educacional)
#
# ENUNCIADO
# Considere o seguinte dicionario de alunos:
# alunos = {"Ana": {"nota": 7.5, "faltas": 2}, "Bruno": {"nota": 3.2, "faltas": 5}, "Carlos": {"nota": 8.0, "faltas": 1}, "Daniela": {"nota": 5.5, "faltas": 3}}
# O programa deve:
## separar alunos aprovados (nota >= 6 e faltas <= 3);
## criar um novo dicionario apenas com aprovados;
## identificar o aluno mais frequente (menos faltas).
#
# ORIENTACOES
## Percorra dicionarios aninhados.
## Utilize condicoes compostas.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()

aprovados = {}
alunos = {
    "Ana": {"nota": 7.5, "faltas": 2},
    "Bruno": {"nota": 3.2, "faltas": 5},
    "Carlos": {"nota": 8.0, "faltas": 1},
    "Daniela": {"nota": 5.5, "faltas": 3},
}


def pegar_faltas(nome):
    return alunos[nome]["faltas"]


for aluno, dados in alunos.items():
    if dados["nota"] >= 6 and dados["faltas"] <= 3:
        aprovados[aluno] = dados

aluno_frequente = min(alunos, key=pegar_faltas)

print(f'//green/O dicionário de alunos aprovados é:/green //yellow/{aprovados}/yellow')
print(f'//green/O aluno mais frequente (menos faltas) é:/green //yellow/{aluno_frequente}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro dict aninhado: aluno -> {nota, faltas}
# Regra dupla: nota e limite de faltas no if
# min(alunos, key=funcao) para aluno mais frequente
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
