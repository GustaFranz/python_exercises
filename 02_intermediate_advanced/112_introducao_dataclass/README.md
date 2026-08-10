# 112 - Introducao a dataclass

## Objetivo

Registrar produto com @dataclass e exibir instancia.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / catalogo |
| **Solicitacao** | Padronizar cadastro de produtos do bazar com menos codigo repetitivo. |

## Visao do bloco (exercicios 112 a 116)

Topico **@dataclass**: classes de dados com menos boilerplate.

| # | Foco |
|---|------|
| 112 | Introducao + dataclass Produto |
| 113 | dataclass RegistroAula |
| 114 | Comparar instancias de dataclass |
| 115 | Relatorio analitico (total, ticket medio, top produto) |
| 116 | Converter dicts com validacao e relatorio rejeitados |

## Enunciado

- Crie dataclass Produto com nome, preco e estoque.
- Instancie um produto e exiba com print.

## Passo a passo

1. Importe o decorador: `from dataclasses import dataclass`.
2. Aplique `@dataclass` logo acima de `class Produto:`.
3. Declare os campos apenas com anotacoes de tipo (sem `__init__`): `nome: str`, `preco: float`, `estoque: int` — a dataclass gera `__init__`, `__repr__` e `__eq__` automaticamente.
4. Instancie `Produto("Caderno", 12.50, 30)`.
5. Exiba com `print(produto)` — a saida usa o `__repr__` gerado: `Produto(nome='Caderno', preco=12.5, estoque=30)`.

## Como executar

```bash
cd "112_introducao_dataclass"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Importa o decorador que gera codigo repetitivo por nos
from dataclasses import dataclass


# @dataclass gera automaticamente __init__, __repr__ e __eq__
# a partir dos campos anotados abaixo
@dataclass
class Produto:
    # Cada campo e declarado como: nome_do_campo: tipo
    nome: str
    preco: float
    estoque: int


# O __init__ gerado recebe os campos na ordem declarada
produto = Produto("Caderno", 12.50, 30)

# print usa o __repr__ gerado: Produto(nome='Caderno', preco=12.5, estoque=30)
print(produto)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass


# frozen=True: instancias imutaveis (tentativa de alterar lanca erro) —
# bom padrao para registros de catalogo que nao devem mudar por engano.
# slots=True: economiza memoria e bloqueia atributos nao declarados.
@dataclass(frozen=True, slots=True)
class Produto:
    """Produto do catalogo do bazar escolar."""

    nome: str
    preco: float
    estoque: int


def main() -> None:
    produto = Produto(nome="Caderno", preco=12.50, estoque=30)
    # O __repr__ gerado ja e informativo o suficiente para exibicao/debug
    print(produto)


if __name__ == "__main__":
    main()
```

</details>
