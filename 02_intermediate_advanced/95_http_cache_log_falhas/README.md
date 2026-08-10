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

## Passo a passo

1. Importe `logging` e configure com `logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")`.
2. Crie o dict global `cache_api = {}` — as chaves serao os ids e os valores, os dados retornados pela API.
3. Defina `simular_indicador(id, falhar=False)` que:
   - Se `falhar` for `True`, retorna `{"status": 500, "erro": "Erro interno"}`.
   - Senao, retorna `{"status": 200, "dados": {"id": id, "valor": id * 10}}`.
4. Defina `buscar_indicador(id, falhar=False)` que segue esta ordem:
   - Primeiro verifica o cache: `if id in cache_api:` exibe `f"Cache hit id={id}"` e retorna `cache_api[id]` sem consultar a API.
   - Senao, exibe `f"Consultando API id={id}..."` e chama `resposta = simular_indicador(id, falhar)`.
   - Se `resposta["status"] == 200`: grava `cache_api[id] = resposta["dados"]` e retorna os dados.
   - Se falhou: registra `logging.error(f"Erro ao buscar id={id}")` e retorna `None`.
5. No fluxo principal:
   - Chame `buscar_indicador(1)` duas vezes — a primeira consulta a API, a segunda deve exibir `Cache hit`.
   - Chame `buscar_indicador(2, falhar=True)` — deve gerar o log de erro e retornar `None`.
6. Confira a saida: uma consulta, um cache hit e um erro logado.

## Como executar

```bash
cd "95_http_cache_log_falhas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Cache global: id do indicador -> dados ja consultados
cache_api = {}


def simular_indicador(id, falhar=False):
    # Simula a API de indicadores: erro interno ou sucesso com dados
    if falhar:
        return {"status": 500, "erro": "Erro interno"}
    return {"status": 200, "dados": {"id": id, "valor": id * 10}}


def buscar_indicador(id, falhar=False):
    # 1) Cache primeiro: evita chamada repetida a API
    if id in cache_api:
        print(f"Cache hit id={id}")
        return cache_api[id]

    # 2) Nao esta no cache: consulta a API simulada
    print(f"Consultando API id={id}...")
    resposta = simular_indicador(id, falhar)

    # 3) Sucesso: grava no cache para as proximas chamadas
    if resposta["status"] == 200:
        cache_api[id] = resposta["dados"]
        return resposta["dados"]

    # 4) Falha: registra no log e devolve None
    logging.error(f"Erro ao buscar id={id}")
    return None


# 1a chamada: consulta a API e preenche o cache
buscar_indicador(1)
# 2a chamada do mesmo id: deve responder direto do cache
buscar_indicador(1)
# Chamada com falha: gera logging.error e retorna None
buscar_indicador(2, falhar=True)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cliente de indicadores escolares com cache em memoria e log de falhas."""

import logging

logger = logging.getLogger(__name__)

# Cache de modulo: indicador_id -> dados retornados pela API
_cache_api: dict[int, dict] = {}


def simular_indicador(indicador_id: int, falhar: bool = False) -> dict:
    """Simula a API de indicadores (erro interno ou sucesso)."""
    if falhar:
        return {"status": 500, "erro": "Erro interno"}
    return {"status": 200, "dados": {"id": indicador_id, "valor": indicador_id * 10}}


def buscar_indicador(indicador_id: int, falhar: bool = False) -> dict | None:
    """Busca o indicador com estrategia cache-first.

    Retorna os dados do indicador ou None quando a API falha.
    """
    # Cache hit: responde sem tocar na API
    if indicador_id in _cache_api:
        print(f"Cache hit id={indicador_id}")
        return _cache_api[indicador_id]

    print(f"Consultando API id={indicador_id}...")
    resposta = simular_indicador(indicador_id, falhar)

    # Guard clause: falha e logada e encerra o fluxo cedo
    if resposta["status"] != 200:
        logger.error("Erro ao buscar id=%d", indicador_id)
        return None

    # Sucesso: popula o cache antes de devolver
    _cache_api[indicador_id] = resposta["dados"]
    return resposta["dados"]


def main() -> None:
    buscar_indicador(1)              # consulta a API e grava no cache
    buscar_indicador(1)              # mesma chave: cache hit
    buscar_indicador(2, falhar=True)  # falha: log de ERROR e retorno None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
```

</details>
