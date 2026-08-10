# 81 - Argparse: flags booleanas

## Objetivo

Usar store_true para flags opcionais na CLI.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / deploy |
| **Solicitacao** | Script de deploy com modo verbose e simulacao dry-run. |

## Enunciado

Configure argparse com flags booleanas:

- `--verbose` (`action="store_true"`)
- `--dry-run` (`action="store_true"`)

No `main`, exiba mensagens conforme flags:

- Se `--verbose`: `"Modo detalhado ativo"`
- Se `--dry-run`: `"Simulacao — nenhuma alteracao aplicada"`
- Se nenhuma flag: `"Execucao padrao"`

Exemplo de execucao:

```bash
python main.py --verbose --dry-run
```

Exemplo de saida:

```
Modo detalhado ativo
Simulacao — nenhuma alteracao aplicada
```

## Passo a passo

1. Importe o modulo `argparse` no topo do arquivo.
2. Defina a funcao `criar_parser()` que:
   - Instancia `parser = argparse.ArgumentParser(description="Script de deploy da MonitoraTI")`.
   - Adiciona `parser.add_argument("--verbose", action="store_true")` — com `store_true`, a flag vira `True` quando digitada e `False` quando ausente.
   - Adiciona `parser.add_argument("--dry-run", action="store_true")` — o argparse troca o `-` por `_`, entao o valor fica em `args.dry_run`.
   - Retorna o `parser`.
3. Defina a funcao `main()` que:
   - Obtem os argumentos com `args = criar_parser().parse_args()`.
   - Usa um `if args.verbose:` para exibir `"Modo detalhado ativo"`.
   - Usa um `if args.dry_run:` (separado, nao `elif`, pois as flags podem vir juntas) para exibir `"Simulacao — nenhuma alteracao aplicada"`.
   - Se nenhuma das duas flags estiver ativa (`not args.verbose and not args.dry_run`), exibe `"Execucao padrao"`.
4. Chame `main()` no final do arquivo.
5. Teste no terminal as quatro combinacoes: sem flags, so `--verbose`, so `--dry-run` e as duas juntas.

## Como executar

```bash
cd "81_argparse_flags_booleanas"
python main.py --verbose --dry-run
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import argparse


def criar_parser():
    # Cria o parser, responsavel por interpretar o que foi digitado no terminal
    parser = argparse.ArgumentParser(description="Script de deploy da MonitoraTI")
    # store_true: a flag nao recebe valor; presente = True, ausente = False
    parser.add_argument("--verbose", action="store_true", help="exibe detalhes extras")
    # --dry-run vira args.dry_run (argparse converte '-' em '_' no nome do atributo)
    parser.add_argument("--dry-run", action="store_true", help="simula sem aplicar mudancas")
    return parser


def main():
    # parse_args le os argumentos da linha de comando e devolve um objeto simples
    args = criar_parser().parse_args()

    # Dois ifs independentes: as flags podem estar ativas ao mesmo tempo
    if args.verbose:
        print("Modo detalhado ativo")
    if args.dry_run:
        print("Simulacao — nenhuma alteracao aplicada")

    # Sem nenhuma flag ativa, o deploy roda no modo padrao
    if not args.verbose and not args.dry_run:
        print("Execucao padrao")


main()

# Exemplos de comando:
# python main.py
# python main.py --verbose
# python main.py --dry-run
# python main.py --verbose --dry-run
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CLI de deploy da MonitoraTI com modos verbose e dry-run."""

import argparse


def criar_parser() -> argparse.ArgumentParser:
    """Monta o parser da CLI com as flags booleanas de deploy."""
    parser = argparse.ArgumentParser(
        prog="deploy",
        description="Script de deploy da MonitoraTI",
    )
    # store_true ja define default=False, dispensando valor apos a flag
    parser.add_argument("--verbose", action="store_true", help="exibe detalhes extras")
    parser.add_argument("--dry-run", action="store_true", help="simula sem aplicar mudancas")
    return parser


def main() -> None:
    """Interpreta as flags e exibe o modo de execucao correspondente."""
    args = criar_parser().parse_args()

    # Acumula as mensagens ativas para decidir o modo em um unico lugar
    mensagens: list[str] = []
    if args.verbose:
        mensagens.append("Modo detalhado ativo")
    if args.dry_run:
        mensagens.append("Simulacao — nenhuma alteracao aplicada")

    # Lista vazia significa que nenhuma flag foi usada: modo padrao
    if not mensagens:
        mensagens.append("Execucao padrao")

    # Uma unica chamada de print evita saidas espalhadas pelo codigo
    print("\n".join(mensagens))


# Protege a execucao: so roda a CLI quando o arquivo e chamado diretamente
if __name__ == "__main__":
    main()

# Exemplos de comando:
# python main.py --verbose --dry-run
# python main.py --dry-run
```

</details>
