# 10 - Pandas - Melt (formato longo)

## Demanda

Os professores precisam analisar notas por disciplina, mas o CSV chega com cada disciplina em uma coluna separada. Transforme para formato longo.

## Contexto do problema

O merge entre fontes exige que disciplina seja uma linha, nao uma coluna.

## Conceitos que voce vai usar

### `formato largo`

Cada disciplina e uma coluna. Facil para humanos lerem, dificil para cruzar dados.

### `formato longo`

Cada linha e uma combinacao turma+aluno+disciplina. Ideal para merge e groupby.

### `melt()`

Transforma colunas em linhas. `id_vars` ficam fixas; demais viram pares variavel/valor.

### `id_vars=['turma','aluno']`

Colunas que identificam o registro e nao serao derretidas.

### `var_name='disciplina'`

Nome da nova coluna que guarda o nome da disciplina.

### `value_name='nota_simulado'`

Nome da nova coluna que guarda a nota.

## Tarefas

1. Leia o CSV em formato largo.
2. Aplique melt com id_vars, var_name e value_name corretos.
3. Exiba o resultado (head() ou todas as linhas).

## Criterios de aceite

- Colunas finais: turma, aluno, disciplina, nota_simulado.
- Cada disciplina virou varias linhas.

## Como executar

```bash
cd 10_pandas_melt_formato_longo
python main.py
```

## Referencia no projeto real

`src/leitor_simulados.py - transformar_simulados_para_longo()`
