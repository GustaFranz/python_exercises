# 05 - List comprehension: pipeline de limpeza de notas

## Objetivo

Simular pipeline de qualidade de dados com list comprehension e regras de negocio.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Municipal de Educacao |
| **Setor** | Gestao publica escolar / dados |
| **Solicitacao** | Limpar lote de notas do staging antes de publicar no dashboard da rede. |

## Enunciado

notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]

Regras do pipeline:
- Aceitar apenas `int` ou `float` (ignorar `None` e strings).
- Nota valida: entre 0 e 10 (inclusive).
- Arredondar validas para 1 casa decimal.
- Classificar: `aprovado` (>= 6) ou `recuperacao` (< 6).

Tarefas:
1) `notas_validas` com list comprehension (filtro).
2) `notas_arredondadas` com list comprehension (`round`).
3) `status_lote` com list comprehension de dicts `{nota, status}`.
4) Relatorio de auditoria: recebidas, descartadas, % descartado, media das validas,
   quantidade aprovado/recuperacao, lista final de status.

## Como executar

```bash
cd "05_list_comprehension_normalizar_notas"
python main.py
```
