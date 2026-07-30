# 19 - Zip: margem e alerta comercial por SKU

## Objetivo

Cruzar vendas, custos e meta com zip para relatorio de margem.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Mercado Bom Preco |
| **Setor** | Varejo / comercial |
| **Solicitacao** | Relatorio de margem por SKU com alerta de produtos abaixo da meta. |

## Enunciado

skus = ["SKU01", "SKU02", "SKU03", "SKU04"]
vendas = [1200.0, 800.0, 450.0, 1500.0]
custos = [700.0, 500.0, 300.0, 1200.0]
meta_margem_pct = [35.0, 40.0, 30.0, 25.0]

Para cada SKU (use `zip`):
1) `margem = venda - custo`
2) `margem_pct = (margem / venda) * 100` (se venda > 0)
3) `status = "ok"` se margem_pct >= meta, senao `"abaixo_da_meta"`

Monte lista de dicts `{sku, venda, custo, margem, margem_pct, status, meta}`.
Exiba:
- tabela completa
- SKU com maior margem_pct
- lista de SKUs abaixo da meta (backlog comercial)
- margem media percentual do portfolio

## Como executar

```bash
cd "19_zip_vendas_custos_sku"
python main.py
```
