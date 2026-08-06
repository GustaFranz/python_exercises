# Retorno em 05/08 — comparar com a versao do inicio dos estudos.

from math import sin, cos, tan, radians


def ler_angulo() -> float:
    """Le o angulo em graus informado pelo usuario."""
    return float(input("Digite o angulo em graus: "))


def calcular_trigonometria(angulo_graus: float) -> dict[str, float]:
    """Converte graus em radianos e calcula seno, cosseno e tangente."""
    angulo_radianos = radians(angulo_graus)
    return {
        "seno": sin(angulo_radianos),
        "cosseno": cos(angulo_radianos),
        "tangente": tan(angulo_radianos),
    }


def exibir_resultados(resultados: dict[str, float]) -> None:
    """Imprime seno, cosseno e tangente com 2 casas decimais."""
    for nome, valor in resultados.items():
        print(f"O {nome} do angulo e {valor:.2f}")


# =============================================================================
# RESOLUCAO
# =============================================================================

try:
    angulo = ler_angulo()
    resultados = calcular_trigonometria(angulo)
    exibir_resultados(resultados)
except ValueError:
    print("Erro: digite um numero valido para o angulo.")

# =============================================================================
# APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# math.sin/cos/tan trabalham em radianos — radians() faz a conversao
# Separar leitura, calculo e exibicao deixa cada funcao com uma responsabilidade
# dict[str, float] guarda os tres resultados sem repetir print tres vezes
# f-string com :.2f formata casas decimais de forma mais limpa que .format()
# try/except ValueError cobre entrada que nao e numero (ex.: letras)
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
