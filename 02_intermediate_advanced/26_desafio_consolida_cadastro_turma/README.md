# 26 - DESAFIO - Consolida cadastro de turma

## Objetivo

Integrar list/dict comprehension, set, zip e CRUD em memoria num case de entrevista.

## Conteudos cobertos

- List comprehension e dict comprehension
- Conjuntos (`set`)
- `zip` entre estruturas
- CRUD com lista de dicionarios

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / operacoes academicas |
| **Solicitacao** | Prototipo para consolidar matriculas do dia, detectar duplicatas e gerar painel da turma. |

## Enunciado

Voce recebeu tres listas paralelas do staging (mesmo indice = mesmo aluno):

```python
ids = [1, 2, 3, 2, 4]
nomes = ["Ana", "Bruno", "Carla", "Bruno Dup", "Diego"]
notas = [7.5, 5.0, 8.0, 6.0, 4.5]
```

Checklist do case:

1) Use `zip` para montar registros `{id, nome, nota}`.
2) Implemente CRUD minimo em memoria:
   - `adicionar_aluno` (rejeite id duplicado)
   - `listar_alunos`
   - `buscar_por_id`
3) Ao importar o lote, ignore duplicatas e registre ids rejeitados em um `set`.
4) Com list/dict comprehension:
   - lista de nomes aprovados (nota >= 6)
   - `medias` nao precisa; monte `painel = {id: nota}` dos cadastrados
5) Relatorio final: total cadastrado, ids rejeitados (ordenados), aprovados, taxa de aprovacao %.

## Passo a passo

1. Declare as tres listas paralelas `ids`, `nomes` e `notas` do enunciado.
2. Monte os registros com list comprehension sobre `zip`: `registros = [{"id": i, "nome": n, "nota": t} for i, n, t in zip(ids, nomes, notas)]`.
3. Crie a base `alunos = []` e o conjunto `rejeitados = set()`.
4. Defina `def adicionar_aluno(alunos, registro):` que checa duplicata com `any(a["id"] == registro["id"] for a in alunos)`; se duplicado retorna `False`, senao faz `append` e retorna `True`.
5. Defina `def listar_alunos(alunos):` (exibe todos) e `def buscar_por_id(alunos, id_busca):` (retorna dict ou `None`).
6. Importe o lote: percorra `registros` chamando `adicionar_aluno`; quando retornar `False`, faca `rejeitados.add(registro["id"])`.
7. Com list comprehension, monte `aprovados = [a["nome"] for a in alunos if a["nota"] >= 6]`.
8. Com dict comprehension, monte `painel = {a["id"]: a["nota"] for a in alunos}`.
9. Calcule `taxa = len(aprovados) / len(alunos) * 100`.
10. Exiba o relatorio final: total cadastrado, `sorted(rejeitados)`, lista de aprovados, painel e taxa com `:.1f`.

## Como executar

