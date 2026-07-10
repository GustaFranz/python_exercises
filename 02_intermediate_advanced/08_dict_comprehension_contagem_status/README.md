# 08 - Dict comprehension: contagem de status

## Objetivo

Contar ocorrencias com dict comprehension.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida Entregas |
| **Setor** | Logistica |
| **Solicitacao** | Resumo de pedidos por status para reuniao operacional. |

## Enunciado

pedidos = ["entregue", "pendente", "entregue", "cancelado", "pendente", "entregue", "pendente"]
Status unicos conhecidos: entregue, pendente, cancelado
Monte contagem com dict comprehension:
{status: pedidos.count(status) for status in set(pedidos)}
Exiba cada status e sua quantidade.

## Como executar

```bash
cd "08_dict_comprehension_contagem_status"
python main.py
```
