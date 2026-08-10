# 109 - Heranca: usar super()

## Objetivo

Reutilizar construtor da classe pai com super().__init__.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Cadastrar funcionarios e estagiarios compartilhando dados base de pessoa. |

## Enunciado

Crie as classes:

**`Funcionario`**
- `__init__(self, nome, matricula)` — armazena `nome` e `matricula`
- `__str__(self)` — retorna nome e matricula

**`Estagiario(Funcionario)`**
- `__init__(self, nome, matricula, curso)` — chama `super().__init__(nome, matricula)` e define `self.curso`
- `__str__(self)` — inclui nome, matricula e curso

No `main`:

1) Instancie um estagiario (ex.: `"Lucas"`, matricula `"E2024"`, curso `"Administracao"`).
2) Exiba a instancia com `print()`.

Exemplo de saida:

```
Estagiario: Lucas | Matricula: E2024 | Curso: Administracao
```

## Passo a passo

1. Declare a classe `Funcionario` com `__init__(self, nome, matricula)` guardando `self.nome` e `self.matricula`.
2. Implemente `__str__(self)` em `Funcionario` retornando f-string com nome e matricula.
3. Declare `class Estagiario(Funcionario):` com `__init__(self, nome, matricula, curso)`.
4. Dentro desse `__init__`, a **primeira** linha deve ser `super().__init__(nome, matricula)` — ela delega para a pai a criacao de `self.nome` e `self.matricula`, sem duplicar codigo.
5. Ainda no `__init__` da filha, defina o atributo extra: `self.curso = curso`.
6. Sobrescreva `__str__(self)` em `Estagiario` retornando `"Estagiario: {nome} | Matricula: {matricula} | Curso: {curso}"`.
7. No `main`, instancie `Estagiario("Lucas", "E2024", "Administracao")` e exiba com `print()`.

## Como executar

```bash
cd "109_heranca_super"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Funcionario:
    def __init__(self, nome, matricula):
        # Dados base compartilhados por qualquer funcionario
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Funcionario: {self.nome} | Matricula: {self.matricula}"


class Estagiario(Funcionario):
    def __init__(self, nome, matricula, curso):
        # super().__init__ chama o construtor da pai: e ela quem cria
        # self.nome e self.matricula — nada de repetir atribuicoes aqui
        super().__init__(nome, matricula)
        # A filha so cuida do que e exclusivo dela
        self.curso = curso

    def __str__(self):
        # Sobrescreve o __str__ para incluir o campo extra
        return f"Estagiario: {self.nome} | Matricula: {self.matricula} | Curso: {self.curso}"


# Estagiario "e um" Funcionario com campo extra (curso)
estagiario = Estagiario("Lucas", "E2024", "Administracao")
print(estagiario)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
class Funcionario:
    """Funcionario com os dados base de identificacao no RH."""

    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"Funcionario: {self.nome} | Matricula: {self.matricula}"


class Estagiario(Funcionario):
    """Funcionario em regime de estagio, vinculado a um curso."""

    def __init__(self, nome: str, matricula: str, curso: str) -> None:
        # Delegar a base para a pai mantem um unico ponto de verdade:
        # se Funcionario ganhar um campo novo, Estagiario herda de graca
        super().__init__(nome, matricula)
        self.curso = curso

    def __str__(self) -> str:
        return f"Estagiario: {self.nome} | Matricula: {self.matricula} | Curso: {self.curso}"


def main() -> None:
    estagiario = Estagiario("Lucas", matricula="E2024", curso="Administracao")
    # Argumentos nomeados na chamada deixam claro o papel de cada valor
    print(estagiario)


if __name__ == "__main__":
    main()
```

</details>
