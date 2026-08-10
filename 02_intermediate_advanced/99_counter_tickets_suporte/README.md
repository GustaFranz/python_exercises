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

Tickets do backlog:

```python
tickets = [
    {"id": 101, "categoria": "login", "prioridade": "alta", "titulo": "Senha bloqueada"},
    {"id": 102, "categoria": "notas", "prioridade": "media", "titulo": "Nota errada"},
    {"id": 103, "categoria": "login", "prioridade": "alta", "titulo": "Acesso negado"},
    {"id": 104, "categoria": "video", "prioridade": "baixa", "titulo": "Aula travando"},
    {"id": 105, "categoria": "notas", "prioridade": "alta", "titulo": "Media incorreta"},
    {"id": 106, "categoria": "pagamento", "prioridade": "alta", "titulo": "Boleto duplicado"},
    {"id": 107, "categoria": "video", "prioridade": "media", "titulo": "Sem audio"},
    {"id": 108, "categoria": "login", "prioridade": "alta", "titulo": "2FA falhou"},
]
```

Implemente:

1) `contar_por_categoria(tickets) -> Counter` — conta tickets por categoria.
2) `contar_criticos(tickets) -> int` — conta tickets com `prioridade == "alta"`.
3) `backlog_ordenado(contador) -> list[tuple]` — retorna `contador.most_common()`.
4) `verificar_sla(qtd_criticos, limite=3) -> str` — retorna `"OK"` se `qtd_criticos <= 3`, senao mensagem de alerta.
5) `gerar_relatorio(tickets)` — imprime: total de tickets, contagem por categoria (ordenada), quantidade de criticos e status do SLA.

## Como executar

```bash
cd "99_counter_tickets_suporte"
python main.py
```
