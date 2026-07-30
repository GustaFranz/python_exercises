# 04 - List comprehension: ranking de engajamento

## Objetivo

Montar ranking comercial de posts com list comprehension e metricas.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Rede Social EduConnect |
| **Setor** | Midia / comunicacao escolar |
| **Solicitacao** | Priorizar posts do backlog editorial pelo engajamento relativo ao total. |

## Enunciado

posts = [
    {"titulo": "Feira de Ciencias", "curtidas": 120, "compartilhamentos": 15},
    {"titulo": "Aviso Prova", "curtidas": 45, "compartilhamentos": 2},
    {"titulo": "Projeto Leitura", "curtidas": 200, "compartilhamentos": 40},
    {"titulo": "Recesso", "curtidas": 30, "compartilhamentos": 1},
    {"titulo": "Hackathon", "curtidas": 90, "compartilhamentos": 12},
]

Score de engajamento: `curtidas + (compartilhamentos * 3)`.

1) Gere `scores` com list comprehension: lista de dicts `{titulo, score}`.
2) Calcule o total de scores e, com outra comprehension, a taxa percentual de cada post.
3) Filtre o top 3 (maior score) para o feed de destaque.
4) Exiba relatorio: total de posts, score medio, top 3 com titulo, score e taxa %.

Use list comprehension nos passos 1 e 2. Ordenacao do top 3 pode usar `sorted`.

## Como executar

```bash
cd "04_list_comprehension_engajamento_posts"
python main.py
```
