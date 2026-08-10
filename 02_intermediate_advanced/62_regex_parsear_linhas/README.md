# 62 - Regex: parsear linhas de exportacao escolar

## Objetivo

Extrair dados estruturados de linhas CSV-like com regex, rejeitar sujeira e filtrar por turma.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / importacao |
| **Solicitacao** | Validar lote de exportacao nome;nota;turma antes de carregar no sistema, com relatorio de rejeicoes. |

## Enunciado

Linhas de entrada (incluindo linhas sujas):

```
Ana;7.5;7A
Bruno;8.0;7B
;6.0;7A
Carla;nota;7A
Pedro;5.5;7A
7A;12.0;7A
Lucas;9.2;7B
```

- Para cada linha, use `re.search` com padrao tipo `^(.+);([\d.]+);(\w+)$` (ajuste se necessario).
- Monte `alunos_validos` como lista de dicts `{nome, nota, turma}` (nota como `float`).
- Rejeite linhas invalidas e acumule `rejeitadas` com a linha original.
- Filtre e exiba alunos da turma `7A`.
- Relatorio final: total recebido, validos, rejeitados, lista de rejeitadas.

## Passo a passo

1. Importe `re` e crie a lista `linhas` com as 7 strings do enunciado.
2. Crie duas listas vazias: `alunos_validos` e `rejeitadas`.
3. Defina a funcao `parsear_linha(linha: str) -> dict | None`:
   - use `re.search(r"^(.+);([\d.]+);(\w+)$", linha)` para tentar casar a linha;
   - se nao casar, retorne `None`;
   - extraia `nome = match.group(1).strip()`, `nota = float(match.group(2))` e `turma = match.group(3)`;
   - aplique as regras de negocio: se `nome` ficou vazio apos o strip, ou se `nota` esta fora de 0 a 10, retorne `None`;
   - se passou em tudo, retorne o dict `{"nome": nome, "nota": nota, "turma": turma}`.
4. Percorra `linhas` com um `for`: se `parsear_linha` retornar um dict, adicione em `alunos_validos`; se retornar `None`, adicione a linha original em `rejeitadas`.
5. Filtre os alunos da turma `7A` com list comprehension (`[a for a in alunos_validos if a["turma"] == "7A"]`) e exiba nome e nota de cada um.
6. Exiba o relatorio final: total de linhas recebidas (`len(linhas)`), total de validos, total de rejeitados e a lista de linhas rejeitadas.

## Como executar

```bash
cd "62_regex_parsear_linhas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import re

# Lote de exportacao recebido, com linhas boas e linhas sujas
linhas = [
    "Ana;7.5;7A",
    "Bruno;8.0;7B",
    ";6.0;7A",
    "Carla;nota;7A",
    "Pedro;5.5;7A",
    "7A;12.0;7A",
    "Lucas;9.2;7B",
]

# Padrao: (.+) = nome, ([\d.]+) = nota numerica, (\w+) = turma
PADRAO = r"^(.+);([\d.]+);(\w+)$"


def parsear_linha(linha):
    # Tenta casar a linha inteira com o padrao esperado
    match = re.search(PADRAO, linha)
    if match is None:
        # Linha fora do formato nome;nota;turma -> invalida
        return None

    # group(N) devolve o texto capturado por cada parenteses do padrao
    nome = match.group(1).strip()
    nota = float(match.group(2))
    turma = match.group(3)

    # Regras de negocio: nome nao pode ser vazio e nota deve estar em 0..10
    if not nome:
        return None
    if not (0 <= nota <= 10):
        return None

    return {"nome": nome, "nota": nota, "turma": turma}


alunos_validos = []
rejeitadas = []

# Classifica cada linha do lote
for linha in linhas:
    aluno = parsear_linha(linha)
    if aluno is not None:
        alunos_validos.append(aluno)
    else:
        # Guarda a linha original para o relatorio de rejeicoes
        rejeitadas.append(linha)

# Filtra apenas a turma 7A com list comprehension
turma_7a = [aluno for aluno in alunos_validos if aluno["turma"] == "7A"]

print("Alunos da turma 7A:")
for aluno in turma_7a:
    print(f"- {aluno['nome']}: {aluno['nota']}")

# Relatorio final de qualidade do lote
print("\n=== Relatorio ===")
print(f"Total recebido: {len(linhas)}")
print(f"Validos: {len(alunos_validos)}")
print(f"Rejeitados: {len(rejeitadas)}")
print("Linhas rejeitadas:")
for linha in rejeitadas:
    print(f"- {linha!r}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Valida lote de exportacao nome;nota;turma e gera relatorio de rejeicoes."""

import re
from dataclasses import dataclass

# Padrao compilado uma unica vez; nomear os grupos documenta o formato esperado
PADRAO_LINHA = re.compile(r"^(?P<nome>.+);(?P<nota>[\d.]+);(?P<turma>\w+)$")

# Faixa valida de notas como constantes (facil de ajustar sem cacar numeros no codigo)
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0


@dataclass
class Aluno:
    """Registro validado de um aluno do lote."""

    nome: str
    nota: float
    turma: str


def parsear_linha(linha: str) -> Aluno | None:
    """Converte uma linha bruta em Aluno; retorna None se a linha for invalida."""
    match = PADRAO_LINHA.search(linha)
    # Guard clause: sai cedo se o formato nao bate
    if match is None:
        return None

    # Grupos nomeados deixam claro o que cada captura significa
    nome = match.group("nome").strip()
    nota = float(match.group("nota"))
    turma = match.group("turma")

    # Guard clauses para as regras de negocio
    if not nome:
        return None
    if not (NOTA_MINIMA <= nota <= NOTA_MAXIMA):
        return None

    return Aluno(nome=nome, nota=nota, turma=turma)


def main() -> None:
    linhas = [
        "Ana;7.5;7A",
        "Bruno;8.0;7B",
        ";6.0;7A",
        "Carla;nota;7A",
        "Pedro;5.5;7A",
        "7A;12.0;7A",
        "Lucas;9.2;7B",
    ]

    validos: list[Aluno] = []
    rejeitadas: list[str] = []

    # Separa o lote em validos e rejeitados em uma unica passada
    for linha in linhas:
        aluno = parsear_linha(linha)
        if aluno is None:
            rejeitadas.append(linha)
        else:
            validos.append(aluno)

    # Filtro por turma usando atributo da dataclass (mais seguro que chave de dict)
    turma_7a = [aluno for aluno in validos if aluno.turma == "7A"]

    print("Alunos da turma 7A:")
    for aluno in turma_7a:
        print(f"- {aluno.nome}: {aluno.nota}")

    print("\n=== Relatorio ===")
    print(f"Total recebido: {len(linhas)}")
    print(f"Validos: {len(validos)}")
    print(f"Rejeitados: {len(rejeitadas)}")
    print("Linhas rejeitadas:")
    for linha in rejeitadas:
        # !r mostra as aspas e evidencia linhas vazias ou com espacos
        print(f"- {linha!r}")


if __name__ == "__main__":
    main()
```

</details>
