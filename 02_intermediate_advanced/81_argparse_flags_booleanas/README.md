# 81 - Argparse: flags booleanas

## Objetivo

Usar store_true para flags opcionais na CLI.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / deploy |
| **Solicitacao** | Script de deploy com modo verbose e simulacao dry-run. |

## Enunciado

Configure argparse com flags booleanas:

- `--verbose` (`action="store_true"`)
- `--dry-run` (`action="store_true"`)

No `main`, exiba mensagens conforme flags:

- Se `--verbose`: `"Modo detalhado ativo"`
- Se `--dry-run`: `"Simulacao — nenhuma alteracao aplicada"`
- Se nenhuma flag: `"Execucao padrao"`

Exemplo de execucao:

```bash
python main.py --verbose --dry-run
```

Exemplo de saida:

```
Modo detalhado ativo
Simulacao — nenhuma alteracao aplicada
```

## Como executar

```bash
cd "81_argparse_flags_booleanas"
python main.py --verbose --dry-run
```
