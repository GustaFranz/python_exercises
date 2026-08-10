# 130 - Type hints: modulo publico tipado

## Objetivo

Publicar modulo de mensalidades com contrato tipado completo (padrao de API interna em entrevista).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Expor modulo de calculo de mensalidades com hints, docstrings e estrutura de retorno tipada. |

## Estrutura de arquivos

```
130_type_hints_modulo_publico/
├── README.md
├── main.py
└── mensalidades.py   # API publica tipada
```

## Enunciado

- Em `mensalidades.py`, implemente funcoes publicas com type hints completos:
  - `calcular_desconto(valor: float, percentual: float) -> float`
  - `somar_valores(valores: List[float]) -> float`
  - `resumo_mensalidades(alunos: List[Dict[str, float]]) -> Dict[str, float]`
- `resumo_mensalidades` deve retornar dict com chaves: `total`, `media`, `maior`, `menor`.
- Use `from typing import List, Dict, Optional` (Optional se aplicavel).
- Toda funcao publica deve ter docstring explicando parametros e retorno.
- `main.py` importa o modulo, processa lista de alunos e exibe resumo formatado.

## Passo a passo

1. Em `mensalidades.py`, complete `calcular_desconto(valor: float, percentual: float) -> float` retornando `valor * (1 - percentual / 100)` (percentual de 0 a 100).
2. Complete `somar_valores(valores: List[float]) -> float`: retorne `sum(valores)` — `sum` de lista vazia ja devolve `0` naturalmente.
3. Complete `resumo_mensalidades(alunos: List[Dict[str, float]]) -> Dict[str, float]`:
   - trate a borda: se `alunos` vazio, retorne `{"total": 0.0, "media": 0.0, "maior": 0.0, "menor": 0.0}`;
   - extraia os valores com list comprehension: `valores = [a["valor"] for a in alunos]`;
   - monte o dict de retorno com `somar_valores(valores)` (reutilizacao!), `total / len(valores)`, `max(valores)` e `min(valores)`.
4. Em `main.py`, faca `import mensalidades` e monte a lista de alunos do enunciado (`Ana` 850.0, `Bruno` 920.0, `Carla` 780.0).
5. Aplique 5% de desconto em cada aluno usando `mensalidades.calcular_desconto` dentro de uma list comprehension, gerando nova lista de dicts.
6. Chame `mensalidades.resumo_mensalidades` com a lista com desconto e exiba cada chave (`total`, `media`, `maior`, `menor`) formatada com 2 casas decimais.

## Como executar

```bash
cd "130_type_hints_modulo_publico"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`mensalidades.py`**

```python
"""Calculos de mensalidade escolar — API publica tipada."""

from typing import Dict, List


def calcular_desconto(valor: float, percentual: float) -> float:
    """Aplica desconto percentual sobre valor de mensalidade.

    Args:
        valor: valor base da mensalidade.
        percentual: percentual de desconto entre 0 e 100.

    Returns:
        Valor final apos aplicar o desconto.
    """
    # Percentual 0-100 vira fator: 5% -> pagar 95% do valor
    return valor * (1 - percentual / 100)


def somar_valores(valores: List[float]) -> float:
    """Soma lista de valores de mensalidades.

    Args:
        valores: lista de valores numericos.

    Returns:
        Soma total dos valores. Retorna 0.0 se lista vazia.
    """
    # sum([]) ja retorna 0 — a borda de lista vazia vem de graca
    return sum(valores)


def resumo_mensalidades(alunos: List[Dict[str, float]]) -> Dict[str, float]:
    """Gera resumo estatistico das mensalidades dos alunos.

    Args:
        alunos: lista de dicts com chaves "nome" (str) e "valor" (float).

    Returns:
        Dict com chaves total, media, maior e menor.
        Se lista vazia, retorna zeros.
    """
    # Borda primeiro: sem alunos nao ha max/min nem divisao
    if not alunos:
        return {"total": 0.0, "media": 0.0, "maior": 0.0, "menor": 0.0}
    # Extrai apenas os valores para reutilizar nas agregacoes
    valores = [aluno["valor"] for aluno in alunos]
    total = somar_valores(valores)  # reutiliza a funcao publica
    return {
        "total": total,
        "media": total / len(valores),
        "maior": max(valores),
        "menor": min(valores),
    }
