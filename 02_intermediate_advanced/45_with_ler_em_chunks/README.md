# 45 - With open: ler em blocos

## Objetivo

Crie notas_export.txt com 20+ linhas aluno_id;nota.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Processar exportacao grande de notas sem carregar tudo na memoria de uma vez. |

## Enunciado

- Crie notas_export.txt com 20+ linhas aluno_id;nota.
- Leia em chunks de 64 caracteres com read(64).
- Exiba total de blocos e caracteres processados.

## Como executar

```bash
cd "45_with_ler_em_chunks"
python main.py
```
