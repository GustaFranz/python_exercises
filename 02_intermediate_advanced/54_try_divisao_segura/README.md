# 54 - Try except: divisao segura

## Objetivo

Implemente media_segura(valores) com try/except.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | CalcEscolar |
| **Setor** | Educacao / matematica |
| **Solicitacao** | Calcular media de turma sem travar quando lista vier vazia. |

## Enunciado

Implemente:

```python
def media_segura(valores: list) -> float | None:
    try:
        return sum(valores) / len(valores)
    except ZeroDivisionError:
        print("Lista vazia")
        return None
```

No `main`, teste:

1) `[8, 7, 9]` — exiba a media retornada.
2) `[]` — exiba a mensagem e o retorno `None`.

Exemplo de saida:

```
Media: 8.0
Lista vazia
Media: None
```

## Passo a passo

1. Defina `def media_segura(valores: list) -> float | None:`.
2. No `try:`, retorne `sum(valores) / len(valores)` — quando a lista e vazia, `len(valores)` e `0` e a divisao levanta `ZeroDivisionError`.
3. No `except ZeroDivisionError:`, exiba `"Lista vazia"` e retorne `None`.
4. No fluxo principal, teste com `[8, 7, 9]`: guarde o retorno em uma variavel e exiba `f"Media: {resultado}"`.
5. Teste com `[]`: a funcao imprime `"Lista vazia"` e retorna `None`; exiba `f"Media: {resultado}"` do mesmo jeito para ver o `None`.

## Como executar

```bash
cd "54_try_divisao_segura"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def media_segura(valores):
    try:
        # Lista vazia -> len == 0 -> ZeroDivisionError na divisao
        return sum(valores) / len(valores)
    except ZeroDivisionError:
        # Trata o caso vazio sem derrubar o programa
        print("Lista vazia")
        return None


# Teste 1: lista com notas — media normal
resultado = media_segura([8, 7, 9])
print(f"Media: {resultado}")

# Teste 2: lista vazia — imprime "Lista vazia" e retorna None
resultado = media_segura([])
print(f"Media: {resultado}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Media de notas tolerante a lista vazia."""


def media_segura(valores: list[float]) -> float | None:
    """Retorna a media dos valores, ou None quando a lista e vazia.

    O except pratica o tratamento pedido no exercicio; em producao
    tambem seria comum o guard `if not valores: return None`.
    """
    try:
        return sum(valores) / len(valores)
    except ZeroDivisionError:
        print("Lista vazia")
        return None


def main() -> None:
    # Cenarios do enunciado: turma com notas e turma vazia
    for notas in ([8, 7, 9], []):
        resultado = media_segura(notas)
        print(f"Media: {resultado}")


if __name__ == "__main__":
    main()
```

</details>
