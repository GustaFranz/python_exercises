# 110 - Heranca: descontos polimorficos por cliente

## Objetivo

Aplicar descontos diferentes por tipo de cliente usando heranca e polimorfismo (OOP em entrevista).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / precificacao |
| **Solicitacao** | Calcular preco final no bazar conforme perfil: cliente comum, escola ou parceiro. |

## Enunciado

- Crie hierarquia: `Cliente` (base), `ClienteEscola`, `ClienteParceiro`.
- Cada subclasse sobrescreve `desconto()` com percentual distinto (0%, 10%, 15%).
- Implemente `calcular_preco_final(cliente, valor)` usando polimorfismo (`cliente.desconto()`).
- Processe lista heterogenea de clientes e exiba nome, percentual e preco final para valor base (ex.: R$ 100,00).
- Bonus de entrevista: mesma funcao funciona para qualquer instancia da hierarquia.

## Como executar

```bash
cd "110_heranca_descontos_cliente"
python main.py
```
