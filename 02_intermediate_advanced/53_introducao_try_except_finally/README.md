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

## Passo a passo

1. Defina `def operacao_segura(a, b):` com os 4 blocos na ordem obrigatoria:
   - `try:` — faca `resultado = a / b` (unica linha que pode falhar).
   - `except ZeroDivisionError:` — exiba `"Erro: divisao por zero"`.
   - `else:` — exiba `f"Resultado: {resultado}"` (roda apenas quando o `try` nao levantou excecao).
   - `finally:` — exiba `"Operacao finalizada."` (roda sempre, com ou sem erro).
2. No fluxo principal, chame `operacao_segura(10, 2)` — deve exibir o resultado e a mensagem de encerramento.
3. Chame `operacao_segura(10, 0)` — deve exibir a mensagem de erro e a mesma mensagem de encerramento.
4. Confira que `"Operacao finalizada."` aparece nas duas chamadas: essa e a garantia do `finally`.

## Como executar

```bash
cd "53_introducao_try_except_finally"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def operacao_segura(a, b):
    try:
        # Unica linha que pode falhar: divisao por zero levanta excecao
        resultado = a / b
    except ZeroDivisionError:
        # Trata o erro especifico sem derrubar o programa
        print("Erro: divisao por zero")
    else:
        # else roda somente quando o try passou sem excecao
        print(f"Resultado: {resultado}")
    finally:
        # finally roda SEMPRE: sucesso ou erro — ideal para encerramento
        print("Operacao finalizada.")


# Caso valido: exibe resultado + encerramento
operacao_segura(10, 2)

# Caso com erro: exibe mensagem de erro + encerramento
operacao_segura(10, 0)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Demonstracao do fluxo completo try/except/else/finally em divisao."""


def operacao_segura(a: float, b: float) -> float | None:
    """Divide a por b exibindo cada etapa do fluxo de tratamento de erros.

    Retorna o resultado da divisao ou None quando b e zero — assim quem
    chama tambem consegue usar o valor, nao apenas ler o print.
    """
    resultado = None
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: divisao por zero")
    else:
        print(f"Resultado: {resultado}")
    finally:
        # Em producao este bloco fecharia conexao, liberaria lock, gravaria log
        print("Operacao finalizada.")
    return resultado


def main() -> None:
    # Cenarios do enunciado: divisao valida e divisao por zero
    operacao_segura(10, 2)
    operacao_segura(10, 0)


if __name__ == "__main__":
    main()
```

</details>
