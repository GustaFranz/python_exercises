# 11 - Introducao a conjuntos set

## Objetivo

Conhecer o tipo set e o mapa dos exercicios 11 a 15.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Marketing Digital Escolar |
| **Setor** | Comunicacao / newsletters |
| **Solicitacao** | Limpar lista de e-mails com duplicatas antes do envio. |

## Visao do bloco (exercicios 11 a 15)

Topico **conjuntos (set)**: unicidade, intersecao, diferenca e auditoria.

| # | Foco |
|---|------|
| 11 | Introducao + e-mails unicos |
| 12 | Intersecao de turmas |
| 13 | Diferenca simetrica |
| 14 | Tags de catalogo |
| 15 | Auditoria de acesso |

## Enunciado

emails_brutos = [
    "ana@escola.com", "bruno@escola.com", "ana@escola.com",
    "carla@escola.com", "bruno@escola.com", "daniel@escola.com",
]
Gere emails_unicos com set e converta de volta para lista ordenada.
Exiba: total bruto, total unico, lista final.

## Passo a passo

1. Crie a lista `emails_brutos` com os 6 e-mails do enunciado (com as duplicatas).
2. Crie `emails_unicos` convertendo a lista em conjunto com `set(emails_brutos)` — o set descarta as duplicatas automaticamente.
3. Converta de volta para lista ordenada com `sorted(emails_unicos)` (set nao tem ordem garantida; `sorted` ja devolve uma lista).
4. Calcule os totais: `len(emails_brutos)` (bruto) e `len(emails_unicos)` (unico).
5. Calcule a economia de envios: diferenca entre o total bruto e o total unico.
6. Exiba: total bruto, total unico, economia de envios e a lista final ordenada.

## Como executar

```bash
cd "11_introducao_conjuntos_set"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Lista bruta exportada da ferramenta de captacao (enunciado)
emails_brutos = [
    "ana@escola.com", "bruno@escola.com", "ana@escola.com",
    "carla@escola.com", "bruno@escola.com", "daniel@escola.com",
]

# set() elimina duplicatas automaticamente: cada e-mail aparece uma vez
emails_unicos = set(emails_brutos)

# sorted() devolve uma lista ordenada (set nao garante ordem de exibicao)
lista_final = sorted(emails_unicos)

# Economia = envios que deixariam de ser duplicados
economia = len(emails_brutos) - len(emails_unicos)

print("Total bruto: ", len(emails_brutos))
print("Total unico: ", len(emails_unicos))
print("Economia de envios:", economia)
print("Lista final: ", lista_final)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Deduplicacao da lista de e-mails antes do envio da newsletter."""


def deduplicar_emails(emails: list[str]) -> list[str]:
    """Remove duplicatas e devolve lista ordenada.

    Normaliza com .strip().lower() antes de deduplicar: em bases reais,
    "Ana@Escola.com " e "ana@escola.com" sao a mesma pessoa.
    """
    return sorted({email.strip().lower() for email in emails})


def main() -> None:
    # Dados de entrada do enunciado
    emails_brutos = [
        "ana@escola.com", "bruno@escola.com", "ana@escola.com",
        "carla@escola.com", "bruno@escola.com", "daniel@escola.com",
    ]

    # Deduplica com set comprehension + ordenacao
    lista_final = deduplicar_emails(emails_brutos)

    # Relatorio de limpeza para o time de marketing
    economia = len(emails_brutos) - len(lista_final)
    print(f"Total bruto:        {len(emails_brutos)}")
    print(f"Total unico:        {len(lista_final)}")
    print(f"Economia de envios: {economia}")
    print("Lista final:")
    for email in lista_final:
        print(f"  {email}")


if __name__ == "__main__":
    main()
```

</details>
