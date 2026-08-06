# Retorno em 05/08 — comparar com a versao do inicio dos estudos.


def ler_dados() -> tuple[float, float]:
    """Le massa (kg) e altura (m) e valida valores positivos."""
    massa = float(input("Digite sua massa em kg: "))
    altura = float(input("Digite sua altura em m: "))
    if massa <= 0 or altura <= 0:
        raise ValueError("Massa e altura devem ser maiores que zero.")
    return massa, altura


def calcular_imc(massa: float, altura: float) -> float:
    """Calcula o IMC com a formula massa / altura²."""
    return massa / (altura ** 2)


def classificar_imc(imc: float) -> str:
    """Retorna a faixa de classificacao do IMC."""
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"


def exibir_resultado(imc: float, classificacao: str) -> None:
    """Imprime o IMC formatado e a classificacao."""
    print(f"Seu Indice de Massa Corporal e {imc:.2f}")
    print(f"Classificacao: {classificacao}")


# =============================================================================
# RESOLUCAO
# =============================================================================

try:
    massa, altura = ler_dados()
    imc = calcular_imc(massa, altura)
    classificacao = classificar_imc(imc)
    exibir_resultado(imc, classificacao)
except ValueError as erro:
    print(f"Erro: {erro}")

# =============================================================================
# APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# IMC = massa / altura**2 — altura ao quadrado no denominador
# Separar calcular_imc e classificar_imc deixa cada regra isolada
# Encadear if imc < 18.5 / < 25 / < 30 evita buracos entre 24.9 e 25
# Validar massa e altura > 0 evita divisao por zero e dados impossiveis
# f-string com :.2f substitui .format() de forma mais direta
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
