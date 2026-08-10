# 85 - Introducao ao logging

## Objetivo

Substituir prints por logging.info em fluxo simples.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Padronizar mensagens do script de verificacao de servidores. |

## Visao do bloco (exercicios 85 a 89)

Topico **logging**: registrar eventos com niveis e destinos configuraveis.

| # | Foco |
|---|------|
| 85 | Introducao + logging.info |
| 86 | Niveis INFO e ERROR |
| 87 | Log em arquivo |
| 88 | Mini ETL com log INFO/WARNING/ERROR por etapa |
| 89 | Auditoria de importacao CSV com log estruturado |

## Enunciado

1) Configure logging no inicio:
```python
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
```

2) Implemente:
```python
def verificar_servidor(nome: str, online: bool) -> None:
    # online True  -> logging.info(f"Servidor {nome}: OK")
    # online False -> logging.error(f"Servidor {nome}: OFFLINE")
```

3) Teste com `("web-01", True)` e `("db-01", False)`.

Nao use `print` — apenas `logging`.

Exemplo de saida:

```
INFO: Servidor web-01: OK
ERROR: Servidor db-01: OFFLINE
```

## Passo a passo

1. Importe o modulo `logging` no topo do arquivo.
2. Logo apos o import, configure o logging com `logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")`:
   - `level=logging.INFO` faz mensagens INFO (e acima) aparecerem — sem isso, o padrao e WARNING e o INFO seria ignorado.
   - `format` define como cada linha sera exibida: nivel, dois pontos e a mensagem.
3. Defina a funcao `verificar_servidor(nome, online)` que:
   - Se `online` for `True`, chama `logging.info(f"Servidor {nome}: OK")`.
   - Senao, chama `logging.error(f"Servidor {nome}: OFFLINE")`.
4. No fluxo principal, chame a funcao duas vezes: `verificar_servidor("web-01", True)` e `verificar_servidor("db-01", False)`.
5. Confira a saida no console: uma linha `INFO:` e uma linha `ERROR:`. Nao use `print` em nenhum ponto.

## Como executar

```bash
cd "85_introducao_logging"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import logging

# Configura o logging uma unica vez, no inicio do script
# level=INFO libera mensagens INFO e acima (WARNING, ERROR, CRITICAL)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def verificar_servidor(nome, online):
    # Servidor no ar: evento normal, registrado como INFO
    if online:
        logging.info(f"Servidor {nome}: OK")
    # Servidor fora do ar: problema real, registrado como ERROR
    else:
        logging.error(f"Servidor {nome}: OFFLINE")


# Testa um servidor online e um offline
verificar_servidor("web-01", True)
verificar_servidor("db-01", False)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Verificacao de servidores da MonitoraTI com mensagens padronizadas via logging."""

import logging

# getLogger(__name__) cria um logger nomeado pelo modulo — padrao de mercado
# que permite filtrar e configurar logs por modulo em projetos maiores
logger = logging.getLogger(__name__)


def verificar_servidor(nome: str, online: bool) -> None:
    """Registra o status do servidor com o nivel adequado (INFO ou ERROR)."""
    if online:
        # %s com argumento separado: o logging so formata se a mensagem for emitida
        logger.info("Servidor %s: OK", nome)
        return
    logger.error("Servidor %s: OFFLINE", nome)


def main() -> None:
    servidores = [("web-01", True), ("db-01", False)]
    for nome, online in servidores:
        verificar_servidor(nome, online)


if __name__ == "__main__":
    # basicConfig fica no bloco de execucao: quem importa o modulo
    # nao tem a configuracao global de logging alterada
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
```

</details>
