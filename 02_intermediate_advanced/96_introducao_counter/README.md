# 96 - Introducao ao Counter

## Objetivo

Contar frequencia de palavras com collections.Counter.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MktEscolar |
| **Setor** | Marketing / conteudo |
| **Solicitacao** | Analisar palavras mais usadas em depoimentos de alunos no site. |

## Visao do bloco (exercicios 96 a 100)

Topico **Counter e defaultdict**: agregar e agrupar dados com collections.

| # | Foco |
|---|------|
| 96 | Introducao + Counter frequencia de palavras |
| 97 | Top 3 itens mais frequentes |
| 98 | defaultdict agrupar vendas por vendedor |
| 99 | Tickets por categoria + SLA de prioridade alta |
| 100 | Dashboard textual com percentual e gargalo |

## Enunciado

Texto de depoimentos:

```python
texto = "python e bom e python e facil e python"
```

1) Normalize o texto: `lower()` e `split()` por espaco.
2) Use `Counter` para contar a frequencia de cada palavra.
3) Exiba o `Counter` completo e a palavra mais frequente (use `most_common(1)`).

Exemplo de saida esperada:

```
Counter({'python': 3, 'e': 2, 'bom': 1, 'facil': 1})
Palavra mais frequente: python (3 ocorrencias)
```

## Como executar

```bash
cd "96_introducao_counter"
python main.py
```
