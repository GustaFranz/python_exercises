# 141 - Funcao geradora: lotes de registros

## Objetivo

Criar gerador que entrega dados em lotes (chunks) para processamento incremental.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiEscolar |
| **Setor** | Logistica / operacoes |
| **Solicitacao** | Processar entregas em lotes para evitar sobrecarga no sistema. |

## Enunciado

```python
entregas = list(range(1, 14))  # ids 1 a 13
TAMANHO_LOTE = 4
```

Implemente `gerar_lotes(itens, tamanho)` que:
- recebe lista (ou iteravel) e tamanho do lote;
- usa `yield` para entregar sublistas consecutivas;
- ultimo lote pode ter menos itens.

No `main`:
1) Itere sobre os lotes e exiba cada lote.
2) Conte quantos lotes foram gerados.
3) Some todos os ids processados (prova de que nenhum foi perdido).

## Como executar

```bash
cd "141_funcao_geradora_lotes"
python main.py
```
