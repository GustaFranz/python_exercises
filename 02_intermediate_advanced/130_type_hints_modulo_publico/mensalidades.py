"""Calculos de mensalidade escolar — API publica tipada (implemente as funcoes)."""

from typing import Dict, List, Optional


def calcular_desconto(valor: float, percentual: float) -> float:
    """Aplica desconto percentual sobre valor de mensalidade.

    Args:
        valor: valor base da mensalidade.
        percentual: percentual de desconto entre 0 e 100.

    Returns:
        Valor final apos aplicar o desconto.
    """
    # Implemente aqui
    pass


def somar_valores(valores: List[float]) -> float:
    """Soma lista de valores de mensalidades.

    Args:
        valores: lista de valores numericos.

    Returns:
        Soma total dos valores. Retorna 0.0 se lista vazia.
    """
    # Implemente aqui
    pass


def resumo_mensalidades(alunos: List[Dict[str, float]]) -> Dict[str, float]:
    """Gera resumo estatistico das mensalidades dos alunos.

    Args:
        alunos: lista de dicts com chaves "nome" (str) e "valor" (float).

    Returns:
        Dict com chaves total, media, maior e menor.
        Se lista vazia, retorna zeros.
    """
    # Implemente aqui
    pass
