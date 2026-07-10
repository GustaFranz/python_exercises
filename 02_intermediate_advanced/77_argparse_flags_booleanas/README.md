# 77 - Argparse: flags booleanas

## Objetivo

Usar store_true para flags opcionais na CLI.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / deploy |
| **Solicitacao** | Script de deploy com modo verbose e simulacao dry-run. |

## Enunciado

- Adicione flags --verbose e --dry-run com action=store_true.
- Exiba mensagem conforme combinacao de flags.

## Como executar

```bash
cd "77_argparse_flags_booleanas"
python main.py --verbose --dry-run
```
