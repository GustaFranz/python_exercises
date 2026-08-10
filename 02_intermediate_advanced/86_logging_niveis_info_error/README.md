# 86 - Logging: niveis INFO e ERROR

## Objetivo

Registrar sucesso e falha com niveis distintos de log.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / plataforma |
| **Solicitacao** | Registrar tentativas de login de alunos no painel administrativo. |

## Enunciado

1) Configure logging:
```python
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
```

2) Implemente:
```python
def registrar_login(usuario: str, sucesso: bool) -> None:
    # sucesso True  -> logging.info(f"Login OK: {usuario}")
    # sucesso False -> logging.error(f"Login falhou: {usuario}")
```

3) Teste 3 usuarios: `("ana", True)`, `("bruno", False)`, `("carla", True)`.

Exemplo de saida:

```
2026-08-09 19:00:00 INFO Login OK: ana
2026-08-09 19:00:00 ERROR Login falhou: bruno
2026-08-09 19:00:00 INFO Login OK: carla
```

## Passo a passo

1. Importe o modulo `logging`.
2. Configure o logging no inicio com `logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")`:
   - `%(asctime)s` acrescenta data e hora em cada linha — essencial para auditoria de logins.
   - `%(levelname)s` mostra o nivel (INFO ou ERROR).
3. Defina a funcao `registrar_login(usuario, sucesso)` que:
   - Se `sucesso` for `True`, chama `logging.info(f"Login OK: {usuario}")`.
   - Senao, chama `logging.error(f"Login falhou: {usuario}")`.
4. Crie uma lista de tentativas com as tuplas `("ana", True)`, `("bruno", False)` e `("carla", True)`.
5. Percorra a lista com `for usuario, sucesso in tentativas:` e chame `registrar_login` para cada item.
6. Execute e confira: duas linhas INFO e uma linha ERROR, todas com data e hora.

## Como executar

```bash
cd "86_logging_niveis_info_error"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import logging

# asctime inclui data/hora — importante para rastrear quando cada login ocorreu
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def registrar_login(usuario, sucesso):
    # Sucesso e um evento normal do sistema: nivel INFO
    if sucesso:
        logging.info(f"Login OK: {usuario}")
    # Falha de login merece atencao: nivel ERROR
    else:
        logging.error(f"Login falhou: {usuario}")


# Tentativas de login a registrar (usuario, sucesso)
tentativas = [("ana", True), ("bruno", False), ("carla", True)]

# Desempacota cada tupla direto no for
for usuario, sucesso in tentativas:
    registrar_login(usuario, sucesso)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Registro de tentativas de login do painel administrativo da Edutech Brasil."""

import logging

# Logger nomeado pelo modulo: permite configurar/filtrar por origem do log
logger = logging.getLogger(__name__)


def registrar_login(usuario: str, sucesso: bool) -> None:
    """Loga a tentativa de login com nivel INFO (sucesso) ou ERROR (falha)."""
    # Escolhe o nivel conforme o resultado; logger.log unifica a chamada
    nivel = logging.INFO if sucesso else logging.ERROR
    mensagem = "Login OK: %s" if sucesso else "Login falhou: %s"
    logger.log(nivel, mensagem, usuario)


def main() -> None:
    tentativas = [("ana", True), ("bruno", False), ("carla", True)]
    for usuario, sucesso in tentativas:
        registrar_login(usuario, sucesso)


if __name__ == "__main__":
    # Configuracao global feita apenas quando executado como script
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    main()
```

</details>
