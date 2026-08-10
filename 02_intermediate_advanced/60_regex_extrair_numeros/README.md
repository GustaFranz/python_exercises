# 60 - Regex: extrair numeros

## Objetivo

Extraia todos os numeros de um texto de rastreio com re.findall.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / rastreamento |
| **Solicitacao** | Extrair codigos numericos de texto de rastreio. |

## Enunciado

Texto de rastreio:
```python
texto = "Pedido 4521 enviado em 10/07 com NF 99887"
```

1) Extraia todos os grupos de digitos com `re.findall(r"\d+", texto)`.
2) Exiba a lista de numeros encontrados.

Exemplo de saida:

```
Numeros: ['4521', '10', '07', '99887']
```

## Passo a passo

1. Importe `re` no topo do script.
2. Crie a variavel `texto = "Pedido 4521 enviado em 10/07 com NF 99887"`.
3. Extraia os numeros com `numeros = re.findall(r"\d+", texto)` — no padrao, `\d` casa um digito e `+` significa "um ou mais em sequencia"; o `findall` devolve a lista de todas as ocorrencias, como strings.
4. Exiba o resultado com `print(f"Numeros: {numeros}")`.
5. Observacao: os itens vem como strings (`'4521'`); se precisar somar ou comparar, converta com `int(...)`.

## Como executar

```bash
cd "60_regex_extrair_numeros"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import re

# Texto de rastreio do enunciado
texto = "Pedido 4521 enviado em 10/07 com NF 99887"

# \d casa um digito; + exige um ou mais em sequencia
# findall devolve TODAS as ocorrencias como lista de strings
numeros = re.findall(r"\d+", texto)

# Exibe a lista extraida (itens sao strings, ex.: '4521')
print(f"Numeros: {numeros}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Extrai codigos numericos de textos de rastreio."""

import re

# Padrao compilado uma vez: pronto para processar lotes de mensagens
PADRAO_DIGITOS = re.compile(r"\d+")


def extrair_numeros(texto: str) -> list[str]:
    """Devolve todos os grupos de digitos encontrados no texto.

    Mantem como strings para preservar zeros a esquerda (ex.: '07');
    quem consome decide se converte para int.
    """
    return PADRAO_DIGITOS.findall(texto)


def main() -> None:
    texto = "Pedido 4521 enviado em 10/07 com NF 99887"

    numeros = extrair_numeros(texto)
    print(f"Numeros: {numeros}")


if __name__ == "__main__":
    main()
```

</details>
