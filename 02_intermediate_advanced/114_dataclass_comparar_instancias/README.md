# 114 - Dataclass: comparar instancias

## Objetivo

Comparar igualdade entre instancias de dataclass.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Detectar cadastros duplicados de aluno na base da secretaria. |

## Enunciado

- Crie dataclass AlunoRegistro e compare instancias com ==.
- Demonstre igualdade e diferenca entre registros.

## Passo a passo

1. Importe o decorador: `from dataclasses import dataclass`.
2. Declare `@dataclass` sobre `class AlunoRegistro:` com os campos `matricula: int` e `nome: str`.
3. Crie tres instancias:
   - `a = AlunoRegistro(101, "Ana Silva")`
   - `b = AlunoRegistro(101, "Ana Silva")` — mesmos valores de `a`
   - `c = AlunoRegistro(102, "Bruno Costa")`
4. Compare com `==` e exiba os resultados: `a == b` deve ser `True` (a dataclass gera `__eq__` comparando **todos** os campos) e `a == c` deve ser `False`.
5. Para fixar, valide tambem com `assert a == b` e `assert a != c` — se nada estourar, a regra esta correta.

## Como executar

```bash
cd "114_dataclass_comparar_instancias"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
from dataclasses import dataclass


# Alem do __init__, a dataclass gera __eq__: dois registros sao iguais
# quando TODOS os campos tem o mesmo valor (igualdade por valor)
@dataclass
class AlunoRegistro:
    matricula: int
    nome: str


# a e b tem os mesmos valores; c e diferente
a = AlunoRegistro(101, "Ana Silva")
b = AlunoRegistro(101, "Ana Silva")
c = AlunoRegistro(102, "Bruno Costa")

# Sem dataclass, a == b seria False (objetos diferentes na memoria);
# com o __eq__ gerado, a comparacao olha o conteudo
print(f"a == b: {a == b}")  # True  -> possivel cadastro duplicado
print(f"a == c: {a == c}")  # False -> registros distintos

# assert documenta e valida a regra: falha alta se algo mudar
assert a == b
assert a != c
print("Comparacoes validadas com assert.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
from dataclasses import dataclass


# frozen=True torna o registro imutavel E hashable: alem de comparar
# com ==, da para usar em set/dict — jeito profissional de achar duplicados
@dataclass(frozen=True, slots=True)
class AlunoRegistro:
    """Registro de aluno usado na deteccao de cadastros duplicados."""

    matricula: int
    nome: str


def main() -> None:
    a = AlunoRegistro(101, "Ana Silva")
    b = AlunoRegistro(101, "Ana Silva")
    c = AlunoRegistro(102, "Bruno Costa")

    # Igualdade por valor gerada pela dataclass
    print(f"a == b: {a == b}")  # True
    print(f"a == c: {a == c}")  # False

    assert a == b
    assert a != c
    print("Comparacoes validadas com assert.")

    # Bonus pratico: como a dataclass e frozen (hashable), um set
    # elimina duplicados automaticamente — caso real da secretaria
    base = {a, b, c}
    print(f"Registros unicos na base: {len(base)}")  # 2


if __name__ == "__main__":
    main()
```

</details>
