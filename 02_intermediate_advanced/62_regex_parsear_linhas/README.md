# 62 - Regex: parsear linhas de exportacao escolar

## Objetivo

Extrair dados estruturados de linhas CSV-like com regex, rejeitar sujeira e filtrar por turma.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / importacao |
| **Solicitacao** | Validar lote de exportacao nome;nota;turma antes de carregar no sistema, com relatorio de rejeicoes. |

## Enunciado

Linhas de entrada (incluindo linhas sujas):

```
Ana;7.5;7A
Bruno;8.0;7B
;6.0;7A
Carla;nota;7A
Pedro;5.5;7A
7A;12.0;7A
Lucas;9.2;7B
```

- Para cada linha, use `re.search` com padrao tipo `^(.+);([\d.]+);(\w+)$` (ajuste se necessario).
- Monte `alunos_validos` como lista de dicts `{nome, nota, turma}` (nota como `float`).
- Rejeite linhas invalidas e acumule `rejeitadas` com a linha original.
- Filtre e exiba alunos da turma `7A`.
- Relatorio final: total recebido, validos, rejeitados, lista de rejeitadas.

## Como executar

```bash
cd "62_regex_parsear_linhas"
python main.py
```
