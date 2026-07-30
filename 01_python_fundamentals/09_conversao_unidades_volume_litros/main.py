# Retorno em 30/07 — comparar com a versao do inicio dos estudos.

# Fatores relativos a 1 litro.
FATORES = {
    "kl": 1 / 1000,
    "hl": 1 / 100,
    "dal": 1 / 10,
    "dl": 10,
    "cl": 100,
    "ml": 1000,
}


def ler_litros() -> float:
    """Le litros do usuario e valida o valor."""
    litros = float(input("Digite o valor em litros (L) que voce deseja converter: "))
    if litros < 0:
        raise ValueError("Valor em litros nao pode ser negativo.")
    return litros


def converter_litros(litros: float) -> dict[str, float]:
    """Converte litros para as unidades de volume do sistema metrico."""
    return {unidade: litros * fator for unidade, fator in FATORES.items()}


def exibir_conversoes(conversoes: dict[str, float]) -> None:
    """Imprime o resultado formatado."""
    for unidade, valor in conversoes.items():
        print(f"O valor em {unidade} e {valor}")


# =============================================================================
# RESOLUCAO
# =============================================================================

try:
    litros = ler_litros()
    conversoes = converter_litros(litros)
    exibir_conversoes(conversoes)
except ValueError as erro:
    print(f"Erro: {erro}")
