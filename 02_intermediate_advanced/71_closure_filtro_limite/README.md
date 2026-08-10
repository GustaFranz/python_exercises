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

## Passo a passo

1. Defina a funcao externa `criar_filtro_minimo(limite: float)`.
2. Dentro dela, defina `aceitar(nota: float) -> bool` retornando `nota >= limite` — o limite fica capturado no closure.
3. Retorne `aceitar` sem parenteses.
4. No corpo principal, crie `filtro = criar_filtro_minimo(7.0)`.
5. Teste os dois casos avulsos e exiba: `filtro(6.5)` (esperado `False`) e `filtro(8.0)` (esperado `True`).
6. Crie a lista `notas = [5.5, 7.0, 8.5, 6.0]`.
7. Filtre com list comprehension usando o closure como condicao: `aprovadas = [n for n in notas if filtro(n)]`.
8. Exiba `Notas aprovadas: [7.0, 8.5]`.

## Como executar

```bash
cd "71_closure_filtro_limite"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar_filtro_minimo(limite):
    # Funcao interna compara com o limite capturado do escopo externo
    def aceitar(nota):
        return nota >= limite

    # Retorna a funcao configurada (closure)
    return aceitar


# Cria o filtro com o corte da turma (7.0)
filtro = criar_filtro_minimo(7.0)

# Testes avulsos do closure
print(f"filtro(6.5): {filtro(6.5)}")  # abaixo do corte -> False
print(f"filtro(8.0): {filtro(8.0)}")  # acima do corte -> True

# Notas da turma para filtrar
notas = [5.5, 7.0, 8.5, 6.0]

# O closure vira a condicao da list comprehension
aprovadas = [nota for nota in notas if filtro(nota)]

print(f"Notas aprovadas: {aprovadas}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Filtro de notas com limite configuravel via closure.

Esse padrao (predicado configurado por fabrica) e o mesmo usado em
filter(), sorted(key=...), validacoes de formularios e regras de negocio
parametrizadas. O closure evita repetir o limite em cada chamada.
"""

from collections.abc import Callable

# Predicado: funcao que recebe um valor e responde True/False
Predicado = Callable[[float], bool]


def criar_filtro_minimo(limite: float) -> Predicado:
    """Retorna um predicado que aceita notas maiores ou iguais ao limite."""

    def aceitar(nota: float) -> bool:
        # limite permanece capturado do escopo da fabrica
        return nota >= limite

    return aceitar


def main() -> None:
    # Corte da turma definido uma unica vez
    filtro = criar_filtro_minimo(7.0)

    print(f"filtro(6.5): {filtro(6.5)}")
    print(f"filtro(8.0): {filtro(8.0)}")

    notas = [5.5, 7.0, 8.5, 6.0]

    # List comprehension com o predicado como condicao;
    # filter(filtro, notas) daria o mesmo resultado
    aprovadas = [nota for nota in notas if filtro(nota)]
    print(f"Notas aprovadas: {aprovadas}")


if __name__ == "__main__":
    main()
```

</details>
