# 37 - Introducao a leitura CSV

## Objetivo

Conhecer modulo csv e o mapa dos exercicios 37 a 41.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | NotasOnline Escolas |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Importar planilha CSV de notas exportada do sistema legado. |

## Visao do bloco (exercicios 37 a 41)

Topico **CSV**: importar e exportar planilhas com modulo csv.

| # | Foco |
|---|------|
| 37 | Introducao + ler notas |
| 38 | Escrever relatorio CSV |
| 39 | Delimitador ; (BR) |
| 40 | Importar vendas |
| 41 | Pipeline limpar e exportar |

## Enunciado

Crie ou assuma notas.csv com cabecalho:
aluno,nota,turma
Ana,8.0,9A
Bruno,6.5,9A
Carla,9.0,9B
Leia com csv.DictReader e exiba cada registro formatado.
Calcule media geral das notas.

## Passo a passo

1. Importe o modulo `csv` e crie a constante `CAMINHO = "notas.csv"`.
2. Crie o arquivo de exemplo primeiro (script autossuficiente): grave o texto do enunciado com `with open(CAMINHO, "w", encoding="utf-8", newline="")` — pode escrever a string direto com `arquivo.write(...)`.
3. Abra para leitura com `with open(CAMINHO, encoding="utf-8", newline="") as arquivo:`.
4. Crie o leitor com `leitor = csv.DictReader(arquivo)` — ele usa a primeira linha como cabecalho e devolve cada linha como dict (`{"aluno": ..., "nota": ..., "turma": ...}`).
5. Percorra o leitor com `for linha in leitor:`, converta a nota com `float(linha["nota"])` (CSV entrega tudo como texto) e acumule as notas em uma lista.
6. Exiba cada registro formatado: `aluno | nota | turma`.
7. Apos o loop, calcule `media = sum(notas) / len(notas)` e exiba com `:.2f`.

## Como executar

```bash
cd "37_introducao_csv_leitura"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv

CAMINHO = "notas.csv"

# Etapa 0: grava o CSV de exemplo (script autossuficiente).
CONTEUDO = """aluno,nota,turma
Ana,8.0,9A
Bruno,6.5,9A
Carla,9.0,9B
"""
# newline="" e a recomendacao oficial do modulo csv para evitar
# linhas em branco extras no Windows.
with open(CAMINHO, "w", encoding="utf-8", newline="") as arquivo:
    arquivo.write(CONTEUDO)

# Leitura: DictReader usa o cabecalho como chaves de cada linha.
notas = []
with open(CAMINHO, encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    print("=== Notas importadas ===")
    for linha in leitor:
        # CSV entrega texto; converte a nota para float antes de usar.
        nota = float(linha["nota"])
        notas.append(nota)
        print(f"{linha['aluno']} | nota {nota} | turma {linha['turma']}")

# Media geral calculada sobre as notas acumuladas.
media = sum(notas) / len(notas)
print(f"Media geral: {media:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Importa CSV de notas do sistema legado e calcula a media geral."""

import csv
from pathlib import Path
from statistics import mean

CAMINHO = Path(__file__).parent / "notas.csv"

CONTEUDO_EXEMPLO = """aluno,nota,turma
Ana,8.0,9A
Bruno,6.5,9A
Carla,9.0,9B
"""


def preparar_arquivo(caminho: Path) -> None:
    """Grava o CSV de exemplo para o script ser autossuficiente."""
    caminho.write_text(CONTEUDO_EXEMPLO, encoding="utf-8")


def ler_notas(caminho: Path) -> list[dict[str, str]]:
    """Le o CSV e retorna as linhas como lista de dicts."""
    # newline="" delega ao modulo csv o tratamento de quebras de linha.
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        # list() materializa o leitor antes de o arquivo fechar.
        return list(csv.DictReader(arquivo))


def main() -> None:
    preparar_arquivo(CAMINHO)
    registros = ler_notas(CAMINHO)

    print("=== Notas importadas ===")
    for linha in registros:
        # Conversao explicita: valores do CSV chegam sempre como str.
        print(f"{linha['aluno']} | nota {float(linha['nota'])} | turma {linha['turma']}")

    # statistics.mean deixa a intencao (media) explicita.
    media = mean(float(linha["nota"]) for linha in registros)
    print(f"Media geral: {media:.2f}")


if __name__ == "__main__":
    main()
```

</details>
