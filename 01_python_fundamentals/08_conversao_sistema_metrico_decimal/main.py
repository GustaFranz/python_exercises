# Retorno em 30/07 — comparar com a versao do inicio dos estudos.

# Fatores relativos a 1 metro (dividir = unidades maiores; multiplicar = menores).
FATORES = {
    "km": 1 / 1000,
    "hm": 1 / 100,
    "dam": 1 / 10,
    "dm": 10,
    "cm": 100,
    "mm": 1000,
}


def ler_metros() -> float:
    """Le metros do usuario e valida o valor."""
    metros = float(input("Digite o valor em metros (m) que voce deseja converter: "))
    if metros < 0:
        raise ValueError("Valor em metros nao pode ser negativo.")
    return metros


def converter_metros(metros: float) -> dict[str, float]:
    """Converte metros para as unidades do sistema metrico decimal."""
    return {unidade: metros * fator for unidade, fator in FATORES.items()}


def exibir_conversoes(conversoes: dict[str, float]) -> None:
    """Imprime o resultado formatado."""
    for unidade, valor in conversoes.items():
        print(f"o valor em {unidade} e {valor}")


# =============================================================================
# RESOLUCAO
# =============================================================================

try:
    metros = ler_metros()
    conversoes = converter_metros(metros)
    exibir_conversoes(conversoes)
except ValueError as erro:
    print(f"Erro: {erro}")
