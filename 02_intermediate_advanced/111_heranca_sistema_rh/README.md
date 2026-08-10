# 111 - Heranca: sistema de RH

## Objetivo

Montar mini sistema de RH com 3 classes relacionadas por heranca.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Organizar equipe interna com cargos e salarios em estrutura unificada. |

## Enunciado

Crie a hierarquia de RH:

**`Colaborador`**
- Atributos: `nome`, `salario_base`
- `calcular_salario(self)` — retorna `salario_base`

**`Gerente(Colaborador)`**
- Bonus fixo de **R$ 500**
- `calcular_salario(self)` — retorna `salario_base + 500`

**`Vendedor(Colaborador)`**
- Atributo `comissao_pct` (ex.: `0.05` = 5%)
- `calcular_salario(self, vendas)` — retorna `salario_base + (vendas * comissao_pct)`

No `main`, cadastre 1 de cada tipo e exiba o salario calculado:

- Gerente: salario base **4000**
- Vendedor: salario base **2500**, comissao **5%**, vendas **2000**
- Colaborador comum: salario base **3000**

## Como executar

```bash
cd "111_heranca_sistema_rh"
python main.py
```
