# 135 - map e dict comprehension

## Objetivo

Combinar `map()` para calcular valores e dict comprehension para montar indice de precos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Cantina Escolar Plus |
| **Setor** | Alimentacao / operacoes |
| **Solicitacao** | Aplicar taxa de servico e indexar precos finais por codigo. |

## Enunciado

```python
codigos = ["S1", "S2", "S3", "S4"]
precos_base = [5.0, 8.5, 12.0, 3.5]
TAXA = 0.10  # 10%
```

1) Use `map` com funcao ou lambda para calcular preco final: `preco * (1 + TAXA)`.
2) Arredonde cada valor com `round(valor, 2)`.
3) Monte `tabela = {codigo: preco_final}` com dict comprehension pareando `codigos` e precos finais.
4) Com dict comprehension, filtre `promocionais = {codigo: preco}` apenas onde preco <= 10.0.
5) Exiba tabela completa, promocionais e o item mais caro (codigo + valor).

## Passo a passo

1. Crie `codigos`, `precos_base` e `TAXA` conforme o enunciado.
2. Calcule os precos finais com `map` e `lambda`, ja arredondando: `precos_finais = list(map(lambda p: round(p * (1 + TAXA), 2), precos_base))`.
3. Monte a tabela com dict comprehension sobre o `zip`: `tabela = {c: p for c, p in zip(codigos, precos_finais)}`.
4. Filtre os promocionais com dict comprehension sobre `tabela.items()`: `promocionais = {c: p for c, p in tabela.items() if p <= 10.0}`.
5. Encontre o item mais caro com `max(tabela, key=tabela.get)` (retorna o CODIGO cujo valor e o maior) e busque o valor em `tabela[codigo]`.
6. Exiba a tabela completa, os promocionais e a linha do mais caro (codigo + valor).

## Como executar

```bash
cd "135_map_dict_comprehension"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
codigos = ["S1", "S2", "S3", "S4"]
precos_base = [5.0, 8.5, 12.0, 3.5]
TAXA = 0.10  # 10% de taxa de servico
LIMITE_PROMOCIONAL = 10.0

# map + lambda: aplica taxa e arredonda cada preco em uma passada
precos_finais = list(map(lambda p: round(p * (1 + TAXA), 2), precos_base))

# dict comprehension + zip: indexa preco final pelo codigo do item
tabela = {c: p for c, p in zip(codigos, precos_finais)}

# Outra dict comprehension: mantem apenas itens ate o limite promocional
promocionais = {c: p for c, p in tabela.items() if p <= LIMITE_PROMOCIONAL}

# max com key=tabela.get: compara os VALORES mas retorna a CHAVE (codigo)
codigo_mais_caro = max(tabela, key=tabela.get)

print("=== Tabela de precos (com taxa de 10%) ===")
for codigo, preco in tabela.items():
    print(f"{codigo}: R$ {preco:.2f}")

print("\n=== Promocionais (ate R$ 10.00) ===")
for codigo, preco in promocionais.items():
    print(f"{codigo}: R$ {preco:.2f}")

print(f"\nMais caro: {codigo_mais_caro} (R$ {tabela[codigo_mais_caro]:.2f})")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Tabela de precos da cantina com taxa de servico."""

CODIGOS = ["S1", "S2", "S3", "S4"]
PRECOS_BASE = [5.0, 8.5, 12.0, 3.5]
TAXA_SERVICO = 0.10
LIMITE_PROMOCIONAL = 10.0


def preco_com_taxa(preco_base: float, taxa: float = TAXA_SERVICO) -> float:
    """Aplica a taxa de servico e arredonda para centavos."""
    return round(preco_base * (1 + taxa), 2)


def main() -> None:
    # Uma unica dict comprehension monta a tabela ja com taxa aplicada;
    # strict=True garante que codigos e precos tem o mesmo tamanho
    tabela = {
        codigo: preco_com_taxa(preco)
        for codigo, preco in zip(CODIGOS, PRECOS_BASE, strict=True)
    }

    promocionais = {c: p for c, p in tabela.items() if p <= LIMITE_PROMOCIONAL}

    # max sobre items() com key no valor: devolve o par (codigo, preco) inteiro
    codigo_caro, preco_caro = max(tabela.items(), key=lambda item: item[1])

    print("=== Tabela de precos (com taxa de 10%) ===")
    for codigo, preco in tabela.items():
        print(f"{codigo}: R$ {preco:.2f}")

    print(f"\n=== Promocionais (ate R$ {LIMITE_PROMOCIONAL:.2f}) ===")
    for codigo, preco in promocionais.items():
        print(f"{codigo}: R$ {preco:.2f}")

    print(f"\nMais caro: {codigo_caro} (R$ {preco_caro:.2f})")


if __name__ == "__main__":
    main()
```

</details>
