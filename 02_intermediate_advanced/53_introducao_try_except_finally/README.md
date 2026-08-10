# 53 - Introducao a try except finally

## Objetivo

Implemente operacao_segura(a, b) com try/except/else/finally.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BancoSim Educacao |
| **Setor** | Financeiro / simulacoes |
| **Solicitacao** | Demonstrar fluxo completo de tratamento de erros em operacao sensivel. |

## Visao do bloco (exercicios 53 a 57)

Topico **`try/except/else/finally`**: tratar erros sem perder rastreabilidade.

| # | Nivel | Foco |
|---|-------|------|
| 53 | Leve | Introducao + visao do fluxo completo |
| 54 | Leve | Divisao segura |
| 55 | Ponte | Arquivo opcional |
| 56 | Entrevista | Transferencia com auditoria em finally |
| 57 | Entrevista | Menu CLI robusto + log de sessao |

## Enunciado

Implemente `operacao_segura(a, b)` com estrutura obrigatoria:

```python
def operacao_segura(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: divisao por zero")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operacao finalizada.")
```

No `main`, teste:

1) `(10, 2)` — divisao valida.
2) `(10, 0)` — divisao por zero.

Exemplo de saida (caso valido):

```
Resultado: 5.0
Operacao finalizada.
```

Exemplo de saida (caso erro):

```
Erro: divisao por zero
Operacao finalizada.
```

## Como executar

```bash
cd "53_introducao_try_except_finally"
python main.py
```
