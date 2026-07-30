# 99 - Counter: tickets de suporte e SLA

## Objetivo

Analisar fila de tickets com Counter, prioridade e indicador simples de SLA.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / suporte |
| **Solicitacao** | Resumir backlog da plataforma por categoria e sinalizar risco de SLA em tickets criticos. |

## Enunciado

- Processe tickets com campos **categoria** e **prioridade** (`alta`, `media`, `baixa`).
- Use `Counter` para contar tickets por categoria.
- Conte quantos tickets tem prioridade **alta** (criticos).
- Exiba backlog ordenado por categoria (maior volume primeiro).
- Regra de SLA: se houver **mais de 3** tickets com prioridade alta, exiba alerta textual.
- Gere relatorio final com totais, contagem por categoria e status do SLA.

## Como executar

```bash
cd "99_counter_tickets_suporte"
python main.py
```
