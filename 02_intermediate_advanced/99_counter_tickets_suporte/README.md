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

## Passo a passo

1. Importe `Counter` com `from collections import Counter` e defina a lista `TICKETS` com os 8 dicts do enunciado.
2. Defina `contar_por_categoria(tickets)` que:
   - Extrai as categorias com generator expression e conta: `return Counter(t["categoria"] for t in tickets)`.
3. Defina `contar_criticos(tickets)` que:
   - Retorna `sum(1 for t in tickets if t["prioridade"] == "alta")` — soma 1 para cada ticket critico.
4. Defina `backlog_ordenado(contador)` que retorna `contador.most_common()` — sem argumento, devolve todas as categorias ordenadas da maior para a menor contagem.
5. Defina `verificar_sla(qtd_criticos, limite=3)` que:
   - Se `qtd_criticos <= limite`, retorna `"OK"`.
   - Senao, retorna uma mensagem de alerta, ex.: `f"ALERTA: {qtd_criticos} tickets criticos (limite {limite})"`.
6. Defina `gerar_relatorio(tickets)` que:
   - Chama as funcoes anteriores e imprime, nesta ordem: total de tickets (`len(tickets)`), uma linha `categoria: quantidade` para cada item de `backlog_ordenado`, a quantidade de criticos e o status retornado por `verificar_sla`.
7. No fluxo principal, chame `gerar_relatorio(TICKETS)`. Com os dados do enunciado, espere 5 criticos e SLA em alerta.

## Como executar

```bash
cd "99_counter_tickets_suporte"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from collections import Counter

# Backlog de tickets da plataforma
TICKETS = [
    {"id": 101, "categoria": "login", "prioridade": "alta", "titulo": "Senha bloqueada"},
    {"id": 102, "categoria": "notas", "prioridade": "media", "titulo": "Nota errada"},
    {"id": 103, "categoria": "login", "prioridade": "alta", "titulo": "Acesso negado"},
    {"id": 104, "categoria": "video", "prioridade": "baixa", "titulo": "Aula travando"},
    {"id": 105, "categoria": "notas", "prioridade": "alta", "titulo": "Media incorreta"},
    {"id": 106, "categoria": "pagamento", "prioridade": "alta", "titulo": "Boleto duplicado"},
    {"id": 107, "categoria": "video", "prioridade": "media", "titulo": "Sem audio"},
    {"id": 108, "categoria": "login", "prioridade": "alta", "titulo": "2FA falhou"},
]


def contar_por_categoria(tickets):
    # Generator extrai so a categoria; Counter conta as ocorrencias
    return Counter(t["categoria"] for t in tickets)


def contar_criticos(tickets):
    # Soma 1 para cada ticket com prioridade alta
    return sum(1 for t in tickets if t["prioridade"] == "alta")


def backlog_ordenado(contador):
    # most_common() sem argumento: todas as categorias, da maior para a menor
    return contador.most_common()


def verificar_sla(qtd_criticos, limite=3):
    # Dentro do limite: operacao normal
    if qtd_criticos <= limite:
        return "OK"
    # Acima do limite: alerta de risco operacional
    return f"ALERTA: {qtd_criticos} tickets criticos (limite {limite})"


def gerar_relatorio(tickets):
    contador = contar_por_categoria(tickets)
    criticos = contar_criticos(tickets)

    print(f"Total de tickets: {len(tickets)}")
    print("Por categoria:")
    for categoria, qtd in backlog_ordenado(contador):
        print(f"- {categoria}: {qtd}")
    print(f"Criticos (prioridade alta): {criticos}")
    print(f"SLA: {verificar_sla(criticos)}")


gerar_relatorio(TICKETS)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Relatorio de backlog de tickets e risco de SLA do suporte da Edutech Brasil."""

from collections import Counter

LIMITE_SLA = 3
PRIORIDADE_CRITICA = "alta"

TICKETS = [
    {"id": 101, "categoria": "login", "prioridade": "alta", "titulo": "Senha bloqueada"},
    {"id": 102, "categoria": "notas", "prioridade": "media", "titulo": "Nota errada"},
    {"id": 103, "categoria": "login", "prioridade": "alta", "titulo": "Acesso negado"},
    {"id": 104, "categoria": "video", "prioridade": "baixa", "titulo": "Aula travando"},
    {"id": 105, "categoria": "notas", "prioridade": "alta", "titulo": "Media incorreta"},
    {"id": 106, "categoria": "pagamento", "prioridade": "alta", "titulo": "Boleto duplicado"},
    {"id": 107, "categoria": "video", "prioridade": "media", "titulo": "Sem audio"},
    {"id": 108, "categoria": "login", "prioridade": "alta", "titulo": "2FA falhou"},
]


def contar_por_categoria(tickets: list[dict]) -> Counter:
    """Conta os tickets do backlog por categoria."""
    return Counter(ticket["categoria"] for ticket in tickets)


def contar_criticos(tickets: list[dict]) -> int:
    """Conta os tickets com prioridade critica."""
    return sum(1 for ticket in tickets if ticket["prioridade"] == PRIORIDADE_CRITICA)


def backlog_ordenado(contador: Counter) -> list[tuple[str, int]]:
    """Retorna as categorias ordenadas por volume decrescente."""
    return contador.most_common()


def verificar_sla(qtd_criticos: int, limite: int = LIMITE_SLA) -> str:
    """Avalia o risco de SLA conforme a quantidade de tickets criticos."""
    if qtd_criticos <= limite:
        return "OK"
    return f"ALERTA: {qtd_criticos} tickets criticos (limite {limite})"


def gerar_relatorio(tickets: list[dict]) -> str:
    """Monta o relatorio textual completo do backlog."""
    contador = contar_por_categoria(tickets)
    criticos = contar_criticos(tickets)

    # Monta as linhas em lista e junta no final: facil de testar e estender
    linhas = [f"Total de tickets: {len(tickets)}", "Por categoria:"]
    linhas += [f"- {categoria}: {qtd}" for categoria, qtd in backlog_ordenado(contador)]
    linhas.append(f"Criticos (prioridade {PRIORIDADE_CRITICA}): {criticos}")
    linhas.append(f"SLA: {verificar_sla(criticos)}")
    return "\n".join(linhas)


def main() -> None:
    print(gerar_relatorio(TICKETS))


if __name__ == "__main__":
    main()
```

</details>
