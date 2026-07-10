# 35 - JSON: sincronizar memoria e arquivo

## Objetivo

Manter lista em memoria sincronizada com arquivo JSON validado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | InventarioTech Almoxarifado |
| **Setor** | Logistica interna |
| **Solicitacao** | Sistema de itens com memoria e disco sempre consistentes. |

## Enunciado

Classe ou fluxo com lista itens em memoria + itens.json.
Operacoes: adicionar_item (valida nome nao vazio, quantidade >= 0), salvar, carregar.
Ao adicionar: atualiza memoria E grava arquivo.
Ao iniciar: tenta carregar do arquivo para memoria.
Exiba itens apos cada operacao.

## Como executar

```bash
cd "35_json_sincronizar_memoria"
python main.py
```
