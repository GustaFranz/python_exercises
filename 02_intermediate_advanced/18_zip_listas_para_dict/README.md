# 18 - Zip: listas para dicionario

## Objetivo

Converter duas listas em dicionario com zip.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Financeira Educred |
| **Setor** | Credito estudantil |
| **Solicitacao** | Mapear codigo do aluno para valor de mensalidade. |

## Enunciado

codigos = ["ALU001", "ALU002", "ALU003"]
mensalidades = [450.0, 520.0, 480.0]
Crie tabela = dict(zip(codigos, mensalidades))
Exiba o dicionario e a soma total das mensalidades.

## Passo a passo

1. Crie as listas paralelas `codigos = ["ALU001", "ALU002", "ALU003"]` e `mensalidades = [450.0, 520.0, 480.0]`.
2. Crie `tabela = dict(zip(codigos, mensalidades))` — o atalho classico: zip pareia chave e valor pela posicao e `dict()` monta o dicionario.
3. Calcule o total com `sum(tabela.values())`.
4. Exiba o dicionario `tabela` (ou uma linha por codigo, para leitura melhor).
5. Exiba a soma total das mensalidades formatada com 2 casas decimais.

## Como executar

```bash
cd "18_zip_listas_para_dict"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Listas paralelas vindas do sistema financeiro (enunciado)
codigos = ["ALU001", "ALU002", "ALU003"]
mensalidades = [450.0, 520.0, 480.0]

# dict(zip(chaves, valores)): atalho classico para montar dicionario
# a partir de duas listas paralelas
tabela = dict(zip(codigos, mensalidades))

# soma direta sobre os valores do dicionario
total = sum(tabela.values())

print("Tabela codigo -> mensalidade:", tabela)
print(f"Total das mensalidades: {total:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Mapa codigo do aluno -> valor de mensalidade."""


def montar_tabela(codigos: list[str], valores: list[float]) -> dict[str, float]:
    """Converte listas paralelas em dicionario codigo -> valor.

    strict=True detecta listas de tamanhos diferentes — em dados
    financeiros, perder um registro em silencio e inaceitavel.
    """
    return dict(zip(codigos, valores, strict=True))


def main() -> None:
    # Dados de entrada do enunciado
    codigos = ["ALU001", "ALU002", "ALU003"]
    mensalidades = [450.0, 520.0, 480.0]

    # Monta o indice de consulta
    tabela = montar_tabela(codigos, mensalidades)

    # Exibe uma linha por aluno: mais legivel que o dict cru
    print("Tabela codigo -> mensalidade:")
    for codigo, valor in tabela.items():
        print(f"  {codigo}: {valor:.2f}")

    # Total consolidado da carteira
    print(f"Total das mensalidades: {sum(tabela.values()):.2f}")


if __name__ == "__main__":
    main()
```

</details>
