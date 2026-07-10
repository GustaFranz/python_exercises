# EXERCICIO 46 - Controle de acesso com bloqueio (com break)
#
# ENUNCIADO
# Crie um sistema de acesso com limite de tentativas.
# O usuário tem até 3 tentativas para acertar a senha.
# O programa deve:
## encerrar imediatamente ao acertar a senha (break);
## bloquear acesso após 3 tentativas erradas.
# 
# 
# ORIENTACOES
## Use while
## Use contador de tentativas
## Use break quando acertar
## Controle limite com condição
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================


import easyansi
easyansi.activate()

senha_login = "joao3:16"
tentativas = 0
limite_tentativas = 3

print("=" * 60)
print("//bold-cyan/SISTEMA DE ACESSO/bold-cyan")
print("=" * 60)

while True:
    senha = input("Digite a sua senha: ")
    tentativas += 1

    if senha == senha_login:
        print("//bold-green/Login efetuado com sucesso!/bold-green")
        break

    else:
        print("//bold-yellow/Senha incorreta!/bold-yellow")

        if tentativas == limite_tentativas:
            print("//bold-red/Acesso bloqueado. Limite de tentativas atingido!/bold-red")
            break
        else:
            tentativas_restantes = limite_tentativas - tentativas
            print(f"//yellow/Tentativas restantes: {tentativas_restantes}/yellow")


# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================
# 
# Durante o desenvolvimento deste exercício, tive a oportunidade de:

# Durante o desenvolvimento deste exercício, tive a oportunidade de:
# 
# Relembrar a utilização do while True para manter o sistema em execução contínua.
# Consolidar o uso do comando break para encerrar o laço em condições específicas.
# Reforçar a aplicação de contadores no controle de tentativas de acesso.
# Consolidar o uso de condições compostas na validação de login e bloqueio.
# Relembrar a organização do fluxo lógico em sistemas de autenticação.
# Reforçar a utilização da biblioteca EasyAnsi para destacar mensagens no terminal.
# 
# 🔗 Link do repositório da biblioteca EasyAnsi:
# https://github.com/GustaFranz/easyansi
#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
