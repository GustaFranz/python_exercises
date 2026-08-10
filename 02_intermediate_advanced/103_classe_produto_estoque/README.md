# 103 - Classe Produto: estoque

## Objetivo

Controlar estoque com metodos vender e repor.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / estoque |
| **Solicitacao** | Controlar estoque de material escolar na loja virtual. |

## Enunciado

Crie a classe `Produto` com:

- `__init__(self, nome, preco, estoque)`
- `vender(self, qtd)` — reduz estoque se houver quantidade suficiente; retorna `True` ou `False` (se insuficiente, **nao altera** o estoque)
- `repor(self, qtd)` — aumenta o estoque
- `__str__(self)` — exibe nome, preco e estoque atual

Teste no `main` com produto `"Caderno"`, preco `10.0`, estoque inicial **5**:

1) Vender **3** unidades (ok, estoque vai para 2).
2) Vender **5** unidades (falha, estoque permanece 2).
3) Repor **10** unidades (estoque vai para 12).
4) Exiba o produto apos cada operacao.

## Como executar

```bash
cd "103_classe_produto_estoque"
python main.py
```
