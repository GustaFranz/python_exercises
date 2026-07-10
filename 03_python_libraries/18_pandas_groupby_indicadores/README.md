# 18 - Pandas - Groupby e indicadores

## Demanda

A Coordenacao quer indicadores por turma: media geral, total de alunos, melhor e pior disciplina.

## Contexto do problema

Dashboard e boletins dependem de agregacoes por turma.

## Conceitos que voce vai usar

### `.groupby()`

Agrupa linhas por valor de coluna(s).

### `.mean()`

Calcula media de coluna numerica no grupo.

### `.nunique()`

Conta valores unicos (ex: alunos distintos).

### `.sort_values()`

Ordena para achar melhor/pior disciplina.

### `.iloc[0] / .iloc[-1]`

Acessa primeira e ultima linha apos ordenacao.

## Tarefas

1. Leia notas.csv.
2. Filtre uma turma.
3. Calcule media geral, total alunos, melhor e pior disciplina.

## Criterios de aceite

- Indicadores calculados.
- Melhor disciplina tem maior media.
- Total alunos usa nunique.

## Como executar

```bash
cd 18_pandas_groupby_indicadores
python main.py
```

## Referencia no projeto real

`dashboard.py linhas 19-31`
