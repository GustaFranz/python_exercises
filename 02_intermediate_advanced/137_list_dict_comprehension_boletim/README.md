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

## Passo a passo

1. Crie `alunos` e `NOTA_APROVACAO` conforme o enunciado.
2. Monte as medias com dict comprehension: `medias = {a["id"]: round(sum(a["notas"]) / len(a["notas"]), 2) for a in alunos}` — a chave e o id, o valor e a media.
3. Gere os aprovados com list comprehension consultando o dict recem-criado: `aprovados = [a["nome"] for a in alunos if medias[a["id"]] >= NOTA_APROVACAO]`.
4. Monte a recuperacao com dict comprehension sobre `medias.items()`: `recuperacao = {i: m for i, m in medias.items() if m < NOTA_APROVACAO}`.
5. Calcule a taxa de aprovacao: `len(aprovados) / len(alunos) * 100`.
6. Exiba as quatro informacoes: medias, aprovados, recuperacao e taxa formatada com 1 casa decimal.

## Como executar

```bash
cd "137_list_dict_comprehension_boletim"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
alunos = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5]},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0]},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5]},
    {"id": 104, "nome": "Diego", "notas": [6.0, 7.0, 5.5]},
]
NOTA_APROVACAO = 6.0

# dict comprehension: id vira chave, media aritmetica vira valor
medias = {a["id"]: round(sum(a["notas"]) / len(a["notas"]), 2) for a in alunos}

# list comprehension consultando o dict de medias pelo id do aluno
aprovados = [a["nome"] for a in alunos if medias[a["id"]] >= NOTA_APROVACAO]

# dict comprehension com filtro: so entra quem ficou abaixo da meta
recuperacao = {id_aluno: media for id_aluno, media in medias.items() if media < NOTA_APROVACAO}

# Taxa em percentual: aprovados sobre o total da turma
taxa_aprovacao = len(aprovados) / len(alunos) * 100

print(f"Medias: {medias}")
print(f"Aprovados: {aprovados}")
print(f"Recuperacao: {recuperacao}")
print(f"Taxa de aprovacao: {taxa_aprovacao:.1f}%")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Boletim da turma: medias, aprovados e recuperacao."""

from statistics import fmean

ALUNOS = [
    {"id": 101, "nome": "Ana", "notas": [7.0, 8.0, 6.5]},
    {"id": 102, "nome": "Bruno", "notas": [5.0, 4.5, 6.0]},
    {"id": 103, "nome": "Carla", "notas": [9.0, 8.5, 9.5]},
    {"id": 104, "nome": "Diego", "notas": [6.0, 7.0, 5.5]},
]
NOTA_APROVACAO = 6.0


def main() -> None:
    # fmean e a media da stdlib: mais clara que sum/len
    medias = {a["id"]: round(fmean(a["notas"]), 2) for a in ALUNOS}

    aprovados = [a["nome"] for a in ALUNOS if medias[a["id"]] >= NOTA_APROVACAO]
    recuperacao = {id_: media for id_, media in medias.items() if media < NOTA_APROVACAO}
    taxa_aprovacao = len(aprovados) / len(ALUNOS) * 100

    print(f"Medias: {medias}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperacao: {recuperacao}")
    print(f"Taxa de aprovacao: {taxa_aprovacao:.1f}%")


if __name__ == "__main__":
    main()
```

</details>
