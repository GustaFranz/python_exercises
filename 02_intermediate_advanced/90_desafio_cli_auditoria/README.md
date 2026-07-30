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

## Como executar

```bash
cd "90_desafio_cli_auditoria"
python main.py --acao resumo
```
