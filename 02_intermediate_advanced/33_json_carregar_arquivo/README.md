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

## Como executar

```bash
cd "33_json_carregar_arquivo"
python main.py
```
