# EXERCICIO 115 - Modulos em pacotes (contexto educacional)
#
# ENUNCIADO
# Crie um sistema de analise de notas organizado como pacote Python.
# notas = [7.5, 3.2, 8.0, 6.5, 4.0]
# O pacote analise_notas/ deve conter modulos media.py, estatisticas.py e situacao.py.
# Adicione __init__.py e importe no main.py com:
# from analise_notas import media, estatisticas, situacao
#
# ORIENTACOES
## Crie a pasta analise_notas/ dentro do exercicio.
## Mova ou crie os modulos dentro dela.
## Adicione __init__.py.
## main.py apenas orquestra chamadas ao pacote.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

from analise_notas import obter_media, obter_estatisticas, obter_situacao

def main():
    vendas = [7.5, 3.2, 8.0, 6.5, 4.0]

    minimo, maximo = obter_estatisticas(vendas)
    media = obter_media(vendas)
    situacao = obter_situacao(vendas)

    print(f"Minimo: {minimo}")
    print(f"Maximo: {maximo}")
    print(f"Media: {media:.2f}")
    print(f"Situacao: {situacao}")

if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro pacote Python com pasta analise_notas/
# __init__.py expoe funcoes com from .modulo import
# __all__ define o que o pacote exporta
# Animado em estudar organizacao profissional de codigo
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
