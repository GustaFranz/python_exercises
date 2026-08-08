# 142 - Funcao geradora: filtrar registros validos

## Objetivo

Usar gerador para validar e entregar apenas registros aprovados, um por vez.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | RH Escolar Mais |
| **Setor** | Recursos humanos |
| **Solicitacao** | Liberar bonus apenas para colaboradores elegiveis sem montar lista completa. |

## Enunciado

```python
registros = [
    {"id": 1, "nome": "Ana", "nota": 8.5, "faltas": 2},
    {"id": 2, "nome": "Bruno", "nota": 5.0, "faltas": 1},
    {"id": 3, "nome": "Carla", "nota": 9.0, "faltas": 0},
    {"id": 4, "nome": "Diego", "nota": 7.0, "faltas": 6},
    {"id": 5, "nome": "Elena", "nota": 7.5, "faltas": 3},
]
NOTA_MINIMA = 7.0
FALTAS_MAXIMAS = 4
```

Implemente `gerar_elegiveis(registros)` que:
- percorre registros;
- usa `yield` apenas para quem atende `nota >= NOTA_MINIMA` e `faltas <= FALTAS_MAXIMAS`;
- retorna dict completo do colaborador elegivel.

No `main`:
1) Consuma o gerador e exiba nome + nota de cada elegivel.
2) Conte elegiveis sem converter tudo em lista (use contador no loop).
3) Compare com `sum(1 for _ in gerar_elegiveis(registros))` para validar.

## Como executar

```bash
cd "142_funcao_geradora_filtrar"
python main.py
```
