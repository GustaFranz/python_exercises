# 22 - CRUD: listar e buscar por ID

## Objetivo

Implementar leitura e busca por identificador em lista de dicionarios.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Consulta rapida de funcionario por matricula no piloto. |

## Enunciado

Use a base de funcionarios do exercicio anterior (ou recrie com 3 registros).
Implemente:
- 1) funcao listar_todos(funcionarios) — exibe todos
- 2) funcao buscar_por_id(funcionarios, id_busca) — retorna dict ou None
Teste busca existente (id=2) e inexistente (id=99).
Exiba resultado de cada busca.

## Passo a passo

1. Recrie a lista `funcionarios` com os 3 dicionarios do exercicio 21 (chaves `"id"`, `"nome"`, `"cargo"`).
2. Defina `def listar_todos(funcionarios):` que percorre a lista com `for` e imprime cada registro com f-string no formato `ID | Nome | Cargo`.
3. Defina `def buscar_por_id(funcionarios, id_busca):` que percorre a lista e, quando `funcionario["id"] == id_busca`, retorna o dicionario com `return`.
4. Apos o loop (nenhum registro encontrado), retorne `None` — esse e o sinal de "nao existe".
5. No fluxo principal, chame `listar_todos(funcionarios)`.
6. Chame `buscar_por_id(funcionarios, 2)`, guarde em uma variavel e exiba o resultado.
7. Chame `buscar_por_id(funcionarios, 99)` e exiba uma mensagem diferente quando o retorno for `None` (use `if resultado is None:`).

## Como executar

```bash
cd "22_crud_buscar_por_id"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Base de funcionarios recriada do exercicio anterior.
funcionarios = [
    {"id": 1, "nome": "Ana Silva", "cargo": "Analista"},
    {"id": 2, "nome": "Bruno Costa", "cargo": "Suporte"},
    {"id": 3, "nome": "Carla Mendes", "cargo": "Coordenadora"},
]


def listar_todos(funcionarios):
    # Read (listagem): exibe cada registro em uma linha.
    print("=== Funcionarios ===")
    for funcionario in funcionarios:
        print(f"{funcionario['id']} | {funcionario['nome']} | {funcionario['cargo']}")


def buscar_por_id(funcionarios, id_busca):
    # Read (busca): percorre a lista comparando o campo id.
    for funcionario in funcionarios:
        if funcionario["id"] == id_busca:
            # Encontrou: devolve o dicionario inteiro e encerra a funcao.
            return funcionario
    # Se o loop terminou sem return, o id nao existe na base.
    return None


def exibir_busca(funcionarios, id_busca):
    # Centraliza a exibicao do resultado para nao repetir codigo.
    resultado = buscar_por_id(funcionarios, id_busca)
    if resultado is None:
        # None e o contrato combinado para "nao encontrado".
        print(f"Busca id={id_busca}: funcionario nao encontrado")
    else:
        print(f"Busca id={id_busca}: {resultado['nome']} ({resultado['cargo']})")


# Fluxo principal: lista tudo e testa os dois cenarios de busca.
listar_todos(funcionarios)
exibir_busca(funcionarios, 2)   # caso existente
exibir_busca(funcionarios, 99)  # caso inexistente
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Listagem e busca por ID em base de funcionarios em memoria."""

# Type hints completos deixam o contrato das funcoes explicito.
Funcionario = dict[str, object]

FUNCIONARIOS: list[Funcionario] = [
    {"id": 1, "nome": "Ana Silva", "cargo": "Analista"},
    {"id": 2, "nome": "Bruno Costa", "cargo": "Suporte"},
    {"id": 3, "nome": "Carla Mendes", "cargo": "Coordenadora"},
]


def listar_todos(funcionarios: list[Funcionario]) -> None:
    """Exibe todos os funcionarios, um por linha."""
    print("=== Funcionarios ===")
    for funcionario in funcionarios:
        print(f"{funcionario['id']} | {funcionario['nome']} | {funcionario['cargo']}")


def buscar_por_id(funcionarios: list[Funcionario], id_busca: int) -> Funcionario | None:
    """Retorna o funcionario com o id informado, ou None se nao existir."""
    # next() com generator expression e o idioma padrao de busca:
    # para no primeiro match e devolve o default (None) se nada casar.
    return next((f for f in funcionarios if f["id"] == id_busca), None)


def exibir_busca(funcionarios: list[Funcionario], id_busca: int) -> None:
    """Exibe o resultado de uma busca de forma amigavel."""
    resultado = buscar_por_id(funcionarios, id_busca)
    # Guard clause: trata o caso de falha primeiro e sai cedo.
    if resultado is None:
        print(f"Busca id={id_busca}: funcionario nao encontrado")
        return
    print(f"Busca id={id_busca}: {resultado['nome']} ({resultado['cargo']})")


def main() -> None:
    listar_todos(FUNCIONARIOS)
    exibir_busca(FUNCIONARIOS, 2)   # busca com sucesso
    exibir_busca(FUNCIONARIOS, 99)  # busca sem resultado


if __name__ == "__main__":
    main()
```

</details>
