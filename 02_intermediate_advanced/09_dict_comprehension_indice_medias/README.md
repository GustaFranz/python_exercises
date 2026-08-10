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

## Passo a passo

1. Crie a lista `registros` com os 5 dicionarios do enunciado.
2. Defina as constantes `MEDIA_MINIMA = 7.0` e `FALTAS_MAXIMAS = 4` no topo.
3. Crie `medias_por_id` com dict comprehension sobre `registros`: chave `r["id"]`, valor `round(sum(r["notas"]) / len(r["notas"]), 2)`.
4. Crie `elegiveis` com outra dict comprehension sobre `registros`, com filtro composto no `if`: a media do registro deve ser `>= MEDIA_MINIMA` **e** `r["faltas"] <= FALTAS_MAXIMAS`. Dica: para nao calcular a media duas vezes, reutilize `medias_por_id[r["id"]]` no filtro e no valor.
5. Crie `fora_meta` com dict comprehension sobre `medias_por_id.items()`, filtrando `media < MEDIA_MINIMA`.
6. Exiba o relatorio em tres linhas: indice completo (`medias_por_id`), elegiveis ao bonus (`elegiveis`) e fora da meta (`fora_meta`).

## Como executar

```bash
cd "09_dict_comprehension_indice_medias"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Registros de matricula enviados pelo RH (enunciado)
registros = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5], "faltas": 2},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0], "faltas": 8},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
    {"id": 104, "nome": "Diego", "notas": [7.5, 7.0, 6.0], "faltas": 5},
    {"id": 105, "nome": "Rodrigo", "notas": [8.5, 7.0, 9.0], "faltas": 5},
]

# Regras de elegibilidade como constantes: criterio visivel no topo
MEDIA_MINIMA = 7.0
FALTAS_MAXIMAS = 4

# 1) Indice id -> media: dict comprehension calcula a media de cada registro
medias_por_id = {
    r["id"]: round(sum(r["notas"]) / len(r["notas"]), 2)
    for r in registros
}

# 2) Elegiveis: filtro composto (media E faltas); consultamos o indice
# ja calculado para nao somar as notas de novo
elegiveis = {
    r["id"]: medias_por_id[r["id"]]
    for r in registros
    if medias_por_id[r["id"]] >= MEDIA_MINIMA and r["faltas"] <= FALTAS_MAXIMAS
}

# 3) Fora da meta: filtro simples sobre o proprio indice de medias
fora_meta = {id_: media for id_, media in medias_por_id.items() if media < MEDIA_MINIMA}

# 4) Relatorio nas tres visoes pedidas
print("Indice de medias:  ", medias_por_id)
print("Elegiveis ao bonus:", elegiveis)
print("Fora da meta:      ", fora_meta)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Indice de medias por matricula e elegibilidade ao bonus de desempenho."""

from statistics import fmean

# Criterios de negocio centralizados
MEDIA_MINIMA = 7.0
FALTAS_MAXIMAS = 4


def calcular_medias(registros: list[dict]) -> dict[int, float]:
    """Monta o indice id -> media com 2 casas decimais.

    fmean e a media aritmetica da stdlib: mais clara que sum/len
    e ja levanta erro em lista vazia (falha cedo).
    """
    return {r["id"]: round(fmean(r["notas"]), 2) for r in registros}


def filtrar_elegiveis(registros: list[dict], medias: dict[int, float]) -> dict[int, float]:
    """Elegivel ao bonus: media >= minima E faltas <= maximo."""
    return {
        r["id"]: medias[r["id"]]
        for r in registros
        if medias[r["id"]] >= MEDIA_MINIMA and r["faltas"] <= FALTAS_MAXIMAS
    }


def main() -> None:
    # Dados de entrada do enunciado
    registros = [
        {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5], "faltas": 2},
        {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0], "faltas": 8},
        {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5], "faltas": 1},
        {"id": 104, "nome": "Diego", "notas": [7.5, 7.0, 6.0], "faltas": 5},
        {"id": 105, "nome": "Rodrigo", "notas": [8.5, 7.0, 9.0], "faltas": 5},
    ]

    # Indice base de medias, calculado uma unica vez
    medias_por_id = calcular_medias(registros)

    # Visoes derivadas: elegiveis (regra composta) e fora da meta (media baixa)
    elegiveis = filtrar_elegiveis(registros, medias_por_id)
    fora_meta = {id_: m for id_, m in medias_por_id.items() if m < MEDIA_MINIMA}

    # Relatorio executivo nas tres visoes pedidas
    print("Indice de medias:  ", medias_por_id)
    print("Elegiveis ao bonus:", elegiveis)
    print("Fora da meta:      ", fora_meta)


if __name__ == "__main__":
    main()
```

</details>
