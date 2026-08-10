# 104 - Classe Pedido: CRUD de itens e desconto

## Objetivo

Modelar pedido comercial com OOP: itens, total, desconto e listagem (pergunta classica de entrevista).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / pedidos |
| **Solicitacao** | Calcular pedidos de material escolar com regras de desconto e controle de itens. |

## Enunciado

- Crie classe `Pedido` com cliente e lista interna de itens.
- Metodos esperados:
  - `adicionar_item(nome, qtd, preco)` — adiciona item valido
  - `remover_item(nome)` — remove item pelo nome (retorne bool ou trate ausencia)
  - `listar_itens()` — retorna copia ou visao dos itens
  - `total()` — soma `preco * qtd` de todos os itens
  - `aplicar_desconto(pct)` — aplica percentual (0 a 100) sobre o total com validacao
- Valide entradas: quantidade e preco positivos; desconto entre 0 e 100.
- Monte cenario de teste manual no `main.py` (adicionar, remover, desconto, total).

## Passo a passo

1. Declare a classe `Pedido` com `__init__(self, cliente)` guardando `self.cliente` e iniciando `self.itens = []` (cada item sera um dict `{"nome": ..., "qtd": ..., "preco": ...}`).
2. Implemente `adicionar_item(self, nome, qtd, preco)`: valide `qtd > 0` e `preco > 0` (lance `ValueError` se invalido) e faca `append` do dict na lista.
3. Implemente `remover_item(self, nome) -> bool`: percorra `self.itens`, remova o item cujo `"nome"` bate e retorne `True`; se nao encontrar, retorne `False`.
4. Implemente `listar_itens(self) -> list` retornando uma **copia** da lista (ex.: `list(self.itens)`) para proteger o estado interno.
5. Implemente `total(self) -> float` somando `item["preco"] * item["qtd"]` de todos os itens (use `sum` com generator).
6. Implemente `aplicar_desconto(self, pct) -> float`: valide `0 <= pct <= 100` (lance `ValueError` se invalido) e retorne `self.total() * (1 - pct / 100)` — sem alterar os itens.
7. Implemente `__str__(self)` exibindo cliente, quantidade de itens e total formatado.
8. No `main`, monte o cenario: crie `Pedido("Escola 7B")`, adicione 3 itens, remova 1, exiba o pedido, o total e o total com desconto de 10%.

## Como executar

```bash
cd "104_classe_pedido_total"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        # Lista interna de itens; cada item e um dict {nome, qtd, preco}
        self.itens = []

    def adicionar_item(self, nome, qtd, preco):
        # Validacao na entrada: dados invalidos nunca entram no pedido
        if qtd <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if preco <= 0:
            raise ValueError("Preco deve ser positivo")
        self.itens.append({"nome": nome, "qtd": qtd, "preco": preco})

    def remover_item(self, nome):
        # Percorre os itens procurando pelo nome
        for item in self.itens:
            if item["nome"] == nome:
                self.itens.remove(item)
                return True  # removeu com sucesso
        return False  # nome nao encontrado

    def listar_itens(self):
        # Retorna copia: quem chamar nao consegue alterar a lista interna
        return list(self.itens)

    def total(self):
        # Soma preco * qtd de cada item com generator expression
        return sum(item["preco"] * item["qtd"] for item in self.itens)

    def aplicar_desconto(self, pct):
        # Percentual fora de 0..100 e erro de uso, nao de dado
        if pct < 0 or pct > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        # Usa total() como base; nao altera os itens do pedido
        return self.total() * (1 - pct / 100)

    def __str__(self):
        return f"Pedido de {self.cliente} | Itens: {len(self.itens)} | Total: R$ {self.total():.2f}"


# Cenario de teste manual
pedido = Pedido("Escola 7B")

# Adiciona 3 itens validos
pedido.adicionar_item("Caderno", 10, 8.50)
pedido.adicionar_item("Caneta", 20, 2.00)
pedido.adicionar_item("Mochila", 2, 120.00)
print(pedido)  # 3 itens, total 365.00

# Remove um item e tenta remover um inexistente
print(f"Remover Mochila: {pedido.remover_item('Mochila')}")   # True
print(f"Remover Estojo: {pedido.remover_item('Estojo')}")     # False
print(pedido)  # 2 itens, total 125.00

# Lista os itens restantes
for item in pedido.listar_itens():
    print(f"- {item['nome']}: {item['qtd']} x R$ {item['preco']:.2f}")

# Aplica desconto de 10% sobre o total
total_final = pedido.aplicar_desconto(10)
print(f"Total com 10% de desconto: R$ {total_final:.2f}")  # 112.50
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ItemPedido:
    """Item imutavel do pedido: depois de criado, ninguem altera por engano."""

    nome: str
    qtd: int
    preco: float

    def __post_init__(self) -> None:
        # __post_init__ roda apos o __init__ gerado pela dataclass:
        # lugar certo para validar os campos recebidos
        if self.qtd <= 0:
            raise ValueError(f"Quantidade invalida: {self.qtd}")
        if self.preco <= 0:
            raise ValueError(f"Preco invalido: {self.preco}")

    @property
    def subtotal(self) -> float:
        # Subtotal calculado sob demanda, sem campo duplicado
        return self.qtd * self.preco


class Pedido:
    """Pedido com CRUD de itens, total e desconto percentual."""

    def __init__(self, cliente: str) -> None:
        self.cliente = cliente
        # Lista privada por convencao (_): acesso externo via listar_itens()
        self._itens: list[ItemPedido] = []

    def adicionar_item(self, nome: str, qtd: int, preco: float) -> None:
        # A validacao mora na dataclass; aqui so montamos e guardamos o item
        self._itens.append(ItemPedido(nome, qtd, preco))

    def remover_item(self, nome: str) -> bool:
        for item in self._itens:
            if item.nome == nome:
                self._itens.remove(item)
                return True
        return False

    def listar_itens(self) -> list[ItemPedido]:
        # Copia rasa protege a lista interna de alteracoes externas
        return list(self._itens)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._itens)

    def aplicar_desconto(self, pct: float) -> float:
        # Guard clause: rejeita percentual invalido antes de calcular
        if not 0 <= pct <= 100:
            raise ValueError(f"Desconto deve estar entre 0 e 100, recebido: {pct}")
        return self.total * (1 - pct / 100)

    def __str__(self) -> str:
        return f"Pedido de {self.cliente} | Itens: {len(self._itens)} | Total: R$ {self.total:.2f}"


def main() -> None:
    pedido = Pedido("Escola 7B")

    # Monta o pedido com 3 itens
    pedido.adicionar_item("Caderno", 10, 8.50)
    pedido.adicionar_item("Caneta", 20, 2.00)
    pedido.adicionar_item("Mochila", 2, 120.00)
    print(pedido)

    # Demonstra remocao existente e inexistente
    print(f"Remover Mochila: {pedido.remover_item('Mochila')}")
    print(f"Remover Estojo: {pedido.remover_item('Estojo')}")
    print(pedido)

    for item in pedido.listar_itens():
        print(f"- {item.nome}: {item.qtd} x R$ {item.preco:.2f} = R$ {item.subtotal:.2f}")

    print(f"Total com 10% de desconto: R$ {pedido.aplicar_desconto(10):.2f}")


if __name__ == "__main__":
    main()
```

</details>
