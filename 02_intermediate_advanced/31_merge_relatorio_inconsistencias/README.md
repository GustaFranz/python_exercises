# 31 - Merge: relatorio com inconsistencias

## Objetivo

Detectar e destacar inconsistencias em merge de multiplas fontes.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Auditoria Educacional Brasil |
| **Setor** | Consultoria / auditoria |
| **Solicitacao** | Auditar cruzamento entre cadastro oficial e notas importadas. |

## Enunciado

cadastro = {"A01": "Ana", "A02": "Bruno", "A03": "Carla"}
notas_importadas = {"A01": 8.0, "A04": 7.0, "A02": -1}
Gere relatorio com categorias:
- ok — matricula em ambos e nota valida (0 a 10)
- sem_nota — no cadastro mas sem nota importada
- orfa — nota importada sem cadastro
- invalida — nota fora do intervalo 0-10
Exiba contagem e detalhes de cada categoria.

## Passo a passo

1. Declare os dicionarios `cadastro` e `notas_importadas` do enunciado.
2. Crie um dicionario de categorias com listas vazias: `relatorio = {"ok": [], "sem_nota": [], "orfa": [], "invalida": []}`.
3. Percorra o cadastro com `for matricula, nome in cadastro.items():`:
   - se `matricula not in notas_importadas`, adicione `(matricula, nome)` em `relatorio["sem_nota"]`;
   - senao, pegue a nota; se `0 <= nota <= 10`, va para `relatorio["ok"]`; caso contrario, para `relatorio["invalida"]`.
4. Percorra as notas com `for matricula, nota in notas_importadas.items():` e, quando `matricula not in cadastro`, adicione em `relatorio["orfa"]` — nota importada sem dono no cadastro.
5. Exiba o relatorio: para cada categoria, imprima o nome, a contagem (`len`) e os detalhes de cada item.
6. Confira com os dados do enunciado: `ok` deve ter A01, `sem_nota` A03, `orfa` A04 e `invalida` A02.

## Como executar

```bash
cd "31_merge_relatorio_inconsistencias"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Fonte oficial (cadastro) e fonte externa (notas importadas).
cadastro = {"A01": "Ana", "A02": "Bruno", "A03": "Carla"}
notas_importadas = {"A01": 8.0, "A04": 7.0, "A02": -1}

# Intervalo valido de nota, como constantes nomeadas.
NOTA_MIN = 0
NOTA_MAX = 10

# Uma lista por categoria de auditoria.
relatorio = {"ok": [], "sem_nota": [], "orfa": [], "invalida": []}

# Passo 1: audita cada matricula do cadastro oficial.
for matricula, nome in cadastro.items():
    if matricula not in notas_importadas:
        # Esta no cadastro mas nenhuma nota chegou para ela.
        relatorio["sem_nota"].append(f"{matricula} ({nome})")
        continue
    nota = notas_importadas[matricula]
    if NOTA_MIN <= nota <= NOTA_MAX:
        # Matricula nas duas fontes e nota dentro do intervalo.
        relatorio["ok"].append(f"{matricula} ({nome}) nota {nota}")
    else:
        # Nota existe, mas o valor e impossivel (ex.: -1).
        relatorio["invalida"].append(f"{matricula} ({nome}) nota {nota}")

# Passo 2: audita notas cuja matricula nao existe no cadastro.
for matricula, nota in notas_importadas.items():
    if matricula not in cadastro:
        # Nota "orfa": veio na importacao sem dono no cadastro.
        relatorio["orfa"].append(f"{matricula} nota {nota}")

# Exibe contagem e detalhes de cada categoria.
print("=== Relatorio de inconsistencias ===")
for categoria, itens in relatorio.items():
    print(f"{categoria}: {len(itens)}")
    for item in itens:
        print(f"  - {item}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Audita o cruzamento entre cadastro oficial e notas importadas."""

from collections import defaultdict
from enum import Enum

CADASTRO = {"A01": "Ana", "A02": "Bruno", "A03": "Carla"}
NOTAS_IMPORTADAS = {"A01": 8.0, "A04": 7.0, "A02": -1}

NOTA_MIN, NOTA_MAX = 0, 10


class Categoria(str, Enum):
    """Categorias possiveis da auditoria (evita strings soltas no codigo)."""

    OK = "ok"
    SEM_NOTA = "sem_nota"
    ORFA = "orfa"
    INVALIDA = "invalida"


def classificar_matricula(matricula: str, notas: dict[str, float]) -> Categoria:
    """Classifica uma matricula do cadastro em relacao as notas importadas."""
    # Guard clause: sem nota importada nao ha o que validar.
    if matricula not in notas:
        return Categoria.SEM_NOTA
    nota = notas[matricula]
    if NOTA_MIN <= nota <= NOTA_MAX:
        return Categoria.OK
    return Categoria.INVALIDA


def auditar(
    cadastro: dict[str, str], notas: dict[str, float]
) -> dict[Categoria, list[str]]:
    """Cruza as duas fontes e agrupa os achados por categoria."""
    # defaultdict(list) cria a lista da categoria no primeiro append.
    relatorio: defaultdict[Categoria, list[str]] = defaultdict(list)

    # Audita o cadastro oficial (detecta ok, sem_nota e invalida).
    for matricula, nome in cadastro.items():
        categoria = classificar_matricula(matricula, notas)
        nota = notas.get(matricula)
        detalhe = f"{matricula} ({nome})"
        if nota is not None:
            detalhe += f" nota {nota}"
        relatorio[categoria].append(detalhe)

    # Audita as notas importadas (detecta orfas, sem cadastro).
    for matricula, nota in notas.items():
        if matricula not in cadastro:
            relatorio[Categoria.ORFA].append(f"{matricula} nota {nota}")

    return relatorio


def main() -> None:
    relatorio = auditar(CADASTRO, NOTAS_IMPORTADAS)

    print("=== Relatorio de inconsistencias ===")
    # Itera sobre o Enum para exibir todas as categorias, mesmo vazias.
    for categoria in Categoria:
        itens = relatorio.get(categoria, [])
        print(f"{categoria.value}: {len(itens)}")
        for item in itens:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
```

</details>
