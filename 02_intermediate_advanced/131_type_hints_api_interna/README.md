# 131 - Type hints: API interna completa

## Objetivo

Montar API interna tipada com docstrings e asserts de validacao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / formacao dev |
| **Solicitacao** | Entregar modulo de biblioteca escolar com contrato tipado para o time. |

## Estrutura de arquivos

```
131_type_hints_api_interna/
├── main.py
└── biblioteca.py
```

## Enunciado

Em `biblioteca.py`, crie:

```python
@dataclass
class Livro:
    titulo: str
    autor: str
    ano: int

def cadastrar_livro(titulo: str, autor: str, ano: int) -> Livro:
    # assert ano >= 0; docstring obrigatoria

def buscar_por_autor(livros: list[Livro], autor: str) -> list[Livro]:
    # docstring obrigatoria

def relatorio(livros: list[Livro]) -> str:
    # docstring obrigatoria
```

No `main.py`:

1) Cadastre 2 livros com autores diferentes.
2) Busque por autor e gere relatorio.
3) Escreva asserts de teste validando cadastro, busca e relatorio.

Requisitos:
- Docstring em cada funcao publica.
- `assert ano >= 0` em `cadastrar_livro`.
- Demonstracao completa do fluxo com asserts.

## Passo a passo

1. Em `biblioteca.py`, crie a `@dataclass Livro` com os campos `titulo: str`, `autor: str` e `ano: int` (o decorator gera `__init__` e `__repr__` automaticamente).
2. Defina `cadastrar_livro(titulo: str, autor: str, ano: int) -> Livro` com docstring; dentro, valide `assert ano >= 0, "ano nao pode ser negativo"` e retorne `Livro(titulo, autor, ano)`.
3. Defina `buscar_por_autor(livros: list[Livro], autor: str) -> list[Livro]` com docstring, usando list comprehension: `[livro for livro in livros if livro.autor == autor]`.
4. Defina `relatorio(livros: list[Livro]) -> str` com docstring, montando uma string com uma linha por livro no formato `"titulo (autor, ano)"` — acumule as linhas numa lista e junte com `"\n".join(...)`.
5. Em `main.py`, importe as funcoes (`from biblioteca import ...`), cadastre 2 livros com autores diferentes e monte a lista `acervo`.
6. Escreva os asserts de teste:
   - cadastro: `assert livro1.titulo == ...` e `assert isinstance(livro1, Livro)`;
   - busca: `assert buscar_por_autor(acervo, autor_do_livro1) == [livro1]` e busca por autor inexistente retorna `[]`;
   - relatorio: `assert titulo_do_livro1 in relatorio(acervo)`.
7. Exiba o relatorio e a mensagem `Todos os testes passaram.` ao final.

## Como executar

```bash
cd "131_type_hints_api_interna"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`biblioteca.py`**

```python
"""API interna da biblioteca escolar — modulo tipado."""

from dataclasses import dataclass


@dataclass
class Livro:
    # dataclass gera __init__, __repr__ e __eq__ a partir dos campos tipados
    titulo: str
    autor: str
    ano: int


def cadastrar_livro(titulo: str, autor: str, ano: int) -> Livro:
    """Cria um Livro validado.

    Args:
        titulo: titulo da obra.
        autor: nome do autor.
        ano: ano de publicacao (>= 0).

    Returns:
        Instancia de Livro.
    """
    # assert documenta e valida a pre-condicao durante o desenvolvimento
    assert ano >= 0, f"ano nao pode ser negativo: {ano}"
    return Livro(titulo, autor, ano)


def buscar_por_autor(livros: list[Livro], autor: str) -> list[Livro]:
    """Filtra livros de um autor.

    Args:
        livros: acervo completo.
        autor: nome exato do autor.

    Returns:
        Lista (possivelmente vazia) dos livros do autor.
    """
    # List comprehension: filtro direto pelo atributo da dataclass
    return [livro for livro in livros if livro.autor == autor]


