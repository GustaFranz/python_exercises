# 27 - Merge: left join simples

## Objetivo

Simular left join mantendo todos os registros da fonte principal.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Dados educacionais |
| **Solicitacao** | Manter todos os alunos da turma mesmo sem nota lancada. |

## Enunciado

turma = [
    {"matricula": "A01", "nome": "Ana"},
    {"matricula": "A02", "nome": "Bruno"},
    {"matricula": "A03", "nome": "Carla"},
]
notas = {"A01": 7.5, "A03": 8.0}
Faca left join: todos da turma + nota (ou "sem nota").
Exiba tabela matricula | nome | nota.

## Como executar

```bash
cd "27_merge_left_join_simples"
python main.py
```
