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

## Passo a passo

1. Declare a classe base `Colaborador` com `__init__(self, nome, salario_base)` guardando os dois atributos em `self`.
2. Implemente `calcular_salario(self)` em `Colaborador` retornando apenas `self.salario_base`.
3. Declare `class Gerente(Colaborador):` — herda o `__init__` da pai — e sobrescreva `calcular_salario(self)` retornando `self.salario_base + 500` (bonus fixo).
4. Declare `class Vendedor(Colaborador):` com `__init__(self, nome, salario_base, comissao_pct)`: chame `super().__init__(nome, salario_base)` e defina `self.comissao_pct`.
5. Em `Vendedor`, sobrescreva `calcular_salario(self, vendas)` — repare que aqui o metodo recebe um argumento extra — retornando `self.salario_base + (vendas * self.comissao_pct)`.
6. No `main`, cadastre: `Gerente("...", 4000)`, `Vendedor("...", 2500, 0.05)` e `Colaborador("...", 3000)`.
7. Exiba o salario calculado de cada um: gerente com `calcular_salario()`, vendedor com `calcular_salario(2000)` e colaborador com `calcular_salario()`.
8. Confira os valores esperados: gerente `4500`, vendedor `2600` (2500 + 2000 * 0.05) e colaborador `3000`.

## Como executar

```bash
cd "111_heranca_sistema_rh"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Colaborador:
    def __init__(self, nome, salario_base):
        # Dados comuns a todos os cargos
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        # Regra padrao: colaborador comum recebe apenas o salario base
        return self.salario_base


class Gerente(Colaborador):
    # Herda o __init__ da pai; so muda a regra de calculo
    def calcular_salario(self):
        # Gerente recebe bonus fixo de R$ 500 sobre a base
        return self.salario_base + 500


class Vendedor(Colaborador):
    def __init__(self, nome, salario_base, comissao_pct):
        # Reaproveita a base via super() e adiciona o percentual de comissao
        super().__init__(nome, salario_base)
        self.comissao_pct = comissao_pct

    def calcular_salario(self, vendas):
        # Vendedor depende do desempenho: base + comissao sobre as vendas
        return self.salario_base + (vendas * self.comissao_pct)


# Um colaborador de cada tipo, com os dados do enunciado
gerente = Gerente("Paula", 4000)
vendedor = Vendedor("Rafael", 2500, 0.05)
comum = Colaborador("Sonia", 3000)

# Vendedor precisa do total de vendas para fechar o salario
print(f"Gerente {gerente.nome}: R$ {gerente.calcular_salario():.2f}")
print(f"Vendedor {vendedor.nome}: R$ {vendedor.calcular_salario(2000):.2f}")
print(f"Colaborador {comum.nome}: R$ {comum.calcular_salario():.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
class Colaborador:
    """Colaborador comum: recebe apenas o salario base."""

    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        """Salario do mes; subclasses aplicam suas proprias regras."""
        return self.salario_base


class Gerente(Colaborador):
    """Gerente: salario base + bonus fixo."""

    # Constante de classe: a regra do bonus fica nomeada e visivel
    BONUS_FIXO = 500.0

    def calcular_salario(self) -> float:
        return self.salario_base + self.BONUS_FIXO


class Vendedor(Colaborador):
    """Vendedor: salario base + comissao sobre as vendas do mes."""

    def __init__(self, nome: str, salario_base: float, comissao_pct: float) -> None:
        super().__init__(nome, salario_base)
        self.comissao_pct = comissao_pct

    # Assinatura diferente da pai e aceitavel aqui porque o calculo do
    # vendedor depende de um dado externo (vendas do mes)
    def calcular_salario(self, vendas: float) -> float:
        return self.salario_base + (vendas * self.comissao_pct)


def main() -> None:
    gerente = Gerente("Paula", salario_base=4000)
    vendedor = Vendedor("Rafael", salario_base=2500, comissao_pct=0.05)
    comum = Colaborador("Sonia", salario_base=3000)

    vendas_do_mes = 2000.0

    # Folha do mes com valores formatados em duas casas
    print("=== FOLHA DO MES ===")
    print(f"Gerente {gerente.nome}: R$ {gerente.calcular_salario():.2f}")
    print(f"Vendedor {vendedor.nome}: R$ {vendedor.calcular_salario(vendas_do_mes):.2f}")
    print(f"Colaborador {comum.nome}: R$ {comum.calcular_salario():.2f}")


if __name__ == "__main__":
    main()
```

</details>
