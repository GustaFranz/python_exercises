# 65 - Recursao: soma de 1 ate N

## Objetivo

Somar 1 + 2 + ... + N usando recursao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Somar parcelas mensais acumuladas para simulacao de plano. |

## Enunciado

Implemente recursivamente:

```python
def soma_ate(n: int) -> int:
    # soma_ate(0) retorna 0
    # soma_ate(n) retorna n + soma_ate(n - 1)
```

No `main`, exiba:

1) `soma_ate(1)` → `1`
2) `soma_ate(5)` → `15`
3) `soma_ate(10)` → `55`

Exemplo de saida:

```
soma_ate(1) = 1
soma_ate(5) = 15
soma_ate(10) = 55
```

## Como executar

```bash
cd "65_recursao_soma_ate_n"
python main.py
```
