# EXERCICIO 78 - Verificar chave no dicionario (contexto educacional)
#
# ENUNCIADO
# Dado o dicionario abaixo:
# notas = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
# Peca ao usuario que digite o nome de um aluno.
# Se o aluno existir, exiba a nota.
# Se nao existir, informe que nao foi encontrado.
#
# ORIENTACOES
# Use o operador in para verificar se a chave existe.
# Alternativamente, use get() com valor padrao: dicionario.get("chave", None).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
notas = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}

while True:
    aluno = input("Digite o nome do aluno ou 'sair' para encerrar: ")
    aluno = aluno.strip().capitalize()

    if aluno == "":
        print("Nome inválido.")
        continue

    elif aluno == "Sair":
        print("Encerrando o programa.")
        break

    else:
        if aluno in notas:
            print(f"A nota de {aluno} é: {notas[aluno]}")
        else:
            print(f"Aluno {aluno} não encontrado.")

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Operador in para testar chave no dict
# while True com break, continue e input do usuario
# capitalize() para padronizar nome digitado
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
