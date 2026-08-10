# 50 - Excecao customizada: nota fora do intervalo

## Objetivo

Crie NotaInvalidaError e validar_nota(nota) entre 0 e 10.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Rejeitar notas digitadas fora da escala 0 a 10. |

## Enunciado

1) Crie a excecao:
```python
class NotaInvalidaError(Exception):
    pass
```

2) Implemente:
```python
def validar_nota(nota: float) -> None:
    # aceita apenas 0 <= nota <= 10
```

3) Teste cada nota em `[-1, 0, 7.5, 10, 11]` com `try/except` separado.
4) Exiba resultado de cada teste: `"Valida"` ou mensagem de erro.

Exemplo de saida:

```
-1: Invalida — nota fora do intervalo 0-10
0: Valida
7.5: Valida
10: Valida
11: Invalida — nota fora do intervalo 0-10
```

## Como executar

```bash
cd "50_excecao_nota_intervalo"
python main.py
```
