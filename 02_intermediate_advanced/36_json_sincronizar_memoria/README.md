# 36 - JSON: sincronizar memoria e arquivo

## Objetivo

Manter lista em memoria sincronizada com arquivo JSON validado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | InventarioTech Almoxarifado |
| **Setor** | Logistica interna |
| **Solicitacao** | Sistema de itens com memoria e disco sempre consistentes. |

## Enunciado

Use lista global `itens = []` sincronizada com `itens.json`.

Implemente:

```python
def carregar() -> None:
    # tenta carregar itens.json para memoria no inicio

def salvar() -> None:
    # grava lista itens em itens.json

def adicionar_item(nome: str, quantidade: int) -> None:
    # valida: nome nao vazio, quantidade >= 0
    # atualiza memoria E chama salvar()
```

No `main`:

1) Chame `carregar()` ao iniciar.
2) Adicione 2 itens validos (ex.: `"Caderno"`, `50` e `"Caneta"`, `100`).
3) Exiba itens apos cada operacao.

Exemplo de saida:

```
Itens carregados: 0
Item adicionado: Caderno (50)
Itens: [{'nome': 'Caderno', 'quantidade': 50}]
Item adicionado: Caneta (100)
Itens: [{'nome': 'Caderno', 'quantidade': 50}, {'nome': 'Caneta', 'quantidade': 100}]
```

## Como executar

```bash
cd "36_json_sincronizar_memoria"
python main.py
```
