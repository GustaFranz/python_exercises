# 39 - CSV: delimitador ponto e virgula

## Objetivo

Trabalhar CSV no padrao brasileiro com delimitador ;.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Contabilidade Brasil Fiscal |
| **Setor** | Contabilidade |
| **Solicitacao** | Gerar CSV compativel com Excel brasileiro (separador ;). |

## Enunciado

Exporte vendas para vendas_br.csv com delimitador ";".
Dados: produto;preco — ex.: caderno;12,50 (use ponto no valor no CSV: 12.50).
Cabecalho: produto;preco
Leia de volta com csv.reader(delimiter=";") e exiba.

## Passo a passo

1. Importe `csv` e crie as constantes `CAMINHO = "vendas_br.csv"` e `CAMPOS = ["produto", "preco"]`.
2. Declare uma lista `vendas` com alguns produtos e precos usando ponto decimal (ex.: `{"produto": "caderno", "preco": 12.50}`, `{"produto": "caneta", "preco": 2.30}`, `{"produto": "mochila", "preco": 89.90}`).
3. Abra para escrita com `with open(CAMINHO, "w", encoding="utf-8", newline="") as arquivo:`.
4. Crie o escritor com `csv.DictWriter(arquivo, fieldnames=CAMPOS, delimiter=";")` — o `delimiter=";"` troca a virgula pelo ponto e virgula esperado pelo Excel brasileiro.
5. Grave com `writeheader()` e `writerows(vendas)`.
6. Releia com `with open(CAMINHO, encoding="utf-8", newline="")` e `csv.reader(arquivo, delimiter=";")` — o mesmo delimitador precisa ser informado na leitura.
7. Percorra o leitor e exiba cada linha (a primeira sera o cabecalho; cada linha vem como lista, ex.: `["caderno", "12.5"]`).

## Como executar

```bash
cd "39_csv_delimitador_ponto_virgula"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv

CAMINHO = "vendas_br.csv"
CAMPOS = ["produto", "preco"]

# Precos com ponto decimal (formato interno do CSV).
vendas = [
    {"produto": "caderno", "preco": 12.50},
    {"produto": "caneta", "preco": 2.30},
    {"produto": "mochila", "preco": 89.90},
]

# Escrita com delimitador ; — padrao esperado pelo Excel brasileiro.
with open(CAMINHO, "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS, delimiter=";")
    escritor.writeheader()
    escritor.writerows(vendas)

print(f"Arquivo {CAMINHO} gerado com delimitador ';'")

# Leitura: o MESMO delimitador precisa ser informado ao reader.
with open(CAMINHO, encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo, delimiter=";")
    print("=== Conteudo lido ===")
    for linha in leitor:
        # csv.reader devolve cada linha como lista de strings.
        print(" | ".join(linha))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Gera CSV com separador ';' compativel com Excel brasileiro."""

import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / "vendas_br.csv"
CAMPOS = ["produto", "preco"]
# Delimitador centralizado: escrita e leitura usam a mesma constante.
DELIMITADOR = ";"

VENDAS = [
    {"produto": "caderno", "preco": 12.50},
    {"produto": "caneta", "preco": 2.30},
    {"produto": "mochila", "preco": 89.90},
]


def exportar_vendas(caminho: Path, vendas: list[dict]) -> None:
    """Grava as vendas em CSV no padrao BR (separador ;)."""
    # utf-8-sig inclui BOM, que faz o Excel reconhecer acentos direto.
    with caminho.open("w", encoding="utf-8-sig", newline="") as arquivo:
        escritor = csv.DictWriter(
            arquivo, fieldnames=CAMPOS, delimiter=DELIMITADOR
        )
        escritor.writeheader()
        escritor.writerows(vendas)


def ler_vendas(caminho: Path) -> list[list[str]]:
    """Le o arquivo de volta com o mesmo delimitador."""
    with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
        return list(csv.reader(arquivo, delimiter=DELIMITADOR))


def main() -> None:
    exportar_vendas(CAMINHO, VENDAS)
    print(f"Arquivo {CAMINHO.name} gerado com delimitador '{DELIMITADOR}'")

    print("=== Conteudo lido ===")
    for linha in ler_vendas(CAMINHO):
        print(" | ".join(linha))


if __name__ == "__main__":
    main()
```

</details>
