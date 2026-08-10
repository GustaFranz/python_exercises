# 33 - JSON: carregar arquivo

## Objetivo

Ler dados de arquivo JSON e exibir conteudo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | TaskFlow Produtividade |
| **Setor** | Software / tarefas |
| **Solicitacao** | Carregar tarefas salvas e exibir status na reuniao diaria. |

## Enunciado

Dados de exemplo (grave antes de carregar, conforme exercicio 32):
```python
tarefas = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]
```

1) Grave `tarefas.json` com `json.dump` (`indent=2`, `ensure_ascii=False`).
2) Implemente:
```python
def carregar_tarefas(caminho: str) -> list[dict]:
    # json.load dentro de with open(..., encoding="utf-8")
    # trate FileNotFoundError com mensagem amigavel
```
3) Exiba cada tarefa: `[x] titulo` se concluida, `[ ] titulo` se pendente.

Exemplo de saida:

```
[x] Enviar relatorio
[ ] Revisar proposta
```

## Passo a passo

1. Importe `json` e crie a constante `CAMINHO = "tarefas.json"`.
2. Declare a lista `tarefas` do enunciado e grave o arquivo primeiro (mesmo padrao do exercicio 32): `with open(CAMINHO, "w", encoding="utf-8")` + `json.dump(..., indent=2, ensure_ascii=False)` — assim o script e autossuficiente.
3. Defina `def carregar_tarefas(caminho):` que:
   - abre com `with open(caminho, encoding="utf-8") as arquivo:` (modo leitura e o padrao);
   - retorna `json.load(arquivo)` — o inverso do `dump`: le o JSON e reconstroi a lista de dicts;
   - envolve tudo em `try/except FileNotFoundError`, exibindo mensagem amigavel e retornando `[]` quando o arquivo nao existe.
4. Chame `carregar_tarefas(CAMINHO)` e guarde o resultado.
5. Percorra as tarefas carregadas e monte o marcador com expressao condicional: `"[x]" if tarefa["concluida"] else "[ ]"`.
6. Exiba cada linha no formato `[x] titulo` / `[ ] titulo`.

## Como executar

```bash
cd "33_json_carregar_arquivo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import json

CAMINHO = "tarefas.json"

# Etapa 0: grava o arquivo de exemplo (deixa o script autossuficiente).
tarefas_iniciais = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]
with open(CAMINHO, "w", encoding="utf-8") as arquivo:
    json.dump(tarefas_iniciais, arquivo, indent=2, ensure_ascii=False)


def carregar_tarefas(caminho):
    # Tenta abrir e desserializar o JSON; trata arquivo inexistente.
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            # json.load le o arquivo e reconstroi a lista de dicts.
            return json.load(arquivo)
    except FileNotFoundError:
        # Mensagem amigavel + lista vazia mantem o programa funcionando.
        print(f"Arquivo {caminho} nao encontrado. Nenhuma tarefa carregada.")
        return []


# Carrega e exibe o status de cada tarefa.
tarefas = carregar_tarefas(CAMINHO)
for tarefa in tarefas:
    # Expressao condicional escolhe o marcador conforme o status.
    marcador = "[x]" if tarefa["concluida"] else "[ ]"
    print(f"{marcador} {tarefa['titulo']}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Carrega tarefas de um arquivo JSON e exibe o status de cada uma."""

import json
from pathlib import Path

# Arquivo sempre relativo a pasta do script.
CAMINHO = Path(__file__).parent / "tarefas.json"

TAREFAS_INICIAIS = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]


def preparar_arquivo(caminho: Path) -> None:
    """Grava o JSON de exemplo para o script ser autossuficiente."""
    conteudo = json.dumps(TAREFAS_INICIAIS, indent=2, ensure_ascii=False)
    caminho.write_text(conteudo, encoding="utf-8")


def carregar_tarefas(caminho: Path) -> list[dict]:
    """Le o JSON de tarefas; retorna lista vazia se o arquivo nao existir."""
    # Guard clause: checa existencia antes de abrir (evita try/except aqui).
    if not caminho.exists():
        print(f"Arquivo {caminho.name} nao encontrado. Nenhuma tarefa carregada.")
        return []
    # read_text + json.loads: leitura completa e desserializacao.
    return json.loads(caminho.read_text(encoding="utf-8"))


def formatar_tarefa(tarefa: dict) -> str:
    """Monta a linha de status: [x] concluida, [ ] pendente."""
    marcador = "[x]" if tarefa["concluida"] else "[ ]"
    return f"{marcador} {tarefa['titulo']}"


def main() -> None:
    preparar_arquivo(CAMINHO)
    for tarefa in carregar_tarefas(CAMINHO):
        print(formatar_tarefa(tarefa))


if __name__ == "__main__":
    main()
```

</details>
