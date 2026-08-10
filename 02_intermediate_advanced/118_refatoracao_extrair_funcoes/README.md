# 118 - Refatoracao: extrair funcoes

## Objetivo

Extrair funcoes de script procedural repetitivo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | CalcEscolar |
| **Setor** | Educacao / matematica |
| **Solicitacao** | Eliminar duplicacao no calculo de medias por turma. |

## Enunciado

Codigo repetitivo a refatorar:

```python
notas_7b = [8, 7, 9]
s1 = 0
for n in notas_7b:
    s1 += n
media_7b = s1 / len(notas_7b)

notas_8a = [6, 8, 7, 9]
s2 = 0
for n in notas_8a:
    s2 += n
media_8a = s2 / len(notas_8a)
```

Tarefas:

1) Extraia `calcular_media(notas) -> float` eliminando a duplicacao.
2) Use a funcao para calcular a media das turmas **7B** e **8A**.
3) Exiba: `Media 7B: ...` e `Media 8A: ...`.

## Passo a passo

1. Observe a duplicacao: o mesmo bloco (acumulador + loop + divisao) aparece duas vezes, mudando apenas a lista e os nomes `s1`/`s2`.
2. Extraia a logica repetida para uma unica funcao `calcular_media(notas) -> float`: some as notas e divida por `len(notas)`.
3. Defina as duas listas do enunciado: `notas_7b = [8, 7, 9]` e `notas_8a = [6, 8, 7, 9]`.
4. Chame `calcular_media(notas_7b)` e `calcular_media(notas_8a)` — a mesma funcao serve para qualquer turma.
5. Exiba os resultados nos formatos `Media 7B: ...` e `Media 8A: ...` (esperado: `8.0` e `7.5`).

## Como executar

```bash
cd "118_refatoracao_extrair_funcoes"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def calcular_media(notas):
    # A logica que estava duplicada (acumulador + loop + divisao)
    # vive agora em UM unico lugar — principio DRY (Don't Repeat Yourself)
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)


# As listas continuam as mesmas do script original
notas_7b = [8, 7, 9]
notas_8a = [6, 8, 7, 9]

# A mesma funcao atende as duas turmas (e qualquer turma futura)
media_7b = calcular_media(notas_7b)
media_8a = calcular_media(notas_8a)

print("Media 7B:", media_7b)
print("Media 8A:", media_8a)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
def calcular_media(notas: list[float]) -> float:
    """Media aritmetica das notas de uma turma."""
    # sum() do proprio Python substitui o loop manual com acumulador:
    # menos codigo, menos chance de erro
    return sum(notas) / len(notas)


def main() -> None:
    # Turmas em dict: adicionar uma turma nova nao exige variavel nova
    turmas = {
        "7B": [8, 7, 9],
        "8A": [6, 8, 7, 9],
    }

    # Um unico loop calcula e exibe a media de todas as turmas
    for nome, notas in turmas.items():
        print(f"Media {nome}: {calcular_media(notas)}")


if __name__ == "__main__":
    main()
```

</details>
