# 125 - Assert: suite CRUD em memoria

## Objetivo

Montar suite de asserts para CRUD simples em lista de dicts.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Validar modulo de cadastro em memoria antes de conectar ao banco. |

## Enunciado

Cada item e um dict com campo `"id"`. Implemente em memoria:

```python
def criar(lista: list, item: dict) -> None:
    # append na lista

def buscar_por_id(lista: list, id: int) -> dict | None:
    # retorna dict ou None

def remover(lista: list, id: int) -> bool:
    # retorna True se removeu, False se nao encontrou
```

Escreva suite de asserts em sequencia:

1) Crie 2 itens (ex.: `{"id": 1, "nome": "Ana"}` e `{"id": 2, "nome": "Bruno"}`).
2) Busque id existente — assert retorno correto.
3) Busque id inexistente — assert `None`.
4) Remova id existente — assert `True` e `len(lista)` correto em cada etapa.

## Como executar

```bash
cd "125_assert_suite_crud"
python main.py
```
