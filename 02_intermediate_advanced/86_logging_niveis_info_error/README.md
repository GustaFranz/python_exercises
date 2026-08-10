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

## Como executar

```bash
cd "86_logging_niveis_info_error"
python main.py
```
