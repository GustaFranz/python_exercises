# 23 - CRUD: atualizar e remover

## Objetivo

Atualizar campos e remover registros de uma lista de dicionarios.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Promocao de cargo e desligamento de colaborador no sistema piloto. |

## Enunciado

Base inicial com 3 funcionarios (id, nome, cargo).
1) Atualize o cargo do id=2 para "Analista Senior".
2) Remova o funcionario com id=1 da lista.
3) Exiba a lista antes e depois de cada operacao.
Use funcoes: atualizar_cargo(funcionarios, id, novo_cargo) e remover_por_id(funcionarios, id).

## Passo a passo

1. Crie a lista `funcionarios` com os 3 dicionarios (chaves `"id"`, `"nome"`, `"cargo"`).
2. Defina `def exibir(funcionarios, titulo):` para imprimir um titulo e a lista formatada — voce vai chamar essa funcao varias vezes.
3. Defina `def atualizar_cargo(funcionarios, id_alvo, novo_cargo):` que percorre a lista e, ao achar `funcionario["id"] == id_alvo`, faz `funcionario["cargo"] = novo_cargo` e retorna `True`; se nao achar, retorna `False`.
4. Defina `def remover_por_id(funcionarios, id_alvo):` que reconstroi a lista sem o registro alvo: `funcionarios[:] = [f for f in funcionarios if f["id"] != id_alvo]`. O `[:]` altera a lista original (in place), nao cria outra.
5. No fluxo principal: exiba a lista inicial com `exibir`.
6. Chame `atualizar_cargo(funcionarios, 2, "Analista Senior")` e exiba a lista de novo.
7. Chame `remover_por_id(funcionarios, 1)` e exiba a lista final.

## Como executar

```bash
cd "23_crud_atualizar_remover"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Base inicial com 3 funcionarios.
funcionarios = [
    {"id": 1, "nome": "Ana Silva", "cargo": "Analista"},
    {"id": 2, "nome": "Bruno Costa", "cargo": "Suporte"},
    {"id": 3, "nome": "Carla Mendes", "cargo": "Coordenadora"},
]


def exibir(funcionarios, titulo):
    # Funcao de exibicao reutilizada em cada etapa do fluxo.
    print(f"--- {titulo} ---")
    for funcionario in funcionarios:
        print(f"{funcionario['id']} | {funcionario['nome']} | {funcionario['cargo']}")


def atualizar_cargo(funcionarios, id_alvo, novo_cargo):
    # Update: localiza o registro e altera o valor da chave.
    for funcionario in funcionarios:
        if funcionario["id"] == id_alvo:
            funcionario["cargo"] = novo_cargo
            return True  # sinaliza que a atualizacao aconteceu
    return False  # id nao encontrado, nada foi alterado


def remover_por_id(funcionarios, id_alvo):
    # Delete: reconstroi a lista mantendo todos, exceto o id alvo.
    # O [:] substitui o CONTEUDO da lista original (in place),
    # entao quem tem referencia a ela ve a mudanca.
    funcionarios[:] = [f for f in funcionarios if f["id"] != id_alvo]


# Fluxo principal: mostra o estado antes e depois de cada operacao.
exibir(funcionarios, "Lista inicial")

atualizar_cargo(funcionarios, 2, "Analista Senior")
exibir(funcionarios, "Apos atualizar cargo do id=2")

remover_por_id(funcionarios, 1)
exibir(funcionarios, "Apos remover id=1")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Update e delete em base de funcionarios em memoria (piloto GestaoPro RH)."""

Funcionario = dict[str, object]

FUNCIONARIOS: list[Funcionario] = [
    {"id": 1, "nome": "Ana Silva", "cargo": "Analista"},
    {"id": 2, "nome": "Bruno Costa", "cargo": "Suporte"},
    {"id": 3, "nome": "Carla Mendes", "cargo": "Coordenadora"},
]


def exibir(funcionarios: list[Funcionario], titulo: str) -> None:
    """Exibe a lista formatada com um titulo de contexto."""
    print(f"--- {titulo} ---")
    for f in funcionarios:
        print(f"{f['id']} | {f['nome']} | {f['cargo']}")


def atualizar_cargo(
    funcionarios: list[Funcionario], id_alvo: int, novo_cargo: str
) -> bool:
    """Atualiza o cargo do funcionario com id_alvo; retorna se conseguiu."""
    # next() acha o primeiro registro que casa; None indica ausencia.
    alvo = next((f for f in funcionarios if f["id"] == id_alvo), None)
    # Guard clause: sai cedo se o id nao existe.
    if alvo is None:
        return False
    alvo["cargo"] = novo_cargo
    return True


def remover_por_id(funcionarios: list[Funcionario], id_alvo: int) -> bool:
    """Remove o funcionario com id_alvo; retorna se algo foi removido."""
    tamanho_antes = len(funcionarios)
    # Atribuicao com [:] preserva a identidade da lista (mutacao in place).
    funcionarios[:] = [f for f in funcionarios if f["id"] != id_alvo]
    # Se o tamanho mudou, houve remocao de fato.
    return len(funcionarios) < tamanho_antes


def main() -> None:
    exibir(FUNCIONARIOS, "Lista inicial")

    # Promocao: id=2 vira Analista Senior.
    if atualizar_cargo(FUNCIONARIOS, 2, "Analista Senior"):
        exibir(FUNCIONARIOS, "Apos atualizar cargo do id=2")

    # Desligamento: id=1 sai da base.
    if remover_por_id(FUNCIONARIOS, 1):
        exibir(FUNCIONARIOS, "Apos remover id=1")


if __name__ == "__main__":
    main()
```

</details>
