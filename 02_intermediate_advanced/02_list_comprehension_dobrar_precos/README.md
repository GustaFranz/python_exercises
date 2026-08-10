# 02 - List comprehension: dobrar precos

## Objetivo

Aplicar list comprehension para transformar valores numericos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Cantina Escolar Nova Geracao |
| **Setor** | Alimentacao escolar |
| **Solicitacao** | Simular reajuste emergencial dos precos do cardapio. |

## Enunciado

Precos atuais do cardapio:
precos = [4.50, 6.00, 3.50, 8.00, 2.00]
A diretoria pediu simulacao com valores dobrados para analise de margem.
Crie precos_dobrados com list comprehension e exiba as duas listas.

## Passo a passo

1. Crie a lista `precos = [4.50, 6.00, 3.50, 8.00, 2.00]`.
2. Crie `precos_dobrados` com list comprehension aplicando a transformacao em cada item: `[preco * 2 for preco in precos]`.
3. Nao modifique a lista original — a simulacao gera uma lista nova.
4. Exiba `precos` com o rotulo "Precos atuais".
5. Exiba `precos_dobrados` com o rotulo "Precos simulados".

## Como executar

```bash
cd "02_list_comprehension_dobrar_precos"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Precos atuais do cardapio (dados do enunciado)
precos = [4.50, 6.00, 3.50, 8.00, 2.00]

# List comprehension de mapeamento puro: aplica a mesma conta em cada item
# e devolve uma lista nova, sem alterar a original
precos_dobrados = [preco * 2 for preco in precos]

# Exibe antes/depois com rotulos claros para a analise de margem
print("Precos atuais:   ", precos)
print("Precos simulados:", precos_dobrados)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Simulacao de reajuste de precos do cardapio da cantina."""

# Fator de reajuste como constante nomeada: evita numero magico no codigo
# e documenta a regra pedida pela diretoria (dobrar = fator 2.0)
FATOR_REAJUSTE = 2.0


def simular_reajuste(precos: list[float], fator: float) -> list[float]:
    """Aplica um fator multiplicativo em cada preco e devolve lista nova.

    round(..., 2) garante duas casas decimais, padrao para valores monetarios.
    """
    return [round(preco * fator, 2) for preco in precos]


def main() -> None:
    # Dados de entrada do enunciado
    precos = [4.50, 6.00, 3.50, 8.00, 2.00]

    # Gera a simulacao sem tocar na lista original
    precos_dobrados = simular_reajuste(precos, FATOR_REAJUSTE)

    # Relatorio comparativo item a item: facilita a leitura da diretoria
    print("Simulacao de reajuste (fator 2.0)")
    print(f"{'Atual':>8} | {'Simulado':>8}")
    # zip pareia cada preco atual com o simulado, na mesma posicao
    for atual, novo in zip(precos, precos_dobrados):
        print(f"{atual:>8.2f} | {novo:>8.2f}")

    # Listas completas ao final, como pede o enunciado
    print(f"\nPrecos atuais:    {precos}")
    print(f"Precos simulados: {precos_dobrados}")


if __name__ == "__main__":
    main()
```

</details>
