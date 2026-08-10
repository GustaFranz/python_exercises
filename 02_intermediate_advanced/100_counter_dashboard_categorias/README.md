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

Eventos do turno:

```python
eventos = ["cpu", "disco", "cpu", "rede", "cpu", "disco", "memoria", "cpu", "rede", "cpu"]
```

Implemente:

1) `montar_contador(eventos) -> Counter`
2) `calcular_percentual(qtd, total) -> float` — 1 casa decimal
3) `identificar_gargalo(contador) -> tuple[str, int]` — categoria com maior volume
4) `gerar_dashboard(eventos) -> str` — string multilinha para o standup

Formato esperado do dashboard:

```
=== Dashboard de alertas — turno manha ===
cpu: 5 (50.0%)
disco: 2 (20.0%)
rede: 2 (20.0%)
memoria: 1 (10.0%)
Total: 10 eventos
Gargalo: cpu (5 eventos)
```

Ordene categorias por volume decrescente. O `main` deve imprimir o dashboard retornado.

## Como executar

```bash
cd "100_counter_dashboard_categorias"
python main.py
```
