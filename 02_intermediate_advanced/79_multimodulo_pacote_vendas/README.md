# 79 - Multi-modulo: pacote analise_vendas

## Objetivo

Criar pacote Python com __init__.py e imports limpos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / analytics |
| **Solicitacao** | Empacotar analise de vendas escolares para reutilizar em outros scripts. |

## Estrutura de arquivos

```
79_multimodulo_pacote_vendas/
├── main.py
└── analise_vendas/
    ├── __init__.py   # expoe total_vendas e resumo
    ├── vendas.py     # total_vendas(lista_dicts)
    └── relatorio.py  # gerar_resumo(total, qtd)
```

## Enunciado

Dados de teste:
```python
vendas = [
    {"produto": "caderno", "valor": 12},
    {"produto": "caneta", "valor": 3},
]
```

**`analise_vendas/vendas.py`**
```python
def total_vendas(vendas: list[dict]) -> float:
    # soma o campo "valor" de cada dict
```

**`analise_vendas/relatorio.py`**
```python
def gerar_resumo(total: float, qtd: int) -> str:
    # retorna resumo textual da analise
```

**`analise_vendas/__init__.py`**
```python
from .vendas import total_vendas
from .relatorio import gerar_resumo
```

No `main.py`:

1) Importe do pacote: `from analise_vendas import total_vendas, gerar_resumo`.
2) Calcule total e quantidade de vendas.
3) Exiba o resumo.

Exemplo de saida:

```
Total: R$ 15.00 | Vendas: 2
```

## Passo a passo

1. Em `analise_vendas/vendas.py`, implemente `total_vendas(vendas)`: some o campo `"valor"` de cada dict com `sum(venda["valor"] for venda in vendas)` e retorne.
2. Em `analise_vendas/relatorio.py`, implemente `gerar_resumo(total, qtd)`: retorne `f"Total: R$ {total:.2f} | Vendas: {qtd}"`.
3. Em `analise_vendas/__init__.py`, reexporte as funcoes publicas com imports RELATIVOS (com ponto, pois estao dentro do pacote): `from .vendas import total_vendas` e `from .relatorio import gerar_resumo`. E isso que permite importar direto do pacote, sem citar os modulos internos.
4. No `main.py`, importe do pacote: `from analise_vendas import total_vendas, gerar_resumo`.
5. Crie a lista `vendas` com os 2 dicts do enunciado.
6. Calcule `total = total_vendas(vendas)` e `qtd = len(vendas)`.
7. Exiba o retorno de `gerar_resumo(total, qtd)` (`Total: R$ 15.00 | Vendas: 2`).

## Como executar

```bash
cd "79_multimodulo_pacote_vendas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`analise_vendas/vendas.py`**

```python
"""Calculos sobre lista de vendas."""


def total_vendas(vendas):
    """Soma o campo valor de cada dict na lista."""
    # Generator expression percorre a lista somando so o campo "valor"
    return sum(venda["valor"] for venda in vendas)
```

**`analise_vendas/relatorio.py`**

```python
"""Relatorios de vendas."""


def gerar_resumo(total, qtd):
    """Retorna resumo textual com total e quantidade de itens."""
    # :.2f formata o total como valor monetario com 2 casas
    return f"Total: R$ {total:.2f} | Vendas: {qtd}"
```

**`analise_vendas/__init__.py`**

```python
"""Pacote de analise de vendas escolares."""

# Imports relativos (.modulo) reexportam as funcoes publicas:
# quem usa o pacote importa direto de analise_vendas
from .vendas import total_vendas
from .relatorio import gerar_resumo
```

**`main.py`**

```python
# Gracas ao __init__.py, importamos do pacote sem citar modulos internos
from analise_vendas import total_vendas, gerar_resumo

# Dados de teste do enunciado
vendas = [
    {"produto": "caderno", "valor": 12},
    {"produto": "caneta", "valor": 3},
]

# Total vem do modulo de calculo; quantidade e o tamanho da lista
total = total_vendas(vendas)
qtd = len(vendas)

# O modulo de relatorio formata; o main exibe
print(gerar_resumo(total, qtd))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`analise_vendas/vendas.py`**

```python
"""Calculos sobre vendas."""


def total_vendas(vendas: list[dict]) -> float:
    """Soma o campo "valor" de cada venda da lista."""
    # sum com generator: nao cria lista intermediaria
    return sum(venda["valor"] for venda in vendas)
```

**`analise_vendas/relatorio.py`**

```python
"""Apresentacao dos resultados da analise."""


def gerar_resumo(total: float, qtd: int) -> str:
    """Formata o resumo da analise em uma linha."""
    return f"Total: R$ {total:.2f} | Vendas: {qtd}"
```

**`analise_vendas/__init__.py`**

```python
"""Pacote de analise de vendas escolares.

O __init__.py define a interface publica do pacote: quem consome
importa de analise_vendas, sem conhecer a organizacao interna.
"""

from .vendas import total_vendas
from .relatorio import gerar_resumo

# __all__ documenta (e restringe no "import *") a API publica do pacote
__all__ = ["total_vendas", "gerar_resumo"]
```

**`main.py`**

```python
"""Consome o pacote analise_vendas como um cliente externo faria."""

from analise_vendas import total_vendas, gerar_resumo


def main() -> None:
    vendas = [
        {"produto": "caderno", "valor": 12},
        {"produto": "caneta", "valor": 3},
    ]

    # A API publica do pacote resolve tudo: calculo e formatacao
    resumo = gerar_resumo(total_vendas(vendas), len(vendas))
    print(resumo)


if __name__ == "__main__":
    main()
```

</details>
