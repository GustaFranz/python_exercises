# 70 - Closure: multiplicador

## Objetivo

Criar multiplicador que captura fator fixo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Academia Prime |
| **Setor** | Fitness / planos |
| **Solicitacao** | Aplicar multiplicador de bonus fixo em metas de treino. |

## Enunciado

- Implemente criar_multiplicador(fator) com closure.
- Teste com fator 3 e valores 4 e 7.

## Passo a passo

1. Defina a funcao externa `criar_multiplicador(fator)`.
2. Dentro dela, defina a funcao interna `multiplicar(valor)` que retorna `valor * fator` — o `fator` e capturado do escopo externo (closure).
3. Retorne `multiplicar` sem parenteses (devolve a funcao, nao o resultado).
4. No corpo principal, crie `vezes3 = criar_multiplicador(3)`.
5. Chame `vezes3(4)` e `vezes3(7)` e exiba os resultados (esperado: 12 e 21).

## Como executar

```bash
cd "70_closure_multiplicador"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar_multiplicador(fator):
    # Funcao interna captura o fator do escopo externo (closure)
    def multiplicar(valor):
        return valor * fator

    # Devolve a funcao configurada com o fator
    return multiplicar


# Closure com fator 3 (bonus fixo das metas)
vezes3 = criar_multiplicador(3)

# O fator 3 fica lembrado entre as chamadas
print(vezes3(4))  # 4 * 3 -> 12
print(vezes3(7))  # 7 * 3 -> 21
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Fabrica de multiplicadores via closure para bonus de metas.

Padrao identico ao do somador: a fabrica configura, o closure aplica.
Para fixar argumentos de operacoes prontas, o mercado tambem usa
functools.partial com operator.mul (mostrado no final).
"""

from collections.abc import Callable


def criar_multiplicador(fator: float) -> Callable[[float], float]:
    """Retorna funcao que multiplica qualquer valor pelo fator capturado."""

    def multiplicar(valor: float) -> float:
        # fator vive no escopo da fabrica e permanece acessivel aqui
        return valor * fator

    return multiplicar


def main() -> None:
    vezes3 = criar_multiplicador(3)

    for valor in (4, 7):
        print(f"{valor} x 3 = {vezes3(valor)}")

    # Alternativa de mercado (mesmo comportamento):
    # from functools import partial
    # from operator import mul
    # vezes3 = partial(mul, 3)


if __name__ == "__main__":
    main()
```

</details>
