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

## Como executar

```bash
cd "98_defaultdict_agrupar_vendas"
python main.py
```
