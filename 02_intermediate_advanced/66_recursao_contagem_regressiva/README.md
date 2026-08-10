# 66 - Recursao: contagem regressiva

## Objetivo

Imprimir contagem regressiva de N ate 0 com recursao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / expedicao |
| **Solicitacao** | Contagem regressiva antes de liberar lote de entregas no terminal. |

## Enunciado

Implemente recursivamente:

```python
def contagem(n: int) -> None:
    # se n < 0: return (caso base, sem print)
    # senao: imprime n e chama contagem(n - 1)
```

No `main`:

1) Chame `contagem(5)`.
2) Apos a chamada, imprima `"Fim da contagem"`.

Exemplo de saida:

```
5
4
3
2
1
0
Fim da contagem
```

## Passo a passo

1. Defina a funcao `contagem(n: int) -> None` (ela imprime, nao precisa retornar valor).
2. Escreva o caso base: `if n < 0: return`. Note que o caso base aqui NAO imprime nada — ele so interrompe a recursao depois que o 0 ja foi impresso.
3. Depois do caso base, imprima `n` com `print(n)`.
4. Em seguida, faca a chamada recursiva `contagem(n - 1)`. Como o `print` vem ANTES da chamada, os numeros saem em ordem decrescente.
5. No corpo principal, chame `contagem(5)`.
6. Apos a chamada, imprima `"Fim da contagem"` — essa linha roda so quando toda a cadeia recursiva terminou.

## Como executar

```bash
cd "66_recursao_contagem_regressiva"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def contagem(n):
    # Caso base: abaixo de zero nao ha o que imprimir — apenas para
    if n < 0:
        return

    # Imprime ANTES da chamada recursiva: por isso a ordem e 5, 4, 3...
    print(n)

    # Chamada recursiva com o problema menor (n diminui rumo ao caso base)
    contagem(n - 1)


# Dispara a contagem a partir de 5
contagem(5)

# So executa quando todas as chamadas recursivas ja terminaram
print("Fim da contagem")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Contagem regressiva recursiva antes de liberar lote de entregas.

Em producao, um dev escreveria simplesmente:
    for n in range(5, -1, -1): print(n)
O range decrescente e mais claro e nao consome pilha de chamadas.
A versao recursiva abaixo treina o padrao caso base + reducao do problema.
"""


def contagem(n: int) -> None:
    """Imprime n, n-1, ..., 0 usando recursao."""
    # Caso base silencioso: encerra sem imprimir quando passa do zero
    if n < 0:
        return

    # A impressao antes da recursao garante ordem decrescente;
    # se viesse depois, a saida seria crescente (0, 1, 2...)
    print(n)
    contagem(n - 1)


def main() -> None:
    contagem(5)
    # Executa apos toda a pilha de chamadas recursivas se desfazer
    print("Fim da contagem")


if __name__ == "__main__":
    main()
```

</details>
