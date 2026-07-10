# 34 - JSON: backup incremental

## Objetivo

Gerar backup com timestamp antes de atualizar cadastro JSON.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Seguros Familia Protegida |
| **Setor** | Seguros / cadastro de clientes |
| **Solicitacao** | Backup automatico antes de cada atualizacao do cadastro de clientes. |

## Enunciado

clientes.json com lista de clientes (id, nome, plano).
Ao atualizar cliente (por id), antes salve copia em backup_YYYYMMDD_HHMMSS.json.
Use datetime.now().strftime("%Y%m%d_%H%M%S") no nome.
Implemente: fazer_backup(origem), atualizar_cliente(caminho, id, campo, valor).
Simule uma atualizacao e confirme que backup foi criado.

## Como executar

```bash
cd "34_json_backup_incremental"
python main.py
```
