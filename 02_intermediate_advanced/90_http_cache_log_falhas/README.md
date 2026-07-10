# 90 - HTTP: cache e log de falhas

## Objetivo

Cachear respostas HTTP simuladas e registrar falhas em log.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Evitar consultas repetidas a API de indicadores escolares. |

## Enunciado

- Implemente buscar_indicador com cache em dict.
- Registre falhas com logging.error.
- Teste cache hit e falha de API.

## Como executar

```bash
cd "90_http_cache_log_falhas"
python main.py
```
