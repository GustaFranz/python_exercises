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

## Passo a passo

1. Importe `Counter` com `from collections import Counter`.
2. Crie a variavel `texto = "python e bom e python e facil e python"`.
3. Normalize e separe as palavras: `palavras = texto.lower().split()` — `lower()` evita que "Python" e "python" contem separado; `split()` quebra por espaco.
4. Conte com `contagem = Counter(palavras)` — o Counter recebe a lista e ja devolve cada palavra com sua frequencia.
5. Exiba o Counter completo com `print(contagem)`.
6. Pegue a mais frequente com `mais_comum = contagem.most_common(1)` — retorna uma lista com uma tupla, ex.: `[('python', 3)]`. Desempacote com `palavra, qtd = mais_comum[0]`.
7. Exiba `f"Palavra mais frequente: {palavra} ({qtd} ocorrencias)"`.

## Como executar

```bash
cd "96_introducao_counter"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from collections import Counter

# Texto dos depoimentos a analisar
texto = "python e bom e python e facil e python"

# lower() normaliza maiusculas/minusculas; split() separa por espaco
palavras = texto.lower().split()

# Counter conta quantas vezes cada palavra aparece na lista
contagem = Counter(palavras)

# Exibe o Counter completo, ja ordenado do mais para o menos frequente
print(contagem)

# most_common(1) devolve [('python', 3)]; [0] pega a tupla e desempacota
palavra, qtd = contagem.most_common(1)[0]
print(f"Palavra mais frequente: {palavra} ({qtd} ocorrencias)")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Analise de frequencia de palavras em depoimentos de alunos da MktEscolar."""

from collections import Counter

TEXTO_DEPOIMENTOS = "python e bom e python e facil e python"


def contar_palavras(texto: str) -> Counter:
    """Normaliza o texto e devolve a frequencia de cada palavra."""
    # Normalizacao minima: caixa baixa + separacao por espacos
    return Counter(texto.lower().split())


def main() -> None:
    contagem = contar_palavras(TEXTO_DEPOIMENTOS)
    print(contagem)

    # most_common(1)[0] entrega a tupla (palavra, quantidade) do topo
    palavra, qtd = contagem.most_common(1)[0]
    print(f"Palavra mais frequente: {palavra} ({qtd} ocorrencias)")


if __name__ == "__main__":
    main()
```

</details>
