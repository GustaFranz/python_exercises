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

## Como executar

```bash
cd "138_list_dict_comprehension_estoque"
python main.py
```
