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

## Como executar

```bash
cd "66_recursao_contagem_regressiva"
python main.py
```
