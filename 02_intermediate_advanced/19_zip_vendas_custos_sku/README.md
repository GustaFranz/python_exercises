# 19 - Zip: margem e alerta comercial por SKU

## Objetivo

Cruzar vendas, custos e meta com zip para relatorio de margem.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Mercado Bom Preco |
| **Setor** | Varejo / comercial |
| **Solicitacao** | Relatorio de margem por SKU com alerta de produtos abaixo da meta. |

## Enunciado

skus = ["SKU01", "SKU02", "SKU03", "SKU04"]
vendas = [1200.0, 800.0, 450.0, 1500.0]
custos = [700.0, 500.0, 300.0, 1200.0]
meta_margem_pct = [35.0, 40.0, 30.0, 25.0]

Para cada SKU (use `zip`):
1) `margem = venda - custo`
2) `margem_pct = (margem / venda) * 100` (se venda > 0)
3) `status = "ok"` se margem_pct >= meta, senao `"abaixo_da_meta"`

Monte lista de dicts `{sku, venda, custo, margem, margem_pct, status, meta}`.
Exiba:
- tabela completa
- SKU com maior margem_pct
- lista de SKUs abaixo da meta (backlog comercial)
- margem media percentual do portfolio

## Passo a passo

1. Crie as quatro listas paralelas `skus`, `vendas`, `custos` e `meta_margem_pct` com os dados do enunciado.
2. Crie uma lista vazia `linhas` e percorra as quatro listas juntas com `for sku, venda, custo, meta in zip(skus, vendas, custos, meta_margem_pct):`.
3. Dentro do loop, calcule `margem = venda - custo` e `margem_pct = round((margem / venda) * 100, 1)` — proteja contra divisao por zero com ternario (`... if venda > 0 else 0.0`).
4. Ainda no loop, defina `status = "ok" if margem_pct >= meta else "abaixo_da_meta"` e faca `linhas.append({...})` com as chaves `sku, venda, custo, margem, margem_pct, status, meta`.
5. Exiba a tabela completa: cabecalho + uma linha formatada por SKU.
6. Encontre o campeao com `max(linhas, key=lambda x: x["margem_pct"])` e exiba SKU e margem.
7. Monte o backlog com list comprehension: `[linha["sku"] for linha in linhas if linha["status"] == "abaixo_da_meta"]`.
8. Calcule a margem media do portfolio: soma das `margem_pct` dividida pela quantidade de SKUs.
9. Exiba o campeao, o backlog e a margem media formatados.

## Como executar

```bash
cd "19_zip_vendas_custos_sku"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Quatro listas paralelas do sistema comercial (enunciado)
skus = ["SKU01", "SKU02", "SKU03", "SKU04"]
vendas = [1200.0, 800.0, 450.0, 1500.0]
custos = [700.0, 500.0, 300.0, 1200.0]
meta_margem_pct = [35.0, 40.0, 30.0, 25.0]

# Monta um registro por SKU cruzando as quatro listas com zip
linhas = []
for sku, venda, custo, meta in zip(skus, vendas, custos, meta_margem_pct):
    # Margem absoluta em reais
    margem = venda - custo
    # Margem percentual sobre a venda; ternario evita divisao por zero
    margem_pct = round((margem / venda) * 100, 1) if venda > 0 else 0.0
    # Compara com a meta individual do SKU
    status = "ok" if margem_pct >= meta else "abaixo_da_meta"
    linhas.append({
        "sku": sku, "venda": venda, "custo": custo,
        "margem": margem, "margem_pct": margem_pct,
        "status": status, "meta": meta,
    })

# Tabela completa com colunas alinhadas
print(f'{"SKU":<6} | {"VENDA":>8} | {"CUSTO":>8} | {"MARGEM":>8} | {"MARGEM %":>8} | {"META %":>6} | STATUS')
print("-" * 75)
for linha in linhas:
    print(
        f'{linha["sku"]:<6} | {linha["venda"]:>8.2f} | {linha["custo"]:>8.2f} | '
        f'{linha["margem"]:>8.2f} | {linha["margem_pct"]:>8.1f} | '
        f'{linha["meta"]:>6.1f} | {linha["status"]}'
    )

# max com key acha o registro de maior margem percentual
campeao = max(linhas, key=lambda x: x["margem_pct"])

# Comprehension filtra o backlog comercial (quem ficou abaixo da meta)
backlog = [linha["sku"] for linha in linhas if linha["status"] == "abaixo_da_meta"]

# Media simples das margens percentuais do portfolio
margem_media = round(sum(l["margem_pct"] for l in linhas) / len(linhas), 1)

print(f'\nMaior margem %: {campeao["sku"]} ({campeao["margem_pct"]}%)')
print(f"SKUs abaixo da meta: {backlog}")
print(f"Margem media do portfolio: {margem_media}%")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Relatorio de margem por SKU com alerta de produtos abaixo da meta."""

from dataclasses import dataclass
from operator import attrgetter
from statistics import fmean


@dataclass(frozen=True)
class LinhaMargem:
    """Registro consolidado de margem de um SKU.

    frozen=True torna o registro imutavel: relatorio nao deve ser
    alterado depois de calculado.
    """

    sku: str
    venda: float
    custo: float
    meta: float

    @property
    def margem(self) -> float:
        """Margem absoluta em reais."""
        return self.venda - self.custo

    @property
    def margem_pct(self) -> float:
        """Margem percentual sobre a venda (0 se nao houve venda)."""
        return round(self.margem / self.venda * 100, 1) if self.venda > 0 else 0.0

    @property
    def status(self) -> str:
        """Compara a margem percentual com a meta individual do SKU."""
        return "ok" if self.margem_pct >= self.meta else "abaixo_da_meta"


def main() -> None:
    # Dados de entrada do enunciado
    skus = ["SKU01", "SKU02", "SKU03", "SKU04"]
    vendas = [1200.0, 800.0, 450.0, 1500.0]
    custos = [700.0, 500.0, 300.0, 1200.0]
    meta_margem_pct = [35.0, 40.0, 30.0, 25.0]

    # zip com strict=True cruza as quatro listas e falha se desalinharem
    linhas = [
        LinhaMargem(sku, venda, custo, meta)
        for sku, venda, custo, meta in zip(skus, vendas, custos, meta_margem_pct, strict=True)
    ]

    # Tabela completa
    print(f'{"SKU":<6} | {"VENDA":>8} | {"CUSTO":>8} | {"MARGEM":>8} | {"MARGEM %":>8} | {"META %":>6} | STATUS')
    print("-" * 75)
    for l in linhas:
        print(
            f"{l.sku:<6} | {l.venda:>8.2f} | {l.custo:>8.2f} | "
            f"{l.margem:>8.2f} | {l.margem_pct:>8.1f} | {l.meta:>6.1f} | {l.status}"
        )

    # attrgetter le a property direto, sem lambda
    campeao = max(linhas, key=attrgetter("margem_pct"))

    # Backlog comercial: SKUs que nao bateram a meta
    backlog = [l.sku for l in linhas if l.status == "abaixo_da_meta"]

    # fmean calcula a media das margens percentuais
    margem_media = round(fmean(l.margem_pct for l in linhas), 1)

    print(f"\nMaior margem %: {campeao.sku} ({campeao.margem_pct}%)")
    print(f"SKUs abaixo da meta: {backlog}")
    print(f"Margem media do portfolio: {margem_media}%")


if __name__ == "__main__":
    main()
```

</details>
