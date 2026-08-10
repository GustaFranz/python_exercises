# 38 - CSV: escrever relatorio

## Objetivo

Exportar relatorio em CSV com csv.writer.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | RH Consolidado |
| **Setor** | Recursos humanos |
| **Solicitacao** | Exportar relatorio de horas para planilha do financeiro. |

## Enunciado

Dados em memoria:
relatorio = [
    {"funcionario": "Ana", "horas": 160},
    {"funcionario": "Bruno", "horas": 152},
]
Exporte para horas.csv com cabecalho funcionario,horas usando csv.DictWriter.
Confirme gravacao lendo e exibindo o arquivo.

## Passo a passo

1. Importe `csv` e crie as constantes `CAMINHO = "horas.csv"` e `CAMPOS = ["funcionario", "horas"]`.
2. Declare a lista `relatorio` do enunciado.
3. Abra o arquivo para escrita com `with open(CAMINHO, "w", encoding="utf-8", newline="") as arquivo:` — o `newline=""` evita linhas em branco extras no Windows.
4. Crie o escritor com `escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)`.
5. Grave o cabecalho com `escritor.writeheader()` e depois todas as linhas de uma vez com `escritor.writerows(relatorio)`.
6. Confirme a gravacao reabrindo o arquivo em modo leitura com `csv.DictReader` e exibindo cada linha no formato `funcionario | horas`.

## Como executar

```bash
cd "38_csv_escrever_relatorio"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv

CAMINHO = "horas.csv"
# fieldnames define a ordem das colunas no arquivo.
CAMPOS = ["funcionario", "horas"]

# Dados em memoria que serao exportados.
relatorio = [
    {"funcionario": "Ana", "horas": 160},
    {"funcionario": "Bruno", "horas": 152},
]

# Escrita: DictWriter mapeia as chaves dos dicts para as colunas.
with open(CAMINHO, "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
    escritor.writeheader()        # primeira linha: funcionario,horas
    escritor.writerows(relatorio)  # grava todas as linhas de uma vez

print(f"Relatorio exportado para {CAMINHO}")

# Confirmacao: reler o arquivo prova que a gravacao funcionou.
with open(CAMINHO, encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    print("=== Conteudo gravado ===")
    for linha in leitor:
        print(f"{linha['funcionario']} | {linha['horas']} horas")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Exporta relatorio de horas para CSV e confirma a gravacao."""

import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / "horas.csv"
CAMPOS = ["funcionario", "horas"]

RELATORIO = [
    {"funcionario": "Ana", "horas": 160},
    {"funcionario": "Bruno", "horas": 152},
]


def exportar_csv(caminho: Path, linhas: list[dict], campos: list[str]) -> None:
    """Grava as linhas em CSV com cabecalho."""
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas)


def ler_csv(caminho: Path) -> list[dict[str, str]]:
    """Le o CSV de volta como lista de dicts."""
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def main() -> None:
    exportar_csv(CAMINHO, RELATORIO, CAMPOS)
    print(f"Relatorio exportado para {CAMINHO.name}")

    # Round-trip: ler o que foi gravado valida a exportacao.
    print("=== Conteudo gravado ===")
    for linha in ler_csv(CAMINHO):
        print(f"{linha['funcionario']} | {linha['horas']} horas")


if __name__ == "__main__":
    main()
```

</details>
