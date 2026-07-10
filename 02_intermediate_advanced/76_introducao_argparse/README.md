# 76 - Introducao ao argparse

## Objetivo

Criar CLI com argumentos --arquivo e --limite.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Script de linha de comando para processar exportacao de notas com parametros. |

## Visao do bloco (exercicios 76 a 80)

Topico **argparse**: interfaces de linha de comando profissionais.

| # | Foco |
|---|------|
| 76 | Introducao + --arquivo e --limite |
| 77 | Flags booleanas |
| 78 | Subcomando simples |
| 79 | CLI relatorio de notas |
| 80 | Ferramenta com 3 operacoes |

## Enunciado

- Configure argparse com --arquivo (obrigatorio) e --limite (padrao 10).
- Exiba os valores recebidos ao executar o script.

## Como executar

```bash
cd "76_introducao_argparse"
python main.py --arquivo notas.csv --limite 5
```
