# 100 - Counter: dashboard textual para standup

## Objetivo

Montar dashboard textual de alertas por categoria com percentuais e destaque de gargalo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / NOC |
| **Solicitacao** | Painel rapido de alertas por tipo para reuniao diaria de status (standup). |

## Enunciado

- Use `Counter` sobre lista de eventos/alertas por categoria.
- Calcule percentual de cada categoria sobre o total (1 casa decimal).
- Identifique a categoria com maior volume como **gargalo** do periodo.
- Gere dashboard textual pronto para colar no standup (titulo, linhas por categoria, total e gargalo).
- Ordene categorias por volume decrescente no relatorio.

## Como executar

```bash
cd "100_counter_dashboard_categorias"
python main.py
```
