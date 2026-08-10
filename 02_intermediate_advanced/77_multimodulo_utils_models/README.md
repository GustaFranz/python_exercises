# 77 - Multi-modulo: utils e models

## Objetivo

Separar modelos de dados e funcoes utilitarias.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Organizar cadastro de alunos em camadas para manutencao futura. |

## Estrutura de arquivos

```
77_multimodulo_utils_models/
├── main.py
├── models.py   # criar_aluno(nome, turma) -> dict
└── utils.py    # validar_nome(nome) -> bool
```

## Enunciado

**`models.py`**
```python
def criar_aluno(nome: str, turma: str) -> dict:
    return {"nome": nome, "turma": turma}
```

**`utils.py`**
```python
def validar_nome(nome: str) -> bool:
    return len(nome.strip()) >= 3
```

No `main.py`:

1) Teste `"Ana"` — nome invalido; exiba mensagem de erro.
2) Teste `"Bruno Costa"` — nome valido; crie o aluno com `criar_aluno` e exiba o dict.

Regras:
- `models.py` nao valida.
- `utils.py` valida.
- `main.py` orquestra.

Exemplo de saida:

```
Nome invalido: Ana
Aluno cadastrado: {'nome': 'Bruno Costa', 'turma': '7A'}
```

## Passo a passo

1. Em `models.py`, implemente `criar_aluno(nome, turma)`: apenas retorne o dict `{"nome": nome, "turma": turma}` — nenhuma validacao aqui (modelo so representa dados).
2. Em `utils.py`, implemente `validar_nome(nome)`: retorne `len(nome.strip()) >= 3` (o `strip` evita que espacos contem como caracteres).
3. No `main.py`, importe as duas funcoes: `from models import criar_aluno` e `from utils import validar_nome`.
4. Ainda no `main.py`, defina a funcao `cadastrar(nome: str, turma: str)` que orquestra o fluxo:
   - se `validar_nome(nome)` for `False`, exiba `Nome invalido: {nome}`;
   - se for `True`, crie o aluno com `criar_aluno(nome, turma)` e exiba `Aluno cadastrado: {dict}`.
5. Chame `cadastrar("Ana", "7A")` (deve cair no caso invalido) e depois `cadastrar("Bruno Costa", "7A")` (caso valido).
6. Confira a saida com o exemplo do enunciado.

> Nota: ha uma inconsistencia no enunciado — "Ana" tem exatamente 3 caracteres, entao a regra literal `>= 3` a tornaria VALIDA, mas o exemplo de saida a rejeita. Para reproduzir o exemplo, as propostas abaixo usam corte de 4 caracteres (constante `MINIMO_CARACTERES = 4`). O foco do exercicio e a separacao de camadas, nao o corte exato.

## Como executar

```bash
cd "77_multimodulo_utils_models"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`models.py`**

```python
"""Modelos de dados do cadastro escolar."""


def criar_aluno(nome, turma):
    """Retorna dicionario representando um aluno."""
    # Modelo puro: so monta a estrutura, sem validar nada
    return {"nome": nome, "turma": turma}
```

**`utils.py`**

```python
"""Funcoes utilitarias de validacao."""

# Tamanho minimo do nome como constante nomeada
MINIMO_CARACTERES = 4


def validar_nome(nome):
    """Retorna True se nome tiver pelo menos 4 caracteres uteis.

    Usamos 4 para que nomes muito curtos como "Ana" sejam rejeitados,
    conforme o exemplo de saida do enunciado.
    """
    # strip() remove espacos das pontas antes de medir
    return len(nome.strip()) >= MINIMO_CARACTERES
```

**`main.py`**

```python
# Cada camada vem do seu modulo: modelo, validacao e orquestracao
from models import criar_aluno
from utils import validar_nome


def cadastrar(nome, turma):
    # main orquestra: valida primeiro, so cria se passou
    if not validar_nome(nome):
        print(f"Nome invalido: {nome}")
        return

    # Validou: o modelo monta o dict e o main exibe
    aluno = criar_aluno(nome, turma)
    print(f"Aluno cadastrado: {aluno}")


# Caso invalido: nome curto demais
cadastrar("Ana", "7A")

# Caso valido: cria e exibe o dict do aluno
cadastrar("Bruno Costa", "7A")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`models.py`**

```python
"""Modelos de dados do cadastro escolar."""


def criar_aluno(nome: str, turma: str) -> dict[str, str]:
    """Monta o registro de um aluno; nao aplica regras de negocio."""
    return {"nome": nome, "turma": turma}
```

**`utils.py`**

```python
"""Regras de validacao do cadastro."""

# Regra centralizada: mudar o corte exige alterar um unico lugar
MINIMO_CARACTERES = 4


def validar_nome(nome: str) -> bool:
    """Valida se o nome tem tamanho minimo apos remover espacos das pontas."""
    return len(nome.strip()) >= MINIMO_CARACTERES
```

**`main.py`**

```python
"""Orquestra o cadastro: valida (utils), cria (models) e exibe (aqui)."""

from models import criar_aluno
from utils import validar_nome


def cadastrar(nome: str, turma: str) -> None:
    """Fluxo completo de cadastro de um aluno."""
    # Guard clause: sai cedo no caso invalido, sem else aninhado
    if not validar_nome(nome):
        print(f"Nome invalido: {nome}")
        return

    aluno = criar_aluno(nome, turma)
    print(f"Aluno cadastrado: {aluno}")


def main() -> None:
    cadastrar("Ana", "7A")          # invalido: curto demais
    cadastrar("Bruno Costa", "7A")  # valido: cadastra e exibe


if __name__ == "__main__":
    main()
```

</details>
