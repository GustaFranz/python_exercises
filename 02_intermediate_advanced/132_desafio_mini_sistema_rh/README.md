# 132 - DESAFIO - Mini sistema de RH

## Objetivo

Case final mais trabalhado: heranca/dataclass, refatoracao, asserts e type hints.

## Conteudos cobertos

- Heranca e/ou dataclass
- Refatoracao em funcoes/modulos
- Testes com `assert` em arquivo separado
- Type hints basicos
- Relatorio de folha simplificado

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | PeopleFirst RH Tech |
| **Setor** | Recursos humanos / sistemas internos |
| **Solicitacao** | Mini modulo de colaboradores com calculo de pagamento, tipagem e suite de testes. |

## Estrutura obrigatoria

```
132_desafio_mini_sistema_rh/
├── main.py
├── models.py
├── calculos.py
├── testes.py
└── README.md
```

## Enunciado

Checklist:

1) Em `models.py` (type hints + docstring):
   - dataclass ou classes `Colaborador` (nome, cargo, salario_base)
   - `Gerente(Colaborador)` com bonus fixo (ex.: +15%)
   - `Vendedor(Colaborador)` com comissao (ex.: +10% sobre salario_base * meta_atingida)
   - metodo `pagamento() -> float` polimorfico
2) Em `calculos.py`:
   - `folha_total(colaboradores: list) -> float`
   - `resumo_por_cargo(colaboradores: list) -> dict[str, float]`
   - `filtrar_acima_de(colaboradores, limite: float) -> list`
3) Em `testes.py`:
   - asserts para pagamento de Gerente e Vendedor
   - assert de folha_total
   - caso de borda: lista vazia -> folha 0
4) Em `main.py`:
   - monte 3 colaboradores
   - imprima pagamento individual e resumo por cargo
   - opcional: chame/lembre de rodar `python testes.py`
5) Codigo limpo: nomes claros, funcoes curtas (refatoracao consciente).

Nao e um ERP completo: foque no nucleo tipado + testes + polimorfismo.

## Passo a passo

1. Em `models.py`, crie a `@dataclass Colaborador` com `nome: str`, `cargo: str`, `salario_base: float` e o metodo `pagamento(self) -> float` retornando `self.salario_base` (comportamento padrao).
2. Crie `@dataclass Gerente(Colaborador)` sobrescrevendo `pagamento()` para retornar `self.salario_base * 1.15` (bonus fixo de 15%).
3. Crie `@dataclass Vendedor(Colaborador)` adicionando o campo `meta_atingida: float` (0 a 1) e sobrescrevendo `pagamento()` para retornar `self.salario_base * (1 + 0.10 * self.meta_atingida)`. Dica: envolva os calculos de pagamento com `round(..., 2)` — sem isso, `3000 * 1.1` da `3300.0000000000005` em float e os asserts de igualdade falham.
4. Em `calculos.py`, implemente com type hints:
   - `folha_total(colaboradores: list) -> float`: `sum(c.pagamento() for c in colaboradores)` — o polimorfismo faz cada classe usar sua propria regra;
   - `resumo_por_cargo(colaboradores: list) -> dict[str, float]`: percorra a lista acumulando `pagamento()` por `cargo` num dict;
   - `filtrar_acima_de(colaboradores: list, limite: float) -> list`: list comprehension com `if c.pagamento() > limite`.
5. Em `testes.py`, importe `models` e `calculos` e escreva os asserts:
   - `Gerente("Ana", "Gerente", 5000.0).pagamento() == 5750.0`;
   - `Vendedor("Bruno", "Vendedor", 3000.0, 1.0).pagamento() == 3300.0`;
   - `folha_total` com os dois acima `== 9050.0`;
   - borda: `folha_total([]) == 0`.
   Finalize com `print("Todos os testes passaram.")`.
6. Em `main.py`, monte 3 colaboradores (ex.: 1 Gerente e 2 Vendedores com metas diferentes), imprima o pagamento individual de cada um, o resumo por cargo e a folha total; lembre o leitor de rodar `python testes.py`.

## Como executar

```bash
cd "132_desafio_mini_sistema_rh"
python testes.py
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`models.py`**

```python
"""Modelos de colaboradores com pagamento polimorfico."""

from dataclasses import dataclass


@dataclass
class Colaborador:
    """Colaborador generico: pagamento e o proprio salario base."""

    nome: str
    cargo: str
    salario_base: float

    def pagamento(self) -> float:
        """Valor a pagar no mes (regra padrao: sem adicional)."""
        return self.salario_base


