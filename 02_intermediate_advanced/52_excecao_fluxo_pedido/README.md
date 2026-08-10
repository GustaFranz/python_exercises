# 52 - Excecao customizada: fluxo de pedido

## Objetivo

Crie EstoqueInsuficienteError e PedidoVazioError.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / e-commerce |
| **Solicitacao** | Garantir que pedidos invalidos nao entrem na fila de separacao. |

## Enunciado

Estoque fixo:
```python
estoque = {"caderno": 5, "caneta": 0}
```

1) Crie as excecoes:
```python
class EstoqueInsuficienteError(Exception):
    pass

class PedidoVazioError(Exception):
    pass
```

2) Implemente:
```python
def processar_pedido(itens: list[dict]) -> str:
    # itens: lista de {"produto": str, "qtd": int}
    # PedidoVazioError se lista vazia
    # EstoqueInsuficienteError se qtd > estoque ou estoque zero
    # retorna "Pedido aceito" se ok
```

3) Teste 3 cenarios (cada um com `try/except`, sem derrubar o programa):
   - Pedido vazio: `[]`
   - Sem estoque: `[{"produto": "caneta", "qtd": 1}]`
   - Pedido valido: `[{"produto": "caderno", "qtd": 2}]`

Exemplo de saida:

```
Erro: Pedido vazio
Erro: Estoque insuficiente para caneta
Pedido aceito
```

## Passo a passo

1. Defina as classes `EstoqueInsuficienteError(Exception)` e `PedidoVazioError(Exception)`, ambas com corpo `pass` (ou docstring).
2. Crie o dicionario `estoque = {"caderno": 5, "caneta": 0}`.
3. Defina `def processar_pedido(itens: list[dict]) -> str:` com esta logica:
   - Se `not itens` (lista vazia), levante `PedidoVazioError("Pedido vazio")`.
   - Percorra os itens com `for item in itens:`; para cada um, pegue `produto = item["produto"]` e `disponivel = estoque.get(produto, 0)` — o `.get` com padrao 0 tambem cobre produto inexistente.
   - Se `item["qtd"] > disponivel`, levante `EstoqueInsuficienteError(f"Estoque insuficiente para {produto}")` (estoque zero cai nessa mesma regra).
   - Se o loop terminar sem erro, retorne `"Pedido aceito"`.
4. Crie a lista `pedidos` com os 3 cenarios do enunciado, na ordem: `[]`, caneta qtd 1, caderno qtd 2.
5. Percorra `pedidos` e, para cada um, chame `processar_pedido(pedido)` dentro de `try:`, exibindo o retorno com `print`.
6. Capture os dois erros em um unico `except (PedidoVazioError, EstoqueInsuficienteError) as e:` e exiba `f"Erro: {e}"` — assim nenhum cenario derruba o programa.

## Como executar

```bash
cd "52_excecao_fluxo_pedido"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Excecoes de negocio: uma para pedido vazio, outra para falta de estoque
class EstoqueInsuficienteError(Exception):
    pass


class PedidoVazioError(Exception):
    pass


# Estoque fixo do enunciado
estoque = {"caderno": 5, "caneta": 0}


def processar_pedido(itens):
    # Primeira validacao: pedido sem itens nao entra na fila
    if not itens:
        raise PedidoVazioError("Pedido vazio")

    # Valida cada item contra o estoque disponivel
    for item in itens:
        produto = item["produto"]
        # .get com padrao 0 cobre produto inexistente e estoque zero
        disponivel = estoque.get(produto, 0)
        if item["qtd"] > disponivel:
            raise EstoqueInsuficienteError(f"Estoque insuficiente para {produto}")

    # Nenhuma validacao falhou: pedido liberado
    return "Pedido aceito"


# Os 3 cenarios do enunciado: vazio, sem estoque e valido
pedidos = [
    [],
    [{"produto": "caneta", "qtd": 1}],
    [{"produto": "caderno", "qtd": 2}],
]

for pedido in pedidos:
    try:
        # Sucesso: imprime "Pedido aceito"
        print(processar_pedido(pedido))
    except (PedidoVazioError, EstoqueInsuficienteError) as e:
        # Falha: imprime o motivo sem derrubar o programa
        print(f"Erro: {e}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Validacao de pedidos antes da fila de separacao do e-commerce."""


class EstoqueInsuficienteError(Exception):
    """Quantidade pedida maior que o estoque disponivel."""


class PedidoVazioError(Exception):
    """Pedido chegou sem nenhum item."""


# Estoque recebido por parametro: a funcao nao depende de variavel global
ESTOQUE = {"caderno": 5, "caneta": 0}


def processar_pedido(itens: list[dict], estoque: dict[str, int]) -> str:
    """Valida os itens contra o estoque; devolve 'Pedido aceito' se tudo ok.

    Levanta PedidoVazioError ou EstoqueInsuficienteError na primeira
    regra violada — quem chama decide como tratar.
    """
    # Guard clause: falha cedo no caso mais simples
    if not itens:
        raise PedidoVazioError("Pedido vazio")

    for item in itens:
        produto = item["produto"]
        if item["qtd"] > estoque.get(produto, 0):
            raise EstoqueInsuficienteError(f"Estoque insuficiente para {produto}")

    return "Pedido aceito"


def main() -> None:
    pedidos = [
        [],                                    # vazio
        [{"produto": "caneta", "qtd": 1}],     # sem estoque
        [{"produto": "caderno", "qtd": 2}],    # valido
    ]

    for pedido in pedidos:
        try:
            print(processar_pedido(pedido, ESTOQUE))
        except (PedidoVazioError, EstoqueInsuficienteError) as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
```

</details>
