# 25 - CRUD: menu e relatorio por turma

## Objetivo

Integrar CRUD em mini sistema com menu e relatorio agrupado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Colegio Futuro Ativo |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Protótipo de sistema de alunos com menu e relatorio por turma. |

## Enunciado

Monte menu com opcoes:
- 1 - Cadastrar aluno (id, nome, turma, nota)
- 2 - Listar todos
- 3 - Relatorio por turma (media e quantidade por turma)
- 0 - Sair
Use lista de dicionarios em memoria.
Validacoes do exercicio 24 devem ser aplicadas no cadastro.
Relatorio: agrupe por turma e calcule media e total de alunos.

## Passo a passo

1. Crie a lista vazia `alunos` como base em memoria.
2. Reaproveite do exercicio 24 as funcoes `validar_aluno(dados, alunos)` e `adicionar_aluno(alunos, dados)`.
3. Defina `def cadastrar_via_input(alunos):` que le os campos com `input()`, converte `id` com `int()` e `nota` com `float()` dentro de `try/except ValueError` (dados nao numericos devem gerar mensagem de erro, nao quebrar o programa) e chama `adicionar_aluno`.
4. Defina `def listar_alunos(alunos):` que imprime `id | nome | turma | nota` por linha.
5. Defina `def relatorio_por_turma(alunos):` que:
   - monta um dicionario `notas_por_turma` no formato `{turma: [notas]}` percorrendo `alunos`;
   - para cada turma, calcula `media = sum(notas) / len(notas)` e exibe `turma | quantidade | media` formatando a media com `:.1f`.
6. Defina `def exibir_menu():` que imprime as 4 opcoes.
7. No fluxo principal, use `while True:`; leia a opcao com `input()`; use `if/elif` para chamar a funcao correspondente; `break` na opcao `"0"`; mensagem de "opcao invalida" no `else`.

## Como executar

