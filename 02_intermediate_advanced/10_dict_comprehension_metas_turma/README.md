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

## Passo a passo

1. Crie o dicionario `turmas` com os 4 registros do enunciado.
2. Defina a funcao auxiliar `classificar(indicadores)` que recebe o dict de uma turma e retorna a prioridade usando `if/elif/else`: `"critica"` se `aprovacao < 50 or evasao >= 10`; `"atencao"` se `50 <= aprovacao < 70`; `"estavel"` nos demais casos. Atencao a ordem: a regra critica deve ser testada primeiro (a turma 9D tem aprovacao 45 E evasao 12).
3. Crie `prioridades` com dict comprehension sobre `turmas.items()`: `{turma: classificar(dados) for turma, dados in turmas.items()}`.
4. Crie `backlog` com outra dict comprehension filtrando `prioridades.items()`: so entram pares cuja prioridade e diferente de `"estavel"`.
5. Conte quantas turmas ha em cada prioridade (use `sum(1 for p in prioridades.values() if p == ...)` ou um dict de contagem).
6. Ordene o backlog com `sorted(backlog.items(), key=lambda item: 0 if item[1] == "critica" else 1)` para exibir criticas primeiro.
7. Exiba o relatorio executivo: quantidade por prioridade e o backlog ordenado, uma turma por linha.

## Como executar

```bash
cd "10_dict_comprehension_metas_turma"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Indicadores do portfolio de turmas (enunciado)
turmas = {
    "9A": {"aprovacao": 72, "media": 7.1, "evasao": 3},
    "9B": {"aprovacao": 58, "media": 5.8, "evasao": 8},
    "9C": {"aprovacao": 81, "media": 8.0, "evasao": 2},
    "9D": {"aprovacao": 45, "media": 4.9, "evasao": 12},
}


def classificar(dados):
    """Aplica a regra de prioridade da consultoria a uma turma.

    A regra critica vem primeiro: se aprovacao esta abaixo de 50
    OU a evasao passou de 10, nada mais importa — e intervencao urgente.
    """
    if dados["aprovacao"] < 50 or dados["evasao"] >= 10:
        return "critica"
    if 50 <= dados["aprovacao"] < 70:
        return "atencao"
    return "estavel"


# 1) Dict comprehension aplica a classificacao em todas as turmas
prioridades = {turma: classificar(dados) for turma, dados in turmas.items()}

# 2) Backlog: filtra fora as turmas estaveis (nao precisam de intervencao)
backlog = {turma: p for turma, p in prioridades.items() if p != "estavel"}

# 3a) Contagem por prioridade com generator expressions
qtd_critica = sum(1 for p in prioridades.values() if p == "critica")
qtd_atencao = sum(1 for p in prioridades.values() if p == "atencao")
qtd_estavel = sum(1 for p in prioridades.values() if p == "estavel")

# 3b) Ordena o backlog: critica (0) vem antes de atencao (1)
backlog_ordenado = sorted(backlog.items(), key=lambda item: 0 if item[1] == "critica" else 1)

print("=== PLANO DE ACAO POR TURMA ===")
print(f"Criticas: {qtd_critica} | Atencao: {qtd_atencao} | Estaveis: {qtd_estavel}")
print("--- BACKLOG DE INTERVENCAO (critica primeiro) ---")
for turma, prioridade in backlog_ordenado:
    print(f"  {turma}: {prioridade}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Classificacao de turmas e backlog de intervencao da consultoria."""

from collections import Counter

# Limiares da regra de negocio no topo do modulo
APROVACAO_CRITICA = 50
APROVACAO_ESTAVEL = 70
EVASAO_CRITICA = 10

# Ordem de severidade usada para ordenar o backlog (menor = mais urgente)
SEVERIDADE = {"critica": 0, "atencao": 1, "estavel": 2}


def classificar(dados: dict) -> str:
    """Prioridade da turma com guard clauses, da regra mais grave para a mais leve."""
    if dados["aprovacao"] < APROVACAO_CRITICA or dados["evasao"] >= EVASAO_CRITICA:
        return "critica"
    if dados["aprovacao"] < APROVACAO_ESTAVEL:
        return "atencao"
    return "estavel"


def main() -> None:
    # Dados de entrada do enunciado
    turmas = {
        "9A": {"aprovacao": 72, "media": 7.1, "evasao": 3},
        "9B": {"aprovacao": 58, "media": 5.8, "evasao": 8},
        "9C": {"aprovacao": 81, "media": 8.0, "evasao": 2},
        "9D": {"aprovacao": 45, "media": 4.9, "evasao": 12},
    }

    # Classificacao de todas as turmas em uma comprehension
    prioridades = {turma: classificar(dados) for turma, dados in turmas.items()}

    # Backlog: apenas turmas que exigem intervencao
    backlog = {turma: p for turma, p in prioridades.items() if p != "estavel"}

    # Counter resume a distribuicao por prioridade em uma passagem
    resumo = Counter(prioridades.values())

    # Ordena pelo mapa de severidade: critica antes de atencao
    backlog_ordenado = sorted(backlog.items(), key=lambda item: SEVERIDADE[item[1]])

    print("=== PLANO DE ACAO POR TURMA ===")
    print(
        f"Criticas: {resumo.get('critica', 0)} | "
        f"Atencao: {resumo.get('atencao', 0)} | "
        f"Estaveis: {resumo.get('estavel', 0)}"
    )
    print("--- BACKLOG DE INTERVENCAO (critica primeiro) ---")
    for turma, prioridade in backlog_ordenado:
        print(f"  {turma}: {prioridade}")


if __name__ == "__main__":
    main()
```

</details>
