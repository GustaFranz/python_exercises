def obter_estatisticas(vendas):
    minimo = min(vendas) if vendas else 0
    maximo = max(vendas) if vendas else 0
    return minimo, maximo

