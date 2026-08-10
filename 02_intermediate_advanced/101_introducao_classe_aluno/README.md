# 101 - Introducao a classe Aluno

## Objetivo

Criar classe Aluno com atributos e metodo __str__.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Modelar cadastro de aluno em classe reutilizavel no sistema escolar. |

## Visao do bloco (exercicios 101 a 105)

Topico **Classe simples**: objetos com atributos, metodos e __str__.

| # | Foco |
|---|------|
| 101 | Introducao + classe Aluno |
| 102 | Metodo aprovar() |
| 103 | Classe Produto com estoque |
| 104 | Classe Pedido: itens, total, desconto e remocao |
| 105 | Simulador de caixa com 2 classes |

## Enunciado

Crie a classe `Aluno` com:

- `__init__(self, nome, turma, nota)` — armazena os atributos em `self`
- `__str__(self)` — retorna `"Aluno: {nome} | Turma: {turma} | Nota: {nota}"`

No `main`:

1) Instancie 2 alunos com dados diferentes (ex.: Ana/7A/8.5 e Bruno/8B/6.0).
2) Exiba cada instancia com `print()`.

Exemplo de saida:

```
Aluno: Ana | Turma: 7A | Nota: 8.5
Aluno: Bruno | Turma: 8B | Nota: 6.0
```

## Passo a passo

1. Declare a classe com `class Aluno:`.
2. Implemente o construtor `__init__(self, nome, turma, nota)` guardando cada parametro no objeto: `self.nome = nome`, `self.turma = turma`, `self.nota = nota`.
3. Implemente `__str__(self)` retornando uma f-string no formato `"Aluno: {self.nome} | Turma: {self.turma} | Nota: {self.nota}"`.
4. Fora da classe, instancie dois alunos: `Aluno("Ana", "7A", 8.5)` e `Aluno("Bruno", "8B", 6.0)`.
5. Exiba cada instancia com `print(aluno)` — o `print` chama o `__str__` automaticamente.

## Como executar

```bash
cd "101_introducao_classe_aluno"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Classe e o "molde" que junta dados (atributos) e comportamento (metodos)
class Aluno:
    def __init__(self, nome, turma, nota):
        # __init__ roda automaticamente ao criar o objeto (Aluno(...))
        # self representa a instancia sendo criada; cada atribuicao
        # guarda o dado dentro do proprio objeto
        self.nome = nome
        self.turma = turma
        self.nota = nota

    def __str__(self):
        # __str__ define o texto exibido quando fazemos print(objeto)
        # Sem ele, o print mostraria algo como <__main__.Aluno object at 0x...>
        return f"Aluno: {self.nome} | Turma: {self.turma} | Nota: {self.nota}"


# Instancia dois alunos: cada objeto guarda seus proprios dados
aluno1 = Aluno("Ana", "7A", 8.5)
aluno2 = Aluno("Bruno", "8B", 6.0)

# print() chama o __str__ de cada instancia automaticamente
print(aluno1)
print(aluno2)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass


# @dataclass gera __init__ e __eq__ automaticamente a partir dos campos,
# eliminando o codigo repetitivo de construtor — padrao comum no mercado
# para classes que representam principalmente dados
@dataclass
class Aluno:
    """Representa um aluno do cadastro escolar."""

    # Campos tipados: a anotacao documenta o tipo esperado de cada dado
    nome: str
    turma: str
    nota: float

    def __str__(self) -> str:
        # Sobrescrevemos __str__ para controlar o formato de exibicao
        # (o __repr__ gerado pela dataclass serve para debug, nao para o usuario)
        return f"Aluno: {self.nome} | Turma: {self.turma} | Nota: {self.nota}"


def main() -> None:
    # Guardar as instancias em lista facilita percorrer e escalar o cadastro
    alunos = [
        Aluno("Ana", "7A", 8.5),
        Aluno("Bruno", "8B", 6.0),
    ]

    # Um unico loop exibe todos os alunos, sem repetir prints
    for aluno in alunos:
        print(aluno)


# Garante que main() so roda quando o arquivo e executado diretamente,
# e nao quando e importado por outro modulo
if __name__ == "__main__":
    main()
```

</details>
