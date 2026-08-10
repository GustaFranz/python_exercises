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

## Como executar

```bash
cd "78_multimodulo_folha_pagamento"
python main.py
```
