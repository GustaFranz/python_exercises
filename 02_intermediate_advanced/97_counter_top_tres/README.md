# 97 - Counter: top 3 itens

## Objetivo

Encontrar os 3 produtos mais vendidos com Counter.most_common.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / e-commerce |
| **Solicitacao** | Identificar os 3 itens mais vendidos no bazar da escola. |

## Enunciado

Lista de vendas do bazar:

```python
vendas = ["caderno", "caneta", "caderno", "borracha", "caneta", "caderno", "caneta"]
```

1) Use `Counter(vendas).most_common(3)` para obter os 3 produtos mais vendidos.
2) Exiba ranking formatado com posicao, produto e quantidade.

Exemplo de saida esperada:

```
1) caderno (3)
2) caneta (3)
3) borracha (1)
```

## Passo a passo

1. Importe `Counter` com `from collections import Counter`.
2. Crie a lista `vendas` com os itens do enunciado.
3. Calcule o top 3 com `top3 = Counter(vendas).most_common(3)` — o resultado e uma lista de tuplas `(produto, quantidade)` ja ordenada da maior para a menor contagem.
4. Percorra o ranking com `for posicao, (produto, qtd) in enumerate(top3, start=1):`
   - `enumerate(..., start=1)` numera as posicoes a partir de 1.
   - O parentese `(produto, qtd)` desempacota a tupla interna direto no `for`.
5. Dentro do loop, exiba `f"{posicao}) {produto} ({qtd})"`.
6. Confira que a saida bate com o exemplo do enunciado.

## Como executar

```bash
cd "97_counter_top_tres"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from collections import Counter

# Registro de cada venda do bazar (uma entrada por item vendido)
vendas = ["caderno", "caneta", "caderno", "borracha", "caneta", "caderno", "caneta"]

# Counter conta as ocorrencias; most_common(3) devolve as 3 maiores
top3 = Counter(vendas).most_common(3)

# enumerate com start=1 numera o ranking a partir de 1
# (produto, qtd) desempacota cada tupla do most_common
for posicao, (produto, qtd) in enumerate(top3, start=1):
    print(f"{posicao}) {produto} ({qtd})")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Ranking dos itens mais vendidos no bazar da Loja Virtual Escolar."""

from collections import Counter

VENDAS = ["caderno", "caneta", "caderno", "borracha", "caneta", "caderno", "caneta"]
TAMANHO_RANKING = 3


def montar_ranking(vendas: list[str], tamanho: int = TAMANHO_RANKING) -> list[str]:
    """Monta as linhas formatadas do ranking dos itens mais vendidos."""
    top = Counter(vendas).most_common(tamanho)
    # Uma linha por posicao, ja formatada para exibicao
    return [
        f"{posicao}) {produto} ({qtd})"
        for posicao, (produto, qtd) in enumerate(top, start=1)
    ]


def main() -> None:
    print("\n".join(montar_ranking(VENDAS)))


if __name__ == "__main__":
    main()
```

</details>
