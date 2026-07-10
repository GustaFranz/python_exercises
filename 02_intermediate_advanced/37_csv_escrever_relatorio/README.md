# 37 - CSV: escrever relatorio

## Objetivo

Exportar relatorio em CSV com csv.writer.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | RH Consolidado |
| **Setor** | Recursos humanos |
| **Solicitacao** | Exportar relatorio de horas para planilha do financeiro. |

## Enunciado

Dados em memoria:
relatorio = [
    {"funcionario": "Ana", "horas": 160},
    {"funcionario": "Bruno", "horas": 152},
]
Exporte para horas.csv com cabecalho funcionario,horas usando csv.DictWriter.
Confirme gravacao lendo e exibindo o arquivo.

## Como executar

```bash
cd "37_csv_escrever_relatorio"
python main.py
```
