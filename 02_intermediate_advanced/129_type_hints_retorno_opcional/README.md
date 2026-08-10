# 129 - Type hints: retorno opcional

## Objetivo

Indicar retorno opcional com | None nas anotacoes.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Tipar busca de aluno que pode nao existir na base. |

## Enunciado

Implemente:

```python
def buscar_aluno(alunos: list[dict[str, str]], nome: str) -> dict[str, str] | None:
    # retorna dict do aluno ou None se nao encontrar
```

No `main`:

1) Monte lista com 2 alunos (ex.: `{"nome": "Ana", "turma": "7A"}` e `{"nome": "Bruno", "turma": "8B"}`).
2) Busque aluno existente (ex.: `"Ana"`) e exiba resultado.
3) Busque aluno inexistente (ex.: `"Carla"`) e exiba `None`.

Exemplo de saida:

```
Encontrado: {'nome': 'Ana', 'turma': '7A'}
Nao encontrado: None
```

## Como executar

```bash
cd "129_type_hints_retorno_opcional"
python main.py
```
