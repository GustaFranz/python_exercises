# 32 - JSON: carregar arquivo

## Objetivo

Ler dados de arquivo JSON e exibir conteudo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | TaskFlow Produtividade |
| **Setor** | Software / tarefas |
| **Solicitacao** | Carregar tarefas salvas e exibir status na reuniao diaria. |

## Enunciado

Primeiro grave tarefas.json (ou use arquivo criado no ex. 31).
Implemente carregar_tarefas(caminho) que retorna lista de dicts.
Exiba cada tarefa: [x] ou [ ] titulo conforme concluida.
Trate FileNotFoundError com mensagem amigavel.

## Como executar

```bash
cd "32_json_carregar_arquivo"
python main.py
```
