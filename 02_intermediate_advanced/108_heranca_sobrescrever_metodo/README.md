# 108 - Heranca: sobrescrever metodo

## Objetivo

Sobrescrever metodo apresentar() em subclasses.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Personalizar mensagem de boas-vindas por tipo de usuario no portal. |

## Enunciado

Crie a hierarquia com metodo `apresentar()` sobrescrito:

**`Usuario`**
- `__init__(self, nome)`
- `apresentar(self)` — retorna `"Ola, {nome}"`

**`Aluno(Usuario)`**
- `apresentar(self)` — retorna `"Aluno {nome}, bem-vindo ao portal!"`

**`Responsavel(Usuario)`**
- `apresentar(self)` — retorna `"Responsavel {nome}, acompanhe o boletim."`

No `main`, crie uma instancia de cada tipo e exiba o retorno de `apresentar()` para cada uma.

## Passo a passo

1. Declare a classe `Usuario` com `__init__(self, nome)` guardando `self.nome`.
2. Implemente `apresentar(self)` em `Usuario` retornando `f"Ola, {self.nome}"`.
3. Declare `class Aluno(Usuario):` **sem** novo `__init__` — a subclasse herda o construtor da pai automaticamente.
4. Em `Aluno`, defina `apresentar(self)` com o **mesmo nome** retornando `f"Aluno {self.nome}, bem-vindo ao portal!"` — isso e sobrescrever: a versao da filha substitui a da pai.
5. Repita para `class Responsavel(Usuario):` retornando `f"Responsavel {self.nome}, acompanhe o boletim."`.
6. No `main`, crie uma instancia de cada tipo (ex.: `Usuario("Carlos")`, `Aluno("Ana")`, `Responsavel("Marcia")`).
7. Exiba `print(instancia.apresentar())` para cada uma e observe que cada classe responde com a sua propria mensagem.

## Como executar

```bash
cd "108_heranca_sobrescrever_metodo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
class Usuario:
    def __init__(self, nome):
        # Construtor unico da hierarquia: as filhas herdam este __init__
        self.nome = nome

    def apresentar(self):
        # Mensagem generica da classe base
        return f"Ola, {self.nome}"


class Aluno(Usuario):
    # Nao precisa de __init__: herda o da pai sem mudanca
    def apresentar(self):
        # Mesmo nome de metodo = sobrescrita; esta versao vale para Aluno
        return f"Aluno {self.nome}, bem-vindo ao portal!"


class Responsavel(Usuario):
    def apresentar(self):
        # Cada subclasse personaliza a mensagem do portal
        return f"Responsavel {self.nome}, acompanhe o boletim."


# Uma instancia de cada tipo
usuario = Usuario("Carlos")
aluno = Aluno("Ana")
responsavel = Responsavel("Marcia")

# Python escolhe o apresentar() da classe real de cada objeto
print(usuario.apresentar())
print(aluno.apresentar())
print(responsavel.apresentar())
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
class Usuario:
    """Usuario generico do portal escolar."""

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def apresentar(self) -> str:
        """Mensagem de boas-vindas padrao (subclasses personalizam)."""
        return f"Ola, {self.nome}"


class Aluno(Usuario):
    """Aluno logado no portal."""

    def apresentar(self) -> str:
        # Sobrescrita: mesma assinatura da pai, comportamento especifico
        return f"Aluno {self.nome}, bem-vindo ao portal!"


class Responsavel(Usuario):
    """Responsavel que acompanha o aluno."""

    def apresentar(self) -> str:
        return f"Responsavel {self.nome}, acompanhe o boletim."


def main() -> None:
    # Lista tipada pela base: o codigo cliente nao precisa saber o tipo
    # concreto — isso e polimorfismo na pratica
    usuarios: list[Usuario] = [
        Usuario("Carlos"),
        Aluno("Ana"),
        Responsavel("Marcia"),
    ]

    # Um unico loop atende todos os tipos; nenhum if por classe
    for usuario in usuarios:
        print(usuario.apresentar())


if __name__ == "__main__":
    main()
```

</details>
