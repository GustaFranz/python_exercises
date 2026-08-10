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

## Passo a passo

1. Defina `buscar_aluno(alunos: list[dict[str, str]], nome: str) -> dict[str, str] | None`. O `| None` no retorno avisa quem chama: "posso nao encontrar nada".
2. Dentro da funcao, percorra `alunos` com `for` e compare `aluno["nome"] == nome`; se bater, retorne o dict.
3. Apos o loop (sem `else`), retorne `None` — so chega ali se ninguem foi encontrado.
4. No fluxo principal, monte a lista com `{"nome": "Ana", "turma": "7A"}` e `{"nome": "Bruno", "turma": "8B"}`.
5. Busque `"Ana"` e exiba `Encontrado: {resultado}`; busque `"Carla"` e exiba `Nao encontrado: {resultado}` (deve imprimir `None`).

## Como executar

```bash
cd "129_type_hints_retorno_opcional"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def buscar_aluno(alunos: list[dict[str, str]], nome: str) -> dict[str, str] | None:
    # O hint "| None" documenta que a busca pode falhar —
    # quem chama sabe que precisa tratar o caso None
    for aluno in alunos:
        if aluno["nome"] == nome:
            return aluno
    # So chega aqui se o for terminou sem encontrar
    return None


alunos = [
    {"nome": "Ana", "turma": "7A"},
    {"nome": "Bruno", "turma": "8B"},
]

# Busca que encontra: retorna o dict completo
print(f"Encontrado: {buscar_aluno(alunos, 'Ana')}")
# Busca que falha: retorna None (e o print exibe 'None')
print(f"Nao encontrado: {buscar_aluno(alunos, 'Carla')}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Busca de aluno com retorno opcional tipado.

dict[str, str] | None e a sintaxe moderna (Python 3.10+);
em codigo legado voce vera Optional[dict[str, str]] — significam o mesmo.
"""


def buscar_aluno(alunos: list[dict[str, str]], nome: str) -> dict[str, str] | None:
    """Retorna o primeiro aluno com o nome informado, ou None.

    next() com default resolve a busca em uma expressao:
    o generator para no primeiro match, sem percorrer o resto.
    """
    return next((aluno for aluno in alunos if aluno["nome"] == nome), None)


def main() -> None:
    alunos = [
        {"nome": "Ana", "turma": "7A"},
        {"nome": "Bruno", "turma": "8B"},
    ]
    print(f"Encontrado: {buscar_aluno(alunos, 'Ana')}")
    print(f"Nao encontrado: {buscar_aluno(alunos, 'Carla')}")


if __name__ == "__main__":
    main()
```

</details>
