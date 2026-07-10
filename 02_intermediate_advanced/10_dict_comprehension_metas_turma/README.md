# 10 - Dict comprehension: metas por turma

## Objetivo

Aplicar regras condicionais em dict comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Consultoria MetaEdu |
| **Setor** | Consultoria educacional |
| **Solicitacao** | Definir meta de aprovacao personalizada por desempenho atual da turma. |

## Enunciado

turmas = {"9A": 72, "9B": 58, "9C": 81, "9D": 45}  # % aprovacao atual
Regra de meta:
- Se aprovacao >= 70: meta = "manter"
- Se 50 <= aprovacao < 70: meta = "reforcar"
- Se aprovacao < 50: meta = "intervencao"
Gere metas com dict comprehension e exiba relatorio por turma.

## Como executar

```bash
cd "10_dict_comprehension_metas_turma"
python main.py
```
