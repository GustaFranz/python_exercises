# 133 - Introducao a map com list comprehension

## Objetivo

Conhecer `map()` e combinar com list comprehension para transformar e filtrar dados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataClean Escolar |
| **Setor** | Educacao / qualidade de dados |
| **Solicitacao** | Normalizar notas recebidas como texto e listar apenas valores validos. |

## Visao do bloco (exercicios 133 a 136)

Topico **map() + comprehensions**: aplicar funcoes em lote e montar estruturas com comprehensions.

| # | Nivel | Foco |
|---|-------|------|
| 133 | Leve | Introducao: map + list comprehension |
| 134 | Leve | map com lambda + filtro em list comprehension |
| 135 | Ponte | map + dict comprehension |
| 136 | Entrevista | Relatorio comercial com map e comprehensions |

## Enunciado

Dados de entrada:
```python
notas_texto = ["7.5", "8", "abc", "6.0", "-1", "9.5", "5.5"]
```

1) Crie funcao auxiliar:
```python
def converter_seguro(valor: str) -> float | None:
    try:
        return float(valor)
    except ValueError:
        return None
```
2) Converta com `map(converter_seguro, notas_texto)` e filtre `None` em list comprehension.
3) Filtre apenas notas entre `0` e `10` (inclusive) com list comprehension.
4) Exiba: lista original, notas convertidas validas e quantidade aprovada (nota >= 6).

Exemplo de saida:

```
Original: ['7.5', '8', 'abc', '6.0', '-1', '9.5', '5.5']
Validas (0-10): [7.5, 8.0, 6.0, 9.5, 5.5]
Aprovadas (>= 6): 4
```

## Como executar

```bash
cd "133_introducao_map_list_comprehension"
python main.py
```
