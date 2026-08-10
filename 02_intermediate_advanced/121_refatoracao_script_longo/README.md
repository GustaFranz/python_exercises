# 121 - Refatoracao: script longo em funcoes

## Objetivo

Refatorar script monolitico (~70 linhas) em funcoes claras com menu, preservando regras de negocio.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | AgroEscola |
| **Setor** | Educacao / campo |
| **Solicitacao** | Reorganizar controle de estoque do viveiro escolar antes da safra de plantio. |

## Estrutura de arquivos

```
121_refatoracao_script_longo/
├── README.md
├── main.py      # sua versao refatorada
└── legado.py    # script monolitico de referencia (~70 linhas)
```

## Enunciado

- Estude o comportamento do script monolitico em `legado.py` (nao altere a logica de negocio).
- Refatore em `main.py` separando responsabilidades:
  - `carregar_estoque()` — dados iniciais
  - `validar_movimentacao(item, qtd)` — regras antes de entrada/saida
  - `calcular_estoque_atual(estoque, movimentos)` — aplica entradas e saidas
  - `exibir_relatorio(estoque, resumo)` — saida formatada
- Inclua `main()` com menu textual (consultar, movimentar, relatorio, sair).
- Preserve regras: saida bloqueada se estoque insuficiente; alerta para estoque baixo (< 10).

## Passo a passo

1. Rode `python legado.py` e anote as regras de negocio: qtd deve ser positiva, saida bloqueada se maior que o disponivel, item inexistente gera erro sem alterar estoque, item com `qtd < minimo` entra nos alertas.
2. Em `main.py`, defina `carregar_estoque() -> list[dict]` retornando os mesmos 4 itens do legado (`Muda de tomate`, `Muda de alface`, `Substrato`, `Adubo organico`, cada um com `nome`, `qtd` e `minimo`).
3. Defina a auxiliar `buscar_item(estoque, nome)` que percorre a lista com `for` e retorna o dict do item ou `None`.
4. Defina `validar_movimentacao(estoque, nome, qtd, tipo) -> tuple[bool, str]` concentrando as validacoes: qtd nao positiva, item inexistente, tipo desconhecido e saida maior que o disponivel. Retorne `(False, mensagem)` no erro e `(True, "")` no sucesso.
5. Defina `calcular_estoque_atual(estoque, movimentos)` que, para cada movimento, chama `validar_movimentacao`; se valido, soma ou subtrai `qtd` do item e acumula `total_entradas` / `total_saidas`; se invalido, guarda a mensagem numa lista `erros`.
6. Defina `gerar_alertas(estoque) -> list[str]` listando itens com `qtd < minimo` e `exibir_relatorio(estoque, alertas, erros, total_entradas, total_saidas)` imprimindo resumo, erros, alertas e estoque final com status `OK`/`BAIXO` (mesmo formato do legado).
7. Defina `main()` que carrega o estoque, processa a mesma lista fixa de movimentos do legado (para comparar as saidas) e abre um menu `while True` com `input()`: `1` consultar, `2` movimentar, `3` relatorio, `0` sair.
8. Compare a saida da parte automatica com a de `python legado.py`: deve ser logicamente identica.

## Como executar

