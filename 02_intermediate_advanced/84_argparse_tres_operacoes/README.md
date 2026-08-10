# 84 - Argparse: ferramenta com 3 operacoes

## Objetivo

Integrar argparse com tres subcomandos em ferramenta unica.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | CLI interna para contar, filtrar e exportar linhas de arquivo texto. |

## Enunciado

Crie `dados.txt` com 5 linhas de exemplo no inicio do script.

Configure 3 subcomandos:

**`contar --arquivo`**
- Exibe total de linhas do arquivo

**`filtrar --arquivo --texto`**
- Exibe linhas que contem o texto informado

**`exportar --arquivo --saida`**
- Copia arquivo para destino com `with open`

Implemente cada operacao em funcao separada: `contar_linhas`, `filtrar_linhas`, `exportar_arquivo`.

No `main`, roteie com `if args.comando == "contar": ...`

Exemplo de execucao:

```bash
python main.py contar --arquivo dados.txt
python main.py filtrar --arquivo dados.txt --texto erro
python main.py exportar --arquivo dados.txt --saida copia.txt
```

## Passo a passo

1. Importe `argparse` e `os` no topo do arquivo.
2. Defina a funcao `criar_dados_exemplo(caminho)` que:
   - Retorna sem fazer nada se `os.path.exists(caminho)` for `True`.
   - Senao, grava 5 linhas de exemplo com `with open(caminho, "w", encoding="utf-8")` — inclua pelo menos duas linhas com a palavra `erro` para o subcomando `filtrar` ter o que encontrar.
3. Defina `contar_linhas(arquivo)` que:
   - Abre o arquivo com `with open`, le com `.readlines()` e retorna `len(linhas)`.
4. Defina `filtrar_linhas(arquivo, texto)` que:
   - Abre o arquivo e retorna uma lista com as linhas (sem `\n`, use `.strip()`) que contem o texto (`if texto in linha`).
5. Defina `exportar_arquivo(arquivo, saida)` que:
   - Abre a origem em modo leitura e o destino em modo escrita (pode usar dois `with open` aninhados ou na mesma linha separados por virgula) e copia o conteudo com `destino.write(origem.read())`.
6. Defina `criar_parser()` que:
   - Cria o parser e `subparsers = parser.add_subparsers(dest="comando")`.
   - Subcomando `contar`: argumento `--arquivo` (obrigatorio).
   - Subcomando `filtrar`: argumentos `--arquivo` e `--texto` (obrigatorios).
   - Subcomando `exportar`: argumentos `--arquivo` e `--saida` (obrigatorios).
7. Defina `main()` que:
   - Chama `criar_dados_exemplo("dados.txt")` e faz o parse dos argumentos.
   - Roteia com `if args.comando == "contar": ...`, `elif args.comando == "filtrar": ...`, `elif args.comando == "exportar": ...`.
   - `contar`: exibe `f"Total de linhas: {total}"`.
   - `filtrar`: exibe cada linha encontrada (ou aviso se nenhuma contem o texto).
   - `exportar`: exibe confirmacao `f"Arquivo copiado para {args.saida}"`.
8. Chame `main()` no final e teste os tres subcomandos.

## Como executar

