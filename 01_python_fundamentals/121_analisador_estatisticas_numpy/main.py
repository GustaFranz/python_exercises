# EXERCICIO 121 - Analisador de estatisticas com NumPy (contexto cientifico leve)
#
# ENUNCIADO
# Um pesquisador deseja analisar um conjunto de dados numericos de forma simples.
# dados = [10, 20, 30, 40, 50, 60, 70, 80]
# O sistema deve:
## calcular media;
## calcular desvio simples (diferenca em relacao a media);
## identificar valores acima da media.
#
# ORIENTACOES
## Utilize numpy se disponivel (pip install numpy).
## Ou implemente logica equivalente com Python puro.
## Mantenha o codigo organizado em funcoes.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import numpy as np

import easyansi

easyansi.activate()

dados = [10, 20, 30, 40, 50, 60, 70, 80]


def calcular_media(dados):
    """Calcula a media dos dados"""
    return float(np.mean(dados))


def calcular_desvio(dados):
    """Calcula o desvio simples dos dados"""
    media = calcular_media(dados)
    return [float(abs(x - media)) for x in dados]


def identificar_acima_media(dados):
    """Identifica os valores acima da media"""
    media = calcular_media(dados)
    return [float(x) for x in dados if x > media]


def main():
    print(f"//green/Dados: //magenta/{dados}")
    print(f'//yellow/---------------------------------------------------------------')
    media = calcular_media(dados)
    print(f"//green/Media: //magenta/{media}")
    print(f'//yellow/---------------------------------------------------------------')
    desvio = calcular_desvio(dados)
    print(f"//green/Desvio simples: //magenta/{desvio}")
    print(f'//yellow/---------------------------------------------------------------')
    acima_media = identificar_acima_media(dados)
    print(f"//green/Valores acima da media:, //magenta/{acima_media}\n")


if __name__ == "__main__":
    main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com NumPy e np.mean() para calcular media
# Funcoes separadas para media, desvio simples e valores acima da media
# abs(x - media) mede distancia de cada valor em relacao a media
# List comprehension filtra valores acima da media sem alterar a lista original
# float() garante saida legivel mesmo com tipos do NumPy
# Animado em analisar dados cientificos com biblioteca especializada
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
