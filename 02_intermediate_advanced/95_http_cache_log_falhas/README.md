# 95 - HTTP: cache e log de falhas

## Objetivo

Cachear respostas HTTP simuladas e registrar falhas em log.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Evitar consultas repetidas a API de indicadores escolares. |

## Enunciado

Cache global:
```python
cache_api = {}
```

Implemente:

```python
def simular_indicador(id: int, falhar: bool = False) -> dict:
    # falhar True  -> {"status": 500, "erro": "Erro interno"}
    # falhar False -> {"status": 200, "dados": {"id": id, "valor": id * 10}}

def buscar_indicador(id: int, falhar: bool = False):
    # se id no cache: retorna cache[id] com mensagem "Cache hit"
    # senao consulta API; se 200 grava cache e retorna
    # se falha: logging.error e retorna None
```

No `main`:

1) Chame `buscar_indicador(1)` duas vezes — 2a deve usar cache.
2) Chame `buscar_indicador(2, falhar=True)` — registre falha com `logging.error`.

Exemplo de saida:

```
Consultando API id=1...
Cache hit id=1
Erro ao buscar id=2
```

## Como executar

```bash
cd "95_http_cache_log_falhas"
python main.py
```
