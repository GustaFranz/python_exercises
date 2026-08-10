# 103 - Classe Produto: estoque

## Objetivo

Controlar estoque com metodos vender e repor.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / estoque |
| **Solicitacao** | Controlar estoque de material escolar na loja virtual. |

## Enunciado

Crie a classe `Produto` com:

- `__init__(self, nome, preco, estoque)`
- `vender(self, qtd)` — reduz estoque se houver quantidade suficiente; retorna `True` ou `False` (se insuficiente, **nao altera** o estoque)
- `repor(self, qtd)` — aumenta o estoque
- `__str__(self)` — exibe nome, preco e estoque atual

Teste no `main` com produto `"Caderno"`, preco `10.0`, estoque inicial **5**:

1) Vender **3** unidades (ok, estoque vai para 2).
2) Vender **5** unidades (falha, estoque permanece 2).
3) Repor **10** unidades (estoque vai para 12).
4) Exiba o produto apos cada operacao.

## Passo a passo

1. Declare a classe `Produto` com `__init__(self, nome, preco, estoque)` guardando os tres parametros em `self`.
2. Implemente `vender(self, qtd)`:
   - Se `qtd > self.estoque`, retorne `False` **sem** alterar o estoque.
   - Caso contrario, subtraia (`self.estoque -= qtd`) e retorne `True`.
3. Implemente `repor(self, qtd)` somando a quantidade ao estoque (`self.estoque += qtd`).
4. Implemente `__str__(self)` retornando f-string com nome, preco e estoque atual.
5. No fluxo principal, crie `Produto("Caderno", 10.0, 5)`.
6. Execute a sequencia: `vender(3)`, `vender(5)`, `repor(10)` — exibindo o produto (e o retorno de `vender`, se quiser) apos cada operacao.
7. Confira os estoques esperados: 2, 2 (venda recusada) e 12.

## Como executar

```bash
cd "103_classe_produto_estoque"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Produto:
    def __init__(self, nome, preco, estoque):
        # Estado do produto: nome, preco unitario e quantidade disponivel
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, qtd):
        # Sem estoque suficiente: recusa a venda e NAO altera nada
        if qtd > self.estoque:
            return False
        # Estoque suficiente: baixa a quantidade e confirma a venda
        self.estoque -= qtd
        return True

    def repor(self, qtd):
        # Reposicao simplesmente soma ao estoque atual
        self.estoque += qtd

    def __str__(self):
        # Representacao amigavel usada pelo print()
        return f"Produto: {self.nome} | Preco: {self.preco} | Estoque: {self.estoque}"


# Produto do cenario de teste: estoque inicial 5
produto = Produto("Caderno", 10.0, 5)

# Venda possivel: 3 <= 5, estoque cai para 2
ok = produto.vender(3)
print(f"Vender 3: {ok}")
print(produto)

# Venda impossivel: 5 > 2, retorna False e estoque continua 2
ok = produto.vender(5)
print(f"Vender 5: {ok}")
print(produto)

# Reposicao: estoque sobe de 2 para 12
produto.repor(10)
print("Repor 10")
print(produto)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
class Produto:
    """Produto da loja com controle de estoque simples."""

    def __init__(self, nome: str, preco: float, estoque: int) -> None:
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, qtd: int) -> bool:
        """Baixa `qtd` do estoque; retorna False se nao houver saldo."""
        # Guard clause: trata o caso invalido primeiro e sai cedo,
        # deixando o caminho principal sem aninhamento
        if qtd > self.estoque:
            return False
        self.estoque -= qtd
        return True

    def repor(self, qtd: int) -> None:
        """Adiciona `qtd` unidades ao estoque."""
        self.estoque += qtd

    def __str__(self) -> str:
        # :.2f padroniza o preco com duas casas, como em telas de varejo
        return f"Produto: {self.nome} | Preco: R$ {self.preco:.2f} | Estoque: {self.estoque}"


def main() -> None:
    produto = Produto("Caderno", preco=10.0, estoque=5)

    # Cada operacao exibe o resultado e o estado atualizado do produto,
    # facilitando a conferencia do comportamento passo a passo
    print(f"Vender 3: {'ok' if produto.vender(3) else 'sem estoque'}")
    print(produto)  # estoque esperado: 2

    print(f"Vender 5: {'ok' if produto.vender(5) else 'sem estoque'}")
    print(produto)  # venda recusada, estoque continua 2

    produto.repor(10)
    print("Repor 10: ok")
    print(produto)  # estoque esperado: 12


if __name__ == "__main__":
    main()
```

</details>