```bash
cd "121_refatoracao_script_longo"
python legado.py    # referencia do comportamento
python main.py      # sua versao refatorada
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Movimentos fixos do legado: permitem comparar a saida refatorada com legado.py
MOVIMENTOS_TESTE = [
    {"tipo": "saida", "nome": "Muda de tomate", "qtd": 10},
    {"tipo": "saida", "nome": "Muda de pepino", "qtd": 5},
    {"tipo": "entrada", "nome": "Substrato", "qtd": 20},
    {"tipo": "saida", "nome": "Adubo organico", "qtd": 3},
    {"tipo": "entrada", "nome": "Muda de alface", "qtd": 15},
    {"tipo": "saida", "nome": "Muda de alface", "qtd": 40},
]


def carregar_estoque():
    # Isola os dados iniciais: se amanha vierem de um CSV, so esta funcao muda
    return [
        {"nome": "Muda de tomate", "qtd": 50, "minimo": 10},
        {"nome": "Muda de alface", "qtd": 30, "minimo": 10},
        {"nome": "Substrato", "qtd": 100, "minimo": 20},
        {"nome": "Adubo organico", "qtd": 8, "minimo": 10},
    ]


def buscar_item(estoque, nome):
    # Auxiliar reutilizada por validacao e movimentacao; None sinaliza "nao existe"
    for item in estoque:
        if item["nome"] == nome:
            return item
    return None


def validar_movimentacao(estoque, nome, qtd, tipo):
    # Todas as regras de negocio em um unico lugar (no legado estavam espalhadas)
    if qtd <= 0:
        return False, f"Movimento invalido: {tipo} {nome} qtd={qtd}"
    if tipo not in ("entrada", "saida"):
        return False, f"Tipo desconhecido: {tipo}"
    item = buscar_item(estoque, nome)
    if item is None:
        return False, f"Item nao encontrado: {nome}"
    if tipo == "saida" and item["qtd"] < qtd:
        return False, f"Estoque insuficiente para {nome} (disp: {item['qtd']}, pedido: {qtd})"
    return True, ""


def calcular_estoque_atual(estoque, movimentos):
    # Aplica cada movimento valido e acumula erros e totais para o relatorio
    erros = []
    total_entradas = 0
    total_saidas = 0
    for mov in movimentos:
        ok, msg = validar_movimentacao(estoque, mov["nome"], mov["qtd"], mov["tipo"])
        if not ok:
            erros.append(msg)
            print(msg)
            continue
        item = buscar_item(estoque, mov["nome"])
        if mov["tipo"] == "entrada":
            item["qtd"] += mov["qtd"]
            total_entradas += mov["qtd"]
            print(f"Entrada registrada: {mov['nome']} +{mov['qtd']}")
        else:
            item["qtd"] -= mov["qtd"]
            total_saidas += mov["qtd"]
            print(f"Saida registrada: {mov['nome']} -{mov['qtd']}")
    return erros, total_entradas, total_saidas


def gerar_alertas(estoque):
    # List comprehension: so entra no alerta quem esta abaixo do minimo
    return [
        f"{item['nome']} abaixo do minimo ({item['qtd']}/{item['minimo']})"
        for item in estoque
        if item["qtd"] < item["minimo"]
    ]


def exibir_estoque(estoque):
    # Consulta rapida usada pelo menu (opcao 1)
    for item in estoque:
        print(f"  {item['nome']}: {item['qtd']} un (min: {item['minimo']})")


def exibir_relatorio(estoque, alertas, erros, total_entradas, total_saidas):
    # Reproduz o formato do legado, mas agora em funcao dedicada
    print("\n--- Resumo de movimentacoes ---")
    print(f"Total entradas: +{total_entradas}")
    print(f"Total saidas: -{total_saidas}")
    if erros:
        print("\nErros registrados:")
        for e in erros:
            print(f"  ! {e}")
    if alertas:
        print("\nAlertas de estoque baixo:")
        for a in alertas:
            print(f"  * {a}")
    else:
        print("\nNenhum alerta de estoque baixo.")
    print("\nEstoque final:")
    for item in estoque:
        status = "OK" if item["qtd"] >= item["minimo"] else "BAIXO"
        print(f"  {item['nome']}: {item['qtd']} [{status}]")


def movimentar_interativo(estoque, erros):
    # Le os dados do usuario e reutiliza a MESMA validacao do fluxo automatico
    nome = input("Item: ").strip()
    tipo = input("Tipo (entrada/saida): ").strip().lower()
    try:
        qtd = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade invalida.")
        return 0, 0
    ok, msg = validar_movimentacao(estoque, nome, qtd, tipo)
    if not ok:
        erros.append(msg)
        print(msg)
        return 0, 0
    item = buscar_item(estoque, nome)
    if tipo == "entrada":
        item["qtd"] += qtd
        print(f"Entrada registrada: {nome} +{qtd}")
        return qtd, 0
    item["qtd"] -= qtd
    print(f"Saida registrada: {nome} -{qtd}")
    return 0, qtd


def main():
    print("=== Viveiro Escolar — refatorado ===")
    estoque = carregar_estoque()
    print("Estoque inicial:")
    exibir_estoque(estoque)

    # Fase automatica: mesmos movimentos do legado para validar a refatoracao
    erros, entradas, saidas = calcular_estoque_atual(estoque, MOVIMENTOS_TESTE)
    exibir_relatorio(estoque, gerar_alertas(estoque), erros, entradas, saidas)

    # Fase interativa: menu textual pedido no enunciado
    while True:
        print("\n1 consultar | 2 movimentar | 3 relatorio | 0 sair")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            exibir_estoque(estoque)
        elif opcao == "2":
            e, s = movimentar_interativo(estoque, erros)
            entradas += e
            saidas += s
        elif opcao == "3":
            exibir_relatorio(estoque, gerar_alertas(estoque), erros, entradas, saidas)
        elif opcao == "0":
            print("Fim.")
            break
        else:
            print("Opcao invalida.")


main()
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Controle de estoque do viveiro escolar — versao refatorada e tipada."""

from dataclasses import dataclass

# Movimentos fixos do legado para validar que a refatoracao preservou o comportamento
MOVIMENTOS_TESTE: list[dict] = [
    {"tipo": "saida", "nome": "Muda de tomate", "qtd": 10},
    {"tipo": "saida", "nome": "Muda de pepino", "qtd": 5},
    {"tipo": "entrada", "nome": "Substrato", "qtd": 20},
    {"tipo": "saida", "nome": "Adubo organico", "qtd": 3},
    {"tipo": "entrada", "nome": "Muda de alface", "qtd": 15},
    {"tipo": "saida", "nome": "Muda de alface", "qtd": 40},
]


@dataclass
class Item:
    """Item de estoque: dataclass evita dicts soltos e da autocomplete na IDE."""

    nome: str
    qtd: int
    minimo: int

    @property
    def abaixo_do_minimo(self) -> bool:
        # Regra de alerta vive junto do dado que ela descreve
        return self.qtd < self.minimo


def carregar_estoque() -> list[Item]:
    """Fonte unica dos dados iniciais (mesmos itens do legado)."""
    return [
        Item("Muda de tomate", 50, 10),
        Item("Muda de alface", 30, 10),
        Item("Substrato", 100, 20),
        Item("Adubo organico", 8, 10),
    ]


def buscar_item(estoque: list[Item], nome: str) -> Item | None:
    """Localiza item pelo nome; next() com default evita loop manual."""
    return next((item for item in estoque if item.nome == nome), None)


def validar_movimentacao(estoque: list[Item], nome: str, qtd: int, tipo: str) -> tuple[bool, str]:
    """Guard clauses: cada regra falha cedo com mensagem propria."""
    if qtd <= 0:
        return False, f"Movimento invalido: {tipo} {nome} qtd={qtd}"
    if tipo not in ("entrada", "saida"):
        return False, f"Tipo desconhecido: {tipo}"
    item = buscar_item(estoque, nome)
    if item is None:
        return False, f"Item nao encontrado: {nome}"
    if tipo == "saida" and item.qtd < qtd:
        return False, f"Estoque insuficiente para {nome} (disp: {item.qtd}, pedido: {qtd})"
    return True, ""


def aplicar_movimentos(estoque: list[Item], movimentos: list[dict]) -> tuple[list[str], int, int]:
    """Aplica movimentos validos; devolve (erros, total_entradas, total_saidas)."""
    erros: list[str] = []
    total_entradas = total_saidas = 0
    for mov in movimentos:
        ok, msg = validar_movimentacao(estoque, mov["nome"], mov["qtd"], mov["tipo"])
        if not ok:
            erros.append(msg)
            print(msg)
            continue
        item = buscar_item(estoque, mov["nome"])
        if mov["tipo"] == "entrada":
            item.qtd += mov["qtd"]
            total_entradas += mov["qtd"]
            print(f"Entrada registrada: {item.nome} +{mov['qtd']}")
        else:
            item.qtd -= mov["qtd"]
            total_saidas += mov["qtd"]
            print(f"Saida registrada: {item.nome} -{mov['qtd']}")
    return erros, total_entradas, total_saidas


def exibir_estoque(estoque: list[Item]) -> None:
    """Consulta simples usada pelo menu."""
    for item in estoque:
        print(f"  {item.nome}: {item.qtd} un (min: {item.minimo})")


def exibir_relatorio(estoque: list[Item], erros: list[str], entradas: int, saidas: int) -> None:
    """Relatorio no mesmo formato logico do legado."""
    alertas = [
        f"{item.nome} abaixo do minimo ({item.qtd}/{item.minimo})"
        for item in estoque
        if item.abaixo_do_minimo
    ]
    print("\n--- Resumo de movimentacoes ---")
    print(f"Total entradas: +{entradas}")
    print(f"Total saidas: -{saidas}")
    if erros:
        print("\nErros registrados:")
        for erro in erros:
            print(f"  ! {erro}")
    if alertas:
        print("\nAlertas de estoque baixo:")
        for alerta in alertas:
            print(f"  * {alerta}")
    else:
        print("\nNenhum alerta de estoque baixo.")
    print("\nEstoque final:")
    for item in estoque:
        status = "BAIXO" if item.abaixo_do_minimo else "OK"
        print(f"  {item.nome}: {item.qtd} [{status}]")


def ler_movimento() -> dict | None:
    """Le um movimento do usuario; None se a quantidade nao for numerica."""
    nome = input("Item: ").strip()
    tipo = input("Tipo (entrada/saida): ").strip().lower()
    try:
        qtd = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade invalida.")
        return None
    return {"tipo": tipo, "nome": nome, "qtd": qtd}


def main() -> None:
    print("=== Viveiro Escolar — refatorado ===")
    estoque = carregar_estoque()
    print("Estoque inicial:")
    exibir_estoque(estoque)

    # Reproduz o legado com os mesmos dados: saida deve bater com python legado.py
    erros, entradas, saidas = aplicar_movimentos(estoque, MOVIMENTOS_TESTE)
    exibir_relatorio(estoque, erros, entradas, saidas)

    # Menu interativo: match/case deixa o roteamento das opcoes explicito
    while True:
        print("\n1 consultar | 2 movimentar | 3 relatorio | 0 sair")
        match input("Opcao: ").strip():
            case "1":
                exibir_estoque(estoque)
            case "2":
                movimento = ler_movimento()
                if movimento is not None:
                    novos_erros, e, s = aplicar_movimentos(estoque, [movimento])
                    erros.extend(novos_erros)
                    entradas += e
                    saidas += s
            case "3":
                exibir_relatorio(estoque, erros, entradas, saidas)
            case "0":
                print("Fim.")
                break
            case _:
                print("Opcao invalida.")


if __name__ == "__main__":
    main()
```

</details>
