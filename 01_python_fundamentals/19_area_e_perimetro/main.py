# Retorno em 05/08 — comparar com a versao do inicio dos estudos.


def ler_dimensoes() -> tuple[float, float]:
    """Le comprimento e largura do retangulo e valida valores positivos."""
    comprimento = float(input("Digite o comprimento do retangulo (m): "))
    largura = float(input("Digite a largura do retangulo (m): "))
    if comprimento <= 0 or largura <= 0:
        raise ValueError("Comprimento e largura devem ser maiores que zero.")
    return comprimento, largura


def calcular_retangulo(comprimento: float, largura: float) -> dict[str, float]:
    """Calcula area, perimetro e a soma dos dois."""
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    return {
        "area": area,
        "perimetro": perimetro,
        "soma": area + perimetro,
    }


def exibir_resultados(resultados: dict[str, float]) -> None:
    """Imprime area, perimetro e a soma formatados."""
    print(f"A area do retangulo e {resultados['area']} m²")
    print(f"O perimetro do retangulo e {resultados['perimetro']} m")
    print(f"A soma da area e do perimetro e {resultados['soma']}")


# =============================================================================
# RESOLUCAO
# =============================================================================

try:
    comprimento, largura = ler_dimensoes()
    resultados = calcular_retangulo(comprimento, largura)
    exibir_resultados(resultados)
except ValueError as erro:
    print(f"Erro: {erro}")

# =============================================================================
# APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Area = comprimento * largura; perimetro = 2 * (comprimento + largura)
# tuple[float, float] devolve as duas dimensoes juntas na leitura
# Validar <= 0 evita retangulo com lado impossivel
# O enunciado pedia a soma area + perimetro — a versao antiga nao fazia isso
# Separar leitura, calculo e exibicao facilita testar cada parte depois
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
