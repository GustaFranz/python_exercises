# EXERCICIO 135 - Login seguro com controle de erro (contexto digital)
#
# ENUNCIADO
# Crie um sistema de login que protege contra erros de entrada e multiplas tentativas invalidas.
# O sistema deve:
## pedir usuario e senha;
## permitir ate 3 tentativas;
## tratar entradas invalidas sem quebrar o sistema;
## bloquear acesso apos falhas consecutivas.
#
# ORIENTACOES
## Use try/except dentro do loop.
## Controle tentativas com contador.
## Trate erros de entrada inesperada.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
class SenhaInvalidaError(Exception):
    """Lançado quando houver entrada inválida para Senha"""

#APESAR DO FATO DE QUE NOS CASOS REAIS AS MENSAGENS DE ERRO NÃO TRAZEREM ESSAS DICAS PARA O CASO DE ALGUÉM QUERER DESCOBRIR, 
#COLOQUEI ESSAS MENSGAENS PARA TREINAR O TRATAMENTO DE ERROS

senha_real = "1GustAvo2"

def validar_senha(senha_digitada):
    if senha_digitada.strip() == "":
        raise SenhaInvalidaError("A senha deve conter pelo menos 1 caractere")

    elif not senha_digitada.isalnum():
        raise SenhaInvalidaError("A senha só pode conter digitos alfanuméricos")

    elif senha_digitada != senha_real:
        raise SenhaInvalidaError("As senhas não coincidem")

    return True

maximo_tentativas = 3
tentativas = 0

while tentativas < maximo_tentativas:
    senha_input = input("Digite a sua senha: ")

    try:
        validar_senha(senha_input)

    except SenhaInvalidaError as e:
        print(f'Erro: {e}')
        tentativas += 1
        restantes = maximo_tentativas - tentativas

        if restantes > 0:
            print(f'Você ainda tem {restantes} tentativas')

    else:
        print("\nLogin realizado com sucesso!")
        break

else:
    print("\nNúmero máximo de tentativas excedido. Acesso bloqueado!")






# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Excecao customizada SenhaInvalidaError deixa as regras de senha mais claras
# validar_senha() concentra validacao; try/except fica no loop de tentativas
# Contador com limite de 3 tentativas evita tentativas infinitas de acesso
# else do while trata sucesso; else do while externo bloqueia apos o limite
# Animado em juntar tratamento de erros com controle de tentativas no login
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
