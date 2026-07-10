# 16 - Pandas - Regra de aprovacao

## Demanda

O sistema deve classificar cada registro como Aprovado ou Recuperacao conforme media minima 6.0.

## Contexto do problema

Apos calcular media, a escola precisa de situacao pedagogica automatica.

## Conceitos que voce vai usar

### `.apply(funcao)`

Aplica funcao linha a linha. Util para regras customizadas.

### `lambda media: ...`

Funcao anonima para condicao simples.

### `coluna derivada`

Nova coluna situacao baseada em media existente.

## Tarefas

1. Leia base_com_media.csv.
2. Crie coluna situacao com apply.
3. Conte quantos em cada situacao.

## Criterios de aceite

- Situacao Aprovado para media >= 6.
- Situacao Recuperacao para media < 6.

## Como executar

```bash
cd 16_pandas_regra_aprovacao
python main.py
```

## Referencia no projeto real

`src/consolidacao.py linhas 39-41`
