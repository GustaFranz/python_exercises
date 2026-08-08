# 143 - Funcao geradora: pipeline de relatorio

## Objetivo

Encadear geradores para simular pipeline de dados (parse -> filtro -> metricas).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinTech Escolar |
| **Setor** | Financeiro / analytics |
| **Solicitacao** | Processar transacoes do dia em pipeline lazy para relatorio executivo. |

## Enunciado

```python
transacoes_brutas = [
    "101;Ana;150.0;ok",
    "102;Bruno;-20.0;ok",
    "103;Carla;300.0;ok",
    "104;Diego;abc;ok",
    "105;Elena;80.0;cancelado",
    "106;Fabio;45.5;ok",
]
VALOR_MINIMO = 50.0
```

Implemente tres geradores:

1) `parse_transacoes(linhas)` — `yield` dict `{id, nome, valor, status}` (ignore linhas invalidas).
2) `filtrar_validas(transacoes)` — `yield` apenas status `"ok"` e valor numerico >= `VALOR_MINIMO`.
3) `gerar_resumo(transacoes)` — `yield` strings `"ID NOME: R$ VALOR"` formatadas.

No `main`:
- Encadeie: `resumo = gerar_resumo(filtrar_validas(parse_transacoes(transacoes_brutas)))`.
- Exiba cada linha do resumo.
- Calcule total aritmetico das transacoes validas (segundo filtro).
- Exiba quantidade processada vs quantidade no lote bruto.

## Como executar

```bash
cd "143_funcao_geradora_pipeline"
python main.py
```
