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

## Como executar

```bash
cd "17_zip_produto_preco_estoque"
python main.py
```
