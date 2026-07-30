# 106 - DESAFIO - Monitor de integracoes

## Objetivo

Case mais trabalhado: classes + Counter + HTTP simulado com cache e fallback.

## Conteudos cobertos

- Classes simples
- `Counter` / agregacoes
- Tratamento HTTP simulado (retry/fallback/cache)
- Logging de falhas
- Relatorio operacional

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Nexus Integracoes |
| **Setor** | Tecnologia / integracoes B2B |
| **Solicitacao** | Monitorar consultas a APIs parceiras com cache, fallback e painel de falhas. |

## Estrutura sugerida

```
106_desafio_monitor_integracoes/
├── main.py
├── monitor.py
└── README.md
```

## Enunciado

Simule um cliente HTTP instavel:

```python
def api_parceiro(endpoint: str, falhar: bool = False) -> dict:
    if falhar:
        raise ConnectionError(f"Falha ao consultar {endpoint}")
    return {"endpoint": endpoint, "payload": {"ok": True, "valor": 10}}
```

Checklist (trabalhado, ainda intermediario):

1) Classe `CacheSimples` com `get(chave)` e `set(chave, valor)`.
2) Classe `MonitorIntegracao`:
   - `consultar(endpoint, forcar_falha=False)`:
     - se cache hit -> retorna do cache e registra origem `"cache"`
     - senao chama `api_parceiro`
     - em sucesso: grava cache, origem `"api"`
     - em falha: registra erro (lista ou logging), tenta fallback `{"endpoint": endpoint, "payload": {"ok": False, "valor": 0}}`, origem `"fallback"`
3) Guarde historico de consultas: lista de dicts `{endpoint, origem, ok}`.
4) Com `Counter`, monte painel: contagem por `origem` e por `endpoint`.
5) Metodo `relatorio()` imprime:
   - total de consultas
   - taxa de fallback %
   - top endpoint mais consultado
   - lista de falhas
6) Em `main.py`, execute um roteiro: 2 sucessos no mesmo endpoint (2ª deve ser cache),
   1 falha com fallback, 1 sucesso em outro endpoint; depois imprima o relatorio.

## Como executar

```bash
cd "106_desafio_monitor_integracoes"
python main.py
```
