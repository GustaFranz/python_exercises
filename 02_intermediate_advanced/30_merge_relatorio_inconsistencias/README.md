# 30 - Merge: relatorio com inconsistencias

## Objetivo

Detectar e destacar inconsistencias em merge de multiplas fontes.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Auditoria Educacional Brasil |
| **Setor** | Consultoria / auditoria |
| **Solicitacao** | Auditar cruzamento entre cadastro oficial e notas importadas. |

## Enunciado

cadastro = {"A01": "Ana", "A02": "Bruno", "A03": "Carla"}
notas_importadas = {"A01": 8.0, "A04": 7.0, "A02": -1}
Gere relatorio com categorias:
- ok — matricula em ambos e nota valida (0 a 10)
- sem_nota — no cadastro mas sem nota importada
- orfa — nota importada sem cadastro
- invalida — nota fora do intervalo 0-10
Exiba contagem e detalhes de cada categoria.

## Como executar

```bash
cd "30_merge_relatorio_inconsistencias"
python main.py
```
