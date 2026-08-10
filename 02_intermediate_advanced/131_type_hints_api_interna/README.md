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

## Como executar

```bash
cd "131_type_hints_api_interna"
python main.py
```
