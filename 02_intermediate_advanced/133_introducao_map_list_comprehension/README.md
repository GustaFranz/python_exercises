# 133 - Introducao a map com list comprehension

## Objetivo

Conhecer `map()` e combinar com list comprehension para transformar e filtrar dados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataClean Escolar |
| **Setor** | Educacao / qualidade de dados |
| **Solicitacao** | Normalizar notas recebidas como texto e listar apenas valores validos. |

## Visao do bloco (exercicios 133 a 136)

Topico **map() + comprehensions**: aplicar funcoes em lote e montar estruturas com comprehensions.

| # | Nivel | Foco |
|---|-------|------|
| 133 | Leve | Introducao: map + list comprehension |
| 134 | Leve | map com lambda + filtro em list comprehension |
| 135 | Ponte | map + dict comprehension |
| 136 | Entrevista | Relatorio comercial com map e comprehensions |

## Enunciado

Dados de entrada:
```python
notas_texto = ["7.5", "8", "abc", "6.0", "-1", "9.5", "5.5"]
```

1) Crie funcao auxiliar:
```python
def converter_seguro(valor: str) -> float | None:
    try:
        return float(valor)
    except ValueError:
        return None
```
2) Converta com `map(converter_seguro, notas_texto)` e filtre `None` em list comprehension.
3) Filtre apenas notas entre `0` e `10` (inclusive) com list comprehension.
4) Exiba: lista original, notas convertidas validas e quantidade aprovada (nota >= 6).

Exemplo de saida:

```
Original: ['7.5', '8', 'abc', '6.0', '-1', '9.5', '5.5']
Validas (0-10): [7.5, 8.0, 6.0, 9.5, 5.5]
Aprovadas (>= 6): 4
```

## Passo a passo

1. Crie a lista `notas_texto` com os dados do enunciado.
2. Defina `converter_seguro(valor: str) -> float | None` com `try/except ValueError`: retorna `float(valor)` no sucesso e `None` se o texto nao for numerico (como `"abc"`).
3. Converta e descarte falhas numa unica list comprehension sobre o map: `notas = [n for n in map(converter_seguro, notas_texto) if n is not None]`.
4. Filtre o intervalo valido com outra list comprehension: `validas = [n for n in notas if 0 <= n <= 10]` (isso elimina o `-1.0`).
5. Conte as aprovadas com `sum(1 for n in validas if n >= 6)` ou `len([n for n in validas if n >= 6])`.
6. Exiba as tres linhas no formato do exemplo: `Original:`, `Validas (0-10):` e `Aprovadas (>= 6):`.

## Como executar

```bash
cd "133_introducao_map_list_comprehension"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
notas_texto = ["7.5", "8", "abc", "6.0", "-1", "9.5", "5.5"]


def converter_seguro(valor: str) -> float | None:
    # try/except item a item: um texto invalido nao derruba o lote inteiro
    try:
        return float(valor)
    except ValueError:
        return None  # None marca o item como "nao conversivel"


# map aplica a conversao a cada item; a comprehension descarta os None
notas = [n for n in map(converter_seguro, notas_texto) if n is not None]

# Segunda comprehension: mantem apenas o intervalo de nota valido (0 a 10)
validas = [n for n in notas if 0 <= n <= 10]

# Conta as aprovadas sem criar lista: gera 1 para cada nota >= 6 e soma
aprovadas = sum(1 for n in validas if n >= 6)

print(f"Original: {notas_texto}")
print(f"Validas (0-10): {validas}")
print(f"Aprovadas (>= 6): {aprovadas}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Limpeza de notas recebidas como texto (pipeline transformar -> filtrar)."""

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0
NOTA_APROVACAO = 6.0


def converter_seguro(valor: str) -> float | None:
    """Converte texto em float; None sinaliza entrada invalida.

    Padrao comum em limpeza de dados: nunca deixar um registro
    sujo interromper o processamento do lote.
    """
    try:
        return float(valor)
    except ValueError:
        return None


def filtrar_validas(notas_texto: list[str]) -> list[float]:
    """Converte e mantem apenas notas dentro do intervalo permitido."""
    # Uma unica comprehension encadeia conversao + dois filtros;
    # o walrus (:=) guarda a conversao para reusar no filtro de intervalo
    return [
        nota
        for texto in notas_texto
        if (nota := converter_seguro(texto)) is not None
        and NOTA_MINIMA <= nota <= NOTA_MAXIMA
    ]


def main() -> None:
    notas_texto = ["7.5", "8", "abc", "6.0", "-1", "9.5", "5.5"]

    validas = filtrar_validas(notas_texto)
    aprovadas = sum(1 for nota in validas if nota >= NOTA_APROVACAO)

    print(f"Original: {notas_texto}")
    print(f"Validas (0-10): {validas}")
    print(f"Aprovadas (>= 6): {aprovadas}")


if __name__ == "__main__":
    main()
```

</details>
