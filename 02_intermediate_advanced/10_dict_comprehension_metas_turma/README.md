# 10 - Dict comprehension: plano de acao por turma

## Objetivo

Gerar plano de acao pedagogico com dict comprehension e regras compostas.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Consultoria MetaEdu |
| **Setor** | Consultoria educacional |
| **Solicitacao** | Classificar turmas do portfolio e montar backlog de intervencao. |

## Enunciado

turmas = {
    "9A": {"aprovacao": 72, "media": 7.1, "evasao": 3},
    "9B": {"aprovacao": 58, "media": 5.8, "evasao": 8},
    "9C": {"aprovacao": 81, "media": 8.0, "evasao": 2},
    "9D": {"aprovacao": 45, "media": 4.9, "evasao": 12},
}

Regra de prioridade (use dict comprehension + expressao condicional):
- `critica` se aprovacao < 50 **ou** evasao >= 10
- `atencao` se 50 <= aprovacao < 70
- `estavel` caso contrario

Ainda:
1) `prioridades = {turma: prioridade}` via dict comprehension.
2) `backlog = {turma: prioridade}` apenas `critica` e `atencao`.
3) Relatorio executivo: quantidade por prioridade e lista do backlog ordenada
   (critica primeiro).

## Como executar

```bash
cd "10_dict_comprehension_metas_turma"
python main.py
```
