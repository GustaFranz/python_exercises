# 87 - Logging: gravar em arquivo

## Objetivo

Configurar logging para gravar em arquivo de texto.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / operacoes |
| **Solicitacao** | Manter historico de entregas concluidas em arquivo de log. |

## Enunciado

1) Configure logging para gravar em `entregas.log` e exibir no console.

2) Implemente:
```python
def registrar_entrega(codigo: str, status: str) -> None:
    logging.info(f"Entrega {codigo}: {status}")
```

3) Registre 3 entregas (ex.: `"E001"/"Entregue"`, `"E002"/"Em transito"`, `"E003"/"Entregue"`).

4) Ao final, leia `entregas.log` com `with open` e exiba o conteudo.

Exemplo de saida final:

```
--- Conteudo de entregas.log ---
2026-08-09 19:00:00 Entrega E001: Entregue
2026-08-09 19:00:00 Entrega E002: Em transito
2026-08-09 19:00:00 Entrega E003: Entregue
```

## Passo a passo

1. Importe o modulo `logging`.
2. Configure o logging para gravar em arquivo **e** exibir no console usando o parametro `handlers` do `basicConfig`:
   - `logging.FileHandler("entregas.log", encoding="utf-8")` grava cada mensagem no arquivo.
   - `logging.StreamHandler()` exibe a mesma mensagem no console.
   - Use `level=logging.INFO` e `format="%(asctime)s %(message)s"`.
3. Defina a funcao `registrar_entrega(codigo, status)` que chama `logging.info(f"Entrega {codigo}: {status}")`.
4. Crie uma lista de entregas com as tuplas `("E001", "Entregue")`, `("E002", "Em transito")` e `("E003", "Entregue")` e percorra com `for` chamando `registrar_entrega`.
5. Defina a funcao `exibir_log(caminho)` que:
   - Abre `entregas.log` com `with open(caminho, encoding="utf-8")`.
   - Imprime o cabecalho `--- Conteudo de entregas.log ---` e depois o conteudo do arquivo.
6. Chame `exibir_log("entregas.log")` no final e confira que as 3 linhas foram gravadas.

## Como executar

```bash
cd "87_logging_arquivo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import logging

ARQUIVO_LOG = "entregas.log"

# handlers permite dois destinos ao mesmo tempo:
# FileHandler grava no arquivo e StreamHandler exibe no console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    handlers=[
        logging.FileHandler(ARQUIVO_LOG, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def registrar_entrega(codigo, status):
    # A mesma mensagem vai para o arquivo e para o console
    logging.info(f"Entrega {codigo}: {status}")


def exibir_log(caminho):
    # Reabre o arquivo de log para conferir o que foi gravado
    with open(caminho, encoding="utf-8") as arquivo:
        print(f"--- Conteudo de {caminho} ---")
        print(arquivo.read())


# Registra as 3 entregas do dia
entregas = [("E001", "Entregue"), ("E002", "Em transito"), ("E003", "Entregue")]
for codigo, status in entregas:
    registrar_entrega(codigo, status)

# Confirma que o historico ficou salvo no arquivo
exibir_log(ARQUIVO_LOG)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Historico de entregas da LogiRapida gravado em arquivo de log."""

import logging
from pathlib import Path

ARQUIVO_LOG = Path("entregas.log")

logger = logging.getLogger(__name__)


def configurar_logging(arquivo: Path) -> None:
    """Configura log simultaneo em arquivo e console."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        # Dois handlers: persistencia em arquivo + feedback imediato no console
        handlers=[
            logging.FileHandler(arquivo, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def registrar_entrega(codigo: str, status: str) -> None:
    """Registra uma entrega no historico de log."""
    # Formatacao adiada (%s): o logging monta a string apenas se necessario
    logger.info("Entrega %s: %s", codigo, status)


def exibir_log(arquivo: Path) -> None:
    """Exibe o conteudo atual do arquivo de log."""
    print(f"--- Conteudo de {arquivo} ---")
    print(arquivo.read_text(encoding="utf-8"))


def main() -> None:
    entregas = [("E001", "Entregue"), ("E002", "Em transito"), ("E003", "Entregue")]
    for codigo, status in entregas:
        registrar_entrega(codigo, status)

    exibir_log(ARQUIVO_LOG)


if __name__ == "__main__":
    configurar_logging(ARQUIVO_LOG)
    main()
```

</details>
