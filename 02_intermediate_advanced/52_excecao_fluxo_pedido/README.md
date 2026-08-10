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

## Como executar

```bash
cd "52_excecao_fluxo_pedido"
python main.py
```
