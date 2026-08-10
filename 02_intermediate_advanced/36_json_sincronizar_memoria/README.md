# 36 - JSON: sincronizar memoria e arquivo

## Objetivo

Manter lista em memoria sincronizada com arquivo JSON validado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | InventarioTech Almoxarifado |
| **Setor** | Logistica interna |
| **Solicitacao** | Sistema de itens com memoria e disco sempre consistentes. |

## Enunciado

Use lista global `itens = []` sincronizada com `itens.json`.

Implemente:

```python
def carregar() -> None:
    # tenta carregar itens.json para memoria no inicio

def salvar() -> None:
    # grava lista itens em itens.json

def adicionar_item(nome: str, quantidade: int) -> None:
    # valida: nome nao vazio, quantidade >= 0
    # atualiza memoria E chama salvar()
```

No `main`:

1) Chame `carregar()` ao iniciar.
2) Adicione 2 itens validos (ex.: `"Caderno"`, `50` e `"Caneta"`, `100`).
3) Exiba itens apos cada operacao.

Exemplo de saida:

```
Itens carregados: 0
Item adicionado: Caderno (50)
Itens: [{'nome': 'Caderno', 'quantidade': 50}]
Item adicionado: Caneta (100)
Itens: [{'nome': 'Caderno', 'quantidade': 50}, {'nome': 'Caneta', 'quantidade': 100}]
```

## Passo a passo

1. Importe `json`, crie a constante `CAMINHO = "itens.json"` e a lista global `itens = []`.
2. Defina `def salvar():` que grava `itens` em `CAMINHO` com `json.dump(..., indent=2, ensure_ascii=False)` — toda mudanca em memoria passa por aqui para ir ao disco.
3. Defina `def carregar():` que:
   - tenta abrir `CAMINHO` e carregar com `json.load`;
   - usa `itens[:] = dados` para substituir o conteudo da lista global sem trocar o objeto (evita precisar de `global`);
   - em `except FileNotFoundError`, mantem a lista vazia;
   - exibe `Itens carregados: N`.
4. Defina `def adicionar_item(nome, quantidade):` que:
   - valida `nome.strip()` nao vazio e `quantidade >= 0` — se invalido, exibe erro e retorna sem gravar;
   - faz `itens.append({"nome": nome, "quantidade": quantidade})` (memoria);
   - chama `salvar()` imediatamente (disco) — e isso que mantem as duas copias sincronizadas;
   - exibe `Item adicionado: nome (quantidade)`.
5. No fluxo principal: chame `carregar()`, adicione `"Caderno", 50` e `"Caneta", 100`, exibindo `itens` apos cada adicao.

## Como executar

```bash
cd "36_json_sincronizar_memoria"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import json

CAMINHO = "itens.json"

# Lista global: a "memoria" do sistema.
itens = []


def salvar():
    # Grava o estado atual da memoria no disco.
    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(itens, arquivo, indent=2, ensure_ascii=False)


def carregar():
    # Tenta trazer o conteudo do disco para a memoria.
    try:
        with open(CAMINHO, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        # itens[:] substitui o CONTEUDO da lista global (in place),
        # sem precisar da palavra-chave global.
        itens[:] = dados
    except FileNotFoundError:
        # Primeiro uso: arquivo ainda nao existe, memoria fica vazia.
        pass
    print(f"Itens carregados: {len(itens)}")


def adicionar_item(nome, quantidade):
    # Validacao antes de tocar na memoria ou no disco.
    if not nome.strip():
        print("[ERRO] nome nao pode ser vazio")
        return
    if quantidade < 0:
        print("[ERRO] quantidade deve ser >= 0")
        return
    # Atualiza memoria E disco na mesma operacao = sincronia imediata.
    itens.append({"nome": nome, "quantidade": quantidade})
    salvar()
    print(f"Item adicionado: {nome} ({quantidade})")


# Reinicia o arquivo para a demonstracao comecar sempre do zero.
itens.clear()
salvar()

# Fluxo principal: carregar -> adicionar -> exibir apos cada operacao.
carregar()
adicionar_item("Caderno", 50)
print(f"Itens: {itens}")
adicionar_item("Caneta", 100)
print(f"Itens: {itens}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Inventario com memoria e arquivo JSON sempre sincronizados."""

import json
from pathlib import Path

CAMINHO = Path(__file__).parent / "itens.json"

Item = dict[str, object]


class Inventario:
    """Encapsula a lista em memoria e a persistencia em JSON.

    A classe substitui a lista global: o estado fica isolado e toda
    mutacao passa pelos metodos, que garantem a gravacao no disco.
    """

    def __init__(self, caminho: Path) -> None:
        self.caminho = caminho
        self.itens: list[Item] = []

    def salvar(self) -> None:
        """Grava o estado atual da memoria no arquivo."""
        conteudo = json.dumps(self.itens, indent=2, ensure_ascii=False)
        self.caminho.write_text(conteudo, encoding="utf-8")

    def carregar(self) -> None:
        """Carrega o arquivo para a memoria (vazio se nao existir)."""
        if self.caminho.exists():
            self.itens = json.loads(self.caminho.read_text(encoding="utf-8"))
        print(f"Itens carregados: {len(self.itens)}")

    def adicionar_item(self, nome: str, quantidade: int) -> None:
        """Valida, atualiza a memoria e persiste imediatamente."""
        # Guard clauses: rejeita dados invalidos antes de qualquer mutacao.
        if not nome.strip():
            print("[ERRO] nome nao pode ser vazio")
            return
        if quantidade < 0:
            print("[ERRO] quantidade deve ser >= 0")
            return
        self.itens.append({"nome": nome, "quantidade": quantidade})
        # salvar() logo apos o append = memoria e disco nunca divergem.
        self.salvar()
        print(f"Item adicionado: {nome} ({quantidade})")


def main() -> None:
    # Remove o arquivo anterior para a demonstracao ser reprodutivel.
    CAMINHO.unlink(missing_ok=True)

    inventario = Inventario(CAMINHO)
    inventario.carregar()

    inventario.adicionar_item("Caderno", 50)
    print(f"Itens: {inventario.itens}")

    inventario.adicionar_item("Caneta", 100)
    print(f"Itens: {inventario.itens}")


if __name__ == "__main__":
    main()
```

</details>
