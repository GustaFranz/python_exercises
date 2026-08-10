# 51 - Excecao customizada: cadastro com regras

## Objetivo

Crie EmailInvalidoError e CargoInvalidoError.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Validar cadastro de funcionario antes de inserir no sistema piloto. |

## Enunciado

1) Crie as excecoes:
```python
class EmailInvalidoError(Exception):
    pass

class CargoInvalidoError(Exception):
    pass
```

2) Implemente:
```python
def cadastrar_funcionario(nome: str, email: str, cargo: str) -> dict:
    # nome nao vazio
    # email deve conter "@"
    # cargo deve estar em ("Analista", "Suporte", "Coordenador")
    # levanta excecao especifica em cada falha
    # retorna dict do funcionario se tudo ok
```

3) Teste 3 casos:
   - Valido: `"Ana Silva"`, `"ana@empresa.com"`, `"Analista"`.
   - Email invalido: `"Bruno"`, `"bruno-email"`, `"Suporte"`.
   - Cargo invalido: `"Carla"`, `"carla@empresa.com"`, `"Diretor"`.

Use `except EmailInvalidoError` e `except CargoInvalidoError` separados.

## Passo a passo

1. Defina as classes `EmailInvalidoError(Exception)` e `CargoInvalidoError(Exception)`, ambas com corpo `pass` (ou docstring).
2. Defina a constante `CARGOS_VALIDOS = ("Analista", "Suporte", "Coordenador")` no topo.
3. Defina `def cadastrar_funcionario(nome: str, email: str, cargo: str) -> dict:` validando em ordem:
   - Se `not nome.strip()`, levante `ValueError("nome nao pode ser vazio")` (o enunciado nao criou excecao propria para nome — `ValueError` resolve).
   - Se `"@" not in email`, levante `EmailInvalidoError(f"email sem @: {email}")`.
   - Se `cargo not in CARGOS_VALIDOS`, levante `CargoInvalidoError(f"cargo invalido: {cargo}")`.
   - Se tudo passou, retorne `{"nome": nome, "email": email, "cargo": cargo}`.
4. Crie a lista `casos` com as 3 tuplas do enunciado (valido, email invalido, cargo invalido).
5. Percorra `casos` com `for nome, email, cargo in casos:` chamando a funcao dentro de `try:`.
6. Capture com dois `except` separados: `except EmailInvalidoError as e:` exibindo `f"Email invalido: {e}"` e `except CargoInvalidoError as e:` exibindo `f"Cargo invalido: {e}"`.
7. No `else:`, exiba o dict retornado com `f"Cadastrado: {funcionario}"`.

## Como executar

```bash
cd "51_excecao_cadastro_regras"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Excecoes especificas: cada regra de negocio tem seu proprio erro
class EmailInvalidoError(Exception):
    pass


class CargoInvalidoError(Exception):
    pass


# Cargos aceitos no sistema piloto (tupla = colecao imutavel)
CARGOS_VALIDOS = ("Analista", "Suporte", "Coordenador")


def cadastrar_funcionario(nome, email, cargo):
    # Validacoes em ordem logica: nome, email, cargo
    if not nome.strip():
        # Sem excecao propria para nome no enunciado: ValueError resolve
        raise ValueError("nome nao pode ser vazio")
    if "@" not in email:
        raise EmailInvalidoError(f"email sem @: {email}")
    if cargo not in CARGOS_VALIDOS:
        raise CargoInvalidoError(f"cargo invalido: {cargo}")
    # Tudo valido: devolve o registro pronto para inserir no sistema
    return {"nome": nome, "email": email, "cargo": cargo}


# Os 3 casos de teste do enunciado
casos = [
    ("Ana Silva", "ana@empresa.com", "Analista"),   # valido
    ("Bruno", "bruno-email", "Suporte"),            # email invalido
    ("Carla", "carla@empresa.com", "Diretor"),      # cargo invalido
]

for nome, email, cargo in casos:
    try:
        funcionario = cadastrar_funcionario(nome, email, cargo)
    # except separados: cada tipo de erro gera uma mensagem diferente
    except EmailInvalidoError as e:
        print(f"Email invalido: {e}")
    except CargoInvalidoError as e:
        print(f"Cargo invalido: {e}")
    else:
        # Roda apenas quando o cadastro passou em todas as validacoes
        print(f"Cadastrado: {funcionario}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Validacao de cadastro de funcionario com excecoes de negocio especificas."""


class EmailInvalidoError(Exception):
    """Email sem o formato minimo esperado."""


class CargoInvalidoError(Exception):
    """Cargo fora da lista aceita pelo sistema piloto."""


# frozenset: busca rapida e imutavel — ideal para lista de valores permitidos
CARGOS_VALIDOS = frozenset({"Analista", "Suporte", "Coordenador"})


def cadastrar_funcionario(nome: str, email: str, cargo: str) -> dict[str, str]:
    """Valida os campos e devolve o registro pronto para persistencia.

    Levanta ValueError (nome), EmailInvalidoError ou CargoInvalidoError
    conforme a primeira regra violada.
    """
    # Guard clauses: cada regra falha cedo, sem if/else aninhado
    if not nome.strip():
        raise ValueError("nome nao pode ser vazio")
    if "@" not in email:
        raise EmailInvalidoError(f"email sem @: {email}")
    if cargo not in CARGOS_VALIDOS:
        raise CargoInvalidoError(f"cargo invalido: {cargo}")
    return {"nome": nome, "email": email, "cargo": cargo}


def main() -> None:
    casos = [
        ("Ana Silva", "ana@empresa.com", "Analista"),
        ("Bruno", "bruno-email", "Suporte"),
        ("Carla", "carla@empresa.com", "Diretor"),
    ]

    for nome, email, cargo in casos:
        try:
            funcionario = cadastrar_funcionario(nome, email, cargo)
        except EmailInvalidoError as erro:
            print(f"Email invalido: {erro}")
        except CargoInvalidoError as erro:
            print(f"Cargo invalido: {erro}")
        else:
            print(f"Cadastrado: {funcionario}")


if __name__ == "__main__":
    main()
```

</details>
