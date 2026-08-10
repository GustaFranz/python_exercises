# 78 - Multi-modulo: calculadora de folha

## Objetivo

Montar folha de pagamento simples com 3 modulos cooperando.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Calcular holerite simplificado para equipe de agosto. |

## Estrutura de arquivos

```
78_multimodulo_folha_pagamento/
├── main.py
├── models.py    # Funcionario(nome, salario_base)
├── calculos.py  # calcular_liquido(salario, desconto_pct)
└── relatorio.py # formatar_holerite(nome, liquido)
```

## Enunciado

**`models.py`**
```python
def criar_funcionario(nome: str, salario_base: float) -> dict:
    return {"nome": nome, "salario": salario_base}
```

**`calculos.py`**
```python
def calcular_liquido(salario: float, desconto_pct: float) -> float:
    # desconto_pct em decimal (ex.: 0.08 = 8%)
    return salario * (1 - desconto_pct)
```

**`relatorio.py`**
```python
def formatar_holerite(nome: str, liquido: float) -> str:
    # retorna string legivel do holerite
```

No `main.py`:

1) Crie funcionario `"Carla"` com salario `3000.0`.
2) Calcule liquido com `8%` de desconto (`desconto_pct = 0.08`).
3) Exiba holerite formatado.

Exemplo de saida:

```
Holerite — Carla | Salario liquido: R$ 2760.00
```

## Passo a passo

1. Em `models.py`, implemente `criar_funcionario(nome, salario_base)`: retorne o dict `{"nome": nome, "salario": salario_base}` — modelo puro, sem calculo.
2. Em `calculos.py`, implemente `calcular_liquido(salario, desconto_pct)`: retorne `salario * (1 - desconto_pct)` (com `desconto_pct` em decimal, `0.08` = 8%).
3. Em `relatorio.py`, implemente `formatar_holerite(nome, liquido)`: retorne `f"Holerite — {nome} | Salario liquido: R$ {liquido:.2f}"` (duas casas decimais).
4. No `main.py`, importe uma funcao de cada modulo: `from models import criar_funcionario`, `from calculos import calcular_liquido`, `from relatorio import formatar_holerite`.
5. Crie o funcionario: `funcionario = criar_funcionario("Carla", 3000.0)`.
6. Calcule o liquido: `liquido = calcular_liquido(funcionario["salario"], 0.08)` — esperado `2760.0`.
7. Formate e exiba: `print(formatar_holerite(funcionario["nome"], liquido))`.
8. Confira que nenhum modulo faz o trabalho do outro: `calculos` so calcula, `relatorio` so formata, `main` so coordena.

## Como executar

```bash
cd "78_multimodulo_folha_pagamento"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`models.py`**

```python
"""Modelos de funcionario."""


def criar_funcionario(nome, salario_base):
    """Retorna dict com nome e salario_base."""
    # Modelo puro: representa os dados, sem regra de negocio
    return {"nome": nome, "salario": salario_base}
```

**`calculos.py`**

```python
"""Calculos de folha de pagamento."""


def calcular_liquido(salario, desconto_pct):
    """Retorna salario apos desconto percentual."""
    # desconto_pct em decimal: 0.08 = 8%
    # multiplicar por (1 - desconto) aplica o desconto de uma vez
    return salario * (1 - desconto_pct)
```

**`relatorio.py`**

```python
"""Formatacao de holerite."""


def formatar_holerite(nome, liquido):
    """Retorna string de holerite para exibicao."""
    # :.2f garante duas casas decimais no valor em reais
    return f"Holerite — {nome} | Salario liquido: R$ {liquido:.2f}"
```

**`main.py`**

```python
# Um import de cada camada: dados, calculo e apresentacao
from models import criar_funcionario
from calculos import calcular_liquido
from relatorio import formatar_holerite

# 1) Cria o registro do funcionario (models)
funcionario = criar_funcionario("Carla", 3000.0)

# 2) Aplica 8% de desconto sobre o salario (calculos)
liquido = calcular_liquido(funcionario["salario"], 0.08)

# 3) Formata o holerite (relatorio) e exibe (main)
print(formatar_holerite(funcionario["nome"], liquido))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`models.py`**

```python
"""Modelos de dados da folha de pagamento."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Funcionario:
    """Registro imutavel de funcionario (frozen evita alteracao acidental)."""

    nome: str
    salario_base: float
```

**`calculos.py`**

```python
"""Regras de calculo da folha."""


def calcular_liquido(salario: float, desconto_pct: float) -> float:
    """Aplica desconto percentual (decimal) sobre o salario bruto.

    Ex.: calcular_liquido(3000.0, 0.08) -> 2760.0
    """
    # Guard clause: percentual fora de 0..1 indica erro de chamada
    if not (0 <= desconto_pct <= 1):
        raise ValueError(f"desconto_pct deve estar entre 0 e 1: {desconto_pct}")

    return salario * (1 - desconto_pct)
```

**`relatorio.py`**

```python
"""Apresentacao de holerites."""


def formatar_holerite(nome: str, liquido: float) -> str:
    """Monta a linha do holerite com valor em reais (2 casas)."""
    return f"Holerite — {nome} | Salario liquido: R$ {liquido:.2f}"
```

**`main.py`**

```python
"""Orquestra a folha: cria o funcionario, calcula o liquido e exibe."""

from models import Funcionario
from calculos import calcular_liquido
from relatorio import formatar_holerite

# Percentual de desconto de agosto centralizado como constante
DESCONTO_AGOSTO = 0.08


def main() -> None:
    # Dataclass da conveniencia de acesso por atributo (funcionario.nome)
    funcionario = Funcionario(nome="Carla", salario_base=3000.0)

    liquido = calcular_liquido(funcionario.salario_base, DESCONTO_AGOSTO)

    print(formatar_holerite(funcionario.nome, liquido))


if __name__ == "__main__":
    main()
```

</details>
