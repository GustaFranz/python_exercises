# 38 - CSV: delimitador ponto e virgula

## Objetivo

Trabalhar CSV no padrao brasileiro com delimitador ;.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Contabilidade Brasil Fiscal |
| **Setor** | Contabilidade |
| **Solicitacao** | Gerar CSV compativel com Excel brasileiro (separador ;). |

## Enunciado

Exporte vendas para vendas_br.csv com delimitador ";".
Dados: produto;preco — ex.: caderno;12,50 (use ponto no valor no CSV: 12.50).
Cabecalho: produto;preco
Leia de volta com csv.reader(delimiter=";") e exiba.

## Como executar

```bash
cd "38_csv_delimitador_ponto_virgula"
python main.py
```
