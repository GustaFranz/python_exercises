# 31 - Introducao a persistencia JSON

## Objetivo

Conhecer gravacao JSON e o mapa dos exercicios 31 a 35.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | TaskFlow Produtividade |
| **Setor** | Software / tarefas |
| **Solicitacao** | Salvar lista de tarefas em arquivo JSON para retomar depois. |

## Visao do bloco (exercicios 31 a 35)

Topico **persistencia JSON**: salvar e carregar dados estruturados.

| # | Foco |
|---|------|
| 31 | Introducao + salvar tarefas |
| 32 | Carregar JSON |
| 33 | Append em arquivo |
| 34 | Backup incremental |
| 35 | Sincronizar memoria e arquivo |

## Enunciado

tarefas = [
    {"id": 1, "titulo": "Revisar proposta", "concluida": False},
    {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
]
Salve em "tarefas.json" usando json.dump com indent=2 e ensure_ascii=False.
Confirme gravacao exibindo mensagem e caminho do arquivo.

## Como executar

```bash
cd "31_introducao_persistencia_json"
python main.py
```
