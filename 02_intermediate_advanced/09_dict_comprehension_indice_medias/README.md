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

Dados de entrada:
```python
registros = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5], "faltas": 2},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0], "faltas": 8},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
    {"id": 104, "nome": "Diego", "notas": [7.5, 7.0, 6.0], "faltas": 5},
    {"id": 105, "nome": "Rodrigo", "notas": [8.5, 7.0, 9.0], "faltas": 5},
]
```

1) Monte `medias_por_id = {id: media}` com dict comprehension (`media = sum(notas) / len(notas)`).
2) Monte `elegiveis = {id: media}` com dict comprehension sobre `registros`, filtrando `media >= 7` **e** `faltas <= 4`.
3) Monte `fora_meta = {id: media for id, media in medias_por_id.items() if media < 7}`.
4) Exiba relatorio com: indice completo, elegiveis ao bonus e ids fora da meta.

Exemplo de saida:

```
Indice de medias: {101: 7.17, 102: 5.17, ...}
Elegiveis ao bonus: {101: ..., 103: ...}
Fora da meta: {102: 5.17, ...}
```

## Como executar

```bash
cd "09_dict_comprehension_indice_medias"
python main.py
```
