# 82 - Argparse: subcomando simples

## Objetivo

Criar subcomandos listar e exportar na mesma CLI.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Ferramenta unica para listar ou exportar alunos por turma. |

## Enunciado

Configure subcomandos com `subparsers = parser.add_subparsers(dest="comando")`:

**Subcomando `listar`**
- `--turma` (str, obrigatorio)
- Exibe: `"Listando alunos da turma {turma}"`

**Subcomando `exportar`**
- `--turma` (str, obrigatorio)
- `--arquivo` (str, obrigatorio)
- Exibe: `"Exportando turma {turma} para {arquivo}"`

Exemplos de execucao:

```bash
python main.py listar --turma 7B
python main.py exportar --turma 8A --arquivo saida.csv
```

## Passo a passo

1. Importe o modulo `argparse`.
2. Defina a funcao `criar_parser()` que:
   - Instancia `parser = argparse.ArgumentParser(description="Ferramenta de turmas da Secretaria Digital")`.
   - Cria os subparsers com `subparsers = parser.add_subparsers(dest="comando")` — o nome do subcomando digitado ficara em `args.comando`.
   - Cria o subcomando listar: `parser_listar = subparsers.add_parser("listar")` e adiciona `parser_listar.add_argument("--turma", required=True)`.
   - Cria o subcomando exportar: `parser_exportar = subparsers.add_parser("exportar")` e adiciona `--turma` e `--arquivo`, ambos com `required=True`.
   - Retorna o `parser`.
3. Defina a funcao `main()` que:
   - Obtem os argumentos com `args = criar_parser().parse_args()`.
   - Se `args.comando == "listar"`, exibe `f"Listando alunos da turma {args.turma}"`.
   - Se `args.comando == "exportar"`, exibe `f"Exportando turma {args.turma} para {args.arquivo}"`.
   - Se nenhum subcomando foi informado (`args.comando` e `None`), exiba a ajuda com `parser.print_help()` ou uma mensagem orientando o uso.
4. Chame `main()` no final do arquivo.
5. Teste os dois subcomandos no terminal conforme os exemplos do enunciado.

## Como executar

```bash
cd "82_argparse_subcomando"
python main.py listar --turma 7B
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import argparse


def criar_parser():
    # Parser principal da ferramenta
    parser = argparse.ArgumentParser(description="Ferramenta de turmas da Secretaria Digital")
    # dest="comando" guarda em args.comando qual subcomando foi digitado
    subparsers = parser.add_subparsers(dest="comando")

    # Subcomando "listar": cada subparser tem seus proprios argumentos
    parser_listar = subparsers.add_parser("listar", help="lista alunos de uma turma")
    # required=True obriga o usuario a informar --turma
    parser_listar.add_argument("--turma", required=True, help="codigo da turma")

    # Subcomando "exportar": exige turma e arquivo de destino
    parser_exportar = subparsers.add_parser("exportar", help="exporta alunos para arquivo")
    parser_exportar.add_argument("--turma", required=True, help="codigo da turma")
    parser_exportar.add_argument("--arquivo", required=True, help="arquivo de saida")

    return parser


def main():
    parser = criar_parser()
    # parse_args identifica o subcomando e valida os argumentos dele
    args = parser.parse_args()

    # Roteia a execucao conforme o subcomando escolhido
    if args.comando == "listar":
        print(f"Listando alunos da turma {args.turma}")
    elif args.comando == "exportar":
        print(f"Exportando turma {args.turma} para {args.arquivo}")
    else:
        # Sem subcomando, mostra a ajuda para orientar o usuario
        parser.print_help()


main()

# Exemplos de comando:
# python main.py listar --turma 7B
# python main.py exportar --turma 8A --arquivo saida.csv
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CLI da Secretaria Digital para listar e exportar alunos por turma."""

import argparse


def listar_turma(turma: str) -> None:
    """Exibe a acao de listagem de alunos da turma informada."""
    print(f"Listando alunos da turma {turma}")


def exportar_turma(turma: str, arquivo: str) -> None:
    """Exibe a acao de exportacao da turma para o arquivo de destino."""
    print(f"Exportando turma {turma} para {arquivo}")


def criar_parser() -> argparse.ArgumentParser:
    """Monta o parser com os subcomandos listar e exportar."""
    parser = argparse.ArgumentParser(
        prog="turmas",
        description="Ferramenta de turmas da Secretaria Digital",
    )
    # required=True (do add_subparsers) ja rejeita chamadas sem subcomando
    subparsers = parser.add_subparsers(dest="comando", required=True)

    parser_listar = subparsers.add_parser("listar", help="lista alunos de uma turma")
    parser_listar.add_argument("--turma", required=True, help="codigo da turma")
    # set_defaults associa a funcao ao subcomando; o main nao precisa de if/elif
    parser_listar.set_defaults(executar=lambda args: listar_turma(args.turma))

    parser_exportar = subparsers.add_parser("exportar", help="exporta alunos para arquivo")
    parser_exportar.add_argument("--turma", required=True, help="codigo da turma")
    parser_exportar.add_argument("--arquivo", required=True, help="arquivo de saida")
    parser_exportar.set_defaults(
        executar=lambda args: exportar_turma(args.turma, args.arquivo)
    )

    return parser


def main() -> None:
    args = criar_parser().parse_args()
    # Cada subcomando ja carrega sua funcao; basta executa-la
    args.executar(args)


if __name__ == "__main__":
    main()

# Exemplos de comando:
# python main.py listar --turma 7B
# python main.py exportar --turma 8A --arquivo saida.csv
```

</details>
