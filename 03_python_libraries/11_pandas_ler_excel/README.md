# 11 - Pandas - Ler Excel com aba nomeada

## Demanda

Os professores enviam notas de prova em planilha Excel com aba especifica. Importe a aba correta e prepare os dados no formato longo.

## Contexto do problema

Diferente do CSV do portal, as provas chegam em Excel com aba 'Notas das Provas'.

## Conceitos que voce vai usar

### `pd.read_excel()`

Le arquivos .xlsx. Precisa da biblioteca openpyxl instalada.

### `sheet_name='Notas das Provas'`

Seleciona a aba pelo nome. Se errar, gera erro ou le aba errada.

### `openpyxl`

Motor que permite ao Pandas ler/escrever Excel moderno (.xlsx).

### `melt apos leitura`

Mesmo padrao do exercicio 10, agora com value_name='nota_prova'.

## Tarefas

1. Leia `dados/provas_7ano.xlsx`, aba 'Notas das Provas'.
2. Exiba colunas e primeiras linhas.
3. Aplique melt para formato longo com nota_prova.

## Criterios de aceite

- Aba correta lida.
- Formato longo com coluna nota_prova.
- Pelo menos 6 linhas no resultado.

## Como executar

```bash
cd 11_pandas_ler_excel
python main.py
```

## Referencia no projeto real

`src/leitor_provas.py`
