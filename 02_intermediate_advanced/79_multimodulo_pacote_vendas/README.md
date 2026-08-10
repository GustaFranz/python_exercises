# 79 - Multi-modulo: pacote analise_vendas

## Objetivo

Criar pacote Python com __init__.py e imports limpos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / analytics |
| **Solicitacao** | Empacotar analise de vendas escolares para reutilizar em outros scripts. |

## Estrutura de arquivos

```
79_multimodulo_pacote_vendas/
├── main.py
└── analise_vendas/
    ├── __init__.py   # expoe total_vendas e resumo
    ├── vendas.py     # total_vendas(lista_dicts)
    └── relatorio.py  # gerar_resumo(total, qtd)
```

## Enunciado

Dados de teste:
```python
vendas = [
    {"produto": "caderno", "valor": 12},
    {"produto": "caneta", "valor": 3},
]
```

**`analise_vendas/vendas.py`**
```python
def total_vendas(vendas: list[dict]) -> float:
    # soma o campo "valor" de cada dict
```

**`analise_vendas/relatorio.py`**
```python
def gerar_resumo(total: float, qtd: int) -> str:
    # retorna resumo textual da analise
```

**`analise_vendas/__init__.py`**
```python
from .vendas import total_vendas
from .relatorio import gerar_resumo
```

No `main.py`:

1) Importe do pacote: `from analise_vendas import total_vendas, gerar_resumo`.
2) Calcule total e quantidade de vendas.
3) Exiba o resumo.

Exemplo de saida:

```
Total: R$ 15.00 | Vendas: 2
```

## Como executar

```bash
cd "79_multimodulo_pacote_vendas"
python main.py
```
