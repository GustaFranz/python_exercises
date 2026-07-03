# EXERCICIO 66 - Verificar item na lista (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista abaixo:
# frutas = ["maca", "banana", "uva", "laranja", "manga"]
# Peca ao usuario que digite o nome de uma fruta.
# Informe se a fruta digitada esta ou nao na lista.
#
# ORIENTACOES
## Use o operador in para verificar a existencia do item.
## Exiba uma mensagem diferente para cada caso (esta / nao esta).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

frutas = ["maca", "banana", "uva", "laranja", "manga"]

while True:
    pesquisar_fruta = input("Digite o nome de uma fruta: ").strip()

    if pesquisar_fruta in frutas:
        print(f'A fruta {pesquisar_fruta} está na lista {frutas}')

    else:
        acrescentar = input(f'A fruta {pesquisar_fruta} não está na lista {frutas}, deseja acrescentar? ').upper()
        if acrescentar in ["SIM", "S"]:
            frutas.append(pesquisar_fruta)
            continue
        else:
            print(f'A lista frutas é {frutas}')
            break



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Operador in para verificar existencia de item na lista
# Loop com append para incluir novos itens quando solicitado
# Controle de fluxo com continue e break no cadastro
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
