# 50 - Excecao customizada: nota fora do intervalo

## Objetivo

Crie NotaInvalidaError e validar_nota(nota) entre 0 e 10.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Rejeitar notas digitadas fora da escala 0 a 10. |

## Enunciado

1) Crie a excecao:
```python
class NotaInvalidaError(Exception):
    pass
```

2) Implemente:
```python
def validar_nota(nota: float) -> None:
    # aceita apenas 0 <= nota <= 10
```

3) Teste cada nota em `[-1, 0, 7.5, 10, 11]` com `try/except` separado.
4) Exiba resultado de cada teste: `"Valida"` ou mensagem de erro.

Exemplo de saida:

```
-1: Invalida — nota fora do intervalo 0-10
0: Valida
7.5: Valida
10: Valida
11: Invalida — nota fora do intervalo 0-10
```

## Passo a passo

1. Defina a classe `NotaInvalidaError(Exception)` com corpo `pass` (ou docstring).
2. Defina `def validar_nota(nota: float) -> None:` que levanta `raise NotaInvalidaError("nota fora do intervalo 0-10")` quando a condicao `0 <= nota <= 10` for falsa (use `if not 0 <= nota <= 10:`).
3. Crie a lista de testes `notas = [-1, 0, 7.5, 10, 11]`.
4. Percorra a lista com `for nota in notas:` e, dentro do loop, chame `validar_nota(nota)` em um bloco `try:`.
5. No `except NotaInvalidaError as e:`, exiba `f"{nota}: Invalida — {e}"`.
6. Use `else:` (roda quando nao houve excecao) para exibir `f"{nota}: Valida"`.

## Como executar

```bash
cd "50_excecao_nota_intervalo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Excecao customizada para nota fora da escala da escola
class NotaInvalidaError(Exception):
    pass


def validar_nota(nota):
    # Comparacao encadeada: 0 <= nota <= 10 testa os dois limites de uma vez
    if not 0 <= nota <= 10:
        raise NotaInvalidaError("nota fora do intervalo 0-10")


# Casos de teste do enunciado: dois invalidos e tres validos
notas = [-1, 0, 7.5, 10, 11]

for nota in notas:
    try:
        # Cada nota tem seu proprio try: um erro nao interrompe as demais
        validar_nota(nota)
    except NotaInvalidaError as e:
        # Nota rejeitada: mostra o motivo vindo da excecao
        print(f"{nota}: Invalida — {e}")
    else:
        # else roda somente quando o try passou sem erro
        print(f"{nota}: Valida")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Validacao de notas na escala 0 a 10 com excecao de negocio."""

# Limites da escala como constantes: a regra fica visivel e ajustavel
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0


class NotaInvalidaError(Exception):
    """Nota fora da escala permitida pela escola."""


def validar_nota(nota: float) -> None:
    """Levanta NotaInvalidaError se a nota estiver fora de [NOTA_MINIMA, NOTA_MAXIMA]."""
    if not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
        raise NotaInvalidaError(
            f"nota fora do intervalo {NOTA_MINIMA:g}-{NOTA_MAXIMA:g}"
        )


def main() -> None:
    notas = [-1, 0, 7.5, 10, 11]

    for nota in notas:
        try:
            validar_nota(nota)
        except NotaInvalidaError as erro:
            print(f"{nota}: Invalida — {erro}")
        else:
            print(f"{nota}: Valida")


if __name__ == "__main__":
    main()
```

</details>
