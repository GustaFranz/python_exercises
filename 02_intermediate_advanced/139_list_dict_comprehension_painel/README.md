# 139 - List e dict comprehension: painel de desempenho

## Objetivo

Montar painel executivo combinando list comprehension (rankings) e dict comprehension (indices).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Consultoria MetaEdu |
| **Setor** | Consultoria educacional |
| **Solicitacao** | Consolidar desempenho por turma e listar turmas em atencao. |

## Enunciado

```python
turmas = [
    {"codigo": "7A", "alunos": 30, "aprovados": 24},
    {"codigo": "7B", "alunos": 28, "aprovados": 20},
    {"codigo": "8A", "alunos": 32, "aprovados": 30},
    {"codigo": "8B", "alunos": 27, "aprovados": 15},
]
META_APROVACAO = 75.0  # percentual
```

1) Com dict comprehension, calcule `taxas = {codigo: taxa_aprovacao}` em percentual (1 casa decimal).
2) Com list comprehension, gere `em_atencao = [codigo]` onde taxa < `META_APROVACAO`.
3) Com list comprehension, gere `destaques = [codigo]` onde taxa >= 90.0.
4) Com dict comprehension, monte `resumo = {codigo: "ok" if taxa >= META else "atencao"}`.
5) Exiba taxas, em_atencao, destaques e resumo ordenado por taxa (decrescente).

## Como executar

```bash
cd "139_list_dict_comprehension_painel"
python main.py
```
