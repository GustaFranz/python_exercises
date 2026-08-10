# 85 - Introducao ao logging

## Objetivo

Substituir prints por logging.info em fluxo simples.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Padronizar mensagens do script de verificacao de servidores. |

## Visao do bloco (exercicios 85 a 89)

Topico **logging**: registrar eventos com niveis e destinos configuraveis.

| # | Foco |
|---|------|
| 85 | Introducao + logging.info |
| 86 | Niveis INFO e ERROR |
| 87 | Log em arquivo |
| 88 | Mini ETL com log INFO/WARNING/ERROR por etapa |
| 89 | Auditoria de importacao CSV com log estruturado |

## Enunciado

1) Configure logging no inicio:
```python
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
```

2) Implemente:
```python
def verificar_servidor(nome: str, online: bool) -> None:
    # online True  -> logging.info(f"Servidor {nome}: OK")
    # online False -> logging.error(f"Servidor {nome}: OFFLINE")
```

3) Teste com `("web-01", True)` e `("db-01", False)`.

Nao use `print` — apenas `logging`.

Exemplo de saida:

```
INFO: Servidor web-01: OK
ERROR: Servidor db-01: OFFLINE
```

## Como executar

```bash
cd "85_introducao_logging"
python main.py
```
