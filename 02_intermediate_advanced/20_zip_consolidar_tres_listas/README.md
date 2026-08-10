# 20 - Zip: consolidar tres listas

## Objetivo

Consolidar listas paralelas em registros estruturados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | AgroData Cooperativa |
| **Setor** | Agronegocio / cooperativa escolar rural |
| **Solicitacao** | Unificar dados de safra para envio ao sistema da cooperativa. |

## Enunciado

fazendas = ["Sitio Sol", "Fazenda Verde", "Chacara Norte"]
producoes_t = [12.5, 8.0, 15.2]   # toneladas
qualidades = ["A", "B", "A"]
Consolide em lista de dicionarios:
[{"fazenda": ..., "producao_t": ..., "qualidade": ...}, ...]
Use zip e dict comprehension ou loop.
Exiba registros e total de producao das fazendas qualidade A.

## Passo a passo

1. Crie as tres listas paralelas `fazendas`, `producoes_t` e `qualidades` com os dados do enunciado.
2. Crie `registros` com list comprehension sobre o zip das tres listas: `[{"fazenda": f, "producao_t": p, "qualidade": q} for f, p, q in zip(fazendas, producoes_t, qualidades)]`.
3. Exiba cada registro em uma linha (um `for` simples sobre `registros`).
4. Calcule `total_qualidade_a` com `sum` + generator expression filtrando qualidade A: `sum(r["producao_t"] for r in registros if r["qualidade"] == "A")`.
5. Exiba o total de producao das fazendas qualidade A em toneladas.

## Como executar

```bash
cd "20_zip_consolidar_tres_listas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Tres listas paralelas com os dados da safra (enunciado)
fazendas = ["Sitio Sol", "Fazenda Verde", "Chacara Norte"]
producoes_t = [12.5, 8.0, 15.2]   # toneladas
qualidades = ["A", "B", "A"]

# zip cruza as tres listas; a comprehension monta um dict por fazenda
registros = [
    {"fazenda": f, "producao_t": p, "qualidade": q}
    for f, p, q in zip(fazendas, producoes_t, qualidades)
]

# Exibe os registros consolidados, um por linha
print("=== REGISTROS CONSOLIDADOS DA SAFRA ===")
for registro in registros:
    print(f'  {registro["fazenda"]:<15} | {registro["producao_t"]:>5} t | qualidade {registro["qualidade"]}')

# Generator com filtro: soma apenas a producao das fazendas qualidade A
total_qualidade_a = sum(r["producao_t"] for r in registros if r["qualidade"] == "A")
print(f"\nTotal de producao qualidade A: {total_qualidade_a} t")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Consolidacao dos dados de safra para o sistema da cooperativa."""

# Qualidade usada no corte do relatorio, como constante nomeada
QUALIDADE_PREMIUM = "A"


def consolidar_safra(
    fazendas: list[str],
    producoes_t: list[float],
    qualidades: list[str],
) -> list[dict]:
    """Une as tres listas paralelas em registros estruturados.

    strict=True garante alinhamento: se alguma lista vier incompleta
    do campo, o erro aparece na hora em vez de truncar dados.
    """
    return [
        {"fazenda": f, "producao_t": p, "qualidade": q}
        for f, p, q in zip(fazendas, producoes_t, qualidades, strict=True)
    ]


def main() -> None:
    # Dados de entrada do enunciado
    fazendas = ["Sitio Sol", "Fazenda Verde", "Chacara Norte"]
    producoes_t = [12.5, 8.0, 15.2]
    qualidades = ["A", "B", "A"]

    # Consolida em lista de registros prontos para envio
    registros = consolidar_safra(fazendas, producoes_t, qualidades)

    # Exibe os registros formatados
    print("=== REGISTROS CONSOLIDADOS DA SAFRA ===")
    for r in registros:
        print(f'  {r["fazenda"]:<15} | {r["producao_t"]:>5} t | qualidade {r["qualidade"]}')

    # Total apenas das fazendas premium (qualidade A)
    total_premium = sum(
        r["producao_t"] for r in registros if r["qualidade"] == QUALIDADE_PREMIUM
    )
    print(f"\nTotal de producao qualidade {QUALIDADE_PREMIUM}: {total_premium} t")


if __name__ == "__main__":
    main()
```

</details>
