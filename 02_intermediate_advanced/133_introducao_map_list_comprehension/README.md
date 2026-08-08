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

```python
notas_texto = ["7.5", "8", "abc", "6.0", "-1", "9.5", "5.5"]
```

1) Use `map(float, notas_texto)` dentro de um `try/except` **ou** converta com list comprehension protegida.
   Neste exercicio, prefira: primeiro `map(float, notas_texto)` e trate erros convertendo item a item
   em list comprehension (ignore valores invalidos).
2) Com list comprehension, filtre apenas notas entre `0` e `10` (inclusive).
3) Exiba: lista original, notas convertidas validas e quantidade aprovada (nota >= 6).

## Como executar

```bash
cd "133_introducao_map_list_comprehension"
python main.py
```
