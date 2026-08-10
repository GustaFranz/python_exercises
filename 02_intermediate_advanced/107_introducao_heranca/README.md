# 107 - Introducao a heranca

## Objetivo

Criar hierarquia Pessoa -> Aluno e Professor com heranca simples.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Unificar cadastro de pessoas com tipos especificos aluno e professor. |

## Visao do bloco (exercicios 107 a 111)

Topico **Heranca simples**: reutilizar atributos e metodos da classe pai.

| # | Foco |
|---|------|
| 107 | Introducao + Pessoa, Aluno, Professor |
| 108 | Sobrescrever metodo apresentar() |
| 109 | Usar super() no construtor |
| 110 | Heranca polimorfica: descontos por tipo de cliente |
| 111 | Sistema de RH com 3 classes relacionadas |

## Enunciado

Crie a hierarquia:

**`Pessoa`**
- `__init__(self, nome, cpf)`
- `__str__(self)` — exibe nome e cpf

**`Aluno(Pessoa)`**
- Adiciona atributo `turma`
- `__init__` chama `super().__init__(nome, cpf)`
- `__str__` inclui turma

**`Professor(Pessoa)`**
- Adiciona atributo `disciplina`
- `__init__` chama `super().__init__(nome, cpf)`
- `__str__` inclui disciplina

No `main`:

1) Instancie 1 aluno (ex.: Ana, cpf `"111"`, turma `"7A"`).
2) Instancie 1 professor (ex.: Carlos, cpf `"222"`, disciplina `"Matematica"`).
3) Exiba ambos com `print()`.

## Passo a passo

1. Declare a classe base `Pessoa` com `__init__(self, nome, cpf)` guardando `self.nome` e `self.cpf`.
2. Implemente `__str__(self)` em `Pessoa` retornando f-string com nome e cpf.
3. Declare `class Aluno(Pessoa):` — o parenteses indica que `Aluno` **herda** de `Pessoa`.
4. No `__init__(self, nome, cpf, turma)` de `Aluno`, chame `super().__init__(nome, cpf)` para reaproveitar o construtor da pai e depois defina `self.turma = turma`.
5. Sobrescreva `__str__(self)` em `Aluno` incluindo a turma na saida.
6. Repita o padrao para `class Professor(Pessoa):` com o atributo `disciplina` no lugar de `turma`.
7. No `main`, instancie `Aluno("Ana", "111", "7A")` e `Professor("Carlos", "222", "Matematica")` e exiba ambos com `print()`.

## Como executar

```bash
cd "107_introducao_heranca"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Pessoa:
    def __init__(self, nome, cpf):
        # Classe base: guarda os dados comuns a qualquer pessoa
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Pessoa: {self.nome} | CPF: {self.cpf}"


class Aluno(Pessoa):
    # Aluno(Pessoa) significa: Aluno herda atributos e metodos de Pessoa
    def __init__(self, nome, cpf, turma):
        # super().__init__ reaproveita o construtor da pai (nome e cpf),
        # evitando duplicar as atribuicoes
        super().__init__(nome, cpf)
        # Atributo especifico do aluno
        self.turma = turma

    def __str__(self):
        # Sobrescreve o __str__ da pai para incluir a turma
        return f"Aluno: {self.nome} | CPF: {self.cpf} | Turma: {self.turma}"


class Professor(Pessoa):
    def __init__(self, nome, cpf, disciplina):
        # Mesmo padrao: pai cuida do comum, filha adiciona o especifico
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def __str__(self):
        return f"Professor: {self.nome} | CPF: {self.cpf} | Disciplina: {self.disciplina}"


# Cada instancia usa o __str__ da sua propria classe
aluno = Aluno("Ana", "111", "7A")
professor = Professor("Carlos", "222", "Matematica")

print(aluno)
print(professor)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
class Pessoa:
    """Dados comuns a qualquer pessoa do cadastro escolar."""

    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

    def __str__(self) -> str:
        return f"Pessoa: {self.nome} | CPF: {self.cpf}"


class Aluno(Pessoa):
    """Pessoa matriculada em uma turma (relacao 'e um': Aluno e uma Pessoa)."""

    def __init__(self, nome: str, cpf: str, turma: str) -> None:
        # A pai continua dona dos campos comuns; a filha so acrescenta os seus
        super().__init__(nome, cpf)
        self.turma = turma

    def __str__(self) -> str:
        return f"Aluno: {self.nome} | CPF: {self.cpf} | Turma: {self.turma}"


class Professor(Pessoa):
    """Pessoa responsavel por uma disciplina."""

    def __init__(self, nome: str, cpf: str, disciplina: str) -> None:
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def __str__(self) -> str:
        return f"Professor: {self.nome} | CPF: {self.cpf} | Disciplina: {self.disciplina}"


def main() -> None:
    # Lista tipada pela classe base: polimorfismo permite misturar
    # alunos e professores no mesmo cadastro
    pessoas: list[Pessoa] = [
        Aluno("Ana", "111", "7A"),
        Professor("Carlos", "222", "Matematica"),
    ]

    # Cada print usa o __str__ correto da subclasse automaticamente
    for pessoa in pessoas:
        print(pessoa)


if __name__ == "__main__":
    main()
```

</details>
