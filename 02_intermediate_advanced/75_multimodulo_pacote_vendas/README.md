# 75 - Multi-modulo: pacote analise_vendas

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
75_multimodulo_pacote_vendas/
├── main.py
└── analise_vendas/
    ├── __init__.py   # expoe total_vendas e resumo
    ├── vendas.py     # total_vendas(lista_dicts)
    └── relatorio.py  # gerar_resumo(total, qtd)
```

## Enunciado

- Implemente total_vendas e gerar_resumo nos modulos do pacote.
- Configure __init__.py para exportar as funcoes.
- Em main.py importe do pacote e exiba resumo.

## Como executar

```bash
cd "75_multimodulo_pacote_vendas"
python main.py
```
