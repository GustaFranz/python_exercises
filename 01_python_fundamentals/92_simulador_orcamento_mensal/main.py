# EXERCICIO 92 - Simulador de orcamento mensal (contexto financeiro)
#
# ENUNCIADO
# Crie funcoes para analisar um orcamento mensal a partir de uma lista de valores.
# gastos = [1200, 450, 300, 800, 150, 600]
# O programa deve retornar:
## total de gastos;
## media de gastos;
## maior gasto;
## menor gasto;
## saldo considerando uma renda fixa de 4000.
#
# ORIENTACOES
## Crie funcoes separadas para cada calculo.
## Crie uma funcao principal que chama as demais.
## Utilize return.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
gastos = [1200, 450, 300, 800, 150, 600]

def obter_total_gastos(list_gastos):
    total_gastos = sum(list_gastos)
    return total_gastos


def obter_media_gastos(list_gastos):
    media_gastos = sum(list_gastos) / len(list_gastos)
    return media_gastos

def obter_maior_gasto(list_gastos):
    maior_gasto = max(list_gastos)
    return maior_gasto

def obter_menor_gasto(list_gastos):
    menor_gasto = min(list_gastos)
    return menor_gasto

def obter_saldo(list_gastos):
    saldo = 4000 - (sum(list_gastos))
    return saldo

def main():
    total = obter_total_gastos(gastos)
    media = obter_media_gastos(gastos)
    maior = obter_maior_gasto(gastos)
    menor = obter_menor_gasto(gastos)
    saldo = obter_saldo(gastos)
    
    print("=== RELATÓRIO FINANCEIRO ===")
    print(f"Total de gastos: R$ {total:.2f}")
    print(f"Média de gastos: R$ {media:.2f}")
    print(f"Maior gasto:     R$ {maior:.2f}")
    print(f"Menor gasto:     R$ {menor:.2f}")
    print(f"Saldo final:     R$ {saldo:.2f}")

# NOTA: Em projetos reais, o ideal é usar "if __name__ == '__main__':" aqui.
main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Funcoes separadas com return para cada calculo financeiro
# main() centraliza chamadas e exibe o relatorio
# sum, max e min aplicados na mesma lista de gastos
# Saldo: renda fixa menos total de gastos
# Animado em montar um fluxo completo com funcao principal
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
