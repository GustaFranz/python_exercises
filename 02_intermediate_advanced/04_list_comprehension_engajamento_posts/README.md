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

## Passo a passo

1. Crie a lista `posts` com os 5 dicionarios do enunciado.
2. Crie `scores` com list comprehension: para cada post, gere o dict `{"titulo": post["titulo"], "score": post["curtidas"] + post["compartilhamentos"] * 3}`.
3. Calcule `total_scores` com `sum(item["score"] for item in scores)`.
4. Crie `scores_com_taxa` com outra list comprehension: copie `titulo` e `score` e adicione a chave `"taxa"` com `round(score / total_scores * 100, 1)`; proteja contra divisao por zero com ternario (`... if total_scores > 0 else 0.0`).
5. Crie `top_3` com `sorted(scores_com_taxa, key=lambda x: x["score"], reverse=True)[:3]`.
6. Calcule `score_medio` dividindo `total_scores` pela quantidade de posts (arredonde com `round(..., 1)`).
7. Exiba o relatorio: total de posts, score medio e, para cada item do top 3, posicao (use `enumerate(top_3, 1)`), titulo, score e taxa %.

## Como executar

```bash
cd "04_list_comprehension_engajamento_posts"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Backlog editorial enviado pela EduConnect (enunciado)
posts = [
    {"titulo": "Feira de Ciencias", "curtidas": 120, "compartilhamentos": 15},
    {"titulo": "Aviso Prova", "curtidas": 45, "compartilhamentos": 2},
    {"titulo": "Projeto Leitura", "curtidas": 200, "compartilhamentos": 40},
    {"titulo": "Recesso", "curtidas": 30, "compartilhamentos": 1},
    {"titulo": "Hackathon", "curtidas": 90, "compartilhamentos": 12},
]

# Passo 1: comprehension monta um dict novo por post com o score ponderado
# (1 compartilhamento vale por 3 curtidas)
scores = [
    {"titulo": post["titulo"],
     "score": post["curtidas"] + post["compartilhamentos"] * 3}
    for post in posts
]

# Passo 2a: soma de todos os scores (base da taxa percentual)
total_scores = sum(item["score"] for item in scores)

# Passo 2b: nova comprehension adiciona a taxa % de cada post sobre o total;
# o ternario evita divisao por zero se o lote vier vazio de engajamento
scores_com_taxa = [
    {"titulo": item["titulo"],
     "score": item["score"],
     "taxa": round(item["score"] / total_scores * 100, 1) if total_scores > 0 else 0.0}
    for item in scores
]

# Passo 3: ordena do maior score para o menor e fatia os 3 primeiros
top_3 = sorted(scores_com_taxa, key=lambda x: x["score"], reverse=True)[:3]

# Passo 4: indicadores gerais do relatorio
total_posts = len(posts)
score_medio = round(total_scores / total_posts, 1) if total_posts > 0 else 0.0

print("=== RELATORIO DE ENGAJAMENTO EDITORIAL ===")
print(f"Total de posts analisados: {total_posts}")
print(f"Score medio da pagina:     {score_medio}")
print("--- TOP 3 PARA O FEED DE DESTAQUE ---")
# enumerate a partir de 1 gera a posicao do ranking sem contador manual
for posicao, post in enumerate(top_3, 1):
    print(f'{posicao}o | {post["titulo"]:<20} | score: {post["score"]:>3} | taxa: {post["taxa"]}%')
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Ranking de engajamento editorial da EduConnect."""

from operator import itemgetter

# Regras de negocio como constantes: peso do compartilhamento e tamanho do top N
PESO_COMPARTILHAMENTO = 3
TAMANHO_TOP = 3


def calcular_score(post: dict) -> int:
    """Score ponderado: curtidas + compartilhamentos * peso."""
    return post["curtidas"] + post["compartilhamentos"] * PESO_COMPARTILHAMENTO


def montar_ranking(posts: list[dict]) -> list[dict]:
    """Devolve os posts enriquecidos com score e taxa %, ordenados por score."""
    # Enriquecimento em uma passagem: titulo + score calculado
    scores = [{"titulo": p["titulo"], "score": calcular_score(p)} for p in posts]

    # Total geral: base para a taxa relativa de cada post
    total = sum(item["score"] for item in scores)

    # Adiciona a taxa % com protecao contra total zero (guard no ternario)
    com_taxa = [
        {**item, "taxa": round(item["score"] / total * 100, 1) if total else 0.0}
        for item in scores
    ]

    # itemgetter e mais rapido e declarativo que lambda para ordenar por chave
    return sorted(com_taxa, key=itemgetter("score"), reverse=True)


def main() -> None:
    # Dados de entrada do enunciado
    posts = [
        {"titulo": "Feira de Ciencias", "curtidas": 120, "compartilhamentos": 15},
        {"titulo": "Aviso Prova", "curtidas": 45, "compartilhamentos": 2},
        {"titulo": "Projeto Leitura", "curtidas": 200, "compartilhamentos": 40},
        {"titulo": "Recesso", "curtidas": 30, "compartilhamentos": 1},
        {"titulo": "Hackathon", "curtidas": 90, "compartilhamentos": 12},
    ]

    # Ranking completo ja ordenado; o top N e apenas uma fatia
    ranking = montar_ranking(posts)
    top = ranking[:TAMANHO_TOP]

    # Indicadores agregados do relatorio
    total_scores = sum(item["score"] for item in ranking)
    score_medio = round(total_scores / len(posts), 1) if posts else 0.0

    print("=== RELATORIO DE ENGAJAMENTO EDITORIAL ===")
    print(f"Total de posts analisados: {len(posts)}")
    print(f"Score medio da pagina:     {score_medio}")
    print(f"--- TOP {TAMANHO_TOP} PARA O FEED DE DESTAQUE ---")
    for posicao, post in enumerate(top, 1):
        print(f'{posicao}o | {post["titulo"]:<20} | score: {post["score"]:>3} | taxa: {post["taxa"]}%')


if __name__ == "__main__":
    main()
```

</details>