```

**`main.py`**

```python
# main.py apenas orquestra: importa o modulo e exibe — a logica vive em mensalidades.py
import mensalidades

DESCONTO_PONTUALIDADE = 5.0  # 5% para pagamento em dia

alunos = [
    {"nome": "Ana", "valor": 850.0},
    {"nome": "Bruno", "valor": 920.0},
    {"nome": "Carla", "valor": 780.0},
]

# Aplica o desconto em cada aluno gerando NOVA lista (nao altera a original)
com_desconto = [
    {"nome": a["nome"], "valor": mensalidades.calcular_desconto(a["valor"], DESCONTO_PONTUALIDADE)}
    for a in alunos
]

resumo = mensalidades.resumo_mensalidades(com_desconto)

print("=== Resumo de mensalidades (com 5% de desconto) ===")
print(f"Total: R$ {resumo['total']:.2f}")
print(f"Media: R$ {resumo['media']:.2f}")
print(f"Maior: R$ {resumo['maior']:.2f}")
print(f"Menor: R$ {resumo['menor']:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`mensalidades.py`**

```python
"""Calculos de mensalidade escolar — API publica tipada.

Nota: List/Dict do typing eram necessarios ate o Python 3.8;
hoje usa-se list[float] e dict[str, float] direto. O TypedDict
Resumo documenta as chaves exatas do retorno — mais forte que
um Dict[str, float] generico.
"""

from statistics import fmean
from typing import TypedDict


class Resumo(TypedDict):
    """Chaves fixas do resumo: o mypy acusa se alguma faltar."""

    total: float
    media: float
    maior: float
    menor: float


def calcular_desconto(valor: float, percentual: float) -> float:
    """Aplica desconto percentual (0 a 100) sobre o valor da mensalidade."""
    return valor * (1 - percentual / 100)


def somar_valores(valores: list[float]) -> float:
    """Soma os valores; lista vazia resulta em 0.0."""
    return sum(valores)


def resumo_mensalidades(alunos: list[dict[str, float]]) -> Resumo:
    """Consolida total, media, maior e menor mensalidade.

    Args:
        alunos: dicts com "nome" (str) e "valor" (float).

    Returns:
        Resumo com zeros se a lista estiver vazia.
    """
    if not alunos:
        return {"total": 0.0, "media": 0.0, "maior": 0.0, "menor": 0.0}
    valores = [aluno["valor"] for aluno in alunos]
    return {
        "total": somar_valores(valores),
        "media": fmean(valores),
        "maior": max(valores),
        "menor": min(valores),
    }
```

**`main.py`**

```python
"""Orquestra o fluxo: dados -> desconto -> resumo -> exibicao."""

import mensalidades

DESCONTO_PONTUALIDADE = 5.0  # percentual aplicado a quem paga em dia


def main() -> None:
    alunos = [
        {"nome": "Ana", "valor": 850.0},
        {"nome": "Bruno", "valor": 920.0},
        {"nome": "Carla", "valor": 780.0},
    ]

    # Nova lista com desconto: preserva os dados originais
    com_desconto = [
        {
            "nome": aluno["nome"],
            "valor": mensalidades.calcular_desconto(aluno["valor"], DESCONTO_PONTUALIDADE),
        }
        for aluno in alunos
    ]

    resumo = mensalidades.resumo_mensalidades(com_desconto)

    print("=== Resumo de mensalidades (com 5% de desconto) ===")
    # Itera as chaves do resumo para nao repetir 4 prints iguais
    for chave in ("total", "media", "maior", "menor"):
        print(f"{chave.capitalize()}: R$ {resumo[chave]:.2f}")


if __name__ == "__main__":
    main()
```

</details>
