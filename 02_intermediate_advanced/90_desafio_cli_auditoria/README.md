# 90 - DESAFIO - CLI de auditoria operacional

## Objetivo

Montar CLI pequena com multi-modulo, argparse e logging.

## Conteudos cobertos

- Projeto multi-modulo
- `argparse` (subcomandos ou flags)
- `logging` (INFO / ERROR em arquivo)
- Funcoes de auditoria simples

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | OpsBoard Tecnologia |
| **Setor** | Operacoes / SRE junior |
| **Solicitacao** | Ferramenta CLI para auditar lotes de registros e gerar log operacional. |

## Estrutura sugerida

```
90_desafio_cli_auditoria/
├── main.py
├── auditoria.py
└── README.md
```

## Enunciado

Registros embutidos (ou JSON local):
```python
registros = [
    {"id": 1, "status": "ok", "valor": 100},
    {"id": 2, "status": "erro", "valor": -10},
    {"id": 3, "status": "ok", "valor": 50},
    {"id": 4, "status": "erro", "valor": 0},
]
```

Checklist:

1) Em `auditoria.py`:
   - `contar_por_status(registros) -> dict`
   - `listar_erros(registros) -> list`
   - `resumo(registros) -> dict` com total, ok, erro, taxa_erro_%
2) Em `main.py`, configure `logging` para arquivo `ops.log` (e console opcional).
3) Use `argparse` com subcomandos ou `--acao`:
   - `resumo` -> imprime resumo e loga INFO
   - `erros` -> lista erros; se houver erro, loga ERROR
   - `exportar` -> grava `erros.json` com a lista de erros
4) Se acao invalida, mensagem amigavel + log ERROR.
5) Demonstre ao menos duas acoes no fluxo principal (ou documente comandos no README).

Exemplos:
```bash
python main.py --acao resumo
python main.py --acao erros
python main.py --acao exportar
```

## Passo a passo

**Em `auditoria.py` (regras de auditoria, sem CLI nem logging):**

1. Defina `contar_por_status(registros)` que:
   - Cria um dict vazio e percorre os registros somando 1 na chave do `status` de cada um (use `contagem.get(status, 0) + 1`).
   - Retorna algo como `{"ok": 2, "erro": 2}`.
2. Defina `listar_erros(registros)` que retorna, com list comprehension, os registros com `status == "erro"`.
3. Defina `resumo(registros)` que:
   - Calcula `total = len(registros)`, `ok` e `erro` a partir de `contar_por_status`.
   - Calcula `taxa_erro_% = round(erro / total * 100, 1)` quando `total > 0` (senao `0.0`).
   - Retorna `{"total": ..., "ok": ..., "erro": ..., "taxa_erro_%": ...}`.

**Em `main.py` (CLI, logging e orquestracao):**

4. Importe `argparse`, `json`, `logging` e as funcoes de `auditoria` (`from auditoria import listar_erros, resumo`).
5. Configure `logging.basicConfig(filename="ops.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")`.
6. Defina a lista `REGISTROS` com os 4 dicts do enunciado.
7. Defina `criar_parser()` com o argumento `--acao` usando `choices=["resumo", "erros", "exportar"]` e `required=True` — o proprio argparse rejeita acoes invalidas com mensagem amigavel e o `choices` documenta as opcoes no `--help`.
8. Defina uma funcao para cada acao:
   - `executar_resumo(registros)`: imprime o dict de `resumo()` linha a linha e loga `logging.info("Resumo gerado")`.
   - `executar_erros(registros)`: imprime os registros de `listar_erros()`; se a lista nao estiver vazia, loga `logging.error(f"{qtd} registros com erro")`.
   - `executar_exportar(registros)`: grava a lista de erros em `erros.json` com `json.dump(..., indent=2)` dentro de `with open` e loga INFO.
9. No `main()`, roteie com `if/elif` sobre `args.acao` chamando a funcao correspondente.
10. Teste as tres acoes no terminal e confira o conteudo de `ops.log` e `erros.json`.

## Como executar

```bash
cd "90_desafio_cli_auditoria"
python main.py --acao resumo
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`auditoria.py`**

```python
# Modulo de regras de auditoria: sem CLI, sem logging — so logica de negocio


def contar_por_status(registros):
    # Conta quantos registros existem em cada status
    contagem = {}
    for registro in registros:
        status = registro["status"]
        # get(status, 0) devolve 0 na primeira ocorrencia do status
        contagem[status] = contagem.get(status, 0) + 1
    return contagem


def listar_erros(registros):
    # Filtra apenas os registros com falha
    return [registro for registro in registros if registro["status"] == "erro"]


def resumo(registros):
    total = len(registros)
    contagem = contar_por_status(registros)
    erros = contagem.get("erro", 0)
    # Protege contra divisao por zero quando a lista esta vazia
    taxa = round(erros / total * 100, 1) if total > 0 else 0.0
    return {
        "total": total,
        "ok": contagem.get("ok", 0),
        "erro": erros,
        "taxa_erro_%": taxa,
    }
```

**`main.py`**

```python
import argparse
import json
import logging

# Importa as regras de negocio do modulo de auditoria
from auditoria import listar_erros, resumo

