# 08 - Dict comprehension: contagem de status

## Objetivo

Contar ocorrencias com dict comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida Entregas |
| **Setor** | Logistica |
| **Solicitacao** | Resumo de pedidos por status para reuniao operacional. |

## Enunciado

pedidos = ["entregue", "pendente", "entregue", "cancelado", "pendente", "entregue", "pendente"]
Status unicos conhecidos: entregue, pendente, cancelado
Monte contagem com dict comprehension:
{status: pedidos.count(status) for status in set(pedidos)}
Exiba cada status e sua quantidade.

## Passo a passo

1. Crie a lista `pedidos` com os 7 status do enunciado.
2. Obtenha os status unicos com `set(pedidos)` — o set elimina as repeticoes automaticamente.
3. Crie `contagem` com dict comprehension: para cada status unico, a chave e o status e o valor e `pedidos.count(status)`.
4. Saiba o custo: `.count()` dentro da comprehension e O(n^2) porque varre a lista inteira para cada status. Aceitavel neste exercicio introdutorio; em listas grandes prefira `collections.Counter`.
5. Percorra `contagem.items()` e exiba cada status com sua quantidade, um por linha, em formato legivel para a reuniao.

## Como executar

```bash
cd "08_dict_comprehension_contagem_status"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Lote de pedidos do dia (enunciado)
pedidos = ["entregue", "pendente", "entregue", "cancelado", "pendente", "entregue", "pendente"]

# set(pedidos) devolve apenas os status unicos (chaves sem repeticao);
# .count(status) conta quantas vezes cada um aparece na lista original.
# Atencao: .count() na comprehension e O(n^2) — ok aqui, ruim em listas grandes.
contagem = {status: pedidos.count(status) for status in set(pedidos)}

# Resumo legivel para a reuniao operacional, um status por linha;
# sorted() fixa a ordem alfabetica (set nao garante ordem)
print("Resumo de pedidos por status:")
for status in sorted(contagem):
    print(f"  {status}: {contagem[status]}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Resumo de pedidos por status para a reuniao operacional."""

from collections import Counter


def contar_status(pedidos: list[str]) -> Counter:
    """Conta ocorrencias de cada status em uma unica passagem (O(n)).

    Counter e a ferramenta padrao da stdlib para contagem: mais rapido
    e mais expressivo que dict comprehension com .count().
    """
    return Counter(pedidos)


def main() -> None:
    # Dados de entrada do enunciado
    pedidos = [
        "entregue", "pendente", "entregue", "cancelado",
        "pendente", "entregue", "pendente",
    ]

    # Contagem em uma passagem
    contagem = contar_status(pedidos)

    # most_common() ja devolve ordenado do mais frequente para o menos:
    # ordem util para priorizar a discussao na reuniao
    print("Resumo de pedidos por status:")
    for status, quantidade in contagem.most_common():
        print(f"  {status}: {quantidade}")


if __name__ == "__main__":
    main()
```

</details>
