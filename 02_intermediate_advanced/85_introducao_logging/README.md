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

- Configure logging.basicConfig com nivel INFO.
- Implemente verificar_servidor usando logging.info e logging.error.
- Teste servidor online e offline.

## Como executar

```bash
cd "85_introducao_logging"
python main.py
```
