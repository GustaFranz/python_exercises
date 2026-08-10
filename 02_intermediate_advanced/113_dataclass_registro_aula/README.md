# 113 - Dataclass: RegistroAula

## Objetivo

Modelar registro de aula com dataclass e campos de data.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / diario de classe |
| **Solicitacao** | Registrar aulas ministradas com estrutura padronizada. |

## Enunciado

Crie a dataclass:

```python
@dataclass
class RegistroAula:
    disciplina: str
    turma: str
    data: str      # formato "AAAA-MM-DD"
    presentes: int
```

No `main`:

1) Cadastre 2 registros com dados diferentes (ex.: `"Matematica"`, turma `"7A"`, data `"2026-08-15"`, `28` presentes).
2) Exiba cada registro com `print(registro)` — o `__repr__` e gerado automaticamente.

Exemplo de saida:

```
RegistroAula(disciplina='Matematica', turma='7A', data='2026-08-15', presentes=28)
RegistroAula(disciplina='Portugues', turma='8B', data='2026-08-16', presentes=25)
```

## Passo a passo

1. Importe o decorador: `from dataclasses import dataclass`.
2. Declare `@dataclass` sobre `class RegistroAula:` com os 4 campos anotados na ordem do enunciado: `disciplina: str`, `turma: str`, `data: str` (formato `"AAAA-MM-DD"`) e `presentes: int`.
3. No `main`, cadastre o primeiro registro: `RegistroAula("Matematica", "7A", "2026-08-15", 28)`.
4. Cadastre o segundo com dados diferentes: `RegistroAula("Portugues", "8B", "2026-08-16", 25)`.
5. Exiba cada registro com `print(registro)` e confira que a saida segue o formato `RegistroAula(disciplina='...', turma='...', data='...', presentes=...)` gerado pelo `__repr__` automatico.

## Como executar

```bash
cd "113_dataclass_registro_aula"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from dataclasses import dataclass


# A dataclass elimina o __init__ manual: os campos anotados viram
# parametros do construtor na mesma ordem
@dataclass
class RegistroAula:
    disciplina: str
    turma: str
    data: str      # formato "AAAA-MM-DD"
    presentes: int


# Dois registros do diario de classe com dados diferentes
aula1 = RegistroAula("Matematica", "7A", "2026-08-15", 28)
aula2 = RegistroAula("Portugues", "8B", "2026-08-16", 25)

# print usa o __repr__ gerado automaticamente pela dataclass,
# que mostra todos os campos com nome e valor
print(aula1)
print(aula2)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass


# frozen=True: um registro de aula e um fato historico — depois de
# lancado no diario, nao deve ser alterado por engano.
# slots=True: menos memoria por instancia (relevante em bases grandes).
@dataclass(frozen=True, slots=True)
class RegistroAula:
    """Registro de uma aula ministrada no diario de classe."""

    disciplina: str
    turma: str
    data: str  # ISO "AAAA-MM-DD"; ordenavel como texto por ser ano-mes-dia
    presentes: int


def main() -> None:
    # Registros em lista: pronto para crescer e alimentar relatorios
    registros = [
        RegistroAula("Matematica", "7A", "2026-08-15", 28),
        RegistroAula("Portugues", "8B", "2026-08-16", 25),
    ]

    for registro in registros:
        print(registro)


if __name__ == "__main__":
    main()
```

</details>
