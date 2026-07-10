# 08 - Pandas - Ler CSV de simulado

## Demanda

A Secretaria Escolar exportou o primeiro lote de notas de simulado em CSV. Antes de seguir o processamento, voce deve validar se o arquivo foi lido corretamente.

## Contexto do problema

Erros na leitura do CSV contaminam todo o fluxo de consolidacao. Esta etapa e a primeira inspecao de qualidade.

## Conceitos que voce vai usar

### `pd.read_csv(caminho)`

Le o arquivo CSV e retorna um DataFrame (tabela em memoria).

### `.head()`

Mostra as primeiras linhas. Util para conferir se a leitura funcionou.

### `.columns`

Lista os nomes das colunas. Ajuda a detectar nomes errados ou encoding incorreto.

### `.shape`

Tupla (linhas, colunas). Resume o tamanho da tabela.

### `.dtypes`

Mostra o tipo de cada coluna (object, float64, int64...).

### `.info()`

Resumo completo: colunas, tipos, valores nao nulos e uso de memoria.

## Tarefas

1. Leia `dados/simulado_7ano.csv` com `pd.read_csv`.
2. Exiba as 5 primeiras linhas.
3. Exiba nomes das colunas, shape e dtypes.

## Criterios de aceite

- DataFrame carregado sem erro.
- Saida mostra colunas turma, aluno e disciplinas.
- Shape indica 3 alunos e 5 colunas.

## Como executar

```bash
cd 08_pandas_ler_csv
python main.py
```

## Referencia no projeto real

`src/leitor_simulados.py - funcao ler_simulados(), pd.read_csv`
