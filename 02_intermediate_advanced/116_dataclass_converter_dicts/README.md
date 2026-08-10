# 116 - Dataclass: converter dicts com validacao

## Objetivo

Converter dados brutos em objetos tipados, rejeitando linhas invalidas e reportando resultado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | Normalizar JSON de funcionarios importado, ignorando registros incompletos com relatorio. |

## Enunciado

- Crie `@dataclass Funcionario` com `nome`, `cargo`, `salario` e metodo `resumo()`.
- Implemente `converter(dados: list[dict])` retornando tupla `(convertidos, rejeitados)`.
- Linha invalida: falta campo obrigatorio ou `salario` nao numerico/negativo.
- Metodo `resumo()` retorna string curta (ex.: `"Ana — Analista — R$ 3500.00"`).
- Exiba quantidade convertida vs rejeitada e resumo de cada funcionario valido.

## Passo a passo

1. Importe `dataclass` e declare `@dataclass Funcionario` com `nome: str`, `cargo: str`, `salario: float`.
2. Adicione o metodo `resumo(self) -> str` retornando f-string no formato `"{nome} — {cargo} — R$ {salario:.2f}"`.
3. Monte a lista de dados brutos do enunciado (6 dicts, incluindo linhas sem `nome`, sem `cargo`, com salario negativo e com salario em texto `"5200"`).
4. Implemente `validar_linha(item: dict) -> bool`:
   - Verifique se os campos obrigatorios `nome`, `cargo` e `salario` existem no dict.
   - Verifique se `salario` e `int` ou `float` (use `isinstance(salario, (int, float))` — texto como `"5200"` reprova) e se e `>= 0`.
5. Implemente `converter(dados: list[dict]) -> tuple`:
   - Crie as listas `convertidos` e `rejeitados`.
   - Para cada item: se `validar_linha` aprovar, faca `Funcionario(**item)` (desempacota o dict nos campos); senao, guarde o **dict original** em `rejeitados` para auditoria.
   - Retorne `(convertidos, rejeitados)`.
6. Implemente `relatorio_conversao(convertidos, rejeitados) -> None` exibindo quantidade convertida vs rejeitada, o `resumo()` de cada funcionario valido e as linhas rejeitadas.
7. No fluxo principal, chame `converter` com os dados brutos e depois `relatorio_conversao` (esperado: 2 convertidos — Ana e Bruno — e 4 rejeitados).

## Como executar

```bash
cd "116_dataclass_converter_dicts"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from dataclasses import dataclass

# Campos que toda linha precisa ter para ser convertida
CAMPOS_OBRIGATORIOS = ("nome", "cargo", "salario")


@dataclass
class Funcionario:
    nome: str
    cargo: str
    salario: float

    def resumo(self):
        # String curta para exibicao em relatorios
        return f"{self.nome} — {self.cargo} — R$ {self.salario:.2f}"


def validar_linha(item):
    # 1) Todos os campos obrigatorios presentes?
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in item:
            return False
    # 2) Salario precisa ser numero (texto "5200" reprova) e nao negativo
    salario = item["salario"]
    if not isinstance(salario, (int, float)):
        return False
    if salario < 0:
        return False
    return True


def converter(dados):
    convertidos = []
    rejeitados = []
    for item in dados:
        if validar_linha(item):
            # ** desempacota o dict nos parametros da dataclass
            # (so e seguro DEPOIS da validacao)
            convertidos.append(Funcionario(**item))
        else:
            # Guarda o dict original intacto para auditoria
            rejeitados.append(item)
    return convertidos, rejeitados


def relatorio_conversao(convertidos, rejeitados):
    print(f"Convertidos: {len(convertidos)} | Rejeitados: {len(rejeitados)}")
    print("\nFuncionarios validos:")
    for funcionario in convertidos:
        print(f"- {funcionario.resumo()}")
    print("\nLinhas rejeitadas (auditoria):")
    for linha in rejeitados:
        print(f"- {linha}")


# Dados brutos simulando exportacao JSON com problemas tipicos
dados_brutos = [
    {"nome": "Ana", "cargo": "Analista", "salario": 3500},
    {"nome": "Bruno", "cargo": "Suporte", "salario": 2800},
    {"cargo": "Dev", "salario": 4200},                          # sem nome
    {"nome": "Carla", "salario": 3100},                         # sem cargo
    {"nome": "Diego", "cargo": "Estagiario", "salario": -500},  # negativo
    {"nome": "Elena", "cargo": "Coordenadora", "salario": "5200"},  # texto
]

convertidos, rejeitados = converter(dados_brutos)
relatorio_conversao(convertidos, rejeitados)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass

CAMPOS_OBRIGATORIOS = frozenset({"nome", "cargo", "salario"})


@dataclass(frozen=True, slots=True)
class Funcionario:
    """Funcionario normalizado a partir da importacao JSON."""

    nome: str
    cargo: str
    salario: float

    def resumo(self) -> str:
        """Linha curta para relatorios."""
        return f"{self.nome} — {self.cargo} — R$ {self.salario:.2f}"


def validar_linha(item: dict) -> bool:
    """Aprova apenas linhas completas com salario numerico nao negativo."""
    # <= entre sets: todos os campos obrigatorios estao nas chaves do dict?
    if not CAMPOS_OBRIGATORIOS <= item.keys():
        return False
    salario = item["salario"]
    # bool e subclasse de int em Python: excluimos explicitamente para
    # nao aceitar {"salario": True} como valido
    if isinstance(salario, bool) or not isinstance(salario, (int, float)):
        return False
    return salario >= 0


def converter(dados: list[dict]) -> tuple[list[Funcionario], list[dict]]:
    """Separa os dados brutos em (convertidos, rejeitados)."""
    convertidos: list[Funcionario] = []
    rejeitados: list[dict] = []
    for item in dados:
        if validar_linha(item):
            convertidos.append(Funcionario(**item))
        else:
            rejeitados.append(item)
    return convertidos, rejeitados


def relatorio_conversao(convertidos: list[Funcionario], rejeitados: list[dict]) -> None:
    """Exibe o resultado da normalizacao para conferencia."""
    total = len(convertidos) + len(rejeitados)
    print(f"Processadas {total} linhas: {len(convertidos)} convertidas, {len(rejeitados)} rejeitadas")

    print("\nFuncionarios validos:")
    for funcionario in convertidos:
        print(f"- {funcionario.resumo()}")

    print("\nLinhas rejeitadas (auditoria):")
    for linha in rejeitados:
        print(f"- {linha}")


def main() -> None:
    dados_brutos = [
        {"nome": "Ana", "cargo": "Analista", "salario": 3500},
        {"nome": "Bruno", "cargo": "Suporte", "salario": 2800},
        {"cargo": "Dev", "salario": 4200},
        {"nome": "Carla", "salario": 3100},
        {"nome": "Diego", "cargo": "Estagiario", "salario": -500},
        {"nome": "Elena", "cargo": "Coordenadora", "salario": "5200"},
    ]

    convertidos, rejeitados = converter(dados_brutos)
    relatorio_conversao(convertidos, rejeitados)


if __name__ == "__main__":
    main()
```

</details>
