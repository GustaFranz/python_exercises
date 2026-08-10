# 32 - Introducao a persistencia JSON

## Objetivo

Conhecer gravacao JSON e o mapa dos exercicios 32 a 36.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | TaskFlow Produtividade |
| **Setor** | Software / tarefas |
| **Solicitacao** | Salvar lista de tarefas em arquivo JSON para retomar depois. |

## Visao do bloco (exercicios 32 a 36)

Topico **persistencia JSON**: salvar e carregar dados estruturados.

| # | Foco |
|---|------|
| 32 | Introducao + salvar tarefas |
| 33 | Carregar JSON |
| 34 | Append em arquivo |
| 35 | Backup incremental |
| 36 | Sincronizar memoria e arquivo |

## Enunciado

tarefas = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]
Salve em "tarefas.json" usando json.dump com indent=2 e ensure_ascii=False.
Confirme gravacao exibindo mensagem e caminho do arquivo.

## Passo a passo

1. Importe o modulo `json` no topo do arquivo.
2. Declare a lista `tarefas` com os 2 dicionarios do enunciado.
3. Crie a constante `CAMINHO = "tarefas.json"` para nao repetir o nome do arquivo.
4. Abra o arquivo em modo escrita com `with open(CAMINHO, "w", encoding="utf-8") as arquivo:` — o `with` garante o fechamento mesmo se ocorrer erro.
5. Dentro do `with`, grave com `json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)` — `indent=2` deixa o arquivo legivel e `ensure_ascii=False` preserva acentos.
6. Apos o `with`, exiba mensagem de confirmacao com o caminho do arquivo (ex.: `f"Tarefas salvas em {CAMINHO}"`) e a quantidade de tarefas gravadas.

## Como executar

```bash
cd "32_introducao_persistencia_json"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import json

# Nome do arquivo como constante, no topo.
CAMINHO = "tarefas.json"

# Dados em memoria que serao persistidos.
tarefas = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]

# with garante que o arquivo sera fechado ao final do bloco.
with open(CAMINHO, "w", encoding="utf-8") as arquivo:
    # json.dump serializa a lista direto no arquivo:
    # indent=2 formata com identacao legivel;
    # ensure_ascii=False mantem acentos como texto (nao \u00e3).
    json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

# Confirmacao da gravacao com caminho e total de registros.
print(f"Tarefas salvas em {CAMINHO}")
print(f"Total gravado: {len(tarefas)} tarefas")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Persiste a lista de tarefas em arquivo JSON (TaskFlow Produtividade)."""

import json
from pathlib import Path

# Path relativo a pasta do script: funciona de qualquer diretorio de execucao.
CAMINHO = Path(__file__).parent / "tarefas.json"

TAREFAS = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]


def salvar_tarefas(tarefas: list[dict], caminho: Path) -> None:
    """Grava a lista de tarefas em JSON legivel com suporte a acentos."""
    # json.dumps gera a string; write_text abre, grava e fecha em uma chamada.
    conteudo = json.dumps(tarefas, indent=2, ensure_ascii=False)
    caminho.write_text(conteudo, encoding="utf-8")


def main() -> None:
    salvar_tarefas(TAREFAS, CAMINHO)
    # .resolve() exibe o caminho absoluto, util para conferir onde gravou.
    print(f"Tarefas salvas em {CAMINHO.resolve()}")
    print(f"Total gravado: {len(TAREFAS)} tarefas")


if __name__ == "__main__":
    main()
```

</details>
