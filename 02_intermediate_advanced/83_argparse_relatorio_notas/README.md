# 83 - Argparse: relatorio de notas

## Objetivo

CLI aplicada para gerar relatorio a partir de arquivo e media minima.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Ferramenta de linha de comando para filtrar alunos aprovados em CSV. |

## Enunciado

Configure argparse:

- `--entrada` (str): arquivo CSV com colunas `nome,nota`
- `--corte` (float, padrao `7.0`): nota minima para aprovacao

CSV de exemplo (crie `notas.csv` no inicio do script se nao existir):

```csv
nome,nota
Ana,8.5
Bruno,6.0
Carla,9.0
```

No `main`:

1) Leia o CSV com modulo `csv`.
2) Filtre alunos com nota >= corte.
3) Exiba quantidade e nomes dos aprovados.

Exemplo de execucao:

```bash
python main.py --entrada notas.csv --corte 7.0
```

Exemplo de saida:

```
Aprovados (corte 7.0): 2
- Ana
- Carla
```

## Como executar

```bash
cd "83_argparse_relatorio_notas"
python main.py --entrada notas.csv --corte 7.0
```
