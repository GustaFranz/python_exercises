# 54 - Try except: divisao segura

## Objetivo

Implemente media_segura(valores) com try/except.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | CalcEscolar |
| **Setor** | Educacao / matematica |
| **Solicitacao** | Calcular media de turma sem travar quando lista vier vazia. |

## Enunciado

Implemente:

```python
def media_segura(valores: list) -> float | None:
    try:
        return sum(valores) / len(valores)
    except ZeroDivisionError:
        print("Lista vazia")
        return None
```

No `main`, teste:

1) `[8, 7, 9]` — exiba a media retornada.
2) `[]` — exiba a mensagem e o retorno `None`.

Exemplo de saida:

```
Media: 8.0
Lista vazia
Media: None
```

## Como executar

```bash
cd "54_try_divisao_segura"
python main.py
```