@dataclass
class Gerente(Colaborador):
    """Gerente recebe bonus fixo de 15% sobre o salario base."""

    def pagamento(self) -> float:
        # Sobrescreve a regra da classe mae: mesmo nome, novo calculo
        # round(_, 2) fixa em centavos e evita residuo de float nos asserts
        return round(self.salario_base * 1.15, 2)


@dataclass
class Vendedor(Colaborador):
    """Vendedor recebe comissao proporcional a meta atingida (0 a 1)."""

    meta_atingida: float = 0.0  # 1.0 = bateu 100% da meta

    def pagamento(self) -> float:
        # Comissao maxima de 10%, escalada pela fracao da meta;
        # sem round, 3000 * 1.1 daria 3300.0000000000005 (float binario)
        return round(self.salario_base * (1 + 0.10 * self.meta_atingida), 2)
```

**`calculos.py`**

```python
"""Regras da folha de pagamento."""


def folha_total(colaboradores: list) -> float:
    # Polimorfismo em acao: cada objeto usa SUA versao de pagamento()
    return sum(c.pagamento() for c in colaboradores)


def resumo_por_cargo(colaboradores: list) -> dict[str, float]:
    # Acumula o pagamento por cargo; get(cargo, 0.0) cobre a primeira ocorrencia
    resumo: dict[str, float] = {}
    for c in colaboradores:
        resumo[c.cargo] = resumo.get(c.cargo, 0.0) + c.pagamento()
    return resumo


def filtrar_acima_de(colaboradores: list, limite: float) -> list:
    # List comprehension: mantem apenas quem recebe acima do limite
    return [c for c in colaboradores if c.pagamento() > limite]
```

**`testes.py`**

```python
"""Suite de asserts do mini RH — execute: python testes.py"""

from calculos import folha_total, resumo_por_cargo
from models import Gerente, Vendedor

# Pagamento do Gerente: 5000 * 1.15 = 5750
gerente = Gerente("Ana", "Gerente", 5000.0)
assert gerente.pagamento() == 5750.0, "gerente deveria receber 5750.0"

# Pagamento do Vendedor com meta 100%: 3000 * 1.10 = 3300
vendedor = Vendedor("Bruno", "Vendedor", 3000.0, 1.0)
assert vendedor.pagamento() == 3300.0, "vendedor deveria receber 3300.0"

# Folha total soma os pagamentos calculados
assert folha_total([gerente, vendedor]) == 9050.0, "folha deveria ser 9050.0"

# Caso de borda: sem colaboradores, folha zero
assert folha_total([]) == 0, "folha de lista vazia deve ser 0"

# Resumo agrupa por cargo
resumo = resumo_por_cargo([gerente, vendedor])
assert resumo == {"Gerente": 5750.0, "Vendedor": 3300.0}, "resumo por cargo incorreto"

print("Todos os testes passaram.")
```

**`main.py`**

```python
"""Relatorio da folha — monte os dados e exiba os resultados."""

from calculos import folha_total, resumo_por_cargo
from models import Gerente, Vendedor

# 3 colaboradores: 1 gerente e 2 vendedores com metas diferentes
equipe = [
    Gerente("Ana", "Gerente", 5000.0),
    Vendedor("Bruno", "Vendedor", 3000.0, 1.0),   # bateu 100% da meta
    Vendedor("Carla", "Vendedor", 2800.0, 0.5),   # bateu 50% da meta
]

print("=== Pagamentos individuais ===")
for colaborador in equipe:
    print(f"{colaborador.nome} ({colaborador.cargo}): R$ {colaborador.pagamento():.2f}")

print("\n=== Resumo por cargo ===")
for cargo, total in resumo_por_cargo(equipe).items():
    print(f"{cargo}: R$ {total:.2f}")

