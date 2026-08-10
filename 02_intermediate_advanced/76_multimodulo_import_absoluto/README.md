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

## Como executar

```bash
cd "76_multimodulo_import_absoluto"
python main.py
```
