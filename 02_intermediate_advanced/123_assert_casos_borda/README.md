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

## Passo a passo

1. Defina `nota_maxima(notas: list) -> int | None`.
2. Dentro da funcao, trate a borda primeiro: `if not notas: return None` (lista vazia e "falsy" em Python).
3. No caso normal, retorne `max(notas)`.
4. Escreva os tres asserts do enunciado: caso comum (`[6, 9, 7]` -> `9`), lista unitaria (`[5]` -> `5`) e lista vazia (`[]` -> `None`). Use `is None` (identidade) e nao `== None`.
5. Exiba `print("Todos os testes passaram.")` apos os asserts.

## Como executar

```bash
cd "123_assert_casos_borda"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def nota_maxima(notas: list) -> int | None:
    # Caso de borda tratado primeiro: lista vazia nao tem maximo
    # (sem esse if, max([]) levantaria ValueError)
    if not notas:
        return None
    # Caso normal: max() resolve lista unitaria e lista comum
    return max(notas)


# Caso comum: varios valores
assert nota_maxima([6, 9, 7]) == 9, "maximo de [6, 9, 7] deveria ser 9"
# Borda: lista unitaria — o maximo e o unico elemento
assert nota_maxima([5]) == 5, "lista unitaria deve retornar o proprio valor"
# Borda: lista vazia — usar 'is None' pois comparamos identidade
assert nota_maxima([]) is None, "lista vazia deve retornar None"

print("Todos os testes passaram.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Nota maxima com tratamento explicito de borda.

Com pytest, cada caso viraria um teste nomeado (test_lista_vazia, etc.)
e casos parametrizados usariam @pytest.mark.parametrize.
"""


def nota_maxima(notas: list[int]) -> int | None:
    """Retorna a maior nota ou None se a lista estiver vazia.

    O retorno opcional (int | None) documenta no proprio tipo
    que quem chama PRECISA tratar o caso de lista vazia.
    """
    # max() aceita default: elimina o if e ainda cobre a lista vazia
    return max(notas, default=None)


def testar_nota_maxima() -> None:
    """Cobre caso comum e as duas bordas classicas: unitaria e vazia."""
    assert nota_maxima([6, 9, 7]) == 9, "maximo de [6, 9, 7] deveria ser 9"
    assert nota_maxima([5]) == 5, "lista unitaria deve retornar o proprio valor"
    assert nota_maxima([]) is None, "lista vazia deve retornar None"


if __name__ == "__main__":
    testar_nota_maxima()
    print("Todos os testes passaram.")
```

</details>
