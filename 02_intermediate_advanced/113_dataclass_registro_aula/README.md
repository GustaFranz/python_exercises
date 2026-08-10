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

## Como executar

```bash
cd "113_dataclass_registro_aula"
python main.py
```
