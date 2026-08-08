# 135 - map e dict comprehension

## Objetivo

Combinar `map()` para calcular valores e dict comprehension para montar indice de precos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Cantina Escolar Plus |
| **Setor** | Alimentacao / operacoes |
| **Solicitacao** | Aplicar taxa de servico e indexar precos finais por codigo. |

## Enunciado

```python
codigos = ["S1", "S2", "S3", "S4"]
precos_base = [5.0, 8.5, 12.0, 3.5]
TAXA = 0.10  # 10%
```

1) Use `map` com funcao ou lambda para calcular preco final: `preco * (1 + TAXA)`.
2) Arredonde cada valor com `round(valor, 2)`.
3) Monte `tabela = {codigo: preco_final}` com dict comprehension pareando `codigos` e precos finais.
4) Com dict comprehension, filtre `promocionais = {codigo: preco}` apenas onde preco <= 10.0.
5) Exiba tabela completa, promocionais e o item mais caro (codigo + valor).

## Como executar

```bash
cd "135_map_dict_comprehension"
python main.py
```
