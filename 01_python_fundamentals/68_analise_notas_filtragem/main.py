# EXERCICIO 68 - Analise de notas com filtragem (contexto educacional)
#
# ENUNCIADO
# Considere a lista de notas abaixo de uma turma:
# notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]
# O programa deve gerar:
## lista de aprovados (>= 6);
## lista de recuperacao (>= 4 e < 6);
## lista de reprovados (< 4);
## media geral da turma.
#
# ORIENTACOES
## Percorra a lista com for.
## Crie listas separadas com base em condicoes.
## Utilize sum() e len() para a media.
## Mantenha a lista original intacta.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


import easyansi
easyansi.activate()

notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1, 2.8, 5.5, 6.0, 10.0]

media = sum(notas) / len(notas)

list_aprovados = []
list_recuperacao = []
list_reprovados = []

for c in notas:
    if c >= 6:
        list_aprovados.append(c)

    elif c >= 4:
        list_recuperacao.append(c)
    
    else:
        list_reprovados.append(c)

print("//magenta/" + "-" * 95 + "//magenta/")
print("SITUAÇÃO DOS ALUNOS")
print("//magenta/" + "-" * 95 + "//magenta/")

print(f"//green/{'Aprovados':.<45} {list_aprovados} ({len(list_aprovados)}) alunos./green")
print(f"//green/{'Recuperação':.<45} {list_recuperacao} ({len(list_recuperacao)}) alunos./green")
print(f"//red/{'Reprovados':.<45} {list_reprovados} ({len(list_reprovados)}) alunos./red")
      
print(f"\nA média da turma é {media}")

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Classificacao de notas em listas com if/elif/else
# Uso de append para separar aprovados, recuperacao e reprovados
# Calculo de media com sum() e len()
# Formatacao visual com f-strings e alinhamento de texto
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
