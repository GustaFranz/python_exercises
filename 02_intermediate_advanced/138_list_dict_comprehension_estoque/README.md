# 138 - List e dict comprehension: estoque critico

## Objetivo

Usar list e dict comprehension juntas para monitorar estoque baixo e indexar quantidades.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Papelaria Central |
| **Setor** | Varejo / operacoes |
| **Solicitacao** | Identificar itens criticos e montar mapa de reposicao. |

## Enunciado

```python
produtos = [
    {"sku": "P01", "nome": "Caderno", "estoque": 12, "minimo": 10},
    {"sku": "P02", "nome": "Caneta", "estoque": 3, "minimo": 15},
    {"sku": "P03", "nome": "Borracha", "estoque": 25, "minimo": 8},
    {"sku": "P04", "nome": "Estojo", "estoque": 5, "minimo": 5},
    {"sku": "P05", "nome": "Lapis", "estoque": 2, "minimo": 20},
]
```

1) Com list comprehension, gere `criticos = [nome]` onde `estoque <= minimo`.
2) Com dict comprehension, monte `mapa_estoque = {sku: estoque}`.
3) Com dict comprehension, monte `reposicao = {sku: minimo - estoque}` apenas para itens criticos
   (valor minimo 0 se estoque ja atende).
4) Exiba criticos, mapa completo, fila de reposicao e total de SKUs criticos.

## Passo a passo

1. Crie a lista `produtos` conforme o enunciado.
2. Gere os criticos com list comprehension: `criticos = [p["nome"] for p in produtos if p["estoque"] <= p["minimo"]]` — note que `Estojo` entra (5 <= 5, borda de igualdade).
3. Monte o mapa completo com dict comprehension: `mapa_estoque = {p["sku"]: p["estoque"] for p in produtos}`.
4. Monte a reposicao com dict comprehension filtrada pelos mesmos criterios dos criticos, usando `max(0, p["minimo"] - p["estoque"])` como valor — o `max` garante que nunca fique negativo (caso da borda de igualdade, que resulta em 0).
5. Exiba: lista de criticos, `mapa_estoque`, dict de `reposicao` e `len(criticos)` como total de SKUs criticos.

## Como executar

```bash
cd "138_list_dict_comprehension_estoque"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
produtos = [
    {"sku": "P01", "nome": "Caderno", "estoque": 12, "minimo": 10},
    {"sku": "P02", "nome": "Caneta", "estoque": 3, "minimo": 15},
    {"sku": "P03", "nome": "Borracha", "estoque": 25, "minimo": 8},
    {"sku": "P04", "nome": "Estojo", "estoque": 5, "minimo": 5},
    {"sku": "P05", "nome": "Lapis", "estoque": 2, "minimo": 20},
]

# list comprehension: nomes dos itens em situacao critica
# (<= inclui a borda: estoque IGUAL ao minimo ja e critico)
criticos = [p["nome"] for p in produtos if p["estoque"] <= p["minimo"]]

# dict comprehension: indice rapido sku -> quantidade em estoque
mapa_estoque = {p["sku"]: p["estoque"] for p in produtos}

# dict comprehension filtrada: quanto falta comprar de cada item critico
# max(0, ...) evita valor negativo quando estoque == minimo
reposicao = {
    p["sku"]: max(0, p["minimo"] - p["estoque"])
    for p in produtos
    if p["estoque"] <= p["minimo"]
}

print(f"Criticos: {criticos}")
print(f"Mapa de estoque: {mapa_estoque}")
print(f"Fila de reposicao: {reposicao}")
print(f"Total de SKUs criticos: {len(criticos)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Monitor de estoque critico da papelaria."""

PRODUTOS = [
    {"sku": "P01", "nome": "Caderno", "estoque": 12, "minimo": 10},
    {"sku": "P02", "nome": "Caneta", "estoque": 3, "minimo": 15},
    {"sku": "P03", "nome": "Borracha", "estoque": 25, "minimo": 8},
    {"sku": "P04", "nome": "Estojo", "estoque": 5, "minimo": 5},
    {"sku": "P05", "nome": "Lapis", "estoque": 2, "minimo": 20},
]


def esta_critico(produto: dict) -> bool:
    """Regra de criticidade em um unico lugar: muda aqui, muda em todo lugar."""
    return produto["estoque"] <= produto["minimo"]


def main() -> None:
    # Materializa os criticos uma vez e reutiliza nas tres visoes
    produtos_criticos = [p for p in PRODUTOS if esta_critico(p)]

    criticos = [p["nome"] for p in produtos_criticos]
    mapa_estoque = {p["sku"]: p["estoque"] for p in PRODUTOS}
    reposicao = {p["sku"]: max(0, p["minimo"] - p["estoque"]) for p in produtos_criticos}

    print(f"Criticos: {criticos}")
    print(f"Mapa de estoque: {mapa_estoque}")
    print(f"Fila de reposicao: {reposicao}")
    print(f"Total de SKUs criticos: {len(criticos)}")


if __name__ == "__main__":
    main()
```

</details>
