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

Crie a hierarquia:

**`Cliente`**
- `__init__(self, nome)`
- `desconto(self) -> float` — retorna `0.0`

**`ClienteEscola(Cliente)`**
- `desconto(self) -> float` — retorna `0.10`

**`ClienteParceiro(Cliente)`**
- `desconto(self) -> float` — retorna `0.15`

Implemente:

```python
def calcular_preco_final(cliente: Cliente, valor: float) -> float:
    return valor * (1 - cliente.desconto())
```

No `main`:

1) Monte a lista polimorfica de teste:
   ```python
   clientes = [
       Cliente("Maria"),
       ClienteEscola("Escola 12"),
       ClienteParceiro("Papelaria Centro"),
   ]
   ```
2) Use `valor_base = 100.0` e percorra a lista com um unico loop (sem `if/elif` por tipo).
3) Exiba tabela com colunas: `Nome | Tipo | Desconto | Preco final`.

Exemplo de saida:

```
Nome              | Tipo     | Desconto | Preco final
Maria             | Cliente  | 0%       | 100.00
Escola 12         | Escola   | 10%      | 90.00
Papelaria Centro  | Parceiro | 15%      | 85.00
```

## Como executar

```bash
cd "110_heranca_descontos_cliente"
python main.py
```
