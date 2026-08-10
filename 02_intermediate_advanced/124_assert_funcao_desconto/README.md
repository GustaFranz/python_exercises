# 124 - Assert: funcao de desconto

## Objetivo

Testar funcao de desconto com asserts em multiplos cenarios.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / precificacao |
| **Solicitacao** | Validar regras de desconto progressivo antes da campanha do bazar. |

## Enunciado

Implemente:

```python
def aplicar_desconto(valor: float, pct: float) -> float:
    # pct entre 0 e 1; se pct invalido retorna valor original
```

Regra: aplique desconto apenas se `0 <= pct <= 1`.

Escreva asserts de teste:

```python
assert aplicar_desconto(100, 0.10) == 90.0
assert aplicar_desconto(50, 0) == 50.0
assert aplicar_desconto(80, 1.5) == 80.0   # pct invalido
```

## Como executar

```bash
cd "124_assert_funcao_desconto"
python main.py
```
