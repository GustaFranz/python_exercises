# 05 - List comprehension: normalizar notas

## Objetivo

Combinar filtro e transformacao para limpar base de notas.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Municipal de Educacao |
| **Setor** | Gestao publica escolar |
| **Solicitacao** | Limpar notas invalidas antes de calcular estatisticas da rede. |

## Enunciado

notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0]
Regras de validacao: nota numerica entre 0 e 10 (ignore None e valores fora do intervalo).
1) Gere notas_validas com list comprehension (apenas valores validos).
2) Gere notas_arredondadas com uma casa decimal.
3) Exiba: quantidade descartada, media das validas e lista final.

## Como executar

```bash
cd "05_list_comprehension_normalizar_notas"
python main.py
```
