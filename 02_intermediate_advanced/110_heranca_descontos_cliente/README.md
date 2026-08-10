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

## Passo a passo

1. Declare a classe base `Cliente` com `__init__(self, nome)` guardando `self.nome` e o metodo `desconto(self)` retornando `0.0` — cliente comum nao tem desconto, e esse e o comportamento padrao da hierarquia.
2. Declare `class ClienteEscola(Cliente):` sobrescrevendo **apenas** `desconto(self)` para retornar `0.10` (o `__init__` e herdado).
3. Declare `class ClienteParceiro(Cliente):` sobrescrevendo `desconto(self)` para retornar `0.15`.
4. Implemente a funcao `calcular_preco_final(cliente, valor)` exatamente como no enunciado: `valor * (1 - cliente.desconto())`.
5. No `main`, monte a lista polimorfica com os 3 clientes do enunciado e defina `valor_base = 100.0`.
6. Para exibir a coluna `Tipo`, crie um mapeamento do nome da classe para o rotulo (ex.: dict `{"Cliente": "Cliente", "ClienteEscola": "Escola", "ClienteParceiro": "Parceiro"}` consultado com `type(cliente).__name__`).
7. Percorra a lista com **um unico loop**, sem `if/elif` por tipo: em cada iteracao, obtenha tipo, desconto (`cliente.desconto()`, formatado como percentual) e preco final via `calcular_preco_final`.
8. Imprima o cabecalho e uma linha por cliente, alinhando as colunas com f-string (ex.: `{nome:<17}`).

## Como executar

```bash
cd "110_heranca_descontos_cliente"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def desconto(self):
        # Comportamento padrao da hierarquia: cliente comum sem desconto.
        # Retornar 0.0 aqui permite tratar TODOS os clientes do mesmo jeito
        return 0.0


class ClienteEscola(Cliente):
    def desconto(self):
        # Sobrescreve apenas a regra que muda: 10% para escolas
        return 0.10


class ClienteParceiro(Cliente):
    def desconto(self):
        # Parceiros comerciais tem o maior desconto: 15%
        return 0.15


def calcular_preco_final(cliente, valor):
    # Polimorfismo: a funcao nao sabe (nem precisa saber) o tipo concreto;
    # cada objeto responde desconto() com a sua propria regra
    return valor * (1 - cliente.desconto())


# Rotulos de exibicao por nome de classe (so para o relatorio)
TIPOS = {"Cliente": "Cliente", "ClienteEscola": "Escola", "ClienteParceiro": "Parceiro"}

# Lista polimorfica: tipos diferentes na mesma colecao
clientes = [
    Cliente("Maria"),
    ClienteEscola("Escola 12"),
    ClienteParceiro("Papelaria Centro"),
]

valor_base = 100.0

# Cabecalho da tabela com colunas alinhadas
print(f"{'Nome':<17} | {'Tipo':<8} | {'Desconto':<8} | Preco final")

# Um unico loop, sem if/elif por tipo — o metodo certo e escolhido sozinho
for cliente in clientes:
    tipo = TIPOS[type(cliente).__name__]          # rotulo amigavel
    desconto = f"{cliente.desconto():.0%}"        # 0.10 -> "10%"
    preco = calcular_preco_final(cliente, valor_base)
    print(f"{cliente.nome:<17} | {tipo:<8} | {desconto:<8} | {preco:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from typing import ClassVar


class Cliente:
    """Cliente comum do bazar (sem desconto)."""

    # ClassVar: rotulo pertence a classe, nao a cada instancia
    tipo: ClassVar[str] = "Cliente"

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def desconto(self) -> float:
        """Fracao de desconto (0.0 a 1.0); base retorna 0.0 como padrao seguro."""
        return 0.0


class ClienteEscola(Cliente):
    """Escola conveniada: 10% de desconto."""

    tipo: ClassVar[str] = "Escola"

    def desconto(self) -> float:
        return 0.10


class ClienteParceiro(Cliente):
    """Parceiro comercial: 15% de desconto."""

    tipo: ClassVar[str] = "Parceiro"

    def desconto(self) -> float:
        return 0.15


def calcular_preco_final(cliente: Cliente, valor: float) -> float:
    """Aplica o desconto polimorfico do cliente sobre o valor."""
    return valor * (1 - cliente.desconto())


def main() -> None:
    clientes: list[Cliente] = [
        Cliente("Maria"),
        ClienteEscola("Escola 12"),
        ClienteParceiro("Papelaria Centro"),
    ]
    valor_base = 100.0

    print(f"{'Nome':<17} | {'Tipo':<8} | {'Desconto':<8} | Preco final")
    for cliente in clientes:
        # cliente.tipo resolve o rotulo pela propria classe — sem isinstance
        # e sem dicionario externo de mapeamento
        desconto = f"{cliente.desconto():.0%}"
        preco = calcular_preco_final(cliente, valor_base)
        print(f"{cliente.nome:<17} | {cliente.tipo:<8} | {desconto:<8} | {preco:.2f}")


if __name__ == "__main__":
    main()
```

</details>
