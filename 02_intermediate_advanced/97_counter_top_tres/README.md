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

## Como executar

```bash
cd "97_counter_top_tres"
python main.py
```