def relatorio(livros: list[Livro]) -> str:
    """Gera relatorio textual do acervo.

    Args:
        livros: acervo completo.

    Returns:
        Uma linha por livro no formato "titulo (autor, ano)".
    """
    linhas = ["=== Acervo da biblioteca ==="]
    for livro in livros:
        linhas.append(f"- {livro.titulo} ({livro.autor}, {livro.ano})")
    # join monta a string final com quebras de linha
    return "\n".join(linhas)
```

**`main.py`**

```python
from biblioteca import Livro, buscar_por_autor, cadastrar_livro, relatorio

# 1) Cadastro de 2 livros com autores diferentes
livro1 = cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = cadastrar_livro("Vidas Secas", "Graciliano Ramos", 1938)
acervo = [livro1, livro2]

# 2) Busca por autor + relatorio
machado = buscar_por_autor(acervo, "Machado de Assis")
texto = relatorio(acervo)
print(texto)

# 3) Asserts validando cadastro, busca e relatorio
assert isinstance(livro1, Livro), "cadastrar_livro deve retornar Livro"
assert livro1.titulo == "Dom Casmurro", "titulo deve ser preservado"
assert machado == [livro1], "busca deveria retornar apenas o livro do Machado"
assert buscar_por_autor(acervo, "Clarice Lispector") == [], "autor sem livros -> lista vazia"
assert "Vidas Secas" in texto, "relatorio deve conter todos os titulos"

print("\nTodos os testes passaram.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`biblioteca.py`**

```python
"""API interna da biblioteca escolar — modulo tipado.

Contrato do modulo: dataclass imutavel + funcoes puras.
Em producao, os asserts de pre-condicao virariam ValueError
(assert pode ser desligado com python -O).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Livro:
    """Registro imutavel de livro: frozen evita alteracao acidental."""

    titulo: str
    autor: str
    ano: int


def cadastrar_livro(titulo: str, autor: str, ano: int) -> Livro:
    """Cria um Livro validado.

    Args:
        titulo: titulo da obra.
        autor: nome do autor.
        ano: ano de publicacao (>= 0).

    Returns:
        Instancia imutavel de Livro.
    """
    assert ano >= 0, f"ano nao pode ser negativo: {ano}"
    return Livro(titulo=titulo, autor=autor, ano=ano)


def buscar_por_autor(livros: list[Livro], autor: str) -> list[Livro]:
    """Retorna os livros do autor informado (lista vazia se nenhum)."""
    return [livro for livro in livros if livro.autor == autor]


def relatorio(livros: list[Livro]) -> str:
    """Formata o acervo em texto, uma linha por livro."""
    # Generator dentro do join: formata sem lista intermediaria
    corpo = "\n".join(f"- {l.titulo} ({l.autor}, {l.ano})" for l in livros)
    return f"=== Acervo da biblioteca ===\n{corpo}"
```

**`main.py`**

```python
"""Demonstracao do fluxo + suite de asserts da API da biblioteca.

Com pytest, cada bloco de asserts viraria um test_* e o acervo
seria montado por uma fixture.
"""

from biblioteca import Livro, buscar_por_autor, cadastrar_livro, relatorio


def montar_acervo() -> list[Livro]:
    """Centraliza os dados de exemplo usados na demo e nos testes."""
    return [
        cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899),
        cadastrar_livro("Vidas Secas", "Graciliano Ramos", 1938),
    ]


def testar_api() -> None:
    """Valida cadastro, busca e relatorio de ponta a ponta."""
    acervo = montar_acervo()
    dom_casmurro = acervo[0]

    # Cadastro: tipo e campos preservados
    assert isinstance(dom_casmurro, Livro), "cadastrar_livro deve retornar Livro"
    assert dom_casmurro.titulo == "Dom Casmurro", "titulo deve ser preservado"

    # Busca: autor existente e inexistente
    assert buscar_por_autor(acervo, "Machado de Assis") == [dom_casmurro]
    assert buscar_por_autor(acervo, "Clarice Lispector") == []

    # Relatorio: todos os titulos presentes
    texto = relatorio(acervo)
    assert "Dom Casmurro" in texto and "Vidas Secas" in texto


def main() -> None:
    print(relatorio(montar_acervo()))
    testar_api()
    print("\nTodos os testes passaram.")


if __name__ == "__main__":
    main()
```

</details>
