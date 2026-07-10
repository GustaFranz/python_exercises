# 29 - Merge: provas e simulados

## Objetivo

Mesclar duas avaliacoes por aluno em registro unico.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Avalia Escolar Online |
| **Setor** | Edtech / avaliacoes |
| **Solicitacao** | Consolidar nota de prova e simulado por aluno para boletim bimestral. |

## Enunciado

provas = {"Ana": 7.0, "Bruno": 5.5, "Carla": 8.5}
simulados = {"Ana": 8.0, "Bruno": 6.0, "Daniel": 7.0}
Uniao de todos os nomes (set de chaves).
Para cada aluno: nota_prova, nota_simulado (None se ausente), media das disponiveis.
Exiba boletim consolidado.

## Como executar

```bash
cd "29_merge_provas_simulados"
python main.py
```
