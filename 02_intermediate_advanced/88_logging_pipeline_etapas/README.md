# 88 - Logging: pipeline ETL por etapas

## Objetivo

Montar um mini pipeline ETL com logging em cada etapa e niveis corretos para falhas de dados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | Rastrear importacao de vendas escolares com alertas quando a base chega vazia ou invalida. |

## Enunciado

Dados brutos (simulando CSV importado):

```python
vendas_brutas = [
    {"produto": "Caderno", "valor": 12.50},
    {"produto": "", "valor": 0},
    {"produto": "Caneta", "valor": 3.00},
    {"produto": "   ", "valor": 5.00},
    {"produto": "Lapis", "valor": -1},
    {"produto": "Borracha", "valor": 2.00},
]
```

Regra de invalidacao: produto vazio/whitespace **ou** valor <= 0.

Implemente pipeline ETL com logging (`logging.basicConfig`, nivel INFO):

1) `carregar_vendas(fonte)` — log `"Etapa 1: carregar"`, retorna lista bruta
2) `limpar_vendas(vendas)` — log `"Etapa 2: limpar"`, remove invalidos; cada descarte gera `logging.warning` com motivo
3) `agregar_vendas(vendas)` — log `"Etapa 3: agregar"`, retorna `{"qtd": int, "total": float}`; se qtd == 0, `logging.error`
4) `executar_pipeline(fonte)` — orquestra as 3 etapas

Exiba resumo final: quantidade valida e valor total agregado.

## Passo a passo

1. Importe `logging` e configure com `logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")`.
2. Defina a constante `VENDAS_BRUTAS` no topo com a lista de dicts do enunciado.
3. Defina `carregar_vendas(fonte)` que:
   - Registra `logging.info("Etapa 1: carregar")`.
   - Retorna a lista recebida em `fonte` (simula a leitura de um CSV).
4. Defina `registro_valido(venda)` (funcao auxiliar) que retorna `True` quando `venda["produto"].strip()` nao e vazio **e** `venda["valor"] > 0`.
5. Defina `limpar_vendas(vendas)` que:
   - Registra `logging.info("Etapa 2: limpar")`.
   - Percorre a lista; para cada registro invalido, chama `logging.warning` informando o motivo (produto vazio ou valor invalido) e o registro descartado.
   - Retorna somente os registros validos.
6. Defina `agregar_vendas(vendas)` que:
   - Registra `logging.info("Etapa 3: agregar")`.
   - Calcula `qtd = len(vendas)` e `total = sum(v["valor"] for v in vendas)`.
   - Se `qtd == 0`, registra `logging.error("Nenhum registro valido para agregar")`.
   - Retorna `{"qtd": qtd, "total": total}`.
7. Defina `executar_pipeline(fonte)` que chama as 3 funcoes em sequencia (carregar → limpar → agregar) e retorna o dict da agregacao.
8. No fluxo principal, chame `executar_pipeline(VENDAS_BRUTAS)` e exiba o resumo: quantidade valida e valor total (esperado: 3 registros validos, total 17.50).

## Como executar

```bash
cd "88_logging_pipeline_etapas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Dados brutos simulando um CSV importado com registros problematicos
VENDAS_BRUTAS = [
    {"produto": "Caderno", "valor": 12.50},
    {"produto": "", "valor": 0},
    {"produto": "Caneta", "valor": 3.00},
    {"produto": "   ", "valor": 5.00},
    {"produto": "Lapis", "valor": -1},
    {"produto": "Borracha", "valor": 2.00},
]


def carregar_vendas(fonte):
    # Etapa 1: em um caso real, aqui leriamos o CSV do disco
    logging.info("Etapa 1: carregar")
    return fonte


def registro_valido(venda):
    # strip() remove espacos: "   " vira "" e e considerado vazio
    produto_ok = venda["produto"].strip() != ""
    valor_ok = venda["valor"] > 0
    return produto_ok and valor_ok


def limpar_vendas(vendas):
    logging.info("Etapa 2: limpar")
    validas = []
    for venda in vendas:
        if registro_valido(venda):
            validas.append(venda)
        else:
            # WARNING: dado descartado nao para o pipeline, mas precisa ser rastreado
            if venda["produto"].strip() == "":
                logging.warning(f"Descartado (produto vazio): {venda}")
            else:
                logging.warning(f"Descartado (valor invalido): {venda}")
    return validas


def agregar_vendas(vendas):
    logging.info("Etapa 3: agregar")
    qtd = len(vendas)
    # Generator expression soma apenas os valores dos registros validos
    total = sum(venda["valor"] for venda in vendas)
    if qtd == 0:
        # ERROR: base vazia apos limpeza indica problema serio na origem
        logging.error("Nenhum registro valido para agregar")
    return {"qtd": qtd, "total": total}


def executar_pipeline(fonte):
    # Orquestra as 3 etapas na ordem: carregar -> limpar -> agregar
    brutas = carregar_vendas(fonte)
    limpas = limpar_vendas(brutas)
    return agregar_vendas(limpas)


resultado = executar_pipeline(VENDAS_BRUTAS)
print(f"Registros validos: {resultado['qtd']}")
print(f"Total agregado: R$ {resultado['total']:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Mini pipeline ETL de vendas escolares com logging por etapa."""

import logging
from typing import TypedDict

logger = logging.getLogger(__name__)

VENDAS_BRUTAS = [
    {"produto": "Caderno", "valor": 12.50},
    {"produto": "", "valor": 0},
    {"produto": "Caneta", "valor": 3.00},
    {"produto": "   ", "valor": 5.00},
    {"produto": "Lapis", "valor": -1},
    {"produto": "Borracha", "valor": 2.00},
]


class Agregacao(TypedDict):
    """Resultado da etapa de agregacao do pipeline."""

    qtd: int
    total: float


def carregar_vendas(fonte: list[dict]) -> list[dict]:
    """Etapa 1: carrega os dados brutos da fonte (simula leitura de CSV)."""
    logger.info("Etapa 1: carregar")
    return fonte


def motivo_invalidacao(venda: dict) -> str | None:
    """Retorna o motivo da invalidacao ou None se o registro for valido."""
    # Guard clauses: cada regra de negocio testada isoladamente
    if not venda["produto"].strip():
        return "produto vazio"
    if venda["valor"] <= 0:
        return "valor invalido"
    return None


def limpar_vendas(vendas: list[dict]) -> list[dict]:
    """Etapa 2: descarta registros invalidos logando o motivo de cada um."""
    logger.info("Etapa 2: limpar")
    validas = []
    for venda in vendas:
        motivo = motivo_invalidacao(venda)
        if motivo is None:
            validas.append(venda)
        else:
            # WARNING preserva o rastro do descarte sem interromper o fluxo
            logger.warning("Descartado (%s): %s", motivo, venda)
    return validas


def agregar_vendas(vendas: list[dict]) -> Agregacao:
    """Etapa 3: consolida quantidade e total das vendas validas."""
    logger.info("Etapa 3: agregar")
    if not vendas:
        # Base vazia apos limpeza e um problema operacional grave
        logger.error("Nenhum registro valido para agregar")
    return {"qtd": len(vendas), "total": sum(v["valor"] for v in vendas)}


def executar_pipeline(fonte: list[dict]) -> Agregacao:
    """Orquestra as etapas carregar -> limpar -> agregar."""
    return agregar_vendas(limpar_vendas(carregar_vendas(fonte)))


def main() -> None:
    resultado = executar_pipeline(VENDAS_BRUTAS)
    print(f"Registros validos: {resultado['qtd']}")
    print(f"Total agregado: R$ {resultado['total']:.2f}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
```

</details>
