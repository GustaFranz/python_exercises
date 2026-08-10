# 83 - Argparse: relatorio de notas

## Objetivo

CLI aplicada para gerar relatorio a partir de arquivo e media minima.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Ferramenta de linha de comando para filtrar alunos aprovados em CSV. |

## Enunciado

Configure argparse:

- `--entrada` (str): arquivo CSV com colunas `nome,nota`
- `--corte` (float, padrao `7.0`): nota minima para aprovacao

CSV de exemplo (crie `notas.csv` no inicio do script se nao existir):

```csv
nome,nota
Ana,8.5
Bruno,6.0
Carla,9.0
```

No `main`:

1) Leia o CSV com modulo `csv`.
2) Filtre alunos com nota >= corte.
3) Exiba quantidade e nomes dos aprovados.

Exemplo de execucao:

```bash
python main.py --entrada notas.csv --corte 7.0
```

Exemplo de saida:

```
Aprovados (corte 7.0): 2
- Ana
- Carla
```

## Passo a passo

1. Importe `argparse`, `csv` e `os` no topo do arquivo.
2. Defina a funcao `criar_csv_exemplo(caminho)` que:
   - Verifica com `os.path.exists(caminho)` se o arquivo ja existe; se existir, retorna sem fazer nada.
   - Se nao existir, abre com `with open(caminho, "w", newline="", encoding="utf-8")` e grava o cabecalho `nome,nota` e as linhas `Ana,8.5`, `Bruno,6.0` e `Carla,9.0` usando `csv.writer`.
3. Defina a funcao `criar_parser()` que:
   - Instancia `argparse.ArgumentParser`.
   - Adiciona `--entrada` (tipo `str`, padrao `"notas.csv"`).
   - Adiciona `--corte` com `type=float` e `default=7.0` — o argparse converte o texto digitado para float automaticamente.
   - Retorna o parser.
4. Defina a funcao `ler_alunos(caminho)` que:
   - Abre o arquivo com `with open(caminho, encoding="utf-8")`.
   - Le as linhas com `csv.DictReader` e retorna uma lista de dicts `{"nome": str, "nota": float}`, convertendo a nota com `float()`.
5. Defina a funcao `filtrar_aprovados(alunos, corte)` que retorna a lista de nomes com `nota >= corte` (use list comprehension).
6. Defina a funcao `main()` que:
   - Chama `criar_csv_exemplo("notas.csv")`.
   - Faz o parse dos argumentos.
   - Chama `ler_alunos(args.entrada)` e `filtrar_aprovados(alunos, args.corte)`.
   - Exibe `f"Aprovados (corte {args.corte}): {quantidade}"` seguido de uma linha `- {nome}` para cada aprovado.
7. Chame `main()` no final e teste com cortes diferentes (ex.: `--corte 6.0` deve aprovar os 3).

## Como executar

```bash
cd "83_argparse_relatorio_notas"
python main.py --entrada notas.csv --corte 7.0
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import argparse
import csv
import os

# Constante com o arquivo padrao de notas
ARQUIVO_PADRAO = "notas.csv"


def criar_csv_exemplo(caminho):
    # Evita sobrescrever um arquivo que o usuario ja tenha editado
    if os.path.exists(caminho):
        return
    # newline="" evita linhas em branco extras no Windows
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome", "nota"])
        escritor.writerow(["Ana", "8.5"])
        escritor.writerow(["Bruno", "6.0"])
        escritor.writerow(["Carla", "9.0"])


def criar_parser():
    parser = argparse.ArgumentParser(description="Relatorio de aprovados da Edutech Brasil")
    parser.add_argument("--entrada", default=ARQUIVO_PADRAO, help="arquivo CSV com nome,nota")
    # type=float converte o texto digitado no terminal para numero
    parser.add_argument("--corte", type=float, default=7.0, help="nota minima para aprovacao")
    return parser


def ler_alunos(caminho):
    # DictReader transforma cada linha em dict usando o cabecalho como chaves
    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        # Converte a nota (texto no CSV) para float ja na leitura
        return [{"nome": linha["nome"], "nota": float(linha["nota"])} for linha in leitor]


def filtrar_aprovados(alunos, corte):
    # List comprehension: mantem apenas os nomes com nota igual ou acima do corte
    return [aluno["nome"] for aluno in alunos if aluno["nota"] >= corte]


def main():
    # Garante que o CSV de exemplo existe antes de ler
    criar_csv_exemplo(ARQUIVO_PADRAO)
    args = criar_parser().parse_args()

    alunos = ler_alunos(args.entrada)
    aprovados = filtrar_aprovados(alunos, args.corte)

    # Relatorio final: quantidade e lista de nomes
    print(f"Aprovados (corte {args.corte}): {len(aprovados)}")
    for nome in aprovados:
        print(f"- {nome}")


main()

# Exemplos de comando:
# python main.py --entrada notas.csv --corte 7.0
# python main.py --corte 6.0
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CLI da Edutech Brasil para filtrar alunos aprovados em um CSV de notas."""

import argparse
import csv
from pathlib import Path

# Path torna as operacoes de arquivo mais expressivas que strings soltas
ARQUIVO_PADRAO = Path("notas.csv")
CSV_EXEMPLO = "nome,nota\nAna,8.5\nBruno,6.0\nCarla,9.0\n"


def garantir_csv_exemplo(caminho: Path) -> None:
    """Cria o CSV de exemplo apenas se ele ainda nao existir."""
    if caminho.exists():
        return
    # write_text cria e grava o arquivo em uma unica chamada
    caminho.write_text(CSV_EXEMPLO, encoding="utf-8")


def criar_parser() -> argparse.ArgumentParser:
    """Monta o parser com arquivo de entrada e nota de corte."""
    parser = argparse.ArgumentParser(
        prog="relatorio-notas",
        description="Relatorio de aprovados da Edutech Brasil",
    )
    # type=Path ja devolve um objeto Path pronto para uso
    parser.add_argument("--entrada", type=Path, default=ARQUIVO_PADRAO,
                        help="arquivo CSV com colunas nome,nota")
    parser.add_argument("--corte", type=float, default=7.0,
                        help="nota minima para aprovacao")
    return parser


def ler_alunos(caminho: Path) -> list[dict]:
    """Le o CSV e devolve lista de dicts com nota convertida para float."""
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        return [{"nome": linha["nome"], "nota": float(linha["nota"])} for linha in leitor]


def filtrar_aprovados(alunos: list[dict], corte: float) -> list[str]:
    """Retorna os nomes dos alunos com nota maior ou igual ao corte."""
    return [aluno["nome"] for aluno in alunos if aluno["nota"] >= corte]


def main() -> None:
    garantir_csv_exemplo(ARQUIVO_PADRAO)
    args = criar_parser().parse_args()

    # Guard clause: falha cedo com mensagem clara se o arquivo nao existe
    if not args.entrada.exists():
        raise SystemExit(f"Arquivo nao encontrado: {args.entrada}")

    aprovados = filtrar_aprovados(ler_alunos(args.entrada), args.corte)

    print(f"Aprovados (corte {args.corte}): {len(aprovados)}")
    print("\n".join(f"- {nome}" for nome in aprovados))


if __name__ == "__main__":
    main()

# Exemplos de comando:
# python main.py --entrada notas.csv --corte 7.0
# python main.py --corte 6.0
```

</details>
