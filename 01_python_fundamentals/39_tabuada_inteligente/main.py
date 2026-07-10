# EXERCICIO 39 - Tabuada inteligente (contexto educacional)
#
# ENUNCIADO
# Crie um programa que receba um número e gere sua tabuada de forma completa (1 a 10), mas com as seguintes regras:
## mostrar apenas multiplicações cujo resultado seja par;
## contar quantas operações foram exibidas;
## armazenar os resultados em uma lista.
#
# ORIENTACOES
## Use for de 1 a 10.
## Use condição dentro do loop.
## Use operador % para verificar paridade.
## Armazene resultados em lista.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

resultados = []
operacoes_exibidas = 0

numero = int(input("Digite um número inteiro: "))

print("-" * 40)
print(f"Tabuada par do número {numero}")
print("-" * 40)

for n in range(1, 11):
    multiplicacao = numero * n

    if multiplicacao % 2 == 0:
        print(f"{numero} x {n} = {multiplicacao}")
        resultados.append(multiplicacao)
        operacoes_exibidas += 1

print("-" * 40)
print(f"Resultados armazenados: {resultados}")
print(f"Quantidade de operações exibidas: {operacoes_exibidas}")


# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# - Cálculo de operações matemáticas dentro de um loop (tabuada)
# - Uso de contador para registrar quantas operações foram exibidas


# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
