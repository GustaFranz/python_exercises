# 127 - Introducao a type hints

## Objetivo

Anotar funcoes de cadastro com tipos basicos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / desenvolvimento |
| **Solicitacao** | Documentar tipos do modulo de cadastro para facilitar manutencao. |

## Visao do bloco (exercicios 127 a 131)

Topico **Type hints basicos**: anotar parametros e retornos para clareza.

| # | Foco |
|---|------|
| 127 | Introducao + hints em cadastro |
| 128 | list[str] e dict[str, float] |
| 129 | Retorno opcional com None |
| 130 | Modulo publico tipado com resumo_mensalidades estruturado |
| 131 | API interna tipada + docstrings + asserts |

## Enunciado

Implemente com type hints completos:

```python
def criar_aluno(nome: str, matricula: int, turma: str) -> dict[str, str | int]:
    ...

def exibir_aluno(aluno: dict[str, str | int]) -> str:
    ...
```

No `main`:

1) Crie um aluno (ex.: `"Ana Silva"`, matricula `101`, turma `"7A"`).
2) Exiba a string formatada retornada por `exibir_aluno`.

Exemplo de saida:

```
Aluno: Ana Silva | Matricula: 101 | Turma: 7A
```

## Passo a passo

1. Defina `criar_aluno(nome: str, matricula: int, turma: str) -> dict[str, str | int]` retornando o dict `{"nome": nome, "matricula": matricula, "turma": turma}`. Note o retorno `dict[str, str | int]`: chaves sao `str`, valores podem ser `str` OU `int`.
2. Defina `exibir_aluno(aluno: dict[str, str | int]) -> str` retornando a f-string `f"Aluno: {aluno['nome']} | Matricula: {aluno['matricula']} | Turma: {aluno['turma']}"` — a funcao RETORNA a string, quem imprime e o chamador.
3. No fluxo principal, chame `criar_aluno("Ana Silva", 101, "7A")`, guarde o dict e imprima o retorno de `exibir_aluno`.
4. Passe o mouse sobre as funcoes na IDE e observe como os hints documentam os tipos (eles nao sao validados em runtime — sao documentacao para leitura, IDE e ferramentas como mypy).

## Como executar

```bash
cd "127_introducao_type_hints"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar_aluno(nome: str, matricula: int, turma: str) -> dict[str, str | int]:
    # dict[str, str | int]: chaves str, valores podem ser str OU int
    # (nome e turma sao str, matricula e int)
    return {"nome": nome, "matricula": matricula, "turma": turma}


def exibir_aluno(aluno: dict[str, str | int]) -> str:
    # Retorna a string formatada — imprimir e responsabilidade de quem chama
    return f"Aluno: {aluno['nome']} | Matricula: {aluno['matricula']} | Turma: {aluno['turma']}"


# Cria o aluno de exemplo e exibe a string retornada
aluno = criar_aluno("Ana Silva", 101, "7A")
print(exibir_aluno(aluno))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cadastro de alunos com contrato tipado.

TypedDict e mais preciso que dict[str, str | int]: documenta o nome
e o tipo de CADA campo, e o mypy acusa erro se algum faltar.
"""

from typing import TypedDict


class Aluno(TypedDict):
    """Estrutura do registro de aluno: cada campo com seu tipo exato."""

    nome: str
    matricula: int
    turma: str


def criar_aluno(nome: str, matricula: int, turma: str) -> Aluno:
    """Monta o registro do aluno ja no formato tipado."""
    return {"nome": nome, "matricula": matricula, "turma": turma}


def exibir_aluno(aluno: Aluno) -> str:
    """Formata o registro para exibicao (nao imprime: retorna a string)."""
    return f"Aluno: {aluno['nome']} | Matricula: {aluno['matricula']} | Turma: {aluno['turma']}"


def main() -> None:
    aluno = criar_aluno("Ana Silva", 101, "7A")
    print(exibir_aluno(aluno))


if __name__ == "__main__":
    main()
```

</details>
