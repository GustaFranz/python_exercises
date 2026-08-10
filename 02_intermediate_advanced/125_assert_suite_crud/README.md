# 125 - Assert: suite CRUD em memoria

## Objetivo

Montar suite de asserts para CRUD simples em lista de dicts.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Validar modulo de cadastro em memoria antes de conectar ao banco. |

## Enunciado

Cada item e um dict com campo `"id"`. Implemente em memoria:

```python
def criar(lista: list, item: dict) -> None:
    # append na lista

def buscar_por_id(lista: list, id: int) -> dict | None:
    # retorna dict ou None

def remover(lista: list, id: int) -> bool:
    # retorna True se removeu, False se nao encontrou
```

Escreva suite de asserts em sequencia:

1) Crie 2 itens (ex.: `{"id": 1, "nome": "Ana"}` e `{"id": 2, "nome": "Bruno"}`).
2) Busque id existente — assert retorno correto.
3) Busque id inexistente — assert `None`.
4) Remova id existente — assert `True` e `len(lista)` correto em cada etapa.

## Passo a passo

1. Defina `criar(lista: list, item: dict) -> None` fazendo apenas `lista.append(item)`.
2. Defina `buscar_por_id(lista: list, id: int) -> dict | None` percorrendo a lista com `for` e comparando `item["id"] == id`; retorne o dict encontrado ou `None` apos o loop.
3. Defina `remover(lista: list, id: int) -> bool`: reutilize `buscar_por_id`; se achou, faca `lista.remove(item)` e retorne `True`; senao retorne `False`.
4. Monte a suite em sequencia, comecando com `cadastro = []`:
   - crie `{"id": 1, "nome": "Ana"}` e `{"id": 2, "nome": "Bruno"}`; apos cada criacao, `assert len(cadastro)` (1 e depois 2);
   - `assert buscar_por_id(cadastro, 1)["nome"] == "Ana"` (busca existente);
   - `assert buscar_por_id(cadastro, 99) is None` (busca inexistente);
   - `assert remover(cadastro, 1) is True` e `assert len(cadastro) == 1`;
   - `assert remover(cadastro, 99) is False` (remocao de id inexistente nao altera a lista).
5. Exiba `print("Todos os testes passaram.")` ao final.

## Como executar

```bash
cd "125_assert_suite_crud"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar(lista: list, item: dict) -> None:
    # Create do CRUD: apenas adiciona ao final da lista
    lista.append(item)


def buscar_por_id(lista: list, id: int) -> dict | None:
    # Read do CRUD: percorre ate achar o id; None sinaliza "nao existe"
    for item in lista:
        if item["id"] == id:
            return item
    return None


def remover(lista: list, id: int) -> bool:
    # Delete do CRUD: reutiliza a busca em vez de repetir o loop
    item = buscar_por_id(lista, id)
    if item is None:
        return False
    lista.remove(item)
    return True


# --- Suite de asserts: valida o fluxo completo em sequencia ---
cadastro = []

# 1) Criacao: len deve crescer a cada item
criar(cadastro, {"id": 1, "nome": "Ana"})
assert len(cadastro) == 1, "apos criar 1 item, lista deve ter 1"
criar(cadastro, {"id": 2, "nome": "Bruno"})
assert len(cadastro) == 2, "apos criar 2 itens, lista deve ter 2"

# 2) Busca existente: retorna o dict certo
assert buscar_por_id(cadastro, 1)["nome"] == "Ana", "id 1 deveria ser Ana"

# 3) Busca inexistente: retorna None (usar 'is None')
assert buscar_por_id(cadastro, 99) is None, "id 99 nao existe, deveria ser None"

# 4) Remocao existente: True e lista encolhe
assert remover(cadastro, 1) is True, "remover id existente deve retornar True"
assert len(cadastro) == 1, "apos remover, lista deve ter 1"

# Borda extra: remover inexistente nao altera a lista
assert remover(cadastro, 99) is False, "remover id inexistente deve retornar False"
assert len(cadastro) == 1, "lista nao deve mudar ao remover inexistente"

print("Todos os testes passaram.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""CRUD em memoria com suite de asserts.

Com pytest, cada etapa viraria um teste isolado usando uma fixture
que cria a lista limpa, evitando que um teste dependa do estado do anterior.
"""


def criar(lista: list[dict], item: dict) -> None:
    """Adiciona um item ao cadastro em memoria."""
    lista.append(item)


def buscar_por_id(lista: list[dict], id: int) -> dict | None:
    """Retorna o item com o id informado ou None se nao existir.

    next() com default expressa a busca em uma linha, sem loop manual.
    """
    return next((item for item in lista if item["id"] == id), None)


def remover(lista: list[dict], id: int) -> bool:
    """Remove o item com o id informado; True se removeu, False se nao achou."""
    item = buscar_por_id(lista, id)
    if item is None:
        return False
    lista.remove(item)
    return True


def testar_fluxo_crud() -> None:
    """Suite que percorre o ciclo criar -> buscar -> remover com bordas."""
    cadastro: list[dict] = []

    # Create: o tamanho da lista confirma cada insercao
    criar(cadastro, {"id": 1, "nome": "Ana"})
    criar(cadastro, {"id": 2, "nome": "Bruno"})
    assert len(cadastro) == 2, "apos criar 2 itens, lista deve ter 2"

    # Read: existente devolve o registro, inexistente devolve None
    ana = buscar_por_id(cadastro, 1)
    assert ana is not None and ana["nome"] == "Ana", "id 1 deveria ser Ana"
    assert buscar_por_id(cadastro, 99) is None, "id 99 nao existe"

    # Delete: sucesso encolhe a lista, falha mantem
    assert remover(cadastro, 1) is True, "remover existente deve dar True"
    assert len(cadastro) == 1, "apos remover, lista deve ter 1"
    assert remover(cadastro, 99) is False, "remover inexistente deve dar False"
    assert len(cadastro) == 1, "lista nao muda ao remover inexistente"


if __name__ == "__main__":
    testar_fluxo_crud()
    print("Todos os testes passaram.")
```

</details>