```bash
cd "84_argparse_tres_operacoes"
python main.py contar --arquivo dados.txt
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import argparse
import os

ARQUIVO_DADOS = "dados.txt"

# Linhas de exemplo: duas contem "erro" para o subcomando filtrar
LINHAS_EXEMPLO = [
    "sistema iniciado",
    "erro de conexao",
    "backup concluido",
    "erro de disco",
    "processo finalizado",
]


def criar_dados_exemplo(caminho):
    # So cria o arquivo se ele ainda nao existir
    if os.path.exists(caminho):
        return
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for linha in LINHAS_EXEMPLO:
            arquivo.write(linha + "\n")


def contar_linhas(arquivo):
    # readlines devolve uma lista; len conta o total de linhas
    with open(arquivo, encoding="utf-8") as origem:
        return len(origem.readlines())


def filtrar_linhas(arquivo, texto):
    # Mantem apenas as linhas que contem o texto procurado
    with open(arquivo, encoding="utf-8") as origem:
        return [linha.strip() for linha in origem if texto in linha]


def exportar_arquivo(arquivo, saida):
    # Dois with open na mesma linha: leitura da origem e escrita do destino
    with open(arquivo, encoding="utf-8") as origem, open(saida, "w", encoding="utf-8") as destino:
        destino.write(origem.read())


def criar_parser():
    parser = argparse.ArgumentParser(description="CLI de arquivos da LimpezaDados")
    subparsers = parser.add_subparsers(dest="comando")

    # Cada subcomando declara apenas os argumentos de que precisa
    parser_contar = subparsers.add_parser("contar", help="conta linhas do arquivo")
    parser_contar.add_argument("--arquivo", required=True)

    parser_filtrar = subparsers.add_parser("filtrar", help="filtra linhas por texto")
    parser_filtrar.add_argument("--arquivo", required=True)
    parser_filtrar.add_argument("--texto", required=True)

    parser_exportar = subparsers.add_parser("exportar", help="copia arquivo para destino")
    parser_exportar.add_argument("--arquivo", required=True)
    parser_exportar.add_argument("--saida", required=True)

    return parser


def main():
    criar_dados_exemplo(ARQUIVO_DADOS)
    parser = criar_parser()
    args = parser.parse_args()

    # Roteia a execucao conforme o subcomando digitado
    if args.comando == "contar":
        print(f"Total de linhas: {contar_linhas(args.arquivo)}")
    elif args.comando == "filtrar":
        encontradas = filtrar_linhas(args.arquivo, args.texto)
        if encontradas:
            for linha in encontradas:
                print(linha)
        else:
            print(f"Nenhuma linha contem '{args.texto}'")
    elif args.comando == "exportar":
        exportar_arquivo(args.arquivo, args.saida)
        print(f"Arquivo copiado para {args.saida}")
    else:
        # Sem subcomando, orienta o usuario
        parser.print_help()


main()

# Exemplos de comando:
# python main.py contar --arquivo dados.txt
# python main.py filtrar --arquivo dados.txt --texto erro
# python main.py exportar --arquivo dados.txt --saida copia.txt
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CLI da LimpezaDados para contar, filtrar e exportar linhas de arquivo texto."""

import argparse
from pathlib import Path

ARQUIVO_DADOS = Path("dados.txt")

CONTEUDO_EXEMPLO = """sistema iniciado
erro de conexao
backup concluido
erro de disco
processo finalizado
"""


def garantir_dados_exemplo(caminho: Path) -> None:
    """Cria o arquivo de dados de exemplo apenas se ele nao existir."""
    if not caminho.exists():
        caminho.write_text(CONTEUDO_EXEMPLO, encoding="utf-8")


def contar_linhas(arquivo: Path) -> int:
    """Conta as linhas do arquivo."""
    # splitlines evita contar uma linha vazia extra no final
    return len(arquivo.read_text(encoding="utf-8").splitlines())


def filtrar_linhas(arquivo: Path, texto: str) -> list[str]:
    """Retorna as linhas do arquivo que contem o texto informado."""
    linhas = arquivo.read_text(encoding="utf-8").splitlines()
    return [linha for linha in linhas if texto in linha]


def exportar_arquivo(arquivo: Path, saida: Path) -> None:
    """Copia o conteudo do arquivo de origem para o destino."""
    saida.write_text(arquivo.read_text(encoding="utf-8"), encoding="utf-8")


def criar_parser() -> argparse.ArgumentParser:
    """Monta o parser com os subcomandos contar, filtrar e exportar."""
    parser = argparse.ArgumentParser(
        prog="limpeza-dados",
        description="CLI de arquivos da LimpezaDados",
    )
    # required=True exige que um subcomando seja informado
    subparsers = parser.add_subparsers(dest="comando", required=True)

    parser_contar = subparsers.add_parser("contar", help="conta linhas do arquivo")
    parser_contar.add_argument("--arquivo", type=Path, required=True)

    parser_filtrar = subparsers.add_parser("filtrar", help="filtra linhas por texto")
    parser_filtrar.add_argument("--arquivo", type=Path, required=True)
    parser_filtrar.add_argument("--texto", required=True)

    parser_exportar = subparsers.add_parser("exportar", help="copia arquivo para destino")
    parser_exportar.add_argument("--arquivo", type=Path, required=True)
    parser_exportar.add_argument("--saida", type=Path, required=True)

    return parser


def main() -> None:
    garantir_dados_exemplo(ARQUIVO_DADOS)
    args = criar_parser().parse_args()

    # Guard clause: valida a existencia do arquivo antes de qualquer operacao
    if not args.arquivo.exists():
        raise SystemExit(f"Arquivo nao encontrado: {args.arquivo}")

    # match/case deixa o roteamento dos subcomandos explicito e legivel
    match args.comando:
        case "contar":
            print(f"Total de linhas: {contar_linhas(args.arquivo)}")
        case "filtrar":
            encontradas = filtrar_linhas(args.arquivo, args.texto)
            saida = "\n".join(encontradas) if encontradas else f"Nenhuma linha contem '{args.texto}'"
            print(saida)
        case "exportar":
            exportar_arquivo(args.arquivo, args.saida)
            print(f"Arquivo copiado para {args.saida}")


if __name__ == "__main__":
    main()

# Exemplos de comando:
# python main.py contar --arquivo dados.txt
# python main.py filtrar --arquivo dados.txt --texto erro
# python main.py exportar --arquivo dados.txt --saida copia.txt
```

</details>
