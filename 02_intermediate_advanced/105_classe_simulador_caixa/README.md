# 105 - Classe: simulador de caixa

## Objetivo

Simular caixa escolar com duas classes cooperando.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / PDV |
| **Solicitacao** | Simular ponto de venda do bazar escolar com registro de vendas. |

## Enunciado

Crie duas classes:

**`ItemVenda`**
- Atributos: `nome`, `preco`, `quantidade`
- Metodo `subtotal()` — retorna `preco * quantidade`

**`Caixa`**
- `__init__(self, operador)` — inicializa `self.vendas = []`
- `registrar_venda(self, item: ItemVenda)` — adiciona item a `self.vendas`
- `total_dia(self)` — soma os subtotais de todas as vendas
- `__str__(self)` — exibe operador, quantidade de vendas e total do dia

No `main`, simule o caixa da operadora **"Maria"** com **3 itens** vendidos (ex.: caderno, caneta, borracha) e exiba o resumo final.

## Passo a passo

1. Declare a classe `ItemVenda` com `__init__(self, nome, preco, quantidade)` guardando os tres atributos em `self`.
2. Adicione o metodo `subtotal(self)` retornando `self.preco * self.quantidade`.
3. Declare a classe `Caixa` com `__init__(self, operador)` guardando `self.operador` e iniciando `self.vendas = []`.
4. Implemente `registrar_venda(self, item)` fazendo `self.vendas.append(item)` — o caixa recebe **instancias** de `ItemVenda`.
5. Implemente `total_dia(self)` somando `item.subtotal()` de cada item em `self.vendas` (use `sum` com generator).
6. Implemente `__str__(self)` retornando f-string com operador, `len(self.vendas)` e o total do dia.
7. No `main`, crie `Caixa("Maria")`, registre 3 itens (ex.: caderno, caneta, borracha com precos e quantidades diferentes) e exiba o caixa com `print()`.

## Como executar

```bash
cd "105_classe_simulador_caixa"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class ItemVenda:
    def __init__(self, nome, preco, quantidade):
        # Classe de dados: representa um item vendido no PDV
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        # Valor do item = preco unitario x quantidade vendida
        return self.preco * self.quantidade


class Caixa:
    def __init__(self, operador):
        self.operador = operador
        # O caixa agrega as vendas do dia em uma lista de ItemVenda
        self.vendas = []

    def registrar_venda(self, item):
        # Recebe uma instancia de ItemVenda e guarda no historico
        self.vendas.append(item)

    def total_dia(self):
        # Soma o subtotal() de cada item registrado
        return sum(item.subtotal() for item in self.vendas)

    def __str__(self):
        # Resumo do dia: operador, quantidade de vendas e total
        return (
            f"Caixa de {self.operador} | Vendas: {len(self.vendas)} | "
            f"Total do dia: R$ {self.total_dia():.2f}"
        )


# Simula o caixa da operadora Maria
caixa = Caixa("Maria")

# Registra 3 itens vendidos (cada um e um objeto ItemVenda)
caixa.registrar_venda(ItemVenda("Caderno", 12.50, 2))
caixa.registrar_venda(ItemVenda("Caneta", 2.00, 5))
caixa.registrar_venda(ItemVenda("Borracha", 1.50, 3))

# print() chama o __str__ do Caixa com o resumo final
print(caixa)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ItemVenda:
    """Item vendido no PDV; imutavel para nao ser alterado apos registrado."""

    nome: str
    preco: float
    quantidade: int

    @property
    def subtotal(self) -> float:
        # Property: expoe o calculo como atributo de leitura (item.subtotal)
        return self.preco * self.quantidade


@dataclass
class Caixa:
    """Agrega as vendas de um operador ao longo do dia."""

    operador: str
    # field(default_factory=list) cria uma lista NOVA por instancia;
    # usar vendas = [] direto na classe compartilharia a mesma lista entre caixas
    vendas: list[ItemVenda] = field(default_factory=list)

    def registrar_venda(self, item: ItemVenda) -> None:
        """Adiciona um item ao historico de vendas do dia."""
        self.vendas.append(item)

    @property
    def total_dia(self) -> float:
        return sum(item.subtotal for item in self.vendas)

    def __str__(self) -> str:
        return (
            f"Caixa de {self.operador} | Vendas: {len(self.vendas)} | "
            f"Total do dia: R$ {self.total_dia:.2f}"
        )


def main() -> None:
    caixa = Caixa("Maria")

    # Itens do dia definidos em lista: facil adicionar novos cenarios
    itens = [
        ItemVenda("Caderno", 12.50, 2),
        ItemVenda("Caneta", 2.00, 5),
        ItemVenda("Borracha", 1.50, 3),
    ]
    for item in itens:
        caixa.registrar_venda(item)

    # Detalha cada venda antes do resumo final
    for item in caixa.vendas:
        print(f"- {item.nome}: {item.quantidade} x R$ {item.preco:.2f} = R$ {item.subtotal:.2f}")
    print(caixa)


if __name__ == "__main__":
    main()
```

</details>
