# 24 - CRUD de alunos com validacao

## Objetivo

Aplicar CRUD com regras de validacao em cadastro escolar.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Colegio Futuro Ativo |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Cadastro de alunos com validacao antes de gravar na base em memoria. |

## Enunciado

Implemente cadastro de alunos: id, nome, turma, nota.
Regras de validacao ao criar:
- id unico (nao repetir)
- nome nao vazio
- nota entre 0 e 10
Funcoes: adicionar_aluno, listar_alunos, buscar_por_id.
Teste: cadastro valido, id duplicado, nota invalida.
Exiba mensagens claras de sucesso ou erro.

## Passo a passo

1. Crie a lista vazia `alunos` que servira de base em memoria.
2. Defina `def validar_aluno(dados, alunos):` que recebe o dicionario do novo aluno e a base atual, e retorna uma mensagem de erro (`str`) ou `None` se estiver tudo certo. Dentro dela:
   - use `any(a["id"] == dados["id"] for a in alunos)` para detectar id duplicado;
   - use `not dados["nome"].strip()` para detectar nome vazio;
   - use `not (0 <= dados["nota"] <= 10)` para detectar nota fora do intervalo.
3. Defina `def adicionar_aluno(alunos, dados):` que chama `validar_aluno` primeiro; se houver erro, exibe a mensagem e retorna `False`; senao faz `alunos.append(dados)`, exibe sucesso e retorna `True`.
4. Defina `def listar_alunos(alunos):` que percorre a lista e imprime `id | nome | turma | nota` com f-string.
5. Defina `def buscar_por_id(alunos, id_busca):` que retorna o dicionario ou `None` (mesmo padrao do exercicio 22).
6. No fluxo principal, teste os tres cenarios:
   - cadastro valido (ex.: `{"id": 1, "nome": "Ana", "turma": "9A", "nota": 8.5}`);
   - id duplicado (repita o id 1);
   - nota invalida (ex.: nota 15).
7. Finalize chamando `listar_alunos(alunos)` para mostrar que so o registro valido entrou.

## Como executar

```bash
cd "24_crud_alunos_validacao"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Base de alunos em memoria (comeca vazia).
alunos = []


def validar_aluno(dados, alunos):
    # Retorna a mensagem de erro, ou None quando os dados sao validos.
    # any() para no primeiro id igual — eficiente para checar duplicata.
    if any(a["id"] == dados["id"] for a in alunos):
        return f"id {dados['id']} ja cadastrado"
    # strip() remove espacos: "   " tambem conta como nome vazio.
    if not dados["nome"].strip():
        return "nome nao pode ser vazio"
    # Comparacao encadeada checa o intervalo em uma unica expressao.
    if not (0 <= dados["nota"] <= 10):
        return f"nota {dados['nota']} fora do intervalo 0 a 10"
    return None


def adicionar_aluno(alunos, dados):
    # Create com validacao: so grava se validar_aluno nao apontar erro.
    erro = validar_aluno(dados, alunos)
    if erro:
        print(f"[ERRO] {dados['nome'] or '(sem nome)'}: {erro}")
        return False
    alunos.append(dados)
    print(f"[OK] Aluno {dados['nome']} cadastrado com sucesso")
    return True


def listar_alunos(alunos):
    # Read: exibe a base completa formatada.
    print("=== Alunos cadastrados ===")
    for a in alunos:
        print(f"{a['id']} | {a['nome']} | {a['turma']} | nota {a['nota']}")


def buscar_por_id(alunos, id_busca):
    # Busca linear: devolve o dict ou None se nao existir.
    for a in alunos:
        if a["id"] == id_busca:
            return a
    return None


# Cenario 1: cadastro valido.
adicionar_aluno(alunos, {"id": 1, "nome": "Ana", "turma": "9A", "nota": 8.5})
# Cenario 2: id duplicado (1 ja existe) — deve ser rejeitado.
adicionar_aluno(alunos, {"id": 1, "nome": "Bruno", "turma": "9A", "nota": 7.0})
# Cenario 3: nota invalida (15 > 10) — deve ser rejeitado.
adicionar_aluno(alunos, {"id": 2, "nome": "Carla", "turma": "9B", "nota": 15})

# So o registro valido deve aparecer na listagem final.
listar_alunos(alunos)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CRUD de alunos com validacao antes da gravacao (Colegio Futuro Ativo)."""

from dataclasses import dataclass


@dataclass
class Aluno:
    """Registro de aluno com tipos explicitos."""

    id: int
    nome: str
    turma: str
    nota: float


class ValidacaoError(Exception):
    """Erro de regra de negocio ao cadastrar aluno."""


def validar_aluno(aluno: Aluno, base: list[Aluno]) -> None:
    """Levanta ValidacaoError se o aluno violar alguma regra."""
    # Guard clauses: cada regra falha cedo com mensagem especifica.
    if any(a.id == aluno.id for a in base):
        raise ValidacaoError(f"id {aluno.id} ja cadastrado")
    if not aluno.nome.strip():
        raise ValidacaoError("nome nao pode ser vazio")
    if not 0 <= aluno.nota <= 10:
        raise ValidacaoError(f"nota {aluno.nota} fora do intervalo 0 a 10")


def adicionar_aluno(base: list[Aluno], aluno: Aluno) -> bool:
    """Valida e grava o aluno; retorna True em caso de sucesso."""
    try:
        validar_aluno(aluno, base)
    except ValidacaoError as erro:
        # Excecao customizada separa erro de negocio de bug de codigo.
        print(f"[ERRO] {aluno.nome or '(sem nome)'}: {erro}")
        return False
    base.append(aluno)
    print(f"[OK] Aluno {aluno.nome} cadastrado com sucesso")
    return True


def listar_alunos(base: list[Aluno]) -> None:
    """Exibe todos os alunos cadastrados."""
    print("=== Alunos cadastrados ===")
    for a in base:
        print(f"{a.id} | {a.nome} | {a.turma} | nota {a.nota}")


def buscar_por_id(base: list[Aluno], id_busca: int) -> Aluno | None:
    """Retorna o aluno com o id informado, ou None."""
    return next((a for a in base if a.id == id_busca), None)


def main() -> None:
    base: list[Aluno] = []

    # Tres cenarios de teste: valido, id duplicado e nota invalida.
    adicionar_aluno(base, Aluno(id=1, nome="Ana", turma="9A", nota=8.5))
    adicionar_aluno(base, Aluno(id=1, nome="Bruno", turma="9A", nota=7.0))
    adicionar_aluno(base, Aluno(id=2, nome="Carla", turma="9B", nota=15))

    listar_alunos(base)


if __name__ == "__main__":
    main()
```

</details>
