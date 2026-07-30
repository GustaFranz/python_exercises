# 104 - Classe Pedido: CRUD de itens e desconto

## Objetivo

Modelar pedido comercial com OOP: itens, total, desconto e listagem (pergunta classica de entrevista).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / pedidos |
| **Solicitacao** | Calcular pedidos de material escolar com regras de desconto e controle de itens. |

## Enunciado

- Crie classe `Pedido` com cliente e lista interna de itens.
- Metodos esperados:
  - `adicionar_item(nome, qtd, preco)` — adiciona item valido
  - `remover_item(nome)` — remove item pelo nome (retorne bool ou trate ausencia)
  - `listar_itens()` — retorna copia ou visao dos itens
  - `total()` — soma `preco * qtd` de todos os itens
  - `aplicar_desconto(pct)` — aplica percentual (0 a 100) sobre o total com validacao
- Valide entradas: quantidade e preco positivos; desconto entre 0 e 100.
- Monte cenario de teste manual no `main.py` (adicionar, remover, desconto, total).

## Como executar

```bash
cd "104_classe_pedido_total"
python main.py
```
