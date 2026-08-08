# 137 - List e dict comprehension: boletim da turma

## Objetivo

Combinar list comprehension e dict comprehension a partir da mesma fonte de dados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Colegio Horizonte |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Gerar lista de aprovados e indice de medias por matricula. |

## Visao do bloco (exercicios 137 a 139)

Topico **list + dict comprehension**: duas visoes complementares sobre os mesmos registros.

| # | Nivel | Foco |
|---|-------|------|
| 137 | Ponte | Boletim: aprovados + indice de medias |
| 138 | Entrevista | Estoque critico: alertas + mapa de quantidades |
| 139 | Entrevista | Painel de desempenho por turma |

## Enunciado

```python
alunos = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5]},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0]},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5]},
    {"id": 104, "nome": "Diego", "notas": [6.0, 7.0, 5.5]},
]
NOTA_APROVACAO = 6.0
```

1) Com dict comprehension, monte `medias = {id: media}` (media aritmetica das notas).
2) Com list comprehension, gere `aprovados = [nome]` onde media >= `NOTA_APROVACAO`.
3) Com dict comprehension, monte `recuperacao = {id: media}` apenas para quem ficou abaixo da meta.
4) Exiba medias, aprovados, recuperacao e taxa de aprovacao (%).

## Como executar

```bash
cd "137_list_dict_comprehension_boletim"
python main.py
```
