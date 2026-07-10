# 87 - HTTP: retry simples

## Objetivo

Tentar novamente consulta HTTP simulada apos falha temporaria.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / integracoes |
| **Solicitacao** | Repetir consulta ao servico de monitoramento quando falhar na primeira tentativa. |

## Enunciado

- Implemente consultar_com_retry com ate 3 tentativas.
- Simule falha na 1a tentativa e sucesso na 2a.

## Como executar

```bash
cd "87_http_retry_simples"
python main.py
```
