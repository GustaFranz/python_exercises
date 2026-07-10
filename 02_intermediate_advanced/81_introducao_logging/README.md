# 81 - Introducao ao logging

## Objetivo

Substituir prints por logging.info em fluxo simples.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Padronizar mensagens do script de verificacao de servidores. |

## Visao do bloco (exercicios 81 a 85)

Topico **logging**: registrar eventos com niveis e destinos configuraveis.

| # | Foco |
|---|------|
| 81 | Introducao + logging.info |
| 82 | Niveis INFO e ERROR |
| 83 | Log em arquivo |
| 84 | Pipeline com log por etapa |
| 85 | Auditoria de importacao CSV com log estruturado |

## Enunciado

- Configure logging.basicConfig com nivel INFO.
- Implemente verificar_servidor usando logging.info e logging.error.
- Teste servidor online e offline.

## Como executar

```bash
cd "81_introducao_logging"
python main.py
```
