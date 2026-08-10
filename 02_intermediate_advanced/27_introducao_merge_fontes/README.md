# 27 - Introducao a merge de fontes

## Objetivo

Conhecer merge de dados e o mapa dos exercicios 27 a 31.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Dados educacionais |
| **Solicitacao** | Unificar lista de nomes com dicionario de notas para boletim. |

## Visao do bloco (exercicios 27 a 31)

Topico **merge de fontes**: cruzar dados de estruturas diferentes.

| # | Foco |
|---|------|
| 27 | Introducao + nomes e notas |
| 28 | Left join simples |
| 29 | Tratar ausentes |
| 30 | Provas + simulados |
| 31 | Relatorio com inconsistencias |

## Enunciado

nomes = ["Ana", "Bruno", "Carla", "Daniel"]
notas_por_nome = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
Gere boletim unificado: lista de dicts {"nome": ..., "nota": ...}
Para nomes sem nota, use nota = None.
Exiba boletim e quantos ficaram sem nota.

## Passo a passo

1. Declare a lista `nomes` e o dicionario `notas_por_nome` do enunciado.
2. Crie a lista vazia `boletim` que vai receber os registros unificados.
3. Percorra `for nome in nomes:` — a lista de nomes e a fonte principal do merge.
4. Dentro do loop, busque a nota com `notas_por_nome.get(nome)` — o `.get()` retorna `None` automaticamente quando a chave nao existe (exatamente o valor pedido para ausentes).
5. Faca `boletim.append({"nome": nome, "nota": nota})`.
6. Conte os sem nota com `sem_nota = sum(1 for b in boletim if b["nota"] is None)`.
7. Exiba cada registro do boletim com f-string (mostre algo como `sem nota` quando o valor for `None`) e, no final, o total de alunos sem nota.

## Como executar

```bash
cd "27_introducao_merge_fontes"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Fonte principal: todos os alunos da turma.
nomes = ["Ana", "Bruno", "Carla", "Daniel"]
# Fonte secundaria: notas lancadas (Daniel ainda nao tem nota).
notas_por_nome = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}

# Merge: para cada nome, busca a nota; .get() devolve None se ausente.
boletim = [
    {"nome": nome, "nota": notas_por_nome.get(nome)}
    for nome in nomes
]

# Conta quantos registros ficaram com nota None.
# sum(1 for ...) soma 1 a cada item que passa no filtro.
sem_nota = sum(1 for b in boletim if b["nota"] is None)

# Exibe o boletim unificado, tratando None na formatacao.
print("=== Boletim unificado ===")
for registro in boletim:
    if registro["nota"] is None:
        print(f"{registro['nome']}: sem nota")
    else:
        print(f"{registro['nome']}: {registro['nota']}")

print(f"Alunos sem nota: {sem_nota}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Unifica lista de alunos com dicionario de notas em um boletim."""

# Fonte principal (todos os alunos) e fonte secundaria (notas lancadas).
NOMES = ["Ana", "Bruno", "Carla", "Daniel"]
NOTAS_POR_NOME = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}

# Alias de tipo documenta o formato de cada registro do boletim.
RegistroBoletim = dict[str, object]


def montar_boletim(
    nomes: list[str], notas: dict[str, float]
) -> list[RegistroBoletim]:
    """Cruza nomes com notas; alunos sem nota recebem None."""
    # dict.get(chave) retorna None quando a chave nao existe,
    # dispensando if/else para tratar ausencia.
    return [{"nome": nome, "nota": notas.get(nome)} for nome in nomes]


def formatar_nota(nota: object) -> str:
    """Converte a nota em texto amigavel para exibicao."""
    return "sem nota" if nota is None else str(nota)


def main() -> None:
    boletim = montar_boletim(NOMES, NOTAS_POR_NOME)

    # Contagem dos ausentes direto sobre o boletim ja montado.
    sem_nota = sum(1 for b in boletim if b["nota"] is None)

    print("=== Boletim unificado ===")
    for registro in boletim:
        print(f"{registro['nome']}: {formatar_nota(registro['nota'])}")

    print(f"Alunos sem nota: {sem_nota}")


if __name__ == "__main__":
    main()
```

</details>
