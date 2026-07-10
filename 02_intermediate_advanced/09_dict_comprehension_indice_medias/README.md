# 09 - Dict comprehension: indice de medias

## Objetivo

Criar indice aluno_id -> media com dict comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | RH Escolar Mais |
| **Setor** | Recursos humanos / gestao escolar |
| **Solicitacao** | Indice rapido de media por matricula para conferencia de bonus. |

## Enunciado

registros = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5]},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0]},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5]},
]
Crie medias_por_id = {id: media} usando dict comprehension.
Exiba o indice e destaque quem tem media >= 7.

## Como executar

```bash
cd "09_dict_comprehension_indice_medias"
python main.py
```
