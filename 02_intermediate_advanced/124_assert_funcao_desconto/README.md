# 124 - Assert: funcao de desconto

## Objetivo

Testar funcao de desconto com asserts em multiplos cenarios.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / precificacao |
| **Solicitacao** | Validar regras de desconto progressivo antes da campanha do bazar. |

## Enunciado

Implemente:

```python
def aplicar_desconto(valor: float, pct: float) -> float:
    # pct entre 0 e 1; se pct invalido retorna valor original
```

Regra: aplique desconto apenas se `0 <= pct <= 1`.

Escreva asserts de teste:

```python
assert aplicar_desconto(100, 0.10) == 90.0
assert aplicar_desconto(50, 0) == 50.0
assert aplicar_desconto(80, 1.5) == 80.0   # pct invalido
```

## Passo a passo

1. Defina `aplicar_desconto(valor: float, pct: float) -> float`.
2. Valide o percentual primeiro: `if not 0 <= pct <= 1: return valor` (pct invalido devolve o valor original, sem erro).
3. No caso valido, retorne `valor * (1 - pct)`.
4. Escreva os tres asserts do enunciado: desconto normal (`100` com `0.10` -> `90.0`), desconto zero (`50` com `0` -> `50.0`) e pct invalido (`80` com `1.5` -> `80.0`).
5. Acrescente pelo menos um assert extra de borda por conta propria, ex.: `assert aplicar_desconto(100, 1) == 0.0` (desconto total).
6. Exiba `print("Todos os testes passaram.")` ao final.

## Como executar

```bash
cd "124_assert_funcao_desconto"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def aplicar_desconto(valor: float, pct: float) -> float:
    # Regra de negocio: pct fora de [0, 1] e invalido -> devolve valor original
    # (comparacao encadeada 0 <= pct <= 1 e idiomatica em Python)
    if not 0 <= pct <= 1:
        return valor
    # Desconto de 10% = pagar 90% do valor -> valor * (1 - pct)
    return valor * (1 - pct)


# Cenario comum: 10% de desconto sobre 100
assert aplicar_desconto(100, 0.10) == 90.0, "10% sobre 100 deveria dar 90.0"
# Borda: desconto zero nao altera o valor
assert aplicar_desconto(50, 0) == 50.0, "desconto 0 deve manter o valor"
# Borda: pct invalido (> 1) devolve o valor original
assert aplicar_desconto(80, 1.5) == 80.0, "pct invalido deve manter o valor"
# Bordas extras: desconto total e pct negativo
assert aplicar_desconto(100, 1) == 0.0, "desconto de 100% deve zerar o valor"
assert aplicar_desconto(100, -0.2) == 100, "pct negativo e invalido"

print("Todos os testes passaram.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Regra de desconto do bazar escolar com suite de asserts.

Com pytest, valores float seriam comparados com pytest.approx
(ex.: assert aplicar_desconto(100, 0.10) == pytest.approx(90.0)),
evitando surpresas de arredondamento binario.
"""

PCT_MINIMO = 0.0
PCT_MAXIMO = 1.0


def aplicar_desconto(valor: float, pct: float) -> float:
    """Aplica desconto percentual (0 a 1) sobre o valor.

    Percentual fora do intervalo e considerado invalido e o valor
    original e devolvido — regra definida pelo negocio (nao levantar erro).
    """
    # Guard clause: sai cedo no caso invalido, o fluxo principal fica limpo
    if not PCT_MINIMO <= pct <= PCT_MAXIMO:
        return valor
    return valor * (1 - pct)


def testar_aplicar_desconto() -> None:
    """Cobre cenario comum, bordas do intervalo e percentuais invalidos."""
    assert aplicar_desconto(100, 0.10) == 90.0, "10% sobre 100 deveria dar 90.0"
    assert aplicar_desconto(50, 0) == 50.0, "desconto 0 deve manter o valor"
    assert aplicar_desconto(80, 1.5) == 80.0, "pct > 1 e invalido"
    assert aplicar_desconto(100, 1) == 0.0, "desconto de 100% deve zerar o valor"
    assert aplicar_desconto(100, -0.2) == 100, "pct negativo e invalido"


if __name__ == "__main__":
    testar_aplicar_desconto()
    print("Todos os testes passaram.")
```

</details>
