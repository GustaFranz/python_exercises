# 91 - Introducao a tratamento HTTP

## Objetivo

Tratar respostas simuladas 200, 404 e timeout em cliente HTTP.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / integracoes |
| **Solicitacao** | Consumir API de matriculas com tratamento correto de falhas. |

## Visao do bloco (exercicios 91 a 95)

Topico **API com tratamento HTTP**: lidar com sucesso, erro e indisponibilidade.

| # | Foco |
|---|------|
| 91 | Introducao + 200 vs 404 vs timeout |
| 92 | Retry simples |
| 93 | Mensagem amigavel ao usuario |
| 94 | Consulta clima com fallback |
| 95 | Cliente HTTP com cache e log de falhas |

## Enunciado

Implemente `simular_api(codigo) -> dict` com respostas simuladas:

- `200` → `{"status": 200, "dados": {"aluno": "Ana", "turma": "7B"}}`
- `404` → `{"status": 404, "erro": "Matricula nao encontrada"}`
- `0` ou `"timeout"` → `{"status": 0, "erro": "Timeout"}`

Implemente `consultar_matricula(codigo)` que chama `simular_api` e trata cada caso:

- **200** — exibe dados do aluno (nome e turma)
- **404** — exibe erro amigavel
- **timeout (status 0)** — exibe `"Servico indisponivel, tente mais tarde"`

Teste no `main` com codigos **200**, **404** e **"timeout"**.

## Como executar

```bash
cd "91_introducao_http_tratamento"
python main.py
```
