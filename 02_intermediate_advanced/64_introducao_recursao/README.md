# 64 - Introducao a recursao

## Objetivo

Entender caso base, chamada recursiva e calcular fatorial.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | CalcEscolar |
| **Setor** | Educacao / matematica |
| **Solicitacao** | Calcular combinacoes de provas com funcao recursiva didatica. |

## Visao do bloco (exercicios 64 a 68)

Topico **Recursao**: funcoes que chamam a si mesmas com caso base.

| # | Nivel | Foco |
|---|-------|------|
| 64 | Leve | Introducao + fatorial |
| 65 | Leve | Soma de 1 ate N |
| 66 | Ponte | Contagem regressiva |
| 67 | Entrevista | Busca recursiva + contagem com duplicatas |
| 68 | Entrevista | Percorrer estrutura aninhada (dict) |

## Enunciado

- Implemente fatorial(n) recursivo com caso base em n == 0.
- Teste com 0, 1, 5 e 6 e exiba os resultados.

## Passo a passo

1. Defina a funcao `fatorial(n: int) -> int`.
2. Escreva primeiro o caso base: `if n == 0: return 1`. Sem ele a funcao nunca para (recursao infinita).
3. Escreva o caso recursivo: `return n * fatorial(n - 1)`. Note que o problema fica menor a cada chamada (`n` diminui).
4. Nao use `for` nem `while` — apenas a propria funcao chamando a si mesma.
5. No corpo principal, crie a lista de testes `[0, 1, 5, 6]`.
6. Percorra a lista e exiba cada resultado no formato `fatorial(n) = resultado` (esperado: 1, 1, 120, 720).

## Como executar

```bash
cd "64_introducao_recursao"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def fatorial(n):
    # Caso base: fatorial de 0 e 1 por definicao matematica.
    # E ele que interrompe a cadeia de chamadas recursivas.
    if n == 0:
        return 1

    # Caso recursivo: n! = n * (n-1)!
    # A cada chamada o n diminui, aproximando do caso base.
    return n * fatorial(n - 1)


# Testes pedidos no enunciado
testes = [0, 1, 5, 6]

# Exibe cada resultado no formato pedido
for n in testes:
    print(f"fatorial({n}) = {fatorial(n)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Fatorial recursivo com validacao de entrada.

Em producao, um dev usaria math.factorial (implementado em C, mais rapido
e sem limite de profundidade de recursao). A versao recursiva abaixo existe
para dominar o conceito de caso base + caso recursivo.
"""


def fatorial(n: int) -> int:
    """Calcula n! recursivamente.

    Args:
        n: inteiro nao negativo.

    Raises:
        ValueError: se n for negativo (fatorial nao definido).
    """
    # Guard clause: falha cedo com mensagem clara em vez de recursao infinita
    if n < 0:
        raise ValueError(f"fatorial nao definido para negativos: {n}")

    # Caso base: 0! == 1 encerra a recursao
    if n == 0:
        return 1

    # Caso recursivo: reduz o problema ate chegar no caso base
    return n * fatorial(n - 1)


def main() -> None:
    for n in (0, 1, 5, 6):
        print(f"fatorial({n}) = {fatorial(n)}")

    # Alternativa de producao (mesma saida):
    # from math import factorial
    # print(factorial(6))  # 720


if __name__ == "__main__":
    main()
```

</details>
