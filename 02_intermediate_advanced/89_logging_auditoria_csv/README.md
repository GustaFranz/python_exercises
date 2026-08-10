# 89 - Logging: auditoria de importacao CSV

## Objetivo

Auditar importacao CSV com log estruturado de sucesso e rejeicao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Auditar importacao de funcionarios com registro de linhas rejeitadas. |

## Enunciado

Crie `funcionarios.csv` com o conteudo:

```
nome,cargo
Ana,Analista
,Suporte
Bruno,Coordenador
```

Implemente `importar_funcionarios(caminho) -> list[dict]`:

- Linha valida (nome nao vazio): `logging.info(f"Importado: {nome}")` e inclui na lista
- Linha invalida: `logging.error(f"Rejeitado linha: {linha}")` e nao inclui

Exiba ao final:

- Total importado (esperado: **2**)
- Total rejeitado (esperado: **1**)

## Passo a passo

1. Importe `logging`, `csv` e `os`.
2. Configure o logging com `logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")`.
3. Defina `criar_csv_exemplo(caminho)` que:
   - Retorna sem fazer nada se o arquivo ja existe (`os.path.exists`).
   - Senao, grava com `with open(caminho, "w", newline="", encoding="utf-8")` o cabecalho `nome,cargo` e as 3 linhas do enunciado — repare que a segunda linha tem o nome vazio (`,Suporte`).
4. Defina `importar_funcionarios(caminho)` que:
   - Abre o arquivo com `with open(caminho, encoding="utf-8")` e le com `csv.DictReader` — cada linha vira um dict `{"nome": ..., "cargo": ...}`.
   - Cria uma lista vazia `importados`.
   - Para cada linha: se `linha["nome"].strip()` nao for vazio, chama `logging.info(f"Importado: {linha['nome']}")` e adiciona o dict a lista; senao, chama `logging.error(f"Rejeitado linha: {linha}")`.
   - Retorna a lista `importados`.
5. No fluxo principal:
   - Chame `criar_csv_exemplo("funcionarios.csv")`.
   - Chame `importar_funcionarios("funcionarios.csv")` guardando o retorno.
   - Para calcular os rejeitados, conte o total de linhas do CSV (fora o cabecalho) e subtraia os importados — ou faca a funcao contar os dois totais.
   - Exiba `Total importado: 2` e `Total rejeitado: 1`.

## Como executar

```bash
cd "89_logging_auditoria_csv"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ARQUIVO_CSV = "funcionarios.csv"


def criar_csv_exemplo(caminho):
    # Nao sobrescreve um arquivo existente
    if os.path.exists(caminho):
        return
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome", "cargo"])
        escritor.writerow(["Ana", "Analista"])
        # Linha proposital com nome vazio para testar a rejeicao
        escritor.writerow(["", "Suporte"])
        escritor.writerow(["Bruno", "Coordenador"])


def importar_funcionarios(caminho):
    importados = []
    rejeitados = 0
    with open(caminho, encoding="utf-8") as arquivo:
        # DictReader usa o cabecalho como chaves de cada linha
        for linha in csv.DictReader(arquivo):
            # strip() garante que "   " tambem conte como vazio
            if linha["nome"].strip():
                logging.info(f"Importado: {linha['nome']}")
                importados.append(linha)
            else:
                # ERROR deixa rastro de auditoria da linha rejeitada
                logging.error(f"Rejeitado linha: {linha}")
                rejeitados += 1
    # Retorna a lista valida e o total rejeitado para o relatorio final
    return importados, rejeitados


criar_csv_exemplo(ARQUIVO_CSV)
funcionarios, rejeitados = importar_funcionarios(ARQUIVO_CSV)

print(f"Total importado: {len(funcionarios)}")
print(f"Total rejeitado: {rejeitados}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Auditoria de importacao de funcionarios da GestaoPro RH."""

import csv
import logging
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

ARQUIVO_CSV = Path("funcionarios.csv")
CSV_EXEMPLO = "nome,cargo\nAna,Analista\n,Suporte\nBruno,Coordenador\n"


@dataclass
class ResultadoImportacao:
    """Consolida o resultado da importacao para o relatorio final."""

    importados: list[dict] = field(default_factory=list)
    rejeitados: int = 0


def garantir_csv_exemplo(caminho: Path) -> None:
    """Cria o CSV de exemplo apenas se ele nao existir."""
    if not caminho.exists():
        caminho.write_text(CSV_EXEMPLO, encoding="utf-8")


def importar_funcionarios(caminho: Path) -> ResultadoImportacao:
    """Importa funcionarios do CSV, logando cada linha aceita ou rejeitada."""
    resultado = ResultadoImportacao()
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            # Guard clause: rejeita cedo a linha sem nome
            if not linha["nome"].strip():
                logger.error("Rejeitado linha: %s", linha)
                resultado.rejeitados += 1
                continue
            logger.info("Importado: %s", linha["nome"])
            resultado.importados.append(linha)
    return resultado


def main() -> None:
    garantir_csv_exemplo(ARQUIVO_CSV)
    resultado = importar_funcionarios(ARQUIVO_CSV)

    print(f"Total importado: {len(resultado.importados)}")
    print(f"Total rejeitado: {resultado.rejeitados}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
```

</details>
