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

## Como executar

```bash
cd "87_logging_arquivo"
python main.py
```
