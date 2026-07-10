# 40 - CSV: pipeline limpar e exportar

## Objetivo

Pipeline completo: ler CSV sujo, limpar e exportar CSV valido.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | Limpar base de clientes importada antes de subir ao CRM. |

## Enunciado

clientes_sujos.csv com problemas:
nome,email,idade
Ana,ana@mail.com,25
,bruno@mail.com,30        <- nome vazio
Carla,email-invalido,abc  <- idade invalida
Daniel,daniel@mail.com,28
Pipeline:
- 1) Ler CSV
- 2) Filtrar: nome nao vazio, idade numerica, "@" no email
- 3) Exportar clientes_limpos.csv
Exiba: lidos, descartados, exportados.

## Como executar

```bash
cd "40_csv_pipeline_limpar_exportar"
python main.py
```