```bash
cd "25_crud_menu_relatorio_turma"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Base de alunos em memoria.
alunos = []


def validar_aluno(dados, alunos):
    # Mesmas regras do exercicio 24: id unico, nome nao vazio, nota 0-10.
    if any(a["id"] == dados["id"] for a in alunos):
        return f"id {dados['id']} ja cadastrado"
    if not dados["nome"].strip():
        return "nome nao pode ser vazio"
    if not (0 <= dados["nota"] <= 10):
        return f"nota {dados['nota']} fora do intervalo 0 a 10"
    return None


def adicionar_aluno(alunos, dados):
    # Valida antes de gravar; informa o resultado ao usuario.
    erro = validar_aluno(dados, alunos)
    if erro:
        print(f"[ERRO] {erro}")
        return False
    alunos.append(dados)
    print(f"[OK] Aluno {dados['nome']} cadastrado")
    return True


def cadastrar_via_input(alunos):
    # Le os campos do teclado e converte os numericos com seguranca.
    try:
        dados = {
            "id": int(input("id: ")),
            "nome": input("nome: "),
            "turma": input("turma: "),
            "nota": float(input("nota: ")),
        }
    except ValueError:
        # int()/float() levantam ValueError para entrada nao numerica.
        print("[ERRO] id deve ser inteiro e nota deve ser numerica")
        return
    adicionar_aluno(alunos, dados)


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    print("=== Alunos ===")
    for a in alunos:
        print(f"{a['id']} | {a['nome']} | {a['turma']} | nota {a['nota']}")


def relatorio_por_turma(alunos):
    if not alunos:
        print("Nenhum aluno para o relatorio")
        return
    # Agrupamento manual: turma -> lista de notas.
    notas_por_turma = {}
    for a in alunos:
        # setdefault cria a lista vazia na primeira vez que a turma aparece.
        notas_por_turma.setdefault(a["turma"], []).append(a["nota"])
    print("=== Relatorio por turma ===")
    for turma, notas in notas_por_turma.items():
        media = sum(notas) / len(notas)
        print(f"Turma {turma} | alunos: {len(notas)} | media: {media:.1f}")


def exibir_menu():
    print("\n1 - Cadastrar aluno")
    print("2 - Listar todos")
    print("3 - Relatorio por turma")
    print("0 - Sair")


# Loop principal: repete ate o usuario escolher sair.
while True:
    exibir_menu()
    opcao = input("Opcao: ")
    if opcao == "1":
        cadastrar_via_input(alunos)
    elif opcao == "2":
        listar_alunos(alunos)
    elif opcao == "3":
        relatorio_por_turma(alunos)
    elif opcao == "0":
        print("Encerrando...")
        break  # sai do while e termina o programa
    else:
        print("[ERRO] Opcao invalida, tente novamente")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Prototipo de sistema de alunos com menu e relatorio por turma."""

from collections import defaultdict
from statistics import mean

Aluno = dict[str, object]


def validar_aluno(dados: Aluno, base: list[Aluno]) -> str | None:
    """Retorna a mensagem de erro ou None se os dados forem validos."""
    if any(a["id"] == dados["id"] for a in base):
        return f"id {dados['id']} ja cadastrado"
    if not str(dados["nome"]).strip():
        return "nome nao pode ser vazio"
    if not 0 <= float(dados["nota"]) <= 10:  # type: ignore[arg-type]
        return f"nota {dados['nota']} fora do intervalo 0 a 10"
    return None


def adicionar_aluno(base: list[Aluno], dados: Aluno) -> bool:
    """Valida e grava o aluno na base em memoria."""
    erro = validar_aluno(dados, base)
    # Guard clause: falha cedo com mensagem clara.
    if erro:
        print(f"[ERRO] {erro}")
        return False
    base.append(dados)
    print(f"[OK] Aluno {dados['nome']} cadastrado")
    return True


def cadastrar_via_input(base: list[Aluno]) -> None:
    """Le os dados do teclado, convertendo campos numericos com seguranca."""
    try:
        dados: Aluno = {
            "id": int(input("id: ")),
            "nome": input("nome: "),
            "turma": input("turma: "),
            "nota": float(input("nota: ")),
        }
    except ValueError:
        print("[ERRO] id deve ser inteiro e nota deve ser numerica")
        return
    adicionar_aluno(base, dados)


def listar_alunos(base: list[Aluno]) -> None:
    """Exibe todos os alunos cadastrados."""
    if not base:
        print("Nenhum aluno cadastrado")
        return
    print("=== Alunos ===")
    for a in base:
        print(f"{a['id']} | {a['nome']} | {a['turma']} | nota {a['nota']}")


def relatorio_por_turma(base: list[Aluno]) -> None:
    """Agrupa por turma e exibe quantidade e media de notas."""
    if not base:
        print("Nenhum aluno para o relatorio")
        return
    # defaultdict(list) dispensa o setdefault: a lista nasce no primeiro acesso.
    notas_por_turma: defaultdict[str, list[float]] = defaultdict(list)
    for a in base:
        notas_por_turma[str(a["turma"])].append(float(a["nota"]))  # type: ignore[arg-type]
    print("=== Relatorio por turma ===")
    # sorted() garante ordem estavel de exibicao das turmas.
    for turma in sorted(notas_por_turma):
        notas = notas_por_turma[turma]
        # statistics.mean comunica a intencao melhor que sum/len.
        print(f"Turma {turma} | alunos: {len(notas)} | media: {mean(notas):.1f}")


MENU = """
1 - Cadastrar aluno
2 - Listar todos
3 - Relatorio por turma
0 - Sair"""


def main() -> None:
    base: list[Aluno] = []
    while True:
        print(MENU)
        opcao = input("Opcao: ").strip()
        # match/case deixa o roteamento de opcoes mais legivel que if/elif.
        match opcao:
            case "1":
                cadastrar_via_input(base)
            case "2":
                listar_alunos(base)
            case "3":
                relatorio_por_turma(base)
            case "0":
                print("Encerrando...")
                return
            case _:
                print("[ERRO] Opcao invalida, tente novamente")


if __name__ == "__main__":
    main()
```

</details>
