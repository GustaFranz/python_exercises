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

- Configure logging com nivel INFO no console.
- Implemente pipeline com pelo menos 3 etapas: **carregar**, **limpar** e **agregar**.
- Cada etapa deve registrar inicio com `logging.info`.
- Registros vazios ou invalidos removidos na limpeza devem gerar `logging.warning`.
- Se a quantidade final agregada for zero, registre `logging.error`.
- Processe a lista de vendas fornecida no `main.py` e exiba resumo final (total de registros validos e valor agregado).

## Como executar

```bash
cd "88_logging_pipeline_etapas"
python main.py
```
