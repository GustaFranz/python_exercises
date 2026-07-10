# 14 - Pandas - Merge de duas fontes

## Demanda

A Coordenacao solicita cruzar notas de simulado e prova por aluno e disciplina em uma unica tabela.

## Contexto do problema

Cada fonte esta em formato longo. Agora e preciso juntar as colunas de nota.

## Conceitos que voce vai usar

### `merge()`

Junta dois DataFrames com base em colunas em comum.

### `on=['turma','aluno','disciplina']`

Chaves compostas: as tres colunas devem coincidir para formar a linha.

### `how='inner'`

Mantem apenas registros presentes nas duas tabelas. Linhas sem par somem.

## Tarefas

1. Leia simulados_longo.csv e provas_longo.csv.
2. Faca merge inner nas chaves.
3. Exiba total de linhas e head.

## Criterios de aceite

- Merge sem erro.
- Colunas de ambas as fontes presentes.
- Linhas apenas com correspondencia em ambas.

## Como executar

```bash
cd 14_pandas_merge_duas_fontes
python main.py
```

## Referencia no projeto real

`src/consolidacao.py - primeiro merge`