# Log operacional gravado em arquivo, como pede a demanda
logging.basicConfig(
    filename="ops.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

# Lote de registros a auditar
REGISTROS = [
    {"id": 1, "status": "ok", "valor": 100},
    {"id": 2, "status": "erro", "valor": -10},
    {"id": 3, "status": "ok", "valor": 50},
    {"id": 4, "status": "erro", "valor": 0},
]


def criar_parser():
    parser = argparse.ArgumentParser(description="CLI de auditoria da OpsBoard")
    # choices: o argparse rejeita sozinho qualquer acao fora da lista
    parser.add_argument("--acao", choices=["resumo", "erros", "exportar"], required=True)
    return parser


def executar_resumo(registros):
    dados = resumo(registros)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    logging.info(f"Resumo gerado: {dados}")


def executar_erros(registros):
    erros = listar_erros(registros)
    for registro in erros:
        print(registro)
    if erros:
        # Presenca de erros no lote merece nivel ERROR no log
        logging.error(f"{len(erros)} registros com erro no lote")


def executar_exportar(registros):
    erros = listar_erros(registros)
    # indent=2 deixa o JSON legivel para conferencia manual
    with open("erros.json", "w", encoding="utf-8") as arquivo:
        json.dump(erros, arquivo, indent=2, ensure_ascii=False)
    print(f"{len(erros)} erros exportados para erros.json")
    logging.info(f"Exportados {len(erros)} erros para erros.json")


def main():
    args = criar_parser().parse_args()

    # Roteia a acao escolhida para a funcao correspondente
    if args.acao == "resumo":
        executar_resumo(REGISTROS)
    elif args.acao == "erros":
        executar_erros(REGISTROS)
    elif args.acao == "exportar":
        executar_exportar(REGISTROS)


main()

# Exemplos de comando:
# python main.py --acao resumo
# python main.py --acao erros
# python main.py --acao exportar
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`auditoria.py`**

```python
"""Regras de auditoria operacional da OpsBoard (logica pura, sem CLI)."""

from collections import Counter

Registro = dict


def contar_por_status(registros: list[Registro]) -> dict[str, int]:
    """Conta registros por status usando Counter."""
    # Counter faz a contagem em uma linha; dict() converte para dict comum
    return dict(Counter(registro["status"] for registro in registros))


def listar_erros(registros: list[Registro]) -> list[Registro]:
    """Retorna apenas os registros com status de erro."""
    return [registro for registro in registros if registro["status"] == "erro"]


def resumo(registros: list[Registro]) -> dict:
    """Consolida total, contagens e taxa de erro do lote."""
    total = len(registros)
    contagem = contar_por_status(registros)
    erros = contagem.get("erro", 0)
    return {
        "total": total,
        "ok": contagem.get("ok", 0),
        "erro": erros,
        # Divisao protegida: lote vazio resulta em taxa 0.0
        "taxa_erro_%": round(erros / total * 100, 1) if total else 0.0,
    }
```

**`main.py`**

```python
"""CLI de auditoria operacional da OpsBoard Tecnologia."""

import argparse
import json
import logging
from pathlib import Path

from auditoria import listar_erros, resumo

logger = logging.getLogger(__name__)

ARQUIVO_LOG = Path("ops.log")
ARQUIVO_ERROS = Path("erros.json")

REGISTROS = [
    {"id": 1, "status": "ok", "valor": 100},
    {"id": 2, "status": "erro", "valor": -10},
    {"id": 3, "status": "ok", "valor": 50},
    {"id": 4, "status": "erro", "valor": 0},
]


def configurar_logging() -> None:
    """Grava o log operacional em arquivo e espelha no console."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(ARQUIVO_LOG, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def criar_parser() -> argparse.ArgumentParser:
    """Monta o parser da CLI com as acoes disponiveis."""
    parser = argparse.ArgumentParser(
        prog="auditoria",
        description="CLI de auditoria da OpsBoard",
    )
    parser.add_argument(
        "--acao",
        choices=["resumo", "erros", "exportar"],
        required=True,
        help="acao a executar sobre o lote de registros",
    )
    return parser


def executar_resumo(registros: list[dict]) -> None:
    """Imprime o resumo do lote e registra INFO no log."""
    dados = resumo(registros)
    print("\n".join(f"{chave}: {valor}" for chave, valor in dados.items()))
    logger.info("Resumo gerado: %s", dados)


def executar_erros(registros: list[dict]) -> None:
    """Lista os registros com erro; loga ERROR quando existirem."""
    erros = listar_erros(registros)
    if not erros:
        print("Nenhum registro com erro")
        return
    print("\n".join(str(registro) for registro in erros))
    logger.error("%d registros com erro no lote", len(erros))


def executar_exportar(registros: list[dict]) -> None:
    """Exporta os registros com erro para erros.json."""
    erros = listar_erros(registros)
    ARQUIVO_ERROS.write_text(
        json.dumps(erros, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"{len(erros)} erros exportados para {ARQUIVO_ERROS}")
    logger.info("Exportados %d erros para %s", len(erros), ARQUIVO_ERROS)


# Mapeia cada acao para sua funcao: evita cadeia de if/elif no main
ACOES = {
    "resumo": executar_resumo,
    "erros": executar_erros,
    "exportar": executar_exportar,
}


def main() -> None:
    args = criar_parser().parse_args()
    # O dict de acoes despacha direto para a funcao certa
    ACOES[args.acao](REGISTROS)


if __name__ == "__main__":
    configurar_logging()
    main()

# Exemplos de comando:
# python main.py --acao resumo
# python main.py --acao erros
# python main.py --acao exportar
```

</details>
