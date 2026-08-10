# 141 - Funcao geradora: lotes de registros

## Objetivo

Criar gerador que entrega dados em lotes (chunks) para processamento incremental.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiEscolar |
| **Setor** | Logistica / operacoes |
| **Solicitacao** | Processar entregas em lotes para evitar sobrecarga no sistema. |

## Enunciado

```python
entregas = list(range(1, 14))  # ids 1 a 13
TAMANHO_LOTE = 4
```

Implemente `gerar_lotes(itens, tamanho)` que:
- recebe lista (ou iteravel) e tamanho do lote;
- usa `yield` para entregar sublistas consecutivas;
- ultimo lote pode ter menos itens.

No `main`:
1) Itere sobre os lotes e exiba cada lote.
2) Conte quantos lotes foram gerados.
3) Some todos os ids processados (prova de que nenhum foi perdido).

## Passo a passo

1. Crie `entregas = list(range(1, 14))` e `TAMANHO_LOTE = 4`.
2. Defina `gerar_lotes(itens, tamanho)` com `for i in range(0, len(itens), tamanho)` — o terceiro argumento do `range` faz o indice pular de lote em lote (0, 4, 8, 12).
3. Dentro do loop, faca `yield itens[i:i + tamanho]` — o fatiamento entrega a sublista do lote; no ultimo, o slice devolve so o que sobrou (aqui, `[13]`).
4. No fluxo principal, itere com `for lote in gerar_lotes(entregas, TAMANHO_LOTE):`, exibindo cada lote numerado; dentro do mesmo loop, incremente um contador de lotes e acumule `sum(lote)` num total.
5. Exiba a quantidade de lotes (deve dar 4: tres cheios e um com 1 item) e a soma total dos ids.
6. Valide a soma comparando com `sum(entregas)` (91): se bater, nenhum id foi perdido no processo.

## Como executar

```bash
cd "141_funcao_geradora_lotes"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
entregas = list(range(1, 14))  # ids 1 a 13
TAMANHO_LOTE = 4


def gerar_lotes(itens, tamanho):
    # range com passo: i assume 0, 4, 8, 12 — o inicio de cada lote
    for i in range(0, len(itens), tamanho):
        # Fatiamento entrega o lote; no final, devolve so o que sobrou
        yield itens[i:i + tamanho]


numero_lote = 0
total_processado = 0

# O for pede um lote por vez ao gerador (processamento incremental)
for lote in gerar_lotes(entregas, TAMANHO_LOTE):
    numero_lote += 1
    total_processado += sum(lote)  # acumula os ids do lote atual
    print(f"Lote {numero_lote}: {lote}")

print(f"\nLotes gerados: {numero_lote}")
print(f"Soma dos ids processados: {total_processado}")
# Prova de integridade: nada foi perdido nem duplicado no processo
assert total_processado == sum(entregas), "soma deveria bater com a lista original"
print("Verificacao ok: nenhum id perdido.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Processamento de entregas em lotes (chunks).

No Python 3.12+ existe itertools.batched(itens, tamanho), que faz
exatamente isso e devolve tuplas. Implementar na mao continua sendo
pergunta classica de entrevista — a versao abaixo funciona com
qualquer iteravel, nao apenas listas indexaveis.
"""

from itertools import islice
from typing import Iterable, Iterator

ENTREGAS = list(range(1, 14))  # ids 1 a 13
TAMANHO_LOTE = 4


def gerar_lotes(itens: Iterable[int], tamanho: int) -> Iterator[list[int]]:
    """Entrega lotes consecutivos; o ultimo pode vir incompleto.

    iter() + islice funciona ate para iteraveis sem len(),
    como arquivos ou cursores de banco.
    """
    iterador = iter(itens)
    # islice pega ate 'tamanho' itens; lista vazia indica fim dos dados
    while lote := list(islice(iterador, tamanho)):
        yield lote


def main() -> None:
    total_lotes = 0
    total_processado = 0

    for numero, lote in enumerate(gerar_lotes(ENTREGAS, TAMANHO_LOTE), start=1):
        total_lotes = numero
        total_processado += sum(lote)
        print(f"Lote {numero}: {lote}")

    print(f"\nLotes gerados: {total_lotes}")
    print(f"Soma dos ids processados: {total_processado}")
    assert total_processado == sum(ENTREGAS), "soma deveria bater com a lista original"
    print("Verificacao ok: nenhum id perdido.")


if __name__ == "__main__":
    main()
```

</details>
