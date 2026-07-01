# EXERCICIO 58 - Boletim de medias com tuplas (contexto educacional)
#
# ENUNCIADO
# Considere as notas dos alunos em tuplas no formato (nome, nota1, nota2):
# alunos = [("Ana", 8.0, 6.0), ("Bruno", 5.0, 7.0), ("Carla", 9.0, 10.0)]
# O programa deve exibir o nome de cada aluno e a media das duas notas.
#
# ORIENTACOES
## Percorra a lista de tuplas com for.
## Desempacote cada tupla em nome, nota1 e nota2.
## Calcule a media somando as notas e dividindo por 2.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

alunos = [("Ana", 8.0, 6.0), ("Bruno", 5.0, 7.0), ("Carla", 9.0, 10.0)]

for i, (aluno, nota1, nota2) in enumerate(alunos):
    media = (nota1 + nota2) / 2
    if media >= 7:
        print(f"{i + 1} | Aluno: {aluno:.<35} | //green/Média: {media:.2f}/green")
    else:    
        print(f"{i + 1} | Aluno: {aluno:.<35} | //red/Média: {media:.2f}/red")




# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Calculo de media a partir de tuplas com nome e notas
# Desempacotamento de tuplas em variaveis dentro do for
# Classificacao visual com condicional e cores no terminal
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
