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

## Passo a passo

1. Crie `turmas` e `META_APROVACAO` conforme o enunciado.
2. Calcule as taxas com dict comprehension: `taxas = {t["codigo"]: round(t["aprovados"] / t["alunos"] * 100, 1) for t in turmas}`.
3. Gere `em_atencao` com list comprehension sobre `taxas.items()`: codigos com `taxa < META_APROVACAO`.
4. Gere `destaques` da mesma forma, com `taxa >= 90.0`.
5. Monte `resumo` com dict comprehension usando if/else no valor: `{c: "ok" if taxa >= META_APROVACAO else "atencao" for c, taxa in taxas.items()}`.
6. Para exibir ordenado por taxa decrescente, use `sorted(taxas.items(), key=lambda item: item[1], reverse=True)` e imprima uma linha por turma com taxa e status do resumo.

## Como executar

```bash
cd "139_list_dict_comprehension_painel"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
turmas = [
    {"codigo": "7A", "alunos": 30, "aprovados": 24},
    {"codigo": "7B", "alunos": 28, "aprovados": 20},
    {"codigo": "8A", "alunos": 32, "aprovados": 30},
    {"codigo": "8B", "alunos": 27, "aprovados": 15},
]
META_APROVACAO = 75.0  # percentual minimo aceitavel
TAXA_DESTAQUE = 90.0   # percentual para entrar nos destaques

# dict comprehension: taxa de aprovacao em % com 1 casa decimal
taxas = {t["codigo"]: round(t["aprovados"] / t["alunos"] * 100, 1) for t in turmas}

# list comprehensions sobre o dict ja calculado: duas visoes dos mesmos dados
em_atencao = [codigo for codigo, taxa in taxas.items() if taxa < META_APROVACAO]
destaques = [codigo for codigo, taxa in taxas.items() if taxa >= TAXA_DESTAQUE]

# dict comprehension com if/else no valor: classifica cada turma
resumo = {codigo: "ok" if taxa >= META_APROVACAO else "atencao" for codigo, taxa in taxas.items()}

print(f"Taxas: {taxas}")
print(f"Em atencao (< {META_APROVACAO}%): {em_atencao}")
print(f"Destaques (>= {TAXA_DESTAQUE}%): {destaques}")

# sorted sobre items() com key no valor: painel do maior para o menor
print("\n=== Painel (ordenado por taxa) ===")
for codigo, taxa in sorted(taxas.items(), key=lambda item: item[1], reverse=True):
    print(f"{codigo}: {taxa}% [{resumo[codigo]}]")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Painel executivo de desempenho por turma."""

from operator import itemgetter

TURMAS = [
    {"codigo": "7A", "alunos": 30, "aprovados": 24},
    {"codigo": "7B", "alunos": 28, "aprovados": 20},
    {"codigo": "8A", "alunos": 32, "aprovados": 30},
    {"codigo": "8B", "alunos": 27, "aprovados": 15},
]
META_APROVACAO = 75.0
TAXA_DESTAQUE = 90.0


def taxa_aprovacao(turma: dict) -> float:
    """Percentual de aprovados com 1 casa decimal."""
    return round(turma["aprovados"] / turma["alunos"] * 100, 1)


def main() -> None:
    taxas = {t["codigo"]: taxa_aprovacao(t) for t in TURMAS}

    em_atencao = [c for c, taxa in taxas.items() if taxa < META_APROVACAO]
    destaques = [c for c, taxa in taxas.items() if taxa >= TAXA_DESTAQUE]
    resumo = {c: "ok" if taxa >= META_APROVACAO else "atencao" for c, taxa in taxas.items()}

    print(f"Taxas: {taxas}")
    print(f"Em atencao (< {META_APROVACAO}%): {em_atencao}")
    print(f"Destaques (>= {TAXA_DESTAQUE}%): {destaques}")

    print("\n=== Painel (ordenado por taxa) ===")
    # itemgetter(1) pega a taxa (segundo elemento do par) para ordenar
    for codigo, taxa in sorted(taxas.items(), key=itemgetter(1), reverse=True):
        print(f"{codigo}: {taxa}% [{resumo[codigo]}]")


if __name__ == "__main__":
    main()
```

</details>
