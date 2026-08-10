# 105 - Classe: simulador de caixa

## Objetivo

Simular caixa escolar com duas classes cooperando.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / PDV |
| **Solicitacao** | Simular ponto de venda do bazar escolar com registro de vendas. |

## Enunciado

Crie duas classes:

**`ItemVenda`**
- Atributos: `nome`, `preco`, `quantidade`
- Metodo `subtotal()` — retorna `preco * quantidade`

**`Caixa`**
- `__init__(self, operador)` — inicializa `self.vendas = []`
- `registrar_venda(self, item: ItemVenda)` — adiciona item a `self.vendas`
- `total_dia(self)` — soma os subtotais de todas as vendas
- `__str__(self)` — exibe operador, quantidade de vendas e total do dia

No `main`, simule o caixa da operadora **"Maria"** com **3 itens** vendidos (ex.: caderno, caneta, borracha) e exiba o resumo final.

## Como executar

```bash
cd "105_classe_simulador_caixa"
python main.py
```
