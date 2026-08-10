# 17 - Zip: produto, preco e estoque

## Objetivo

Cruzar tres listas com zip em tuplas.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Deposito Escolar Norte |
| **Setor** | Distribuicao / estoque |
| **Solicitacao** | Visao consolidada de produto, preco e quantidade em estoque. |

## Enunciado

produtos = ["caderno", "caneta", "borracha"]
precos = [8.0, 2.5, 1.5]
estoques = [150, 400, 220]
Gere catalogo = list(zip(produtos, precos, estoques))
Exiba tabela: produto | preco | estoque | valor_total_estoque (preco * estoque).

## Passo a passo

1. Crie as tres listas paralelas `produtos`, `precos` e `estoques` com os dados do enunciado.
2. Gere `catalogo = list(zip(produtos, precos, estoques))` — cada item vira uma tupla `(produto, preco, estoque)`.
3. Exiba um cabecalho de tabela com as colunas `produto | preco | estoque | valor_total`.
4. Percorra o catalogo com `for produto, preco, estoque in catalogo:` (desempacotando a tupla direto no for).
5. Dentro do loop, calcule `valor_total_estoque = preco * estoque` e imprima a linha formatada com alinhamento (f-string com `:<10`, `:>8.2f` etc.).

## Como executar

```bash
cd "17_zip_produto_preco_estoque"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Listas paralelas do sistema de estoque (enunciado)
produtos = ["caderno", "caneta", "borracha"]
precos = [8.0, 2.5, 1.5]
estoques = [150, 400, 220]

# zip cruza as tres listas pela posicao; list() materializa as tuplas
catalogo = list(zip(produtos, precos, estoques))

# Cabecalho da tabela com colunas alinhadas
print(f'{"PRODUTO":<10} | {"PRECO":>7} | {"ESTOQUE":>7} | {"VALOR TOTAL":>11}')
print("-" * 45)

# Desempacota cada tupla direto no for: produto, preco e estoque juntos
for produto, preco, estoque in catalogo:
    # Valor imobilizado daquele item: preco unitario x quantidade
    valor_total_estoque = preco * estoque
    print(f"{produto:<10} | {preco:>7.2f} | {estoque:>7} | {valor_total_estoque:>11.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Visao consolidada de produto, preco e estoque do deposito."""


def montar_catalogo(
    produtos: list[str],
    precos: list[float],
    estoques: list[int],
) -> list[tuple[str, float, int]]:
    """Cruza as tres listas em tuplas (produto, preco, estoque).

    strict=True garante que as listas tem o mesmo tamanho; em dados
    de estoque, truncar em silencio esconderia produtos.
    """
    return list(zip(produtos, precos, estoques, strict=True))


def main() -> None:
    # Dados de entrada do enunciado
    produtos = ["caderno", "caneta", "borracha"]
    precos = [8.0, 2.5, 1.5]
    estoques = [150, 400, 220]

    # Consolida as listas paralelas em registros
    catalogo = montar_catalogo(produtos, precos, estoques)

    # Tabela formatada para a operacao
    print(f'{"PRODUTO":<10} | {"PRECO":>7} | {"ESTOQUE":>7} | {"VALOR TOTAL":>11}')
    print("-" * 45)
    for produto, preco, estoque in catalogo:
        valor_total = preco * estoque
        print(f"{produto:<10} | {preco:>7.2f} | {estoque:>7} | {valor_total:>11.2f}")

    # Total geral imobilizado: soma dos valores por item em um generator
    total_geral = sum(preco * estoque for _, preco, estoque in catalogo)
    print("-" * 45)
    print(f"Valor total do estoque: {total_geral:.2f}")


if __name__ == "__main__":
    main()
```

</details>
