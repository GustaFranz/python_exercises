# 16 - Introducao a zip

## Objetivo

Conhecer zip e o mapa dos exercicios 16 a 20.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Avalia Escolar Online |
| **Setor** | Edtech / avaliacoes |
| **Solicitacao** | Parear nomes de alunos com notas para boletim rapido. |

## Visao do bloco (exercicios 16 a 20)

Topico **zip**: cruzar listas paralelas e montar estruturas.

| # | Foco |
|---|------|
| 16 | Introducao + boletim nome/nota |
| 17 | Tuplas produto/preco/estoque |
| 18 | Listas para dicionario |
| 19 | Vendas vs custos |
| 20 | Tres listas consolidadas |

## Enunciado

nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 6.0, 9.0]
Use zip para gerar pares nome-nota e exiba um boletim simples:
Ana: 8.5
Bruno: 6.0
...
Exiba tambem a media da turma.

## Passo a passo

1. Crie as listas paralelas `nomes = ["Ana", "Bruno", "Carla"]` e `notas = [8.5, 6.0, 9.0]`.
2. Percorra as duas listas juntas com `for nome, nota in zip(nomes, notas):` — o zip alinha os elementos pela posicao.
3. Dentro do loop, exiba cada linha do boletim no formato `nome: nota`.
4. Calcule a media da turma com `sum(notas) / len(notas)`.
5. Exiba a media ao final, formatada com 1 ou 2 casas decimais (ex.: `f"{media:.2f}"`).

## Como executar

```bash
cd "16_introducao_zip_estruturas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Listas paralelas: mesma posicao = mesmo aluno (enunciado)
nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 6.0, 9.0]

# zip alinha nome e nota pela posicao e o for desempacota o par direto
print("=== BOLETIM DA TURMA ===")
for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")

# Media aritmetica simples da turma
media = sum(notas) / len(notas)
print(f"Media da turma: {media:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Boletim rapido: pareia nomes e notas e calcula a media da turma."""

from statistics import fmean


def montar_boletim(nomes: list[str], notas: list[float]) -> list[tuple[str, float]]:
    """Pareia nome e nota pela posicao.

    strict=True falha se as listas tiverem tamanhos diferentes:
    melhor um erro claro do que um boletim truncado em silencio.
    """
    return list(zip(nomes, notas, strict=True))


def main() -> None:
    # Dados de entrada do enunciado
    nomes = ["Ana", "Bruno", "Carla"]
    notas = [8.5, 6.0, 9.0]

    # Monta os pares nome-nota
    boletim = montar_boletim(nomes, notas)

    # Exibe uma linha por aluno
    print("=== BOLETIM DA TURMA ===")
    for nome, nota in boletim:
        print(f"{nome}: {nota}")

    # fmean: media aritmetica da stdlib, direta e legivel
    print(f"Media da turma: {fmean(notas):.2f}")


if __name__ == "__main__":
    main()
```

</details>
