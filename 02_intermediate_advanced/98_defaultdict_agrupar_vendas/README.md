# 98 - Defaultdict: agrupar vendas

## Objetivo

Agrupar vendas por vendedor com defaultdict.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Consolidar vendas de material didatico por representante. |

## Enunciado

Vendas do periodo:

```python
vendas = [
    {"vendedor": "Ana", "valor": 50},
    {"vendedor": "Bruno", "valor": 30},
    {"vendedor": "Ana", "valor": 20},
]
```

1) Use `defaultdict(float)` para somar o `valor` de cada vendedor.
2) Exiba o total arrecadado por vendedor.

Exemplo de saida esperada:

```
Ana: R$ 70.00
Bruno: R$ 30.00
```

## Passo a passo

1. Importe com `from collections import defaultdict`.
2. Crie a lista `vendas` com os 3 dicts do enunciado.
3. Crie o acumulador `totais = defaultdict(float)` — quando uma chave nova e acessada, o defaultdict cria automaticamente o valor inicial `0.0`, dispensando o `if chave not in dict`.
4. Percorra as vendas com `for venda in vendas:` e some com `totais[venda["vendedor"]] += venda["valor"]`:
   - Na primeira vez que "Ana" aparece, `totais["Ana"]` nasce como `0.0` e recebe `+50`.
   - Na segunda vez, soma `+20` sobre o valor existente.
5. Exiba o resultado com `for vendedor, total in totais.items():` imprimindo `f"{vendedor}: R$ {total:.2f}"` — o `:.2f` formata com 2 casas decimais.

## Como executar

```bash
cd "98_defaultdict_agrupar_vendas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from collections import defaultdict

# Vendas do periodo: cada dict e uma venda individual
vendas = [
    {"vendedor": "Ana", "valor": 50},
    {"vendedor": "Bruno", "valor": 30},
    {"vendedor": "Ana", "valor": 20},
]

# defaultdict(float): chave nova comeca em 0.0 automaticamente
totais = defaultdict(float)

# Acumula o valor de cada venda no total do vendedor correspondente
for venda in vendas:
    totais[venda["vendedor"]] += venda["valor"]

# Exibe o consolidado; :.2f formata como moeda com 2 casas
for vendedor, total in totais.items():
    print(f"{vendedor}: R$ {total:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Consolidacao de vendas por representante da FinEdu Carteira."""

from collections import defaultdict

VENDAS = [
    {"vendedor": "Ana", "valor": 50},
    {"vendedor": "Bruno", "valor": 30},
    {"vendedor": "Ana", "valor": 20},
]


def totalizar_por_vendedor(vendas: list[dict]) -> dict[str, float]:
    """Soma o valor das vendas agrupando por vendedor."""
    totais: defaultdict[str, float] = defaultdict(float)
    for venda in vendas:
        totais[venda["vendedor"]] += venda["valor"]
    # Converte para dict comum: o chamador nao precisa do comportamento default
    return dict(totais)


def main() -> None:
    totais = totalizar_por_vendedor(VENDAS)
    # sorted por total decrescente: maiores vendedores primeiro
    for vendedor, total in sorted(totais.items(), key=lambda item: item[1], reverse=True):
        print(f"{vendedor}: R$ {total:.2f}")


if __name__ == "__main__":
    main()
```

</details>
