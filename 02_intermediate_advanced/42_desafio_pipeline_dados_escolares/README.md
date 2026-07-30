# 42 - DESAFIO - Pipeline de dados escolares

## Objetivo

Montar pipeline merge + JSON + CSV + with open em um case de dados.

## Conteudos cobertos

- Merge de duas fontes
- Persistencia JSON
- Leitura/escrita CSV
- Context manager `with open`

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Educacao / engenharia de dados junior |
| **Solicitacao** | Pipeline de staging: cruzar cadastro e notas, persistir JSON e exportar CSV limpo. |

## Enunciado

Fontes em memoria (pode gravar em arquivos no inicio):

**cadastro.json** (lista):
```json
[{"id": 1, "nome": "Ana", "turma": "7A"}, {"id": 2, "nome": "Bruno", "turma": "7B"}, {"id": 3, "nome": "Carla", "turma": "7A"}]
```

**notas.csv**:
```
id,nota
1,8.0
2,5.5
4,9.0
```

Checklist:

1) Com `with open`, carregue JSON e CSV.
2) Faca merge (left join por `id`): aluno sem nota -> `nota: None`; nota orfa (id 4) vai para lista de inconsistencias.
3) Persista o resultado consolidado em `saida/consolidado.json`.
4) Exporte apenas registros com nota valida para `saida/aprovacao.csv` (id,nome,turma,nota,status) onde status = aprovado se nota >= 6.
5) Imprima resumo do pipeline: lidos, consolidados, inconsistencias, exportados.

## Como executar

```bash
cd "42_desafio_pipeline_dados_escolares"
python main.py
```
