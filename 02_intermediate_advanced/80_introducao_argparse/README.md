# 80 - Introducao ao argparse

## Objetivo

Criar CLI com argumentos --arquivo e --limite.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Script de linha de comando para processar exportacao de notas com parametros. |

## Visao do bloco (exercicios 80 a 84)

Topico **argparse**: interfaces de linha de comando profissionais.

| # | Foco |
|---|------|
| 80 | Introducao + --arquivo e --limite |
| 81 | Flags booleanas |
| 82 | Subcomando simples |
| 83 | CLI relatorio de notas |
| 84 | Ferramenta com 3 operacoes |

## Enunciado

Configure argparse com:

- `--arquivo` (str, obrigatorio): caminho do arquivo de entrada
- `--limite` (int, padrao `10`): maximo de linhas a processar

No `main`:

1) Parse os argumentos.
2) Exiba os valores recebidos.

Exemplo de execucao:

```bash
python main.py --arquivo notas.csv --limite 5
```

Exemplo de saida:

```
Arquivo: notas.csv
Limite: 5
```

## Passo a passo

1. Importe o modulo `argparse` no topo do arquivo.
2. Crie o parser: `parser = argparse.ArgumentParser(description="Processa exportacao de notas")` — a descricao aparece no `--help`.
3. Registre o argumento obrigatorio: `parser.add_argument("--arquivo", required=True, help="caminho do arquivo de entrada")` (sem `type`, o valor chega como `str`).
4. Registre o argumento opcional com padrao: `parser.add_argument("--limite", type=int, default=10, help="maximo de linhas a processar")` — `type=int` converte automaticamente e rejeita valores nao numericos.
5. Faca o parse: `args = parser.parse_args()` — os valores ficam acessiveis como atributos (`args.arquivo`, `args.limite`).
6. Exiba as duas linhas: `Arquivo: {args.arquivo}` e `Limite: {args.limite}`.
7. Teste no terminal: `python main.py --arquivo notas.csv --limite 5`, depois experimente sem `--limite` (deve usar 10) e sem `--arquivo` (deve dar erro com mensagem automatica do argparse).

## Como executar

```bash
cd "80_introducao_argparse"
python main.py --arquivo notas.csv --limite 5
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import argparse

# Cria o parser; a descricao aparece quando o usuario roda --help
parser = argparse.ArgumentParser(description="Processa exportacao de notas")

# Argumento obrigatorio: sem --arquivo o argparse encerra com erro claro
parser.add_argument("--arquivo", required=True, help="caminho do arquivo de entrada")

# Argumento opcional: type=int converte o texto para inteiro
# e default=10 e usado quando --limite nao e informado
parser.add_argument("--limite", type=int, default=10, help="maximo de linhas a processar")

# Le e valida os argumentos da linha de comando
args = parser.parse_args()

# Os valores ficam disponiveis como atributos do objeto args
print(f"Arquivo: {args.arquivo}")
print(f"Limite: {args.limite}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CLI para processar exportacao de notas.

Estrutura padrao de mercado para CLIs: uma funcao que monta o parser
(testavel isoladamente), um main que orquestra e o guard de execucao.
"""

import argparse

# Valor padrao centralizado: documentado e facil de alterar
LIMITE_PADRAO = 10


def criar_parser() -> argparse.ArgumentParser:
    """Monta e retorna o parser da CLI (separado para facilitar testes)."""
    parser = argparse.ArgumentParser(
        description="Processa exportacao de notas com parametros.",
    )
    parser.add_argument(
        "--arquivo",
        required=True,
        help="caminho do arquivo de entrada",
    )
    parser.add_argument(
        "--limite",
        type=int,
        default=LIMITE_PADRAO,
        help=f"maximo de linhas a processar (padrao: {LIMITE_PADRAO})",
    )
    return parser


def main() -> None:
    # parse_args() valida a entrada e ja gera --help e mensagens de erro
    args = criar_parser().parse_args()

    print(f"Arquivo: {args.arquivo}")
    print(f"Limite: {args.limite}")


if __name__ == "__main__":
    main()
```

</details>
