# 56 - Try finally: transferencia com auditoria obrigatoria

## Objetivo

Simular transferencia entre contas com validacao de saldo e registro de auditoria em todo attempt.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Processar transferencias com fallback seguro e trilha de auditoria mesmo quando a operacao falha. |

## Enunciado

- Use contas simuladas, ex.: `contas = {"ana": 500.0, "bruno": 120.0}`.
- Implemente `transferir(origem, destino, valor)` com `try/except/finally`.
- Se `valor > contas[origem]`, lance `ValueError("Saldo insuficiente")` e nao altere saldos.
- Em caso de sucesso, debite origem e credite destino.
- No `finally`, append em `auditoria.log` (modo append) uma linha por tentativa: origem, destino, valor e status (`ok` ou `fail`).
- Teste 1 transferencia valida e 1 invalida; exiba saldos finais e conteudo do log.

## Passo a passo

1. Crie o dicionario `contas = {"ana": 500.0, "bruno": 120.0}` e a constante `ARQ_AUDITORIA = "auditoria.log"`.
2. Limpe o log no inicio do script (abra com modo `"w"` e feche) para a saida ser igual em toda execucao.
3. Defina `def transferir(origem, destino, valor):` com esta estrutura:
   - Inicie `status = "ok"` antes do `try`.
   - No `try:`, valide primeiro: se `valor > contas[origem]`, levante `raise ValueError("Saldo insuficiente")` — importante: levante ANTES de mexer nos saldos.
   - Ainda no `try:`, faca o debito `contas[origem] -= valor` e o credito `contas[destino] += valor`.
   - No `except ValueError as e:`, mude `status = "fail"` e exiba uma mensagem de falha.
   - No `finally:`, abra `auditoria.log` com `with open(ARQ_AUDITORIA, "a", encoding="utf-8")` e grave `f"{origem}->{destino};{valor};{status}\n"` — o `finally` garante a trilha em sucesso E em falha.
4. Teste `transferir("ana", "bruno", 80.0)` (valida) e `transferir("bruno", "ana", 999.0)` (invalida).
5. Exiba os saldos finais (`print(contas)` ou formatado) — devem ser `ana: 420.0` e `bruno: 200.0`.
6. Leia `auditoria.log` com `with open(..., "r")` e exiba o conteudo: devem existir 2 linhas, uma `ok` e uma `fail`.

## Como executar

```bash
cd "56_try_finally_transacao"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Contas simuladas e arquivo de trilha de auditoria
contas = {"ana": 500.0, "bruno": 120.0}
ARQ_AUDITORIA = "auditoria.log"

# Limpa o log no inicio para a execucao ser reproduzivel
with open(ARQ_AUDITORIA, "w", encoding="utf-8"):
    pass


def transferir(origem, destino, valor):
    # Assume sucesso; o except muda para "fail" se algo der errado
    status = "ok"
    try:
        # Valida ANTES de alterar qualquer saldo
        if valor > contas[origem]:
            raise ValueError("Saldo insuficiente")
        # Transferencia efetiva: debita origem e credita destino
        contas[origem] -= valor
        contas[destino] += valor
    except ValueError as e:
        # Falha de negocio: registra o status e avisa o usuario
        status = "fail"
        print(f"Falha: {e} ({origem} -> {destino}, valor {valor})")
    finally:
        # finally roda SEMPRE: a trilha de auditoria nunca fica sem registro
        with open(ARQ_AUDITORIA, "a", encoding="utf-8") as f:
            f.write(f"{origem}->{destino};{valor};{status}\n")


# Teste 1: valida (ana tem 500, transfere 80)
transferir("ana", "bruno", 80.0)

# Teste 2: invalida (bruno tem 200, tenta transferir 999)
transferir("bruno", "ana", 999.0)

# Saldos finais apos as duas tentativas
print(f"Saldos finais: {contas}")

# Conteudo do log: uma linha por tentativa, com status ok/fail
with open(ARQ_AUDITORIA, "r", encoding="utf-8") as f:
    print("Auditoria:")
    print(f.read(), end="")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Transferencia entre contas com trilha de auditoria garantida por finally."""

from pathlib import Path

ARQ_AUDITORIA = Path("auditoria.log")


def registrar_auditoria(origem: str, destino: str, valor: float, status: str) -> None:
    """Acrescenta uma linha de auditoria; funcao separada facilita teste."""
    with ARQ_AUDITORIA.open("a", encoding="utf-8") as f:
        f.write(f"{origem}->{destino};{valor};{status}\n")


def transferir(contas: dict[str, float], origem: str, destino: str, valor: float) -> bool:
    """Move valor entre contas; devolve True em sucesso, False em falha.

    O finally garante que TODA tentativa gera registro de auditoria,
    mesmo que a validacao de saldo interrompa a operacao.
    """
    status = "ok"
    try:
        # Validacao antes de qualquer alteracao: falha nao corrompe saldos
        if valor > contas[origem]:
            raise ValueError("Saldo insuficiente")
        contas[origem] -= valor
        contas[destino] += valor
    except ValueError as erro:
        status = "fail"
        print(f"Falha: {erro} ({origem} -> {destino}, valor {valor})")
    finally:
        registrar_auditoria(origem, destino, valor, status)
    return status == "ok"


def main() -> None:
    contas = {"ana": 500.0, "bruno": 120.0}

    # Zera o log para a saida ser deterministica a cada execucao
    ARQ_AUDITORIA.write_text("", encoding="utf-8")

    transferir(contas, "ana", "bruno", 80.0)    # sucesso
    transferir(contas, "bruno", "ana", 999.0)   # falha de saldo

    print(f"Saldos finais: {contas}")
    print("Auditoria:")
    print(ARQ_AUDITORIA.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
```

</details>
