# 65 - Recursao: soma de 1 ate N

## Objetivo

Somar 1 + 2 + ... + N usando recursao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Somar parcelas mensais acumuladas para simulacao de plano. |

## Enunciado

Implemente recursivamente:

```python
def soma_ate(n: int) -> int:
    # soma_ate(0) retorna 0
    # soma_ate(n) retorna n + soma_ate(n - 1)
```

No `main`, exiba:

1) `soma_ate(1)` → `1`
2) `soma_ate(5)` → `15`
3) `soma_ate(10)` → `55`

Exemplo de saida:

```
soma_ate(1) = 1
soma_ate(5) = 15
soma_ate(10) = 55
```

## Passo a passo

1. Defina a funcao `soma_ate(n: int) -> int`.
2. Escreva o caso base: `if n == 0: return 0` (a soma de "nada" e zero, e e aqui que a recursao para).
3. Escreva o caso recursivo: `return n + soma_ate(n - 1)` (soma o valor atual com a soma de todos os anteriores).
4. Nao use `for`, `while` nem a funcao `sum` — apenas recursao.
5. No corpo principal, chame a funcao para `1`, `5` e `10`.
6. Exiba cada resultado no formato `soma_ate(n) = resultado` (esperado: 1, 15, 55).

## Como executar

```bash
cd "65_recursao_soma_ate_n"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def soma_ate(n):
    # Caso base: soma ate 0 e 0 — encerra a cadeia de chamadas
    if n == 0:
        return 0

    # Caso recursivo: n + soma de todos os numeros antes dele
    # Ex.: soma_ate(5) = 5 + soma_ate(4) = 5 + 4 + soma_ate(3) ...
    return n + soma_ate(n - 1)


# Testa e exibe os tres casos pedidos
for n in [1, 5, 10]:
    print(f"soma_ate({n}) = {soma_ate(n)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Soma de 1 ate N com recursao.

Em producao, um dev usaria sum(range(1, n + 1)) ou a formula fechada
de Gauss n * (n + 1) // 2 (custo constante, sem risco de estourar a
pilha de recursao). A recursao aqui e exercicio de conceito.
"""


def soma_ate(n: int) -> int:
    """Retorna 1 + 2 + ... + n recursivamente (n >= 0)."""
    # Guard clause: entrada invalida falha cedo e com contexto
    if n < 0:
        raise ValueError(f"n deve ser >= 0, recebido: {n}")

    # Caso base encerra a recursao
    if n == 0:
        return 0

    # Caso recursivo: problema diminui a cada chamada
    return n + soma_ate(n - 1)


def main() -> None:
    for n in (1, 5, 10):
        print(f"soma_ate({n}) = {soma_ate(n)}")

    # Alternativas de producao (mesma saida logica):
    # sum(range(1, n + 1))     -> builtin, linear e sem recursao
    # n * (n + 1) // 2         -> formula de Gauss, custo constante


if __name__ == "__main__":
    main()
```

</details>
