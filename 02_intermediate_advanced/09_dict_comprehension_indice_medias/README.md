# 09 - Dict comprehension: indice de desempenho e elegibilidade

## Objetivo

Montar indice de medias e filtro de elegibilidade com dict comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | RH Escolar Mais |
| **Setor** | Recursos humanos / gestao escolar |
| **Solicitacao** | Indice de media por matricula e lista de elegiveis ao bonus de desempenho. |

## Enunciado

registros = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5], "faltas": 2},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0], "faltas": 8},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
    {"id": 104, "nome": "Diego", "notas": [7.5, 7.0, 6.0], "faltas": 5},
]

1) `medias_por_id = {id: media}` com dict comprehension (media das notas).
2) `elegiveis = {id: media}` apenas quem tem media >= 7 **e** faltas <= 4
   (pode usar dict comprehension sobre `registros` ou filtrar o indice).
3) Relatorio: indice completo, elegiveis ao bonus, e ids fora da meta (media < 7).

## Como executar

```bash
cd "09_dict_comprehension_indice_medias"
python main.py
```
