# 136 - map e comprehensions: relatorio de vendas

## Objetivo

Integrar `map()`, list comprehension e dict comprehension num relatorio comercial.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Tech Escolar |
| **Setor** | Varejo / analytics |
| **Solicitacao** | Calcular margem por SKU, destacar top vendas e indexar alertas. |

## Enunciado

```python
vendas = [
    {"sku": "A1", "produto": "Tablet", "qtd": 3, "preco": 800.0},
    {"sku": "B2", "produto": "Fone", "qtd": 10, "preco": 45.0},
    {"sku": "C3", "produto": "Mouse", "qtd": 25, "preco": 35.0},
    {"sku": "D4", "produto": "Teclado", "qtd": 8, "preco": 120.0},
]
CUSTO_PERCENTUAL = 0.65  # 65% do preco de venda
META_FATURAMENTO = 500.0
```

1) Use `map` para calcular faturamento de cada item: `qtd * preco`.
2) Com list comprehension, monte registros enriquecidos:
   `{sku, produto, faturamento, margem}` onde `margem = faturamento * (1 - CUSTO_PERCENTUAL)`.
3) Com list comprehension, selecione produtos com faturamento >= `META_FATURAMENTO`.
4) Com dict comprehension, monte `alertas = {sku: "meta_ok" if fat >= META else "abaixo"}`.
5) Exiba ranking (ordenado por faturamento desc), destaques e alertas.

## Passo a passo

1. Crie `vendas`, `CUSTO_PERCENTUAL` e `META_FATURAMENTO` conforme o enunciado.
2. Calcule os faturamentos com `map` e `lambda`: `faturamentos = list(map(lambda v: v["qtd"] * v["preco"], vendas))`.
3. Monte os registros enriquecidos com list comprehension sobre `zip(vendas, faturamentos)`, criando dicts com `sku`, `produto`, `faturamento` e `margem` (`faturamento * (1 - CUSTO_PERCENTUAL)`).
4. Selecione os destaques com list comprehension: registros com `faturamento >= META_FATURAMENTO`.
5. Monte os alertas com dict comprehension: `{r["sku"]: "meta_ok" if r["faturamento"] >= META_FATURAMENTO else "abaixo" for r in enriquecidos}`.
6. Ordene o ranking com `sorted(enriquecidos, key=lambda r: r["faturamento"], reverse=True)`.
7. Exiba: ranking (uma linha por SKU com produto, faturamento e margem), nomes dos destaques e o dict de alertas.

## Como executar

```bash
cd "136_map_comprehensions_relatorio_vendas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
vendas = [
    {"sku": "A1", "produto": "Tablet", "qtd": 3, "preco": 800.0},
    {"sku": "B2", "produto": "Fone", "qtd": 10, "preco": 45.0},
    {"sku": "C3", "produto": "Mouse", "qtd": 25, "preco": 35.0},
    {"sku": "D4", "produto": "Teclado", "qtd": 8, "preco": 120.0},
]
CUSTO_PERCENTUAL = 0.65  # custo representa 65% do preco de venda
META_FATURAMENTO = 500.0

# map + lambda: calcula o faturamento (qtd * preco) de cada venda
faturamentos = list(map(lambda v: v["qtd"] * v["preco"], vendas))

# zip alinha cada venda com seu faturamento; a comprehension monta
# o registro enriquecido com a margem (35% do faturamento)
enriquecidos = [
    {
        "sku": v["sku"],
        "produto": v["produto"],
        "faturamento": fat,
        "margem": round(fat * (1 - CUSTO_PERCENTUAL), 2),
    }
    for v, fat in zip(vendas, faturamentos)
]

# Destaques: apenas quem atingiu a meta de faturamento
destaques = [r for r in enriquecidos if r["faturamento"] >= META_FATURAMENTO]

# dict comprehension com if/else no VALOR: classifica cada sku
alertas = {
    r["sku"]: "meta_ok" if r["faturamento"] >= META_FATURAMENTO else "abaixo"
    for r in enriquecidos
}

# sorted com key + reverse: ranking do maior para o menor faturamento
ranking = sorted(enriquecidos, key=lambda r: r["faturamento"], reverse=True)

print("=== Ranking por faturamento ===")
for r in ranking:
    print(f"{r['sku']} {r['produto']}: R$ {r['faturamento']:.2f} (margem R$ {r['margem']:.2f})")

print("\n=== Destaques (meta >= R$ 500.00) ===")
for r in destaques:
    print(f"{r['sku']} {r['produto']}")

print(f"\nAlertas: {alertas}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Relatorio comercial: margem por SKU, destaques e alertas de meta."""

from operator import itemgetter

VENDAS = [
    {"sku": "A1", "produto": "Tablet", "qtd": 3, "preco": 800.0},
    {"sku": "B2", "produto": "Fone", "qtd": 10, "preco": 45.0},
    {"sku": "C3", "produto": "Mouse", "qtd": 25, "preco": 35.0},
    {"sku": "D4", "produto": "Teclado", "qtd": 8, "preco": 120.0},
]
CUSTO_PERCENTUAL = 0.65
META_FATURAMENTO = 500.0


def enriquecer(venda: dict) -> dict:
    """Calcula faturamento e margem de uma venda em um unico lugar."""
    faturamento = venda["qtd"] * venda["preco"]
    return {
        "sku": venda["sku"],
        "produto": venda["produto"],
        "faturamento": faturamento,
        # Margem = o que sobra apos o custo (35% do faturamento)
        "margem": round(faturamento * (1 - CUSTO_PERCENTUAL), 2),
    }


def main() -> None:
    # map com funcao nomeada: mesma ideia da lambda, porem testavel
    enriquecidos = list(map(enriquecer, VENDAS))

    destaques = [r for r in enriquecidos if r["faturamento"] >= META_FATURAMENTO]
    alertas = {
        r["sku"]: "meta_ok" if r["faturamento"] >= META_FATURAMENTO else "abaixo"
        for r in enriquecidos
    }
    # itemgetter e a versao da stdlib para "pegar o campo X" em sorts
    ranking = sorted(enriquecidos, key=itemgetter("faturamento"), reverse=True)

    print("=== Ranking por faturamento ===")
    for r in ranking:
        print(f"{r['sku']} {r['produto']}: R$ {r['faturamento']:.2f} (margem R$ {r['margem']:.2f})")

    print(f"\n=== Destaques (meta >= R$ {META_FATURAMENTO:.2f}) ===")
    for r in destaques:
        print(f"{r['sku']} {r['produto']}")

    print(f"\nAlertas: {alertas}")


if __name__ == "__main__":
    main()
```

</details>
