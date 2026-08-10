# 35 - JSON: backup incremental

## Objetivo

Gerar backup com timestamp antes de atualizar cadastro JSON.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Seguros Familia Protegida |
| **Setor** | Seguros / cadastro de clientes |
| **Solicitacao** | Backup automatico antes de cada atualizacao do cadastro de clientes. |

## Enunciado

Arquivo `clientes.json` com lista de clientes (`id`, `nome`, `plano`).

Implemente:

```python
def fazer_backup(origem: str) -> str:
    # copia origem para backup_YYYYMMDD_HHMMSS.json
    # use datetime.now().strftime("%Y%m%d_%H%M%S") no nome

def atualizar_cliente(caminho: str, id: int, campo: str, valor) -> None:
    # ordem: backup -> carregar -> atualizar -> salvar
```

No `main`:

1) Crie `clientes.json` com 2 clientes de exemplo.
2) Simule atualizacao de um cliente (ex.: alterar `plano` do id `1`).
3) Confirme que arquivo de backup foi criado.

Exemplo de saida:

```
Backup criado: backup_20260809_190000.json
Cliente 1 atualizado: plano = Premium
```

## Passo a passo

1. Importe `json`, `shutil` e `from datetime import datetime`.
2. Crie a constante `CAMINHO = "clientes.json"`.
3. Crie `clientes.json` com 2 clientes de exemplo (ex.: id 1 "Ana" plano "Basico", id 2 "Bruno" plano "Familia") usando `json.dump` com `indent=2` e `ensure_ascii=False`.
4. Defina `def fazer_backup(origem):` que:
   - monta o timestamp com `datetime.now().strftime("%Y%m%d_%H%M%S")`;
   - monta o nome `f"backup_{timestamp}.json"`;
   - copia com `shutil.copy(origem, destino)`;
   - retorna o nome do backup.
5. Defina funcoes auxiliares `carregar(caminho)` (com `json.load`) e `salvar(caminho, clientes)` (com `json.dump`).
6. Defina `def atualizar_cliente(caminho, id_cliente, campo, valor):` seguindo a ordem obrigatoria:
   - `fazer_backup(caminho)` (protecao antes de mexer);
   - `clientes = carregar(caminho)`;
   - localize o cliente pelo id e faca `cliente[campo] = valor`;
   - `salvar(caminho, clientes)`.
7. No fluxo principal: crie o arquivo inicial, chame `atualizar_cliente(CAMINHO, 1, "plano", "Premium")` e exiba as mensagens de backup criado e cliente atualizado.

## Como executar

```bash
cd "35_json_backup_incremental"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import json
import shutil
from datetime import datetime

CAMINHO = "clientes.json"


def carregar(caminho):
    # Le o JSON e devolve a lista de clientes.
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar(caminho, clientes):
    # Regrava o arquivo com a lista atualizada.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=2, ensure_ascii=False)


def fazer_backup(origem):
    # Timestamp no formato AAAAMMDD_HHMMSS para nome unico e ordenavel.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = f"backup_{timestamp}.json"
    # shutil.copy duplica o arquivo byte a byte.
    shutil.copy(origem, destino)
    print(f"Backup criado: {destino}")
    return destino


def atualizar_cliente(caminho, id_cliente, campo, valor):
    # Ordem de seguranca: backup ANTES de qualquer alteracao.
    fazer_backup(caminho)
    clientes = carregar(caminho)
    # Localiza o cliente pelo id e altera o campo pedido.
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            cliente[campo] = valor
            print(f"Cliente {id_cliente} atualizado: {campo} = {valor}")
            break
    else:
        # for/else: executa se o loop terminar sem break (id nao achado).
        print(f"Cliente {id_cliente} nao encontrado")
        return
    salvar(caminho, clientes)


# 1) Cria o cadastro inicial com 2 clientes de exemplo.
clientes_iniciais = [
    {"id": 1, "nome": "Ana", "plano": "Basico"},
    {"id": 2, "nome": "Bruno", "plano": "Familia"},
]
salvar(CAMINHO, clientes_iniciais)

# 2) Simula a atualizacao: plano do id=1 vira Premium.
atualizar_cliente(CAMINHO, 1, "plano", "Premium")

# 3) Exibe o cadastro final para conferencia.
print("=== Cadastro atual ===")
for cliente in carregar(CAMINHO):
    print(f"{cliente['id']} | {cliente['nome']} | {cliente['plano']}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cadastro de clientes em JSON com backup automatico antes de atualizar."""

import json
import shutil
from datetime import datetime
from pathlib import Path

PASTA = Path(__file__).parent
CAMINHO = PASTA / "clientes.json"

Cliente = dict[str, object]

CLIENTES_INICIAIS: list[Cliente] = [
    {"id": 1, "nome": "Ana", "plano": "Basico"},
    {"id": 2, "nome": "Bruno", "plano": "Familia"},
]


def carregar(caminho: Path) -> list[Cliente]:
    """Le e desserializa o cadastro."""
    return json.loads(caminho.read_text(encoding="utf-8"))


def salvar(caminho: Path, clientes: list[Cliente]) -> None:
    """Serializa e grava o cadastro completo."""
    caminho.write_text(
        json.dumps(clientes, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def fazer_backup(origem: Path) -> Path:
    """Copia o arquivo para backup_YYYYMMDD_HHMMSS.json e retorna o destino."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = origem.parent / f"backup_{timestamp}.json"
    # shutil.copy aceita Path diretamente.
    shutil.copy(origem, destino)
    print(f"Backup criado: {destino.name}")
    return destino


def atualizar_cliente(caminho: Path, id_cliente: int, campo: str, valor: object) -> None:
    """Atualiza um campo do cliente com backup previo (backup -> load -> update -> save)."""
    fazer_backup(caminho)  # protecao: estado anterior preservado
    clientes = carregar(caminho)

    # Busca o cliente alvo; None indica id inexistente.
    alvo = next((c for c in clientes if c["id"] == id_cliente), None)
    # Guard clause: nada a fazer se o cliente nao existe.
    if alvo is None:
        print(f"Cliente {id_cliente} nao encontrado")
        return

    alvo[campo] = valor
    salvar(caminho, clientes)
    print(f"Cliente {id_cliente} atualizado: {campo} = {valor}")


def main() -> None:
    # 1) Cria o cadastro inicial (script autossuficiente).
    salvar(CAMINHO, CLIENTES_INICIAIS)

    # 2) Atualiza o plano do cliente 1 (backup e feito antes).
    atualizar_cliente(CAMINHO, 1, "plano", "Premium")

    # 3) Confere o resultado final.
    print("=== Cadastro atual ===")
    for cliente in carregar(CAMINHO):
        print(f"{cliente['id']} | {cliente['nome']} | {cliente['plano']}")


if __name__ == "__main__":
    main()
```

</details>
