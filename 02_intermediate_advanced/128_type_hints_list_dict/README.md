# 128 - Type hints: list e dict

## Objetivo

Anotar funcoes que recebem list[str] e retornam dict[str, float].

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Tipar funcoes do relatorio de frequencia de palavras em redacoes. |

## Enunciado

Implemente com type hints:

```python
def contar_tamanhos(palavras: list[str]) -> dict[str, int]:
    # retorna {palavra: len(palavra)} para cada palavra

def media_tamanhos(palavras: list[str]) -> float:
    # media dos tamanhos; retorna 0.0 se lista vazia
```

No `main`:

1) Teste com `palavras = ["ana", "bolo", "escola"]`.
2) Exiba o dict de tamanhos e a media.

Exemplo de saida:

```
Tamanhos: {'ana': 3, 'bolo': 4, 'escola': 6}
Media: 4.33
```

## Passo a passo

1. Defina `contar_tamanhos(palavras: list[str]) -> dict[str, int]` usando dict comprehension: `{palavra: len(palavra) for palavra in palavras}`.
2. Defina `media_tamanhos(palavras: list[str]) -> float`:
   - trate a borda primeiro: `if not palavras: return 0.0`;
   - senao, retorne `sum(len(p) for p in palavras) / len(palavras)`.
3. No fluxo principal, crie `palavras = ["ana", "bolo", "escola"]`.
4. Exiba `Tamanhos:` com o dict retornado por `contar_tamanhos` e `Media:` com o retorno de `media_tamanhos` formatado com 2 casas (`f"{media:.2f}"`).
5. Confira a saida com o exemplo do enunciado (media de 3, 4 e 6 = 4.33).

## Como executar

```bash
cd "128_type_hints_list_dict"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def contar_tamanhos(palavras: list[str]) -> dict[str, int]:
    # dict comprehension: cada palavra vira chave, seu tamanho vira valor
    return {palavra: len(palavra) for palavra in palavras}


def media_tamanhos(palavras: list[str]) -> float:
    # Borda tratada primeiro: evita divisao por zero com lista vazia
    if not palavras:
        return 0.0
    # Generator expression soma os tamanhos sem criar lista intermediaria
    return sum(len(p) for p in palavras) / len(palavras)


palavras = ["ana", "bolo", "escola"]

# Exibe o dict completo e a media com 2 casas decimais
print(f"Tamanhos: {contar_tamanhos(palavras)}")
print(f"Media: {media_tamanhos(palavras):.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Metricas de tamanho de palavras para o relatorio de redacoes."""

from statistics import fmean


def contar_tamanhos(palavras: list[str]) -> dict[str, int]:
    """Mapeia cada palavra para seu numero de caracteres."""
    return {palavra: len(palavra) for palavra in palavras}


def media_tamanhos(palavras: list[str]) -> float:
    """Media dos tamanhos das palavras; 0.0 para lista vazia."""
    # Guard clause: fmean levanta StatisticsError com sequencia vazia
    if not palavras:
        return 0.0
    # fmean e a media da stdlib: sempre float, precisa e legivel
    return fmean(len(p) for p in palavras)


def main() -> None:
    palavras = ["ana", "bolo", "escola"]
    print(f"Tamanhos: {contar_tamanhos(palavras)}")
    print(f"Media: {media_tamanhos(palavras):.2f}")


if __name__ == "__main__":
    main()
```

</details>
