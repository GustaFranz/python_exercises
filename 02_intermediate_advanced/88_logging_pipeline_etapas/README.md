# 88 - Logging: pipeline ETL por etapas

## Objetivo

Montar um mini pipeline ETL com logging em cada etapa e niveis corretos para falhas de dados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | Rastrear importacao de vendas escolares com alertas quando a base chega vazia ou invalida. |

## Enunciado

Dados brutos (simulando CSV importado):

```python
vendas_brutas = [
    {"produto": "Caderno", "valor": 12.50},
    {"produto": "", "valor": 0},
    {"produto": "Caneta", "valor": 3.00},
    {"produto": "   ", "valor": 5.00},
    {"produto": "Lapis", "valor": -1},
    {"produto": "Borracha", "valor": 2.00},
]
```

Regra de invalidacao: produto vazio/whitespace **ou** valor <= 0.

Implemente pipeline ETL com logging (`logging.basicConfig`, nivel INFO):

1) `carregar_vendas(fonte)` — log `"Etapa 1: carregar"`, retorna lista bruta
2) `limpar_vendas(vendas)` — log `"Etapa 2: limpar"`, remove invalidos; cada descarte gera `logging.warning` com motivo
3) `agregar_vendas(vendas)` — log `"Etapa 3: agregar"`, retorna `{"qtd": int, "total": float}`; se qtd == 0, `logging.error`
4) `executar_pipeline(fonte)` — orquestra as 3 etapas

Exiba resumo final: quantidade valida e valor total agregado.

## Como executar

```bash
cd "88_logging_pipeline_etapas"
python main.py
```
