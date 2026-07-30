# 27 - Introducao a merge de fontes

## Objetivo

Conhecer merge de dados e o mapa dos exercicios 27 a 31.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Dados educacionais |
| **Solicitacao** | Unificar lista de nomes com dicionario de notas para boletim. |

## Visao do bloco (exercicios 27 a 31)

Topico **merge de fontes**: cruzar dados de estruturas diferentes.

| # | Foco |
|---|------|
| 27 | Introducao + nomes e notas |
| 28 | Left join simples |
| 29 | Tratar ausentes |
| 30 | Provas + simulados |
| 31 | Relatorio com inconsistencias |

## Enunciado

nomes = ["Ana", "Bruno", "Carla", "Daniel"]
notas_por_nome = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
Gere boletim unificado: lista de dicts {"nome": ..., "nota": ...}
Para nomes sem nota, use nota = None.
Exiba boletim e quantos ficaram sem nota.

## Como executar

```bash
cd "27_introducao_merge_fontes"
python main.py
```
