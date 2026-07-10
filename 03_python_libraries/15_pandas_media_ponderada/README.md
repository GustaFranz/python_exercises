# 15 - Pandas - Media ponderada

## Demanda

O Conselho Pedagogico definiu formula oficial de media com pesos. Implemente a regra no sistema.

## Contexto do problema

Apos merge triplo, cada linha precisa de uma media final calculada.

## Conceitos que voce vai usar

### `nota_simulado` em escala 0-1

No CSV de simulado, a nota vem como proporcao (ex: 0.95 = 95%). Na formula, multiplique por 10 para equivaler a escala 0-10.

### `nota_projeto * 2`

Converte nota de projeto (0-5) para mesma escala das demais (0-10).

### `operacao vetorizada`

Aplica formula em coluna inteira de uma vez, sem loop.

### `.round(1)`

Arredonda media para uma casa decimal.

### Formula oficial

`(nota_simulado * 10 + nota_prova * 10 + nota_projeto * 2 * 5) / 25`

## Tarefas

1. Leia base_merged.csv.
2. Converta notas para float.
3. Calcule media com pesos 10/10/5 sobre 25.
4. Exiba resultado.

## Criterios de aceite

- Coluna media criada.
- Formula correta aplicada.
- Valores arredondados.

## Como executar

```bash
cd 15_pandas_media_ponderada
python main.py
```

## Referencia no projeto real

`src/consolidacao.py linhas 26-38`
