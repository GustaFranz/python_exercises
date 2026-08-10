# 76 - Multi-modulo: import absoluto

## Objetivo

Usar imports absolutos entre modulos no mesmo projeto.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Padronizar imports no sistema de ponto eletronico piloto. |

## Estrutura de arquivos

```
76_multimodulo_import_absoluto/
├── main.py
├── relogio.py      # horas_trabalhadas(entrada, saida)
└── relatorio.py    # gerar_resumo(nome, horas)
```

## Enunciado

**`relogio.py`**
```python
def horas_trabalhadas(entrada: str, saida: str) -> float:
    # entrada e saida no formato "HH:MM"
    # retorna horas como float (ex.: 9h30 -> 9.5)
```

**`relatorio.py`**
```python
def gerar_resumo(nome: str, horas: float) -> str:
    return f"{nome}: {horas:.1f}h"
```

No `main.py`:

1) Use imports absolutos: `from relogio import horas_trabalhadas` e `from relatorio import gerar_resumo`.
2) Calcule horas de `"Ana Silva"` com entrada `"08:00"` e saida `"17:00"` (resultado esperado: `9.0`).
3) Exiba o resumo retornado por `gerar_resumo`.

Exemplo de saida:

```
Ana Silva: 9.0h
```

## Passo a passo

1. Em `relogio.py`, implemente `horas_trabalhadas(entrada, saida)`:
   - separe horas e minutos de cada horario com `split(":")` e converta para `int` (ex.: `h, m = entrada.split(":")`);
   - converta cada horario para minutos totais: `minutos = int(h) * 60 + int(m)`;
   - subtraia (saida menos entrada) e divida por 60 para voltar a horas como `float` (assim `9h30` vira `9.5`);
   - retorne esse valor.
2. Em `relatorio.py`, implemente `gerar_resumo(nome, horas)`: retorne `f"{nome}: {horas:.1f}h"` (uma casa decimal).
3. No `main.py`, use imports absolutos: `from relogio import horas_trabalhadas` e `from relatorio import gerar_resumo` (sem ponto na frente — import relativo aqui quebraria).
4. Calcule `horas = horas_trabalhadas("08:00", "17:00")` — deve dar `9.0`.
5. Gere o resumo com `gerar_resumo("Ana Silva", horas)` e exiba com `print` (`Ana Silva: 9.0h`).

## Como executar

```bash
cd "76_multimodulo_import_absoluto"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`relogio.py`**

```python
"""Calculo de horas trabalhadas."""


def horas_trabalhadas(entrada, saida):
    """Recebe horarios HH:MM e retorna horas em float."""
    # Separa "08:00" em horas e minutos e converte para int
    h_entrada, m_entrada = entrada.split(":")
    h_saida, m_saida = saida.split(":")

    # Converte cada horario para minutos totais desde 00:00
    minutos_entrada = int(h_entrada) * 60 + int(m_entrada)
    minutos_saida = int(h_saida) * 60 + int(m_saida)

    # Diferenca em minutos dividida por 60 vira horas em float
    # (ex.: 570 minutos -> 9.5 horas)
    return (minutos_saida - minutos_entrada) / 60
```

**`relatorio.py`**

```python
"""Geracao de resumos de ponto."""


def gerar_resumo(nome, horas):
    """Retorna string formatada com nome e horas trabalhadas."""
    # :.1f fixa uma casa decimal (9.0h, 9.5h)
    return f"{nome}: {horas:.1f}h"
```

**`main.py`**

```python
# Imports absolutos: modulos do mesmo diretorio, sem ponto na frente
from relogio import horas_trabalhadas
from relatorio import gerar_resumo

# Calcula as horas do dia de Ana Silva (08:00 as 17:00 -> 9.0)
horas = horas_trabalhadas("08:00", "17:00")

# O modulo de relatorio formata; o main so exibe
print(gerar_resumo("Ana Silva", horas))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`relogio.py`**

```python
"""Calculo de horas trabalhadas a partir de horarios HH:MM."""

from datetime import datetime

# Formato unico dos horarios do ponto, documentado como constante
FORMATO_HORA = "%H:%M"


def horas_trabalhadas(entrada: str, saida: str) -> float:
    """Retorna as horas entre entrada e saida como float (9h30 -> 9.5).

    Usa datetime.strptime: alem de converter, valida o formato
    (horario invalido lanca ValueError com mensagem clara).
    """
    inicio = datetime.strptime(entrada, FORMATO_HORA)
    fim = datetime.strptime(saida, FORMATO_HORA)

    # A subtracao de datetimes gera um timedelta;
    # total_seconds()/3600 converte para horas decimais
    return (fim - inicio).total_seconds() / 3600
```

**`relatorio.py`**

```python
"""Geracao de resumos de ponto para exibicao."""


def gerar_resumo(nome: str, horas: float) -> str:
    """Formata o resumo do dia: nome e horas com 1 casa decimal."""
    return f"{nome}: {horas:.1f}h"
```

**`main.py`**

```python
"""Orquestra o fluxo do ponto: calcula horas e exibe o resumo."""

from relogio import horas_trabalhadas
from relatorio import gerar_resumo


def main() -> None:
    # Dados do enunciado
    horas = horas_trabalhadas("08:00", "17:00")
    print(gerar_resumo("Ana Silva", horas))


if __name__ == "__main__":
    main()
```

</details>
