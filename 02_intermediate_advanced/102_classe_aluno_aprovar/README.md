# 102 - Classe Aluno: metodo aprovar

## Objetivo

Adicionar metodo aprovar() que altera status do aluno.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Marcar alunos aprovados automaticamente apos fechamento de notas. |

## Enunciado

Estenda a classe `Aluno` com:

- `__init__(self, nome, nota)` — define `self.aprovado = False`
- `aprovar(self)` — se `nota >= 7.0`, define `self.aprovado = True`
- `__str__(self)` — inclui status `"Aprovado"` ou `"Reprovado"`

Teste no `main`:

1) Aluno com nota **8.0** — chame `aprovar()` e exiba (deve ficar Aprovado).
2) Aluno com nota **5.5** — chame `aprovar()` e exiba (deve ficar Reprovado).

## Passo a passo

1. Declare a classe `Aluno` com `__init__(self, nome, nota)` guardando `self.nome`, `self.nota` e iniciando `self.aprovado = False`.
2. Implemente o metodo `aprovar(self)`: dentro dele, se `self.nota >= 7.0`, altere `self.aprovado = True` (caso contrario, nao mude nada).
3. Implemente `__str__(self)`: converta o booleano em texto (`"Aprovado"` se `self.aprovado` for `True`, senao `"Reprovado"`) e retorne uma f-string com nome, nota e status.
4. No fluxo principal, crie um aluno com nota `8.0` e outro com nota `5.5`.
5. Chame `aprovar()` em cada um **antes** de exibir.
6. Exiba os dois com `print()` e confira: o primeiro deve aparecer como Aprovado e o segundo como Reprovado.

## Como executar

```bash
cd "102_classe_aluno_aprovar"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Aluno:
    def __init__(self, nome, nota):
        # Guarda os dados basicos do aluno na instancia
        self.nome = nome
        self.nota = nota
        # Todo aluno comeca como nao aprovado; o metodo aprovar() decide depois
        self.aprovado = False

    def aprovar(self):
        # Regra de negocio: nota minima 7.0 para aprovacao
        # So altera o estado quando a condicao e atendida
        if self.nota >= 7.0:
            self.aprovado = True

    def __str__(self):
        # Ternario converte o booleano em texto legivel para o usuario
        status = "Aprovado" if self.aprovado else "Reprovado"
        return f"Aluno: {self.nome} | Nota: {self.nota} | Status: {status}"


# Cria os dois casos de teste do enunciado
aluno1 = Aluno("Ana", 8.0)
aluno2 = Aluno("Bruno", 5.5)

# aprovar() precisa ser chamado antes do print para atualizar o estado
aluno1.aprovar()
aluno2.aprovar()

print(aluno1)  # nota 8.0 -> Aprovado
print(aluno2)  # nota 5.5 -> Reprovado
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
# Constante no topo do modulo: a regra fica visivel e facil de alterar
NOTA_MINIMA_APROVACAO = 7.0


class Aluno:
    """Aluno com aprovacao calculada apos o fechamento de notas."""

    def __init__(self, nome: str, nota: float) -> None:
        self.nome = nome
        self.nota = nota
        # Estado inicial explicito; muda apenas via aprovar()
        self.aprovado = False

    def aprovar(self) -> None:
        """Marca o aluno como aprovado se a nota atingir o corte."""
        # Comparar com a constante evita "numero magico" espalhado no codigo
        if self.nota >= NOTA_MINIMA_APROVACAO:
            self.aprovado = True

    @property
    def status(self) -> str:
        # @property expoe o texto do status como atributo calculado (sem parenteses),
        # mantendo a conversao booleano -> texto num unico lugar
        return "Aprovado" if self.aprovado else "Reprovado"

    def __str__(self) -> str:
        # :.1f fixa uma casa decimal, padronizando a exibicao da nota
        return f"Aluno: {self.nome} | Nota: {self.nota:.1f} | Status: {self.status}"


def main() -> None:
    # Lista permite aplicar o mesmo fluxo (aprovar + exibir) a todos os alunos
    alunos = [Aluno("Ana", 8.0), Aluno("Bruno", 5.5)]

    for aluno in alunos:
        # Processa a regra de aprovacao antes de exibir
        aluno.aprovar()
        print(aluno)


if __name__ == "__main__":
    main()
```

</details>
