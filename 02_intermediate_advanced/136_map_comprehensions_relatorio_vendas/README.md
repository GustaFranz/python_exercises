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

## Como executar

```bash
cd "136_map_comprehensions_relatorio_vendas"
python main.py
```
