# 134 - map com lambda e list comprehension

## Objetivo

Aplicar `map()` com `lambda` e filtrar resultados com list comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Moda Escolar Online |
| **Setor** | Varejo / catalogo |
| **Solicitacao** | Padronizar nomes de produtos e listar itens em promocao. |

## Enunciado

```python
produtos = ["  CAMISETA POLO ", "tenis escolar", " MOCHILA ", "bone oficial", "calcado esportivo"]
precos = [89.9, 120.0, 150.0, 35.0, 199.9]
LIMITE_PROMOCAO = 100.0
```

1) Use `map(lambda p: p.strip().title(), produtos)` para gerar nomes padronizados.
2) Com list comprehension, monte pares `{nome, preco}` cruzando nomes padronizados e `precos`
   (mesmo indice).
3) Filtre com list comprehension apenas produtos com preco <= `LIMITE_PROMOCAO`.
4) Exiba catalogo padronizado, itens em promocao e quantidade promocional.

## Como executar

```bash
cd "134_map_lambda_list_comprehension"
python main.py
```
