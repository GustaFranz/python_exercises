# 123 - Assert: casos de borda

## Objetivo

Testar bordas como valor minimo, maximo e lista unitaria.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Validar funcao de nota maxima que sera usada em todo o sistema. |

## Enunciado

Implemente:

```python
def nota_maxima(notas: list) -> int | None:
    # retorna max(notas) ou None se lista vazia
```

Escreva asserts de teste:

```python
assert nota_maxima([6, 9, 7]) == 9
assert nota_maxima([5]) == 5
assert nota_maxima([]) is None
```

Trate lista vazia explicitamente no codigo (caso de borda).

## Como executar

```bash
cd "123_assert_casos_borda"
python main.py
```
