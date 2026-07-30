"""Regras de negocio do checkout do bazar escolar — implemente as funcoes abaixo."""


def calcular_desconto(valor: float, percentual: float) -> float:
    """Aplica desconto percentual (dividendo entre 0 e 100) sobre valor.

    Args:
        valor: valor base da compra (>= 0).
        percentual: percentual de desconto entre 0 e 100.

    Returns:
        Valor final apos desconto.

    Raises:
        ValueError: se percentual estiver fora do intervalo [0, 100].
    """
    # Implemente aqui
    pass


def validar_pedido(qtd: int) -> bool:
    """Valida se quantidade permite finalizar pedido no checkout.

    Args:
        qtd: quantidade de itens no pedido.

    Returns:
        True se qtd >= 1, False caso contrario.
    """
    # Implemente aqui
    pass
