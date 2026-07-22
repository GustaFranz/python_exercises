# EXERCICIO 132 - Leitor seguro de divisao (contexto matematico)
#
# ENUNCIADO
# Crie um programa que realize divisoes entre dois numeros informados pelo usuario,
# garantindo que o sistema nunca quebre.
# O sistema deve:
## pedir numerador e denominador;
## realizar a divisao;
## tratar divisao por zero e entradas invalidas;
## permitir repeticao ate o usuario decidir sair.
#
# ORIENTACOES
## Use try/except.
## Trate ZeroDivisionError e ValueError.
## Utilize loop while para repeticao.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

def validar_numeros():
    """Pede os números ao usuário e valida se o denominador é zero."""
    numerador = float(input("Digite o numerador: ").replace(",", "."))
    denominador = float(input("Digite o denominador ").replace(",", "."))

    if denominador == 0:
        raise ZeroDivisionError ("O denominador não pode ser zero")
    return numerador, denominador


def calcular_divisao(x, y):
    """Realiza a divisão simples entre dois números."""
    return x / y


try:
    num, den = validar_numeros()
    resultado = calcular_divisao(num, den)

    print(f'Numerador: {num} | Denominador: {den} | Resultado da divisão: {resultado:.2f}')
    print(f'Resultado da divisão: {resultado:.2f}')

except ZeroDivisionError as e:
    print("{e}")

except ValueError:
    print("[Erro de entrada]: Digite apenas números válidos")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Tive certa dificuldade em tratar divisao por zero e entrada invalida no mesmo fluxo
# try/except evita que o programa encerre com erro inesperado
# ZeroDivisionError trata denominador igual a zero
# ValueError trata texto ou simbolos que nao viram numero com float()
# raise ZeroDivisionError em validar_numeros() sinaliza regra de negocio antes do calculo
# replace(',', '.') aceita numeros digitados com virgula antes da conversao
# validar_numeros() e calcular_divisao() separam leitura, validacao e operacao matematica
# except ZeroDivisionError as e permite reutilizar a mensagem personalizada da excecao
# while True com break e o proximo passo para repetir a divisao ate o usuario sair
# Animado em aplicar tratamento de erros em calculos matematicos sem quebrar o sistema
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