print(f"\nFolha total: R$ {folha_total(equipe):.2f}")
print("\nLembrete: rode 'python testes.py' para validar as regras.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`models.py`**

```python
"""Modelos de colaboradores com pagamento polimorfico.

As taxas ficam como ClassVar: pertencem a CLASSE (regra de negocio),
nao a cada instancia — e nao viram campo do __init__.
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Colaborador:
    """Colaborador generico: pagamento e o salario base puro."""

    nome: str
    cargo: str
    salario_base: float

    def pagamento(self) -> float:
        """Valor a pagar no mes."""
        return self.salario_base


@dataclass
class Gerente(Colaborador):
    """Gerente: salario base + bonus fixo."""

    BONUS: ClassVar[float] = 0.15

    def pagamento(self) -> float:
        # Arredonda para centavos: valores monetarios nao carregam
        # residuo binario de float (3000 * 1.1 = 3300.0000000000005)
        return round(self.salario_base * (1 + self.BONUS), 2)


@dataclass
class Vendedor(Colaborador):
    """Vendedor: salario base + comissao proporcional a meta (0 a 1)."""

    meta_atingida: float = 0.0
    COMISSAO_MAXIMA: ClassVar[float] = 0.10

    def pagamento(self) -> float:
        return round(self.salario_base * (1 + self.COMISSAO_MAXIMA * self.meta_atingida), 2)
```

**`calculos.py`**

```python
"""Agregacoes da folha de pagamento."""

from collections import defaultdict

from models import Colaborador


def folha_total(colaboradores: list[Colaborador]) -> float:
    """Soma os pagamentos; lista vazia resulta em 0."""
    return sum(c.pagamento() for c in colaboradores)


def resumo_por_cargo(colaboradores: list[Colaborador]) -> dict[str, float]:
    """Total de pagamentos agrupado por cargo."""
    # defaultdict(float) inicia cada cargo em 0.0 automaticamente
    resumo: dict[str, float] = defaultdict(float)
    for colaborador in colaboradores:
        resumo[colaborador.cargo] += colaborador.pagamento()
    return dict(resumo)  # converte para dict comum na saida da API


def filtrar_acima_de(colaboradores: list[Colaborador], limite: float) -> list[Colaborador]:
    """Colaboradores com pagamento acima do limite informado."""
    return [c for c in colaboradores if c.pagamento() > limite]
```

**`testes.py`**

```python
"""Suite de asserts do mini RH — execute: python testes.py

Com pytest, cada funcao test_* seria descoberta e executada
automaticamente, e os floats usariam pytest.approx.
"""

from calculos import filtrar_acima_de, folha_total, resumo_por_cargo
from models import Gerente, Vendedor


def test_pagamentos() -> None:
    """Regras individuais: bonus do gerente e comissao do vendedor."""
    assert Gerente("Ana", "Gerente", 5000.0).pagamento() == 5750.0
    assert Vendedor("Bruno", "Vendedor", 3000.0, 1.0).pagamento() == 3300.0
    # Meta parcial: 2800 * (1 + 0.10 * 0.5) = 2940
    assert Vendedor("Carla", "Vendedor", 2800.0, 0.5).pagamento() == 2940.0


def test_folha() -> None:
    """Agregacoes: total, borda vazia e agrupamento por cargo."""
    equipe = [
        Gerente("Ana", "Gerente", 5000.0),
        Vendedor("Bruno", "Vendedor", 3000.0, 1.0),
    ]
    assert folha_total(equipe) == 9050.0
    assert folha_total([]) == 0, "folha vazia deve ser 0"
    assert resumo_por_cargo(equipe) == {"Gerente": 5750.0, "Vendedor": 3300.0}
    assert filtrar_acima_de(equipe, 4000.0) == [equipe[0]], "so o gerente passa de 4000"


if __name__ == "__main__":
    test_pagamentos()
    test_folha()
    print("Todos os testes passaram.")
```

**`main.py`**

```python
"""Relatorio executivo da folha do mini sistema de RH."""

from calculos import folha_total, resumo_por_cargo
from models import Colaborador, Gerente, Vendedor


def montar_equipe() -> list[Colaborador]:
    """Dados de exemplo centralizados em um unico lugar."""
    return [
        Gerente("Ana", "Gerente", 5000.0),
        Vendedor("Bruno", "Vendedor", 3000.0, 1.0),
        Vendedor("Carla", "Vendedor", 2800.0, 0.5),
    ]


def main() -> None:
    equipe = montar_equipe()

    print("=== Pagamentos individuais ===")
    for colaborador in equipe:
        print(f"{colaborador.nome} ({colaborador.cargo}): R$ {colaborador.pagamento():.2f}")

    print("\n=== Resumo por cargo ===")
    for cargo, total in resumo_por_cargo(equipe).items():
        print(f"{cargo}: R$ {total:.2f}")

    print(f"\nFolha total: R$ {folha_total(equipe):.2f}")
    print("\nLembrete: rode 'python testes.py' para validar as regras.")


if __name__ == "__main__":
    main()
```

</details>
