# 57 - Try except: menu CLI robusto com log de sessao

## Objetivo

Implementar menu interativo que nao trava com entradas invalidas e registra encerramento da sessao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / atendimento |
| **Solicitacao** | Painel CLI para cadastro rapido de alunos com tratamento de erro e auditoria de encerramento. |

## Enunciado

- Mantenha lista `cadastros = []` em memoria.
- Loop de menu ate o usuario sair:
  - `1` — listar cadastros numerados (ou aviso se vazio)
  - `2` — cadastrar nome (nao aceitar vazio ou so espacos)
  - `0` — sair
- Trate `ValueError` (opcao nao numerica) e entrada vazia com mensagens claras.
- Use `try/except/finally`: no `finally` do bloco principal, grave `"Sessao encerrada"` em `sessao.log` (append).
- Teste manualmente com entradas validas e invalidas.

## Passo a passo

1. Crie a lista `cadastros = []` e a constante `ARQ_SESSAO = "sessao.log"`.
2. Defina `def listar_cadastros():` — se a lista estiver vazia, exiba um aviso; senao, use `for i, nome in enumerate(cadastros, start=1):` para listar numerado.
3. Defina `def cadastrar_nome():` — leia com `nome = input("Nome: ").strip()`; se `not nome` (vazio ou so espacos), exiba `"Nome vazio nao permitido."` e retorne; senao, faca `cadastros.append(nome)` e confirme.
4. Defina `def executar_menu():` com `while True:`:
   - Exiba as opcoes: `1 Listar | 2 Cadastrar | 0 Sair`.
   - Leia a opcao dentro de `try:` com `opcao = int(input("Opcao: ").strip())` e capture `except ValueError:` exibindo `"Opcao invalida — digite um numero."` seguido de `continue`.
   - Trate as opcoes: `0` -> `break`; `1` -> `listar_cadastros()`; `2` -> `cadastrar_nome()`; qualquer outro numero -> `"Opcao inexistente."`.
5. No bloco principal, envolva a chamada em `try:` / `finally:` — no `finally`, grave `"Sessao encerrada\n"` em `sessao.log` com `with open(ARQ_SESSAO, "a", encoding="utf-8")`. Assim o log e gravado mesmo se o programa quebrar no meio.
6. Teste manualmente: digite `abc` (erro tratado), Enter vazio, cadastre um nome valido, liste e saia com `0`. Confira o `sessao.log` depois.

## Como executar

```bash
cd "57_try_menu_robusto"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Estado da sessao: cadastros em memoria e arquivo de auditoria
cadastros = []
ARQ_SESSAO = "sessao.log"


def listar_cadastros():
    # Lista vazia merece aviso claro em vez de tela em branco
    if not cadastros:
        print("Nenhum cadastro ainda.")
        return
    # enumerate com start=1 numera a partir de 1 para o usuario
    for i, nome in enumerate(cadastros, start=1):
        print(f"{i}. {nome}")


def cadastrar_nome():
    # strip remove espacos das pontas; "   " vira "" e e rejeitado
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome vazio nao permitido.")
        return
    cadastros.append(nome)
    print(f"Cadastrado: {nome}")


def executar_menu():
    while True:
        print("\n1 Listar | 2 Cadastrar | 0 Sair")
        try:
            # int() de texto nao numerico levanta ValueError
            opcao = int(input("Opcao: ").strip())
        except ValueError:
            print("Opcao invalida — digite um numero.")
            # continue volta ao topo do loop sem executar o resto
            continue

        if opcao == 0:
            print("Ate logo!")
            break
        elif opcao == 1:
            listar_cadastros()
        elif opcao == 2:
            cadastrar_nome()
        else:
            print("Opcao inexistente.")


# try/finally no bloco principal: o log de sessao e gravado SEMPRE,
# mesmo se um erro inesperado derrubar o menu no meio da execucao
try:
    executar_menu()
finally:
    with open(ARQ_SESSAO, "a", encoding="utf-8") as f:
        f.write("Sessao encerrada\n")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Menu CLI de cadastro com tratamento de erros e log de encerramento."""

from pathlib import Path

ARQ_SESSAO = Path("sessao.log")
MENU = "\n1 Listar | 2 Cadastrar | 0 Sair"


def listar(cadastros: list[str]) -> None:
    """Exibe os cadastros numerados ou um aviso quando nao ha nenhum."""
    if not cadastros:
        print("Nenhum cadastro ainda.")
        return
    for i, nome in enumerate(cadastros, start=1):
        print(f"{i}. {nome}")


def cadastrar(cadastros: list[str]) -> None:
    """Le um nome, rejeita entrada vazia e adiciona a lista."""
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome vazio nao permitido.")
        return
    cadastros.append(nome)
    print(f"Cadastrado: {nome}")


def ler_opcao() -> int | None:
    """Le a opcao do usuario; devolve None quando nao for um numero."""
    try:
        return int(input("Opcao: ").strip())
    except ValueError:
        print("Opcao invalida — digite um numero.")
        return None


def executar_menu(cadastros: list[str]) -> None:
    """Loop principal: despacha cada opcao ate o usuario pedir para sair."""
    while True:
        print(MENU)
        opcao = ler_opcao()
        # Entrada invalida ja foi avisada em ler_opcao; volta ao menu
        if opcao is None:
            continue

        # match/case deixa o despacho das opcoes declarativo
        match opcao:
            case 0:
                print("Ate logo!")
                return
            case 1:
                listar(cadastros)
            case 2:
                cadastrar(cadastros)
            case _:
                print("Opcao inexistente.")


def registrar_encerramento() -> None:
    """Auditoria de sessao em modo append."""
    with ARQ_SESSAO.open("a", encoding="utf-8") as f:
        f.write("Sessao encerrada\n")


def main() -> None:
    cadastros: list[str] = []
    try:
        executar_menu(cadastros)
    finally:
        # Garante o registro mesmo em erro inesperado ou Ctrl+C
        registrar_encerramento()


if __name__ == "__main__":
    main()
```

</details>
