# 93 - HTTP: mensagem amigavel

## Objetivo

Traduzir erros tecnicos HTTP em mensagens para o usuario final.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / atendimento |
| **Solicitacao** | Exibir mensagens claras quando o portal de notas estiver fora do ar. |

## Enunciado

Mapeamento tecnico → amigavel:

| status | mensagem |
|--------|----------|
| `404` | `"Nao encontramos seu cadastro. Verifique a matricula."` |
| `500` | `"Estamos com instabilidade. Tente em alguns minutos."` |
| `0` (timeout) | `"Sem conexao com o servidor. Verifique sua internet."` |

Implemente:

```python
def mensagem_para_usuario(resposta: dict) -> str:
    # recebe dict com campo "status"
    # retorna string amigavel (sem detalhes tecnicos)
```

No `main`, teste os 3 status:

```python
{"status": 404}
{"status": 500}
{"status": 0}
```

Exemplo de saida:

```
404: Nao encontramos seu cadastro. Verifique a matricula.
500: Estamos com instabilidade. Tente em alguns minutos.
0: Sem conexao com o servidor. Verifique sua internet.
```

## Como executar

```bash
cd "93_http_mensagem_amigavel"
python main.py
```
