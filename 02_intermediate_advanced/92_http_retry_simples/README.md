# 92 - HTTP: retry simples

## Objetivo

Tentar novamente consulta HTTP simulada apos falha temporaria.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / integracoes |
| **Solicitacao** | Repetir consulta ao servico de monitoramento quando falhar na primeira tentativa. |

## Enunciado

Implemente simulacao e retry:

```python
def simular_servico(tentativa: int) -> dict:
    # tentativa 1 -> {"status": 0, "erro": "Timeout"}
    # tentativa >= 2 -> {"status": 200, "dados": "Servidor OK"}

def consultar_com_retry(max_tentativas: int = 3):
    # tenta de 1 ate max_tentativas
    # retorna dados quando status 200
    # se esgotar tentativas: retorna None e mensagem de falha
```

No `main`:

1) Chame `consultar_com_retry(3)`.
2) Exiba resultado — falha na 1a tentativa, sucesso na 2a.

Exemplo de saida:

```
Tentativa 1: falhou (Timeout)
Tentativa 2: sucesso
Dados: Servidor OK
```

## Como executar

```bash
cd "92_http_retry_simples"
python main.py
```
