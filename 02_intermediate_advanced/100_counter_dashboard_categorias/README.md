# 100 - Counter: dashboard textual para standup

## Objetivo

Montar dashboard textual de alertas por categoria com percentuais e destaque de gargalo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / NOC |
| **Solicitacao** | Painel rapido de alertas por tipo para reuniao diaria de status (standup). |

## Enunciado

Eventos do turno:

```python
eventos = ["cpu", "disco", "cpu", "rede", "cpu", "disco", "memoria", "cpu", "rede", "cpu"]
```

Implemente:

1) `montar_contador(eventos) -> Counter`
2) `calcular_percentual(qtd, total) -> float` — 1 casa decimal
3) `identificar_gargalo(contador) -> tuple[str, int]` — categoria com maior volume
4) `gerar_dashboard(eventos) -> str` — string multilinha para o standup

Formato esperado do dashboard:

```
=== Dashboard de alertas — turno manha ===
cpu: 5 (50.0%)
disco: 2 (20.0%)
rede: 2 (20.0%)
memoria: 1 (10.0%)
Total: 10 eventos
Gargalo: cpu (5 eventos)
```

Ordene categorias por volume decrescente. O `main` deve imprimir o dashboard retornado.

## Passo a passo

1. Importe `Counter` com `from collections import Counter` e defina a lista `EVENTOS` do enunciado.
2. Defina `montar_contador(eventos)` que retorna `Counter(eventos)`.
3. Defina `calcular_percentual(qtd, total)` que retorna `round(qtd / total * 100, 1)` — divisao pelo total vezes 100, arredondada para 1 casa.
4. Defina `identificar_gargalo(contador)` que:
   - Usa `contador.most_common(1)[0]` para pegar a tupla `(categoria, quantidade)` do topo.
   - Retorna essa tupla.
5. Defina `gerar_dashboard(eventos)` que:
   - Monta o contador e calcula `total = len(eventos)`.
   - Cria uma lista `linhas` comecando com o cabecalho `"=== Dashboard de alertas — turno manha ==="`.
   - Percorre `contador.most_common()` (ja ordena por volume decrescente) adicionando uma linha `f"{categoria}: {qtd} ({percentual}%)"` para cada categoria, usando `calcular_percentual`.
   - Adiciona a linha `f"Total: {total} eventos"`.
   - Chama `identificar_gargalo` e adiciona `f"Gargalo: {categoria} ({qtd} eventos)"`.
   - Retorna as linhas unidas com `"\n".join(linhas)` — a funcao retorna a string, nao imprime.
6. No `main`, imprima o retorno de `gerar_dashboard(EVENTOS)` e confira com o formato esperado.

## Como executar

```bash
cd "100_counter_dashboard_categorias"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from collections import Counter

# Alertas registrados no turno da manha
EVENTOS = ["cpu", "disco", "cpu", "rede", "cpu", "disco", "memoria", "cpu", "rede", "cpu"]


def montar_contador(eventos):
    # Counter conta quantos alertas cada categoria gerou
    return Counter(eventos)


def calcular_percentual(qtd, total):
    # Participacao da categoria no total, com 1 casa decimal
    return round(qtd / total * 100, 1)


def identificar_gargalo(contador):
    # most_common(1)[0] devolve a tupla (categoria, qtd) com maior volume
    return contador.most_common(1)[0]


def gerar_dashboard(eventos):
    contador = montar_contador(eventos)
    total = len(eventos)

    # Monta as linhas em lista e junta tudo no final
    linhas = ["=== Dashboard de alertas — turno manha ==="]

    # most_common() ja entrega as categorias em ordem decrescente
    for categoria, qtd in contador.most_common():
        percentual = calcular_percentual(qtd, total)
        linhas.append(f"{categoria}: {qtd} ({percentual}%)")

    linhas.append(f"Total: {total} eventos")

    # Destaca a categoria que mais gerou alertas no turno
    categoria_top, qtd_top = identificar_gargalo(contador)
    linhas.append(f"Gargalo: {categoria_top} ({qtd_top} eventos)")

    # Retorna a string pronta; quem chama decide onde exibir
    return "\n".join(linhas)


print(gerar_dashboard(EVENTOS))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Dashboard textual de alertas do NOC da MonitoraTI para o standup diario."""

from collections import Counter

EVENTOS = ["cpu", "disco", "cpu", "rede", "cpu", "disco", "memoria", "cpu", "rede", "cpu"]
TITULO = "=== Dashboard de alertas — turno manha ==="


def montar_contador(eventos: list[str]) -> Counter:
    """Conta os alertas por categoria."""
    return Counter(eventos)


def calcular_percentual(qtd: int, total: int) -> float:
    """Calcula a participacao percentual com 1 casa decimal."""
    # Guard clause: evita divisao por zero em turno sem eventos
    if total == 0:
        return 0.0
    return round(qtd / total * 100, 1)


def identificar_gargalo(contador: Counter) -> tuple[str, int]:
    """Retorna a categoria com maior volume de alertas e sua contagem."""
    return contador.most_common(1)[0]


def gerar_dashboard(eventos: list[str]) -> str:
    """Monta o dashboard multilinha ordenado por volume decrescente."""
    contador = montar_contador(eventos)
    total = len(eventos)
    categoria_top, qtd_top = identificar_gargalo(contador)

    # Corpo do painel: uma linha por categoria, ja ordenada pelo most_common
    corpo = [
        f"{categoria}: {qtd} ({calcular_percentual(qtd, total)}%)"
        for categoria, qtd in contador.most_common()
    ]

    rodape = [
        f"Total: {total} eventos",
        f"Gargalo: {categoria_top} ({qtd_top} eventos)",
    ]

    return "\n".join([TITULO, *corpo, *rodape])


def main() -> None:
    print(gerar_dashboard(EVENTOS))


if __name__ == "__main__":
    main()
```

</details>
