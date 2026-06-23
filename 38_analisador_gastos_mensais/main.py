# EXERCICIO 38 - Analisador de gastos mensais (contexto financeiro)
#
# ENUNCIADO
# Uma pessoa registrou seus gastos de um mês. O programa deve solicitar N gastos informados pelo usuário e ao final mostrar:
## total gasto;
## média dos gastos;
## maior e menor gasto;
## quantos gastos foram acima de R$ 100.
#
# ORIENTACOES
## O usuário define quantos registros serão inseridos.
## Use for range(n).
## Converta entradas para float.
## Faça validações simples (valores negativos não são aceitos).
#
# --- Implemente sua solucao abaixo ---
#
# _______________________________________________________________________________
# # RESOLUÇÃO DO EXERCÍCIO
# _______________________________________________________________________________

# =============================================================================
# EXERCÍCIO 38 - ANALISADOR DE GASTOS MENSAIS
# =============================================================================

gastos_do_mes = []
total_gastos = 0
gastos_acima_100 = 0

# -----------------------------------------------------------------------------
# ENTRADA DE DADOS (com validação)
# -----------------------------------------------------------------------------

for g in range(1, 8):

    while True:
        gastos = float(input(f"Gasto {g}: R$ ").replace(',', '.'))

        if gastos < 0:
            print("❌ Valor inválido! Digite um valor positivo.")
        else:
            gastos_do_mes.append(gastos)
            total_gastos += gastos

            if gastos > 100:
                gastos_acima_100 += 1

            break

media = total_gastos / len(gastos_do_mes)

print("-" * 65)
print(f"Gastos do mês: {gastos_do_mes}")
print("-" * 65)
print(f"Total gasto: R$ {total_gastos:.2f}")
print("-" * 65)
print(f"Média dos gastos: R$ {media:.2f}")
print("-" * 65)
print(f"Maior gasto: R$ {max(gastos_do_mes):.2f}")
print("-" * 65)
print(f"Menor gasto: R$ {min(gastos_do_mes):.2f}")
print("-" * 65)
print(f"Gastos acima de R$100: {gastos_acima_100}")

# -----------------------------------------------------------------------------
# O QUE APRENDI
# -----------------------------------------------------------------------------

# - Validação de entrada com while True
# - Uso de listas para armazenar dados
# - Uso de acumuladores (total e contador)
# - Uso de funções nativas: sum(), max(), min(), len()
# - Tratamento de entrada com replace(',', '.')


#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
