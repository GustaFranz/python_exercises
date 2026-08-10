# 134 - map com lambda e list comprehension

## Objetivo

Aplicar `map()` com `lambda` e filtrar resultados com list comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Moda Escolar Online |
| **Setor** | Varejo / catalogo |
| **Solicitacao** | Padronizar nomes de produtos e listar itens em promocao. |

## Enunciado

```python
produtos = ["  CAMISETA POLO ", "tenis escolar", " MOCHILA ", "bone oficial", "calcado esportivo"]
precos = [89.9, 120.0, 150.0, 35.0, 199.9]
LIMITE_PROMOCAO = 100.0
```

1) Use `map(lambda p: p.strip().title(), produtos)` para gerar nomes padronizados.
2) Com list comprehension, monte pares `{nome, preco}` cruzando nomes padronizados e `precos`
   (mesmo indice).
3) Filtre com list comprehension apenas produtos com preco <= `LIMITE_PROMOCAO`.
4) Exiba catalogo padronizado, itens em promocao e quantidade promocional.

## Passo a passo

1. Crie as listas `produtos`, `precos` e a constante `LIMITE_PROMOCAO` do enunciado.
2. Padronize os nomes com `nomes = list(map(lambda p: p.strip().title(), produtos))` — `strip()` remove espacos das pontas e `title()` capitaliza cada palavra.
3. Cruze nome e preco pelo indice com `zip` dentro de list comprehension: `catalogo = [{"nome": n, "preco": p} for n, p in zip(nomes, precos)]`.
4. Filtre a promocao com outra list comprehension: `promocao = [item for item in catalogo if item["preco"] <= LIMITE_PROMOCAO]`.
5. Exiba o catalogo completo (um item por linha com nome e preco), depois os itens em promocao e por fim `len(promocao)` como quantidade promocional.

## Como executar

```bash
cd "134_map_lambda_list_comprehension"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
produtos = ["  CAMISETA POLO ", "tenis escolar", " MOCHILA ", "bone oficial", "calcado esportivo"]
precos = [89.9, 120.0, 150.0, 35.0, 199.9]
LIMITE_PROMOCAO = 100.0

# map + lambda: aplica a mesma padronizacao a todos os nomes
# strip() tira espacos das pontas; title() capitaliza cada palavra
nomes = list(map(lambda p: p.strip().title(), produtos))

# zip alinha nome e preco pelo indice; a comprehension monta um dict por produto
catalogo = [{"nome": n, "preco": p} for n, p in zip(nomes, precos)]

# Filtro da promocao: mantem apenas itens ate o limite
promocao = [item for item in catalogo if item["preco"] <= LIMITE_PROMOCAO]

print("=== Catalogo padronizado ===")
for item in catalogo:
    print(f"{item['nome']}: R$ {item['preco']:.2f}")

print("\n=== Em promocao (ate R$ 100.00) ===")
for item in promocao:
    print(f"{item['nome']}: R$ {item['preco']:.2f}")

print(f"\nQuantidade promocional: {len(promocao)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Padronizacao de catalogo e vitrine de promocao."""

PRODUTOS = ["  CAMISETA POLO ", "tenis escolar", " MOCHILA ", "bone oficial", "calcado esportivo"]
PRECOS = [89.9, 120.0, 150.0, 35.0, 199.9]
LIMITE_PROMOCAO = 100.0


def padronizar_nome(nome: str) -> str:
    """Funcao nomeada no lugar da lambda: reutilizavel e testavel."""
    return nome.strip().title()


def montar_catalogo(produtos: list[str], precos: list[float]) -> list[dict]:
    """Cruza nomes padronizados e precos pelo indice."""
    # zip(strict=True) falha alto se as listas tiverem tamanhos diferentes —
    # melhor um erro imediato do que um catalogo silenciosamente truncado
    return [
        {"nome": padronizar_nome(nome), "preco": preco}
        for nome, preco in zip(produtos, precos, strict=True)
    ]


def main() -> None:
    catalogo = montar_catalogo(PRODUTOS, PRECOS)
    promocao = [item for item in catalogo if item["preco"] <= LIMITE_PROMOCAO]

    print("=== Catalogo padronizado ===")
    for item in catalogo:
        print(f"{item['nome']}: R$ {item['preco']:.2f}")

    print(f"\n=== Em promocao (ate R$ {LIMITE_PROMOCAO:.2f}) ===")
    for item in promocao:
        print(f"{item['nome']}: R$ {item['preco']:.2f}")

    print(f"\nQuantidade promocional: {len(promocao)}")


if __name__ == "__main__":
    main()
```

</details>
