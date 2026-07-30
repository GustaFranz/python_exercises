# 115 - Dataclass: relatorio analitico de vendas

## Objetivo

Gerar metricas de vendas a partir de lista de dataclasses (total, ticket medio, top produto).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Consolidar vendas do bazar em relatorio analitico para reuniao comercial. |

## Enunciado

- Crie `@dataclass Venda` com `produto`, `quantidade` e `valor_unit`.
- Implemente `gerar_relatorio(vendas)` retornando **dict** com:
  - `total` — soma geral
  - `ticket_medio` — total / quantidade de vendas
  - `top_produto` — produto com maior subtotal
- Implemente `filtrar_vendas_acima(vendas, limite)` retornando vendas cujo subtotal >= limite.
- Use lista de exemplo com pelo menos 4 vendas e exiba relatorio + vendas filtradas.

## Como executar

```bash
cd "115_dataclass_relatorio_lista"
python main.py
```
