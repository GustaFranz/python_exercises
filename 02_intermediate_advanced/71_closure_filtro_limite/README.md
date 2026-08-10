# 71 - Closure: filtro com limite

## Objetivo

Filtrar valores acima de limite capturado em closure.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / avaliacoes |
| **Solicitacao** | Filtrar alunos com nota acima do corte da turma. |

## Enunciado

Implemente:

```python
def criar_filtro_minimo(limite: float):
    def aceitar(nota: float) -> bool:
        return nota >= limite
    return aceitar
```

No `main`:

1) Crie `filtro = criar_filtro_minimo(7.0)`.
2) Teste `filtro(6.5)` → `False` e `filtro(8.0)` → `True`.
3) Filtre a lista `[5.5, 7.0, 8.5, 6.0]` com list comprehension e exiba notas aprovadas.

Exemplo de saida:

```
filtro(6.5): False
filtro(8.0): True
Notas aprovadas: [7.0, 8.5]
```

## Como executar

```bash
cd "71_closure_filtro_limite"
python main.py
```
