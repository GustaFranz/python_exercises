# 26 - Introducao a merge de fontes

## Objetivo

Conhecer merge de dados e o mapa dos exercicios 26 a 30.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Dados educacionais |
| **Solicitacao** | Unificar lista de nomes com dicionario de notas para boletim. |

## Visao do bloco (exercicios 26 a 30)

Topico **merge de fontes**: cruzar dados de estruturas diferentes.

| # | Foco |
|---|------|
| 26 | Introducao + nomes e notas |
| 27 | Left join simples |
| 28 | Tratar ausentes |
| 29 | Provas + simulados |
| 30 | Relatorio com inconsistencias |

## Enunciado

nomes = ["Ana", "Bruno", "Carla", "Daniel"]
notas_por_nome = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
Gere boletim unificado: lista de dicts {"nome": ..., "nota": ...}
Para nomes sem nota, use nota = None.
Exiba boletim e quantos ficaram sem nota.

## Como executar

```bash
cd "26_introducao_merge_fontes"
python main.py
```
