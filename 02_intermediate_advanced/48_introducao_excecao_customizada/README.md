# 48 - Introducao a excecao customizada

## Objetivo

Crie SaldoInsuficienteError e funcao sacar(saldo, valor).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Bloquear saque quando saldo da carteira digital for insuficiente. |

## Visao do bloco (exercicios 48 a 52)

Topico **`raise` + excecao customizada**: validar regras de negocio com erros claros.

| # | Foco |
|---|------|
| 48 | Introducao + SaldoInsuficienteError |
| 49 | Validar idade minima |
| 50 | Nota fora do intervalo |
| 51 | Cadastro com excecoes especificas |
| 52 | Fluxo de pedido com propagacao de erros |

## Enunciado

1) Crie a excecao:
```python
class SaldoInsuficienteError(Exception):
    pass
```

2) Implemente:
```python
def sacar(saldo: float, valor: float) -> float:
    # retorna saldo - valor se valor <= saldo
    # levanta SaldoInsuficienteError se valor > saldo
```

3) Teste com `saldo = 100`:
   - Saque `30` — sucesso; exiba novo saldo.
   - Saque `80` — capture com `try/except` e exiba mensagem amigavel ao usuario.

Exemplo de saida:

```
Saque OK. Saldo restante: 70.0
Erro: Saldo 70 insuficiente para sacar 80
```

## Como executar

```bash
cd "48_introducao_excecao_customizada"
python main.py
```
