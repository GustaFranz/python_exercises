# EXERCICIO 81 - Sistema de notas por aluno (contexto educacional)
#
# ENUNCIADO
# Considere o seguinte dicionario de alunos e suas notas finais:
# alunos = {"Ana": 7.5, "Bruno": 3.2, "Carlos": 8.0, "Daniela": 5.5, "Eduardo": 9.1, "Fernanda": 4.0}
# O programa deve:
## separar alunos aprovados (>= 6) e reprovados (< 6) em novos dicionarios;
## calcular a media geral da turma;
## identificar o aluno com maior nota.
#
# ORIENTACOES
## Percorra o dicionario com .items().
## Crie novos dicionarios por categoria.
## Utilize max() com key.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()


alunos = {"Ana": 7.5, "Bruno": 3.2, "Carlos": 8.0, "Daniela": 5.5, "Eduardo": 9.1, "Fernanda": 4.0}

dicionario_aprovados = {}
dicionario_reprovados = {}

notas = list(alunos.values())

for nome, nota in alunos.items():
    if nota >= 6:
        dicionario_aprovados[nome] = nota      
        print(f"//green/{nome} está aprovado(a) com nota/green //yellow/{nota}./yellow")
    else:
        dicionario_reprovados[nome] = nota
        print(f"//red/{nome} está reprovado(a) com nota/red //bold-red/{nota}/bold-red.")

print(f'//green/o dicionário de alunos aprovados é:/green //yellow/{dicionario_aprovados}/yellow')
print(f'//green/o dicionário de alunos reprovados é:/green //yellow/{dicionario_reprovados}/yellow')
print(f'//green/a média geral da turma é:/green //yellow/{sum(notas) / len(notas):.2f}/yellow')
print(f'//green/o aluno com maior nota é:/green //yellow/{max(alunos, key=alunos.get)}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Dois dicts derivados com if/else por nota
# max(alunos, key=alunos.get) para maior nota
# Media da turma com sum() e len() nos values
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
