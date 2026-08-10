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

## Passo a passo

1. Defina a classe `SaldoInsuficienteError(Exception)` — o corpo pode ser so `pass` (ou uma docstring).
2. Defina `def sacar(saldo: float, valor: float) -> float:`.
3. Dentro da funcao, se `valor > saldo`, levante o erro com `raise SaldoInsuficienteError(f"Saldo {saldo:g} insuficiente para sacar {valor:g}")` — o `:g` exibe `70` em vez de `70.0` na mensagem, como no exemplo de saida.
4. Caso contrario, retorne `saldo - valor`.
5. No fluxo principal, crie `saldo = 100.0` e faca o saque valido: `saldo = sacar(saldo, 30)`, exibindo `f"Saque OK. Saldo restante: {saldo}"`.
6. Faca o saque invalido dentro de `try:` -> `sacar(saldo, 80)` e capture com `except SaldoInsuficienteError as e:`, exibindo `f"Erro: {e}"`.

## Como executar

```bash
cd "48_introducao_excecao_customizada"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Excecao customizada: herda de Exception e deixa a regra de negocio explicita
class SaldoInsuficienteError(Exception):
    pass


def sacar(saldo, valor):
    # Regra de negocio: nao permitir saque maior que o saldo disponivel
    if valor > saldo:
        # :g remove o ".0" de numeros inteiros na mensagem (70.0 -> 70)
        raise SaldoInsuficienteError(
            f"Saldo {saldo:g} insuficiente para sacar {valor:g}"
        )
    # Saque aprovado: devolve o saldo atualizado
    return saldo - valor


# Saldo inicial da carteira (float para exibir 70.0 no saque valido)
saldo = 100.0

# Saque valido: atualiza o saldo com o retorno da funcao
saldo = sacar(saldo, 30)
print(f"Saque OK. Saldo restante: {saldo}")

# Saque invalido: captura a excecao e mostra mensagem amigavel
try:
    saldo = sacar(saldo, 80)
except SaldoInsuficienteError as e:
    # str(e) contem a mensagem passada no raise
    print(f"Erro: {e}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Saque de carteira digital com excecao de negocio para saldo insuficiente."""


class SaldoInsuficienteError(Exception):
    """Saque solicitado acima do saldo disponivel na carteira."""


def sacar(saldo: float, valor: float) -> float:
    """Debita valor do saldo; levanta SaldoInsuficienteError se nao houver fundos.

    A funcao nao imprime nada: quem chama decide como apresentar o
    resultado, o que facilita reuso e testes.
    """
    # Guard clause: valida primeiro, fluxo principal fica sem indentacao extra
    if valor > saldo:
        raise SaldoInsuficienteError(
            f"Saldo {saldo:g} insuficiente para sacar {valor:g}"
        )
    return saldo - valor


def main() -> None:
    saldo = 100.0

    # Caso de sucesso: o retorno vira o novo saldo
    saldo = sacar(saldo, 30)
    print(f"Saque OK. Saldo restante: {saldo}")

    # Caso de falha: excecao especifica capturada e traduzida para o usuario
    try:
        saldo = sacar(saldo, 80)
    except SaldoInsuficienteError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
```

</details>
