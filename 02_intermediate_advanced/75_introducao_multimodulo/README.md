# 75 - Introducao a projeto multi-modulo

## Objetivo

Organizar codigo em pasta src/ com dois modulos importados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / formacao dev |
| **Solicitacao** | Separar calculos e formatacao em modulos para projeto piloto. |

## Visao do bloco (exercicios 75 a 79)

Topico **Mini-projeto multi-modulo**: dividir responsabilidades em arquivos Python.

| # | Foco |
|---|------|
| 75 | Introducao + src/ com 2 modulos |
| 76 | Import absoluto entre modulos |
| 77 | Separar utils e models |
| 78 | Calculadora de folha com 3 arquivos |
| 79 | Pacote analise_vendas com __init__.py |

## Estrutura de arquivos

```
75_introducao_multimodulo/
├── README.md
├── main.py
└── src/
    ├── calculos.py    # media(lista)
    └── formatacao.py  # formatar_linha(texto)
```

## Enunciado

Implemente nos modulos e importe em `main.py`:

**`src/calculos.py`**
```python
def media(lista: list) -> float:
    return sum(lista) / len(lista)
```

**`src/formatacao.py`**
```python
def formatar_linha(texto: str) -> str:
    return f"[OK] {texto.upper()}"
```

No `main.py`:

1) Importe com caminho absoluto: `from src.calculos import media` e `from src.formatacao import formatar_linha`.
2) Exiba `media([7, 8, 9])` e `formatar_linha("turma 7b")`.

Exemplo de saida:

```
Media: 8.0
[OK] TURMA 7B
```

Rode sempre da pasta do exercicio: `python main.py`.

## Passo a passo

1. Abra `src/calculos.py` e implemente `media(lista)`: retorne `sum(lista) / len(lista)` (soma dividida pela quantidade).
2. Abra `src/formatacao.py` e implemente `formatar_linha(texto)`: retorne `f"[OK] {texto.upper()}"` (prefixo fixo + texto em maiusculas).
3. No `main.py`, importe as duas funcoes com caminho absoluto a partir da pasta do exercicio: `from src.calculos import media` e `from src.formatacao import formatar_linha`.
4. Ainda no `main.py`, chame `media([7, 8, 9])` e exiba no formato `Media: 8.0`.
5. Chame `formatar_linha("turma 7b")` e exiba o retorno (`[OK] TURMA 7B`).
6. Execute sempre de dentro da pasta do exercicio (`python main.py`) — e o diretorio atual que permite o Python encontrar o pacote `src`.

## Como executar

```bash
cd "75_introducao_multimodulo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`src/calculos.py`**

```python
"""Funcoes de calculo do projeto piloto."""


def media(lista):
    """Calcula media aritmetica de uma lista numerica."""
    # Soma de todos os itens dividida pela quantidade de itens
    return sum(lista) / len(lista)
```

**`src/formatacao.py`**

```python
"""Funcoes de formatacao de texto."""


def formatar_linha(texto):
    """Retorna texto em maiusculas com prefixo [OK] ."""
    # upper() padroniza a caixa; o prefixo marca a linha como processada
    return f"[OK] {texto.upper()}"
```

**`main.py`**

```python
# Imports absolutos a partir da pasta do exercicio:
# src e um pacote, calculos e formatacao sao modulos dentro dele
from src.calculos import media
from src.formatacao import formatar_linha

# Usa a funcao de calculo do modulo src/calculos.py
print(f"Media: {media([7, 8, 9])}")

# Usa a funcao de formatacao do modulo src/formatacao.py
print(formatar_linha("turma 7b"))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`src/calculos.py`**

```python
"""Funcoes de calculo do projeto piloto."""


def media(lista: list[float]) -> float:
    """Retorna a media aritmetica de uma lista numerica nao vazia."""
    # Guard clause: falha cedo com mensagem clara em vez de ZeroDivisionError
    if not lista:
        raise ValueError("lista vazia: media indefinida")

    return sum(lista) / len(lista)
```

**`src/formatacao.py`**

```python
"""Funcoes de formatacao de texto."""


def formatar_linha(texto: str) -> str:
    """Retorna o texto em maiusculas prefixado com [OK]."""
    return f"[OK] {texto.upper()}"
```

**`main.py`**

```python
"""Orquestra os modulos do projeto: calcula e formata, sem logica propria."""

# Imports absolutos: cada modulo tem uma responsabilidade unica
from src.calculos import media
from src.formatacao import formatar_linha


def main() -> None:
    # main.py so coordena: os calculos e formatacoes vivem nos modulos
    print(f"Media: {media([7, 8, 9])}")
    print(formatar_linha("turma 7b"))


# Protege a execucao: se main.py for importado em testes,
# nada roda automaticamente
if __name__ == "__main__":
    main()
```

</details>
