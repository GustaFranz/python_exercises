from .estatisticas import obter_estatisticas
from .media import obter_media

def obter_situacao(vendas):
    minimo, maximo = obter_estatisticas(vendas)
    media = obter_media(vendas)

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
    