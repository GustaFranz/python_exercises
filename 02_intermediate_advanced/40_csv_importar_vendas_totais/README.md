# 40 - CSV: importar vendas com validacao e totais

## Objetivo

Importar CSV de vendas, validar linhas e calcular metricas comerciais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Mercado Bom Preco |
| **Setor** | Varejo / financeiro |
| **Solicitacao** | Importar vendas do caixa, rejeitar linhas invalidas e fechar o dia. |

## Enunciado

Crie `vendas.csv` (ou use dados embutidos e grave o arquivo) com cabecalho:
`produto,quantidade,preco_unitario`

Inclua linhas validas e invalidas, por exemplo:
```
produto,quantidade,preco_unitario
caneta,10,2.50
caderno,5,12.00
borracha,-2,1.00
lapis,3,abc
marcador,8,4.50
```

Regras:
- `quantidade` deve ser int > 0
- `preco_unitario` deve ser float > 0
- linha invalida vai para lista de rejeicoes (motivo claro)

Calcule para linhas validas: subtotal, itens vendidos, faturamento total,
ticket medio (faturamento / qtd de linhas validas).
Exiba tabela valida, rejeicoes e resumo do fechamento do dia.

## Como executar

```bash
cd "40_csv_importar_vendas_totais"
python main.py
```