```bash
cd "26_desafio_consolida_cadastro_turma"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Listas paralelas vindas do staging (mesmo indice = mesmo aluno).
ids = [1, 2, 3, 2, 4]
nomes = ["Ana", "Bruno", "Carla", "Bruno Dup", "Diego"]
notas = [7.5, 5.0, 8.0, 6.0, 4.5]

# Nota minima para aprovacao, como constante nomeada no topo.
NOTA_MINIMA = 6.0


def adicionar_aluno(alunos, registro):
    # Create com regra: rejeita se o id ja existe na base.
    if any(a["id"] == registro["id"] for a in alunos):
        return False
    alunos.append(registro)
    return True


def listar_alunos(alunos):
    # Read: exibe a base cadastrada.
    print("=== Alunos cadastrados ===")
    for a in alunos:
        print(f"{a['id']} | {a['nome']} | nota {a['nota']}")


def buscar_por_id(alunos, id_busca):
    # Busca linear padrao: dict encontrado ou None.
    for a in alunos:
        if a["id"] == id_busca:
            return a
    return None


# 1) zip junta as tres listas; a comprehension monta um dict por aluno.
registros = [
    {"id": i, "nome": n, "nota": t}
    for i, n, t in zip(ids, nomes, notas)
]

# 3) Importacao do lote: duplicatas vao para o set de rejeitados.
alunos = []
rejeitados = set()
for registro in registros:
    if not adicionar_aluno(alunos, registro):
        # set ignora repeticoes automaticamente.
        rejeitados.add(registro["id"])

# 4) List comprehension filtra os aprovados (nota >= 6).
aprovados = [a["nome"] for a in alunos if a["nota"] >= NOTA_MINIMA]
# Dict comprehension monta o painel id -> nota dos cadastrados.
painel = {a["id"]: a["nota"] for a in alunos}

# 5) Relatorio final consolidado.
listar_alunos(alunos)
taxa = len(aprovados) / len(alunos) * 100
print("=== Relatorio ===")
print(f"Total cadastrado: {len(alunos)}")
print(f"Ids rejeitados: {sorted(rejeitados)}")
print(f"Aprovados: {aprovados}")
print(f"Painel: {painel}")
print(f"Taxa de aprovacao: {taxa:.1f}%")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Consolida matriculas do dia: importa lote, rejeita duplicatas e gera painel."""

from dataclasses import dataclass

# Dados do staging: listas paralelas (mesmo indice = mesmo aluno).
IDS = [1, 2, 3, 2, 4]
NOMES = ["Ana", "Bruno", "Carla", "Bruno Dup", "Diego"]
NOTAS = [7.5, 5.0, 8.0, 6.0, 4.5]

NOTA_MINIMA = 6.0


@dataclass
class Aluno:
    """Registro consolidado de matricula."""

    id: int
    nome: str
    nota: float


@dataclass
class ResultadoImportacao:
    """Resultado do processamento do lote: base final + ids rejeitados."""

    alunos: list[Aluno]
    rejeitados: set[int]


def importar_lote(registros: list[Aluno]) -> ResultadoImportacao:
    """Importa registros ignorando ids duplicados (primeiro vence)."""
    alunos: list[Aluno] = []
    vistos: set[int] = set()      # ids ja cadastrados (lookup O(1))
    rejeitados: set[int] = set()  # ids que chegaram repetidos
    for registro in registros:
        if registro.id in vistos:
            rejeitados.add(registro.id)
            continue  # pula a duplicata sem interromper o lote
        vistos.add(registro.id)
        alunos.append(registro)
    return ResultadoImportacao(alunos=alunos, rejeitados=rejeitados)


def buscar_por_id(alunos: list[Aluno], id_busca: int) -> Aluno | None:
    """Retorna o aluno com o id informado, ou None."""
    return next((a for a in alunos if a.id == id_busca), None)


def main() -> None:
    # zip + comprehension transformam listas paralelas em objetos tipados.
    registros = [
        Aluno(id=i, nome=n, nota=t)
        for i, n, t in zip(IDS, NOMES, NOTAS)
    ]

    resultado = importar_lote(registros)
    alunos = resultado.alunos

    # Aprovados (list comprehension) e painel id -> nota (dict comprehension).
    aprovados = [a.nome for a in alunos if a.nota >= NOTA_MINIMA]
    painel = {a.id: a.nota for a in alunos}
    taxa = len(aprovados) / len(alunos) * 100

    print("=== Alunos cadastrados ===")
    for a in alunos:
        print(f"{a.id} | {a.nome} | nota {a.nota}")

    print("=== Relatorio ===")
    print(f"Total cadastrado: {len(alunos)}")
    print(f"Ids rejeitados: {sorted(resultado.rejeitados)}")
    print(f"Aprovados: {aprovados}")
    print(f"Painel: {painel}")
    print(f"Taxa de aprovacao: {taxa:.1f}%")


if __name__ == "__main__":
    main()
```

</details>
