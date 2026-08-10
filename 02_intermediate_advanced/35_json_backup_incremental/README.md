# 35 - JSON: backup incremental

## Objetivo

Gerar backup com timestamp antes de atualizar cadastro JSON.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Seguros Familia Protegida |
| **Setor** | Seguros / cadastro de clientes |
| **Solicitacao** | Backup automatico antes de cada atualizacao do cadastro de clientes. |

## Enunciado

Arquivo `clientes.json` com lista de clientes (`id`, `nome`, `plano`).

Implemente:

```python
def fazer_backup(origem: str) -> str:
    # copia origem para backup_YYYYMMDD_HHMMSS.json
    # use datetime.now().strftime("%Y%m%d_%H%M%S") no nome

def atualizar_cliente(caminho: str, id: int, campo: str, valor) -> None:
    # ordem: backup -> carregar -> atualizar -> salvar
```

No `main`:

1) Crie `clientes.json` com 2 clientes de exemplo.
2) Simule atualizacao de um cliente (ex.: alterar `plano` do id `1`).
3) Confirme que arquivo de backup foi criado.

Exemplo de saida:

```
Backup criado: backup_20260809_190000.json
Cliente 1 atualizado: plano = Premium
```

## Como executar

```bash
cd "35_json_backup_incremental"
python main.py
```
