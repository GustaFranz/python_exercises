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

## Como executar

```bash
cd "56_try_finally_transacao"
python main.py
```
