# EXERCICIO 43 - Cadastro de alunos com parada manual
#
# ENUNCIADO
# Crie um sistema que cadastre nomes de alunos continuamente até que o usuário decida parar.
# O programa deve:
## solicitar nomes;
## armazenar em uma lista;
## parar quando o usuário digitar "fim".
#
# ORIENTACOES
## Use while True
## Use lista para armazenar alunos
## Use condição de parada com string "fim"
## Não inclua "fim" na lista
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

import easyansi
easyansi.activate()

print("//magenta/=/magenta" * 95)
print("CADASTRO DE ALUNOS")
print("//magenta/=/magenta" * 95)

lista_nomes = []

while True:
    nome = input("Nome completo do aluno ou digite 'fim' para encerrar: ").strip().title()

    if nome.lower() == "fim":
        break

    if nome == "":
        print("//red/Nome inválido! O campo não pode ficar vazio./red")
        continue

    if nome in lista_nomes:
        print("//yellow/Aluno já cadastrado! Digite outro nome./yellow")
        continue

    lista_nomes.append(nome)

    while True:
        repetir = input("//green/Deseja cadastrar outro aluno? [S]/[N] /green").strip().upper()

        if repetir not in ["S", "N", "SIM", "NÃO", "NAO"]:
            print("//red/Resposta inválida! Responda com SIM (S) ou NÃO (N)./red")
        else:
            break

    if repetir in ["N", "NÃO", "NAO"]:
        break

print("~" * 95)
print("//bold-green/Alunos cadastrados com sucesso!/bold-green")
print("~" * 95)

quant_alunos = len(lista_nomes)

print(f"//blue/{quant_alunos}/blue alunos cadastrados.")
print("~" * 95)
for aluno in lista_nomes:
    print(f"- {aluno}")




# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================
#
# Aplicação de laço while True para construção de sistemas com repetição contínua e controle manual de parada
# Consolidação do uso de estruturas condicionais (if/else) para validação de entradas do usuário
# Aplicação prática de listas (list) para armazenamento dinâmico de dados
# Uso da função len() para obtenção de métricas simples (quantidade de registros)
# Reforço na utilização de loops aninhados para validação robusta de entradas
# Aplicação do comando break para controle de encerramento do fluxo
# Aplicação do comando continue para ignorar entradas inválidas e manter a integridade dos dados
# Tratamento de dados com métodos de string (strip(), upper(), title())
# Prevenção de inconsistências com validação de dados (entrada vazia e duplicidade)
#
# UTILIZAÇÃO DA BIBLIOTECA PRÓPRIA EASYANSI
# link para o repositorio da easyansi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
