# 09 - Pandas - Concatenar varios CSVs

## Demanda

O portal escolar gera um CSV por turma. A Coordenacao Pedagogica solicita uma base unica com todas as series para analise centralizada.

## Contexto do problema

Cada turma baixa seu arquivo separadamente. O proximo passo exige uma tabela so.

## Conceitos que voce vai usar

### `lista de DataFrames`

Cada arquivo lido vira um DataFrame; guardamos em uma lista antes de juntar.

### `pd.concat(lista, ignore_index=True)`

Empilha varios DataFrames verticalmente. `ignore_index=True` recria o indice 0, 1, 2...

### `loop + glob`

Padrao: listar arquivos, ler cada um, adicionar na lista, concatenar no final.

### `FileNotFoundError`

Excecao lancada quando nenhum arquivo e encontrado. Evita seguir com tabela vazia.

## Tarefas

1. Liste todos os `simulado_*.csv` na pasta dados.
2. Leia cada arquivo e acumule em uma lista.
3. Concatene com `pd.concat(..., ignore_index=True)`.
4. Exiba total de linhas e primeiras linhas.
5. Se nao houver arquivos, lance `FileNotFoundError` com mensagem clara.

## Criterios de aceite

- Tabela final tem linhas das 2 turmas.
- Indice reiniciado apos concat.
- Mensagem de erro se pasta vazia.

## Como executar

```bash
cd 09_pandas_concat_varios_csv
python main.py
```

## Referencia no projeto real

`src/leitor_simulados.py - funcao ler_simulados() completa`
