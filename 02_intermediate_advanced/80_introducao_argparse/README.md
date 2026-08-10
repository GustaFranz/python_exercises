# 80 - Introducao ao argparse

## Objetivo

Criar CLI com argumentos --arquivo e --limite.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Script de linha de comando para processar exportacao de notas com parametros. |

## Visao do bloco (exercicios 80 a 84)

Topico **argparse**: interfaces de linha de comando profissionais.

| # | Foco |
|---|------|
| 80 | Introducao + --arquivo e --limite |
| 81 | Flags booleanas |
| 82 | Subcomando simples |
| 83 | CLI relatorio de notas |
| 84 | Ferramenta com 3 operacoes |

## Enunciado

Configure argparse com:

- `--arquivo` (str, obrigatorio): caminho do arquivo de entrada
- `--limite` (int, padrao `10`): maximo de linhas a processar

No `main`:

1) Parse os argumentos.
2) Exiba os valores recebidos.

Exemplo de execucao:

```bash
python main.py --arquivo notas.csv --limite 5
```

Exemplo de saida:

```
Arquivo: notas.csv
Limite: 5
```

## Como executar

```bash
cd "80_introducao_argparse"
python main.py --arquivo notas.csv --limite 5
```
