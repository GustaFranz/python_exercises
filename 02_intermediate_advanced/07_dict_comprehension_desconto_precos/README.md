# 07 - Dict comprehension: desconto em precos

## Objetivo

Transformar dicionario de precos com dict comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Papelaria Central |
| **Setor** | Varejo escolar |
| **Solicitacao** | Simular campanha com 10% de desconto em todos os itens. |

## Enunciado

precos = {"caderno": 12.0, "caneta": 3.5, "borracha": 2.0, "estojo": 25.0}
DESCONTO = 10  # percentual
Gere precos_promocao com dict comprehension aplicando o desconto.
Exiba tabela comparativa: produto | preco original | preco promocional.

## Passo a passo

1. Crie o dicionario `precos = {"caderno": 12.0, "caneta": 3.5, "borracha": 2.0, "estojo": 25.0}`.
2. Defina a constante `DESCONTO = 10` (percentual) no topo do arquivo.
3. Crie `precos_promocao` com dict comprehension sobre `precos.items()`: para cada par, mantenha a chave e calcule o valor com a formula `preco - (preco * DESCONTO / 100)`.
4. Arredonde o valor promocional com `round(valor, 2)` para manter duas casas decimais.
5. Exiba um cabecalho de tabela com as colunas `produto | preco original | preco promocional`.
6. Percorra `precos.items()` com um `for` e, para cada produto, busque o valor promocional em `precos_promocao[produto]` e imprima a linha formatada (use f-string com alinhamento, ex.: `{produto:<10}`).

## Como executar

```bash
cd "07_dict_comprehension_desconto_precos"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Tabela de precos atual da papelaria (enunciado)
precos = {"caderno": 12.0, "caneta": 3.5, "borracha": 2.0, "estojo": 25.0}

# Percentual da campanha como constante: regra visivel e facil de mudar
DESCONTO = 10

# Dict comprehension sobre .items(): mantem a chave (produto) e transforma
# o valor aplicando o desconto; round(_, 2) padroniza valor monetario
precos_promocao = {
    produto: round(preco - (preco * DESCONTO / 100), 2)
    for produto, preco in precos.items()
}

# Tabela comparativa: cabecalho + uma linha por produto
print(f'{"PRODUTO":<10} | {"ORIGINAL":>9} | {"PROMOCIONAL":>11}')
print("-" * 37)
for produto, preco_original in precos.items():
    # Busca o preco promocional pelo mesmo produto (mesma chave)
    print(f"{produto:<10} | {preco_original:>9.2f} | {precos_promocao[produto]:>11.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Simulacao de campanha promocional da papelaria."""

# Percentual da campanha centralizado como constante de modulo
DESCONTO_PCT = 10.0


def aplicar_desconto(precos: dict[str, float], pct: float) -> dict[str, float]:
    """Devolve um novo dicionario com o desconto aplicado em cada preco.

    Multiplicar por (1 - pct/100) e a forma direta de aplicar desconto
    percentual; round(_, 2) mantem o padrao monetario.
    """
    fator = 1 - pct / 100
    return {produto: round(preco * fator, 2) for produto, preco in precos.items()}


def main() -> None:
    # Dados de entrada do enunciado
    precos = {"caderno": 12.0, "caneta": 3.5, "borracha": 2.0, "estojo": 25.0}

    # Gera a tabela promocional sem alterar a original
    precos_promocao = aplicar_desconto(precos, DESCONTO_PCT)

    # Tabela comparativa formatada para a reuniao da campanha
    print(f"Campanha: {DESCONTO_PCT:.0f}% de desconto em todos os itens\n")
    print(f'{"PRODUTO":<10} | {"ORIGINAL":>9} | {"PROMOCIONAL":>11}')
    print("-" * 37)
    for produto, preco_original in precos.items():
        print(f"{produto:<10} | {preco_original:>9.2f} | {precos_promocao[produto]:>11.2f}")


if __name__ == "__main__":
    main()
```

</details>
