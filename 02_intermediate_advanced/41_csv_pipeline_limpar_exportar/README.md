# 41 - CSV: pipeline limpar e exportar

## Objetivo

Pipeline completo: ler CSV sujo, limpar e exportar CSV valido.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | Limpar base de clientes importada antes de subir ao CRM. |

## Enunciado

clientes_sujos.csv com problemas:
nome,email,idade
Ana,ana@mail.com,25
,bruno@mail.com,30        <- nome vazio
Carla,email-invalido,abc  <- idade invalida
Daniel,daniel@mail.com,28
Pipeline:
- 1) Ler CSV
- 2) Filtrar: nome nao vazio, idade numerica, "@" no email
- 3) Exportar clientes_limpos.csv
Exiba: lidos, descartados, exportados.

## Passo a passo

1. Importe `csv` e crie as constantes `ENTRADA = "clientes_sujos.csv"`, `SAIDA = "clientes_limpos.csv"` e `CAMPOS = ["nome", "email", "idade"]`.
2. Grave `clientes_sujos.csv` com os dados do enunciado (incluindo a linha com nome vazio e a com email/idade invalidos) usando `with open(..., "w", encoding="utf-8", newline="")`.
3. Defina `def linha_valida(linha):` que retorna `True` somente se as tres regras passarem:
   - `linha["nome"].strip()` nao vazio;
   - `"@" in linha["email"]`;
   - idade numerica — use `linha["idade"].strip().isdigit()` ou `int(...)` dentro de `try/except ValueError`.
4. Defina `def ler_clientes(caminho):` que abre o arquivo e retorna `list(csv.DictReader(arquivo))`.
5. Defina `def exportar_clientes(caminho, clientes):` que grava com `csv.DictWriter(arquivo, fieldnames=CAMPOS)`, `writeheader()` e `writerows(clientes)`.
6. Monte o pipeline no fluxo principal:
   - `lidos = ler_clientes(ENTRADA)`;
   - `limpos = [c for c in lidos if linha_valida(c)]` (list comprehension como filtro);
   - `exportar_clientes(SAIDA, limpos)`.
7. Exiba o resumo: total de lidos (`len(lidos)`), descartados (`len(lidos) - len(limpos)`) e exportados (`len(limpos)`).

## Como executar

```bash
cd "41_csv_pipeline_limpar_exportar"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv

ENTRADA = "clientes_sujos.csv"
SAIDA = "clientes_limpos.csv"
CAMPOS = ["nome", "email", "idade"]

# Etapa 0: grava a base suja de exemplo (script autossuficiente).
CONTEUDO_SUJO = """nome,email,idade
Ana,ana@mail.com,25
,bruno@mail.com,30
Carla,email-invalido,abc
Daniel,daniel@mail.com,28
"""
with open(ENTRADA, "w", encoding="utf-8", newline="") as arquivo:
    arquivo.write(CONTEUDO_SUJO)


def linha_valida(linha):
    # Regra 1: nome nao pode ser vazio (strip descarta so-espacos).
    if not linha["nome"].strip():
        return False
    # Regra 2: email precisa conter @ (validacao minima).
    if "@" not in linha["email"]:
        return False
    # Regra 3: idade precisa ser numerica; int() falha para "abc".
    try:
        int(linha["idade"])
    except ValueError:
        return False
    return True


def ler_clientes(caminho):
    # Etapa 1 do pipeline: ler o CSV bruto como lista de dicts.
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def exportar_clientes(caminho, clientes):
    # Etapa 3 do pipeline: gravar somente as linhas aprovadas.
    with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(clientes)


# Pipeline: ler -> filtrar -> exportar.
lidos = ler_clientes(ENTRADA)
# Etapa 2: list comprehension aplica o filtro de qualidade.
limpos = [cliente for cliente in lidos if linha_valida(cliente)]
exportar_clientes(SAIDA, limpos)

# Resumo do processamento.
print(f"Lidos: {len(lidos)}")
print(f"Descartados: {len(lidos) - len(limpos)}")
print(f"Exportados: {len(limpos)} (arquivo {SAIDA})")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Pipeline de qualidade: le CSV sujo, filtra invalidos e exporta base limpa."""

import csv
from pathlib import Path

PASTA = Path(__file__).parent
ENTRADA = PASTA / "clientes_sujos.csv"
SAIDA = PASTA / "clientes_limpos.csv"
CAMPOS = ["nome", "email", "idade"]

CONTEUDO_SUJO = """nome,email,idade
Ana,ana@mail.com,25
,bruno@mail.com,30
Carla,email-invalido,abc
Daniel,daniel@mail.com,28
"""

Cliente = dict[str, str]


def linha_valida(linha: Cliente) -> bool:
    """Aplica as tres regras de qualidade da base."""
    # Guard clauses: qualquer regra violada reprova a linha.
    if not linha["nome"].strip():
        return False
    if "@" not in linha["email"]:
        return False
    # isdigit() cobre inteiros nao negativos vindos como texto.
    if not linha["idade"].strip().isdigit():
        return False
    return True


def ler_clientes(caminho: Path) -> list[Cliente]:
    """Etapa 1: le o CSV bruto como lista de dicts."""
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def exportar_clientes(caminho: Path, clientes: list[Cliente]) -> None:
    """Etapa 3: grava a base limpa com o mesmo cabecalho."""
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(clientes)


def main() -> None:
    # Prepara a base suja de exemplo (script autossuficiente).
    ENTRADA.write_text(CONTEUDO_SUJO, encoding="utf-8")

    # Pipeline: ler -> filtrar -> exportar.
    lidos = ler_clientes(ENTRADA)
    limpos = [cliente for cliente in lidos if linha_valida(cliente)]
    exportar_clientes(SAIDA, limpos)

    # Resumo do processamento para auditoria.
    print(f"Lidos: {len(lidos)}")
    print(f"Descartados: {len(lidos) - len(limpos)}")
    print(f"Exportados: {len(limpos)} (arquivo {SAIDA.name})")


if __name__ == "__main__":
    main()
```

</details>
