# 14 - Set: auditoria de tags do catalogo

## Objetivo

Auditar cobertura de tags obrigatorias e tags orfas com conjuntos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Livraria Saber |
| **Setor** | Varejo / catalogo digital |
| **Solicitacao** | Garantir filtros do e-commerce com tags obrigatorias e limpar tags orfas. |

## Enunciado

produtos = [
    {"nome": "Python Basico", "tags": ["programacao", "iniciante", "python"]},
    {"nome": "Git Pratico", "tags": ["ferramentas", "git", "iniciante"]},
    {"nome": "Logica", "tags": ["logica", "iniciante"]},
    {"nome": "SQL Pro", "tags": ["banco", "avancado", "sql"]},
]

tags_obrigatorias = {"programacao", "iniciante", "ferramentas"}
tags_proibidas = {"spam", "promocao_falsa"}

1) Una todas as tags dos produtos em um `set` (`tags_catalogo`).
2) Calcule:
   - `cobertura_ok`: intersecao com obrigatorias
   - `faltando`: obrigatorias ausentes no catalogo
   - `orfas`: tags do catalogo que nao estao em obrigatorias nem em um set
     `tags_permitidas_extra = {"python", "git", "logica", "banco", "avancado", "sql"}`
   - `bloqueadas`: intersecao com tags_proibidas (deve ficar vazia neste lote)
3) Relatorio de auditoria com totais e cada conjunto ordenado.

## Passo a passo

1. Crie a lista `produtos` e os conjuntos `tags_obrigatorias`, `tags_proibidas` e `tags_permitidas_extra` com os dados do enunciado.
2. Monte `tags_catalogo` unindo as tags de todos os produtos: comece com `tags_catalogo = set()` e, em um `for`, acumule com `tags_catalogo |= set(produto["tags"])` (uniao com atribuicao). Alternativa em uma linha: `set().union(*(p["tags"] for p in produtos))`.
3. Calcule `cobertura_ok = tags_catalogo & tags_obrigatorias` (obrigatorias presentes).
4. Calcule `faltando = tags_obrigatorias - tags_catalogo` (obrigatorias ausentes).
5. Calcule `orfas = tags_catalogo - tags_obrigatorias - tags_permitidas_extra` (tags que ninguem reconhece).
6. Calcule `bloqueadas = tags_catalogo & tags_proibidas` (deve resultar em set vazio neste lote).
7. Exiba o relatorio de auditoria: total de tags no catalogo e cada um dos quatro conjuntos com `sorted(...)`.

## Como executar

```bash
cd "14_set_tags_produtos_catalogo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Catalogo de produtos e regras de tags (enunciado)
produtos = [
    {"nome": "Python Basico", "tags": ["programacao", "iniciante", "python"]},
    {"nome": "Git Pratico", "tags": ["ferramentas", "git", "iniciante"]},
    {"nome": "Logica", "tags": ["logica", "iniciante"]},
    {"nome": "SQL Pro", "tags": ["banco", "avancado", "sql"]},
]

tags_obrigatorias = {"programacao", "iniciante", "ferramentas"}
tags_proibidas = {"spam", "promocao_falsa"}
tags_permitidas_extra = {"python", "git", "logica", "banco", "avancado", "sql"}

# 1) Uniao acumulada: |= agrega as tags de cada produto ao conjunto geral
tags_catalogo = set()
for produto in produtos:
    tags_catalogo |= set(produto["tags"])

# 2) As quatro visoes da auditoria, cada uma com uma operacao de conjunto:
cobertura_ok = tags_catalogo & tags_obrigatorias        # obrigatorias presentes
faltando = tags_obrigatorias - tags_catalogo            # obrigatorias ausentes
orfas = tags_catalogo - tags_obrigatorias - tags_permitidas_extra  # nao reconhecidas
bloqueadas = tags_catalogo & tags_proibidas             # proibidas em uso (esperado: vazio)

# 3) Relatorio com totais e conjuntos ordenados
print("=== AUDITORIA DE TAGS DO CATALOGO ===")
print("Total de tags no catalogo:", len(tags_catalogo))
print("Cobertura ok: ", sorted(cobertura_ok))
print("Faltando:     ", sorted(faltando))
print("Orfas:        ", sorted(orfas))
print("Bloqueadas:   ", sorted(bloqueadas))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Auditoria de tags do catalogo do e-commerce."""

# Regras de tags centralizadas como constantes de modulo
TAGS_OBRIGATORIAS = frozenset({"programacao", "iniciante", "ferramentas"})
TAGS_PROIBIDAS = frozenset({"spam", "promocao_falsa"})
TAGS_PERMITIDAS_EXTRA = frozenset({"python", "git", "logica", "banco", "avancado", "sql"})


def coletar_tags(produtos: list[dict]) -> set[str]:
    """Une as tags de todos os produtos em um unico conjunto.

    set().union(*iteraveis) faz a uniao em uma chamada, sem loop manual.
    """
    return set().union(*(produto["tags"] for produto in produtos))


def auditar(tags_catalogo: set[str]) -> dict[str, set[str]]:
    """Aplica as quatro checagens da auditoria e devolve os conjuntos."""
    return {
        "cobertura_ok": tags_catalogo & TAGS_OBRIGATORIAS,
        "faltando": TAGS_OBRIGATORIAS - tags_catalogo,
        "orfas": tags_catalogo - TAGS_OBRIGATORIAS - TAGS_PERMITIDAS_EXTRA,
        "bloqueadas": tags_catalogo & TAGS_PROIBIDAS,
    }


def main() -> None:
    # Dados de entrada do enunciado
    produtos = [
        {"nome": "Python Basico", "tags": ["programacao", "iniciante", "python"]},
        {"nome": "Git Pratico", "tags": ["ferramentas", "git", "iniciante"]},
        {"nome": "Logica", "tags": ["logica", "iniciante"]},
        {"nome": "SQL Pro", "tags": ["banco", "avancado", "sql"]},
    ]

    # Coleta e audita em duas etapas claras
    tags_catalogo = coletar_tags(produtos)
    resultado = auditar(tags_catalogo)

    # Relatorio ordenado (sorted) para leitura estavel
    print("=== AUDITORIA DE TAGS DO CATALOGO ===")
    print(f"Total de tags no catalogo: {len(tags_catalogo)}")
    for nome, conjunto in resultado.items():
        print(f"{nome:<13}: {sorted(conjunto)}")


if __name__ == "__main__":
    main()
```

</details>
