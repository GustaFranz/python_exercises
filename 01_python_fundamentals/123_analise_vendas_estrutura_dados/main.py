# EXERCICIO 123 - Analise de vendas com estrutura de dados (contexto de comercio)
#
# ENUNCIADO
# Considere a base de vendas abaixo:
# vendas = [{"produto": "camiseta", "valor": 120}, {"produto": "calca", "valor": 250}, {"produto": "tenis", "valor": 0}, {"produto": "bone", "valor": 80}, {"produto": "jaqueta", "valor": -50}]
# O programa deve:
## filtrar vendas validas (valor > 0);
## calcular total arrecadado;
## identificar produto mais caro vendido.
#
# ORIENTACOES
## Use listas de dicionarios.
## Filtre dados antes de calcular estatisticas.
## Utilize max() com key.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()

vendas = [
    {"produto": "camiseta", "valor": 120},
    {"produto": "calca", "valor": 250},
    {"produto": "tenis", "valor": 0},
    {"produto": "bone", "valor": 80},
    {"produto": "jaqueta", "valor": -50},
]


def filtrar_vendas_validas(vendas):
    """Retorna somente as vendas com valor positivo."""
    return [venda for venda in vendas if venda["valor"] > 0]


def calcular_total(vendas):
    """Calcula o valor total das vendas recebidas."""
    return sum(venda["valor"] for venda in vendas)


def identificar_produto_mais_caro(vendas):
    """Retorna a venda de maior valor ou None quando a lista esta vazia."""
    if not vendas:
        return None
    return max(vendas, key=lambda venda: venda["valor"])


def main():
    vendas_validas = filtrar_vendas_validas(vendas)
    total = calcular_total(vendas_validas)
    produto_mais_caro = identificar_produto_mais_caro(vendas_validas)

    print("//bold-blue/ANALISE DE VENDAS/bold-blue")
    print("//green/Vendas validas:/green")
    for venda in vendas_validas:
        print(f"//yellow/{venda['produto'].title()}: R$ {venda['valor']:.2f}/yellow")
    print(f"//green/Total arrecadado: //magenta/R$ {total:.2f}/magenta")
    print(
        "//green/Produto mais caro: "
        f"//magenta/{produto_mais_caro['produto'].title()} "
        f"(R$ {produto_mais_caro['valor']:.2f})/magenta"
    )


if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Lista de dicionarios representa vendas com produto e valor
# List comprehension filtra vendas validas (valor > 0) antes de calcular
# sum() com generator soma o total sem loop manual
# max() com key=lambda encontra o produto mais caro
# Filtrar dados ruins antes das estatisticas evita resultados distorcidos
# Funcoes separadas para filtrar, somar e identificar o maximo
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
