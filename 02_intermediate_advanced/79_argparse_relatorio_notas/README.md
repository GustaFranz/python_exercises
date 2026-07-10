# 79 - Argparse: relatorio de notas

## Objetivo

CLI aplicada para gerar relatorio a partir de arquivo e media minima.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Ferramenta de linha de comando para filtrar alunos aprovados em CSV. |

## Enunciado

- Configure --entrada e --corte (padrao 7.0).
- Leia CSV, filtre aprovados e exiba quantidade e nomes.

## Como executar

```bash
cd "79_argparse_relatorio_notas"
python main.py --entrada notas.csv --corte 7.0
```
