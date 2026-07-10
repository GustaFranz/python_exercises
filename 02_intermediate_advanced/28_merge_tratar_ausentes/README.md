# 28 - Merge: tratar registros ausentes

## Objetivo

Tratar dados ausentes com valor padrao e flags no merge.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Hospital Escola Vida |
| **Setor** | Saude / prontuario |
| **Solicitacao** | Cruzar pacientes com resultados de exame tratando ausencias. |

## Enunciado

pacientes = ["P001", "P002", "P003", "P004"]
resultados = {"P001": "normal", "P003": "atencao", "P005": "normal"}
Cruze pacientes com resultados.
Ausentes: resultado = "pendente", flag_ausente = True.
Presentes: flag_ausente = False.
Exiba relatorio e total pendentes.

## Como executar

```bash
cd "28_merge_tratar_ausentes"
python main.py
```
