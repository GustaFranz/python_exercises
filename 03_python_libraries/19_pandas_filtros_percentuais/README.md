# 19 - Pandas - Filtros e percentuais

## Demanda

O painel gerencial precisa de percentuais: acima da media, abaixo e em recuperacao.

## Contexto do problema

Indicadores percentuais alimentam metricas do dashboard.

## Conceitos que voce vai usar

### `dados[condicao]`

Filtro booleano: mantem linhas onde condicao e True.

### `.eq('Recuperacao')`

Compara coluna com valor exato.

### `.mean() * 100`

Em coluna booleana, mean da proporcao de True (percentual).

## Tarefas

1. Leia `dados/notas.csv`.
2. Calcule % acima de 6, % abaixo de 6, % em recuperacao (sobre linhas do arquivo).
3. Liste alunos em recuperacao.

## Criterios de aceite

- Tres percentuais exibidos (calculados sobre linhas do CSV).
- Lista de recuperacao correta.

## Como executar

```bash
cd 19_pandas_filtros_percentuais
python main.py
```

## Referencia no projeto real

`dashboard.py linhas 21-23 e 57-59`
