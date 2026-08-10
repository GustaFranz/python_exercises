# 94 - HTTP: consulta com fallback

## Objetivo

Consultar API simulada de clima com dados padrao em caso de falha.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | AgroEscola |
| **Setor** | Educacao / campo |
| **Solicitacao** | Exibir previsao do tempo para visita tecnica mesmo se API falhar. |

## Enunciado

Dados padrao (fallback):
```python
DADOS_PADRAO = {"cidade": "Campinas", "temp": 25, "fonte": "cache local"}
```

Implemente:

```python
def simular_clima_api(sucesso: bool = True) -> dict:
    # sucesso True  -> {"status": 200, "cidade": "Campinas", "temp": 28}
    # sucesso False -> {"status": 0, "erro": "Timeout"}

def obter_previsao(usar_api: bool = True) -> dict:
    # tenta API; se status 200 retorna dados com fonte "api"
    # senao retorna DADOS_PADRAO com aviso "Usando dados em cache"
```

No `main`:

1) Teste com API falhando (`usar_api=True`, simule falha).
2) Exiba fonte dos dados (`api` ou `cache local`).

Exemplo de saida:

```
Usando dados em cache
Cidade: Campinas | Temp: 25 | Fonte: cache local
```

## Como executar

```bash
cd "94_http_clima_fallback"
python main.py
```
