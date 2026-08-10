# 115 - Dataclass: relatorio analitico de vendas

## Objetivo

Gerar metricas de vendas a partir de lista de dataclasses (total, ticket medio, top produto).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Consolidar vendas do bazar em relatorio analitico para reuniao comercial. |

## Enunciado

- Crie `@dataclass Venda` com `produto`, `quantidade` e `valor_unit`.
- Implemente `gerar_relatorio(vendas)` retornando **dict** com:
  - `total` — soma geral
  - `ticket_medio` — total / quantidade de vendas
  - `top_produto` — produto com maior subtotal
- Implemente `filtrar_vendas_acima(vendas, limite)` retornando vendas cujo subtotal >= limite.
- Use lista de exemplo com pelo menos 4 vendas e exiba relatorio + vendas filtradas.

## Passo a passo

1. Importe `dataclass` e declare `@dataclass Venda` com `produto: str`, `quantidade: int` e `valor_unit: float`.
2. Adicione a `Venda` um metodo `subtotal(self) -> float` retornando `self.quantidade * self.valor_unit`.
3. Monte a lista de exemplo com 4 vendas: `Venda("Caderno", 10, 8.50)`, `Venda("Caneta", 50, 2.00)`, `Venda("Mochila", 3, 120.00)` e `Venda("Lapis", 30, 1.50)`.
4. Implemente `gerar_relatorio(vendas) -> dict`:
   - `total`: some os subtotais com `sum(v.subtotal() for v in vendas)`.
   - `ticket_medio`: `total / len(vendas)` (proteja contra lista vazia).
   - `top_produto`: use `max(vendas, key=...)` pelo subtotal e pegue `.produto`.
   - Retorne `{"total": ..., "ticket_medio": ..., "top_produto": ...}`.
5. Implemente `filtrar_vendas_acima(vendas, limite) -> list` com list comprehension filtrando `v.subtotal() >= limite`.
6. Implemente `exibir_relatorio(relatorio) -> None` imprimindo as tres metricas formatadas.
7. No fluxo principal: gere o relatorio, exiba, depois filtre com `limite = 50.0` e liste as vendas que passaram (esperado: Caderno, Caneta e Mochila).

## Como executar

```bash
cd "115_dataclass_relatorio_lista"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from dataclasses import dataclass


@dataclass
class Venda:
    produto: str
    quantidade: int
    valor_unit: float

    def subtotal(self):
        # Valor da venda: quantidade x preco unitario
        return self.quantidade * self.valor_unit


def gerar_relatorio(vendas):
    # Soma geral de todas as vendas
    total = sum(v.subtotal() for v in vendas)
    # Ticket medio: total dividido pela quantidade de vendas
    # (protege contra divisao por zero se a lista vier vazia)
    ticket_medio = total / len(vendas) if vendas else 0.0
    # max com key compara os subtotais; .produto pega so o nome
    # Em empate, max mantem o primeiro encontrado (regra do enunciado)
    top_produto = max(vendas, key=lambda v: v.subtotal()).produto if vendas else None
    # Dict de saida: facil de testar e de integrar com outros modulos
    return {"total": total, "ticket_medio": ticket_medio, "top_produto": top_produto}


def filtrar_vendas_acima(vendas, limite):
    # List comprehension: mantem apenas vendas com subtotal >= limite
    return [v for v in vendas if v.subtotal() >= limite]


def exibir_relatorio(relatorio):
    # Camada de apresentacao: so formata e imprime
    print("=== RELATORIO DE VENDAS ===")
    print(f"Total: R$ {relatorio['total']:.2f}")
    print(f"Ticket medio: R$ {relatorio['ticket_medio']:.2f}")
    print(f"Top produto: {relatorio['top_produto']}")


# Massa de dados do enunciado
vendas = [
    Venda("Caderno", 10, 8.50),
    Venda("Caneta", 50, 2.00),
    Venda("Mochila", 3, 120.00),
    Venda("Lapis", 30, 1.50),
]

# Gera e exibe as metricas consolidadas
relatorio = gerar_relatorio(vendas)
exibir_relatorio(relatorio)

# Filtra vendas relevantes (subtotal >= 50) para a reuniao comercial
print("\nVendas com subtotal >= R$ 50.00:")
for venda in filtrar_vendas_acima(vendas, 50.0):
    print(f"- {venda.produto}: R$ {venda.subtotal():.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass

# Limite padrao nomeado no topo: sem "numero magico" no meio do codigo
LIMITE_PADRAO = 50.0


@dataclass(frozen=True, slots=True)
class Venda:
    """Venda individual do bazar escolar."""

    produto: str
    quantidade: int
    valor_unit: float

    @property
    def subtotal(self) -> float:
        # property: leitura natural (venda.subtotal) para valor derivado
        return self.quantidade * self.valor_unit


def gerar_relatorio(vendas: list[Venda]) -> dict:
    """Consolida total, ticket medio e produto de maior subtotal."""
    # Guard clause: lista vazia retorna relatorio neutro sem quebrar
    if not vendas:
        return {"total": 0.0, "ticket_medio": 0.0, "top_produto": None}

    total = sum(v.subtotal for v in vendas)
    top = max(vendas, key=lambda v: v.subtotal)
    return {
        "total": total,
        "ticket_medio": total / len(vendas),
        "top_produto": top.produto,
    }


def filtrar_vendas_acima(vendas: list[Venda], limite: float) -> list[Venda]:
    """Retorna as vendas cujo subtotal atinge o limite informado."""
    return [v for v in vendas if v.subtotal >= limite]


def exibir_relatorio(relatorio: dict) -> None:
    """Apresentacao pura: formata e imprime as metricas."""
    print("=== RELATORIO DE VENDAS ===")
    print(f"Total: R$ {relatorio['total']:.2f}")
    print(f"Ticket medio: R$ {relatorio['ticket_medio']:.2f}")
    print(f"Top produto: {relatorio['top_produto']}")


def main() -> None:
    vendas = [
        Venda("Caderno", 10, 8.50),
        Venda("Caneta", 50, 2.00),
        Venda("Mochila", 3, 120.00),
        Venda("Lapis", 30, 1.50),
    ]

    exibir_relatorio(gerar_relatorio(vendas))

    print(f"\nVendas com subtotal >= R$ {LIMITE_PADRAO:.2f}:")
    for venda in filtrar_vendas_acima(vendas, LIMITE_PADRAO):
        print(f"- {venda.produto}: R$ {venda.subtotal:.2f}")


if __name__ == "__main__":
    main()
```

</details>
